import datetime
from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from forms import ForgotPasswordForm
from flask_migrate import Migrate


# Import models
from models import db, User, Goal, Group, GroupInvitation

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587                
app.config['MAIL_USE_TLS'] = True            
app.config['MAIL_USE_SSL'] = False            
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'goalbondbot@gmail.com') 
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME', 'goalbondbot@gmail.com')  


# Cookies
app.config.update(
    SESSION_COOKIE_SECURE=True,         
    SESSION_COOKIE_HTTPONLY=True,       
    SESSION_COOKIE_SAMESITE='None',    
    PERMANENT_SESSION_LIFETIME=datetime.timedelta(days=7),
)

mail = Mail(app)

# Initialize the serializer
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Update CORS configuration to allow specific methods without preflight
CORS(app, resources={r"/*": {
    "origins": ["https://goalbond.netlify.app", "http://localhost:8080", "http://127.0.0.1:8080"],
    "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"],
    "supports_credentials": True,
    "expose_headers": ["Content-Type", "Authorization"],
    "max_age": 600
}})

db.init_app(app)
migrate = Migrate(app, db)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize the database
with app.app_context():
    db.create_all()  # Ensure all tables are created

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = jsonify({'status': 'OK'})
        response.headers.add("Access-Control-Allow-Origin", request.headers.get("Origin", "*"))
        response.headers.add('Access-Control-Allow-Headers', "Content-Type, Authorization")
        response.headers.add('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS")
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    if origin in ["https://goalbond.netlify.app", "http://localhost:8080", "http://127.0.0.1:8080"]:
        response.headers.add('Access-Control-Allow-Origin', origin)
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


##### User methods

# Get User
@app.route('/user')
@login_required
def get_user():
    # Check if a user is logged in
    if current_user.is_authenticated:
        # Return user's details including groups
        user_data = {
            'id': current_user.id,
            'username': current_user.username,
            'email': current_user.email,
            'groups': [
                {'id': group.id, 'name': group.name}
                for group in current_user.groups
            ]
        }
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "Unauthorized"}), 401    

# User Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    nickname = data.get('nickname') or username  # Default nickname to username if not provided
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    # Create new user
    new_user = User(username=username, email=email, nickname=nickname)  # Include nickname here
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    # Log in the user
    login_user(new_user)  # Log in the newly created user
    return jsonify({'message': 'User created and logged in successfully!'}), 201

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user, remember=True)
        session.permanent = True
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "nickname": user.nickname
            }
        }), 200
    return jsonify({"message": "Invalid username or password"}), 401

# User Deletion
@app.route('/delete_account', methods=['DELETE'])
@login_required
def delete_account():
    try:
        user = User.query.get(current_user.id)

        if not user:
            return jsonify({'success': False, 'message': 'User not found'}), 404
        
        goals = Goal.query.filter_by(user_id=current_user.id).all()
        for goal in goals:
            db.session.delete(goal) 

        db.session.delete(user)
        db.session.commit()

        logout_user()

        return jsonify({'success': True, 'message': 'Your account has been deleted.'}), 200
    except Exception as e:
        app.logger.error(f"Error deleting account: {str(e)}")
        return jsonify({'success': False, 'message': 'Something went wrong. Please try again later.'}), 500



# Check Authentication
@app.route('/check-auth', methods=['GET'])
def check_auth():
    if current_user.is_authenticated:
        session.permanent = True
        return jsonify({
            "authenticated": True,
            "user": {
                "id": current_user.id,
                "username": current_user.username,
                "email": current_user.email,
                "nickname": current_user.nickname
            }
        }), 200
    else:
        return jsonify({"authenticated": False}), 401

# User Logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful!'}), 200

# User Update
@app.route('/update-user', methods=['PUT'])
@login_required
def update_user():
    data = request.get_json()
    
    username = data.get('username', current_user.username)  
    nickname = data.get('nickname', current_user.nickname)
    email = data.get('email', current_user.email)
    password = data.get('password')

    if not email:
        return jsonify({'message': 'Email is required'}), 400
    
    if password and len(password) < 8:  
       return jsonify({'message': 'Password should be at least 8 characters long'}), 400

    current_user.username = username
    current_user.nickname = nickname
    current_user.email = email

    if password:
        current_user.set_password(password)  

    db.session.commit()
    
    return jsonify({'message': 'Details updated successfully!'}), 200

# Check Password
@app.route('/check-password', methods=['POST'])
@login_required
def check_password():
    data = request.get_json()
    password = data.get('password').strip() 

    if not password:
        return jsonify({'message': 'Password is required'}), 400

    if not current_user.check_password(password):
        return jsonify({'message': 'Password is incorrect'}), 401

    return jsonify({'message': 'Password is correct'}), 200

# Search for users
@app.route('/users/search', methods=['GET'])
@login_required
def search_users():
    query = request.args.get('query', '').strip()

    if not query:
        return jsonify([]), 200

    # Search for users by username or nickname
    users = User.query.filter(
        (User.username.ilike(f'%{query}%')) |
        (User.nickname.ilike(f'%{query}%'))
    ).filter(User.id != current_user.id).all()  # Exclude current user

    result = [{
        'id': user.id,
        'username': user.username,
        'nickname': user.nickname,
        'email': user.email
    } for user in users]

    return jsonify(result), 200

##### Goal Methods

# Create a Goal
@app.route('/goals', methods=['POST'])
@login_required
def create_goal():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    deadline = data.get('deadline')
    group_id = data.get('group_id')  # Get the group_id if provided
    user_id = current_user.id  # User ID to associate the goal with a user
    category = data.get('category')

    if not title or user_id is None:
        return jsonify({'message': 'Missing title or user_id'}), 400

    # Extract season and episode if category is 'Series'
    season = data.get('season') if category == 'Series' else None
    episode = data.get('episode') if category == 'Series' else None

    # Create the new goal
    new_goal = Goal(
        title=title,
        description=description,
        deadline=deadline if deadline else None,  # Allow deadline to be None if not provided
        completed=False,
        user_id=user_id,
        group_id=group_id,  # Associate with the group if provided
        category=category,
        season=season,  # Include season
        episode=episode   # Include episode
    )
    
    db.session.add(new_goal)
    db.session.commit()

    return jsonify({
        'message': 'Goal created successfully!',
        'goal': new_goal.to_dict()  # Call the updated to_dict() method
    }), 201


# Get all Goals
@app.route('/goals', methods=['GET'])
@login_required  # Make sure this endpoint requires authentication
def get_goals():
    user_id = current_user.id  # Optional user ID to filter goals by user

    # Retrieve goals for the user, whether personal or group-related, ordered by creation date
    goals = Goal.query.filter((Goal.user_id == user_id) | (Goal.group_id.isnot(None))).order_by(Goal.created_at.desc()).all()

    return jsonify([goal.to_dict() for goal in goals]), 200
 
# Update a Goal
@app.route('/goals/<int:goal_id>', methods=['PUT'])
@login_required
def update_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)  # Get the goal or return 404 if not found

    # Check if the user is part of the group that shares the goal
    if goal.group_id and current_user not in goal.group.members:
        return jsonify({'message': 'You are not authorized to update this goal.'}), 403

    data = request.get_json()
    
    # Update completed status if provided
    if 'completed' in data:
        goal.completed = data['completed']  # Update the completed status
    
    # Update progress if provided
    if 'progress' in data:
        goal.progress = data['progress']  # Update the progress percentage

    # Update season and episode if the goal is a series
    if goal.category == 'Series':
        if 'season' in data:
            goal.season = data['season']  # Update the season if provided
        if 'episode' in data:
            goal.episode = data['episode']  # Update the episode if provided
            
    # Update deadline if provided
    if 'deadline' in data:
        goal.deadline = data['deadline']  # Update the deadline if provided

    db.session.commit()  # Save changes to the database

    return jsonify({
        'message': 'Goal updated successfully!', 
        'goal': {
            'id': goal.id,
            'title': goal.title,
            'description': goal.description,
            'deadline': goal.deadline,
            'completed': goal.completed,
            'user_id': goal.user_id,
            'group_id': goal.group_id,  # Include group_id if applicable
            'season': goal.season,  # Include season in the response
            'episode': goal.episode,   # Include episode in the response
            'progress': goal.progress  # Include progress in the response
        }
    }), 200

# Remove a Goal
@app.route('/goals/<int:goal_id>', methods=['DELETE'])
@login_required
def delete_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)  # Get the goal or return 404 if not found

    # Only allow the owner of the goal to delete it
    if goal.user_id != current_user.id:
        return jsonify({'message': 'You are not authorized to delete this goal.'}), 403

    db.session.delete(goal)  # Delete the goal
    db.session.commit()  # Commit the changes to the database

    return jsonify({'message': 'Goal deleted successfully!'}), 200

##### Group Methods

# Create a Group
@app.route('/groups', methods=['POST'])
@login_required
def create_group():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    is_public = data.get('is_public') 

    if not name:
        return jsonify({'message': 'Group name is required'}), 400

    # Use current_user.id for the owner field
    new_group = Group(
        name=name,
        description=description,
        is_public=is_public,
        owner=current_user.id 
    )
    db.session.add(new_group)
    db.session.commit()

    # Automatically add the creator to the group
    new_group.members.append(current_user)
    db.session.commit()

    return jsonify({
        'message': 'Group created successfully!',
        'group': {
            'id': new_group.id,
            'name': new_group.name,
            'is_public': new_group.is_public
        }
    }), 201


# Join a Group
@app.route('/groups/join/<int:group_id>', methods=['POST'])
@login_required
def join_group(group_id):
    group = Group.query.get_or_404(group_id)
    
    # Prevent joining private groups directly unless the user is invited
    if not group.is_public and current_user not in group.members:
        return jsonify({'message': 'You cannot join a private group without an invitation.'}), 403
    
    if current_user not in group.members:
        group.members.append(current_user)
        db.session.commit()
        return jsonify({'message': 'You have joined the group!'}), 200
    else:
        return jsonify({'message': 'You are already a member of this group.'}), 400


# Get All Groups
@app.route('/groups', methods=['GET'])
@login_required
def get_groups():
    groups = Group.query.all()
    result = []

    for group in groups:
        # Show public groups to everyone; private groups only to members
        if group.is_public or current_user in group.members:
            result.append({
                'id': group.id,
                'name': group.name,
                'description': group.description,
                'is_public': group.is_public,
                'owner' : { 'id': group.owner, 'username': User.query.get(group.owner).username },
                'members': [{'id': user.id, 'username': user.username} for user in group.members]
            })

    return jsonify(result), 200

    
# Get User's Groups 
@app.route('/groups/mine', methods=['GET'])
@login_required
def get_user_groups():
    groups = current_user.groups 

    return jsonify([{
        'id': group.id,
        'name': group.name,
        'description': group.description,
        'is_public': group.is_public,
        'owner' : { 'id': group.owner, 'username': User.query.get(group.owner).username },
        'members': [{'id': member.id, 'username': member.username} for member in group.members]
    } for group in groups]), 200
    
# Get Groups User Isn't Part Of
@app.route('/groups/not-mine', methods=['GET'])
@login_required
def get_groups_not_mine():
    # Get all groups
    all_groups = Group.query.all()

    # Get user's groups
    user_groups = set(group.id for group in current_user.groups) 

    groups_not_mine = [
        {
            'id': group.id,
            'name': group.name,
            'description': group.description,
            'is_public': group.is_public,
            'owner' : { 'id': group.owner, 'username': User.query.get(group.owner).username },
            'members': [{'id': member.id, 'username': member.username} for member in group.members]
        }
        for group in all_groups 
        if group.id not in user_groups and group.is_public  # Only include public groups
    ]

    return jsonify(groups_not_mine), 200

# Join a Group
@app.route('/groups/<int:group_id>/join', methods=['POST'])
@login_required
def join_group_by_id(group_id):
    group = Group.query.get_or_404(group_id)
    
    # Add the user to the group
    if current_user not in group.members:
        group.members.append(current_user)
        db.session.commit()
        return jsonify({'message': 'You have joined the group!'}), 200
    else:
        return jsonify({'message': 'You are already a member of this group.'}), 400

# Leave a Group
@app.route('/groups/<int:group_id>/leave', methods=['POST'])
@login_required
def leave_group(group_id):
    group = Group.query.get_or_404(group_id)
    
    if current_user in group.members:
        if current_user.id == group.owner and len(group.members) == 1:
            db.session.delete(group)
            db.session.commit()
            return jsonify({'message': 'You have left the group successfully! As you were the last member, the group has been deleted.'}), 200
        else:
            group.members.remove(current_user)
            db.session.commit()
            return jsonify({'message': 'You have left the group!'}), 200
    else:
        return jsonify({'message': 'You are not a member of this group.'}), 400
    
# Delete or Edit a Group
@app.route('/groups/<int:group_id>', methods=['DELETE', 'PUT'])
@login_required
def manage_group(group_id):
    group = Group.query.get_or_404(group_id)

    if group.owner != current_user.id:
        return jsonify({'message': 'You are not authorized to manage this group.'}), 403

    if request.method == 'DELETE':
        # Delete the group
        try:
            db.session.delete(group)
            db.session.commit()
            return jsonify({'message': 'Group deleted successfully!'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Something went wrong. Please try again later.'}), 500

    elif request.method == 'PUT':
        # Edit the group
        try:
            data = request.get_json()
            group.name = data.get('name', group.name)
            group.description = data.get('description', group.description)
            group.is_public = data.get('is_public', group.is_public)

            db.session.commit()
            return jsonify({'message': 'Group updated successfully!'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': 'Something went wrong. Please try again later.'}), 500
    
# Search for Groups
@app.route('/groups/search', methods=['GET'])
@login_required
def search_groups():
    query = request.args.get('query', '').strip()
    
    if not query:
        return jsonify([]), 200

    groups = Group.query.filter(Group.is_public.is_(True), Group.name.ilike(f'%{query}%')).all()

    owners = {user.id: user.username for user in User.query.filter(User.id.in_([group.owner for group in groups])).all()}

    result = [{
        'id': group.id,
        'name': group.name,
        'description': group.description,
        'is_public': group.is_public,
        'owner': {'id': group.owner, 'username': owners.get(group.owner)},
        'members': [{'id': member.id, 'username': member.username} for member in group.members]
    } for group in groups]

    return jsonify(result), 200

##### Group Invitation Methods

# Send group invitation
@app.route('/groups/<int:group_id>/invite', methods=['POST'])
@login_required
def invite_to_group(group_id):
    group = Group.query.get_or_404(group_id)

    # Only group owner can send invitations
    if group.owner != current_user.id:
        return jsonify({'message': 'Only the group owner can send invitations.'}), 403

    data = request.get_json()
    recipient_id = data.get('recipient_id')

    if not recipient_id:
        return jsonify({'message': 'Recipient ID is required'}), 400

    recipient = User.query.get(recipient_id)
    if not recipient:
        return jsonify({'message': 'User not found'}), 404

    # Check if user is already a member
    if recipient in group.members:
        return jsonify({'message': 'User is already a member of this group'}), 400

    # Check if invitation already exists
    existing_invitation = GroupInvitation.query.filter_by(
        group_id=group_id,
        recipient_id=recipient_id,
        status='pending'
    ).first()

    if existing_invitation:
        return jsonify({'message': 'Invitation already sent to this user'}), 400

    # Create new invitation
    invitation = GroupInvitation(
        group_id=group_id,
        sender_id=current_user.id,
        recipient_id=recipient_id,
        status='pending'
    )

    db.session.add(invitation)
    db.session.commit()

    return jsonify({
        'message': 'Invitation sent successfully!',
        'invitation': {
            'id': invitation.id,
            'group_name': group.name,
            'recipient_username': recipient.username
        }
    }), 201

# Get user's received invitations
@app.route('/invitations', methods=['GET'])
@login_required
def get_invitations():
    invitations = GroupInvitation.query.filter_by(
        recipient_id=current_user.id,
        status='pending'
    ).all()

    result = []
    for inv in invitations:
        result.append({
            'id': inv.id,
            'group': {
                'id': inv.group.id,
                'name': inv.group.name,
                'description': inv.group.description
            },
            'sender': {
                'id': inv.sender.id,
                'username': inv.sender.username
            },
            'created_at': inv.created_at.isoformat() if inv.created_at else None
        })

    return jsonify(result), 200

# Accept invitation
@app.route('/invitations/<int:invitation_id>/accept', methods=['POST'])
@login_required
def accept_invitation(invitation_id):
    invitation = GroupInvitation.query.get_or_404(invitation_id)

    # Check if the invitation is for the current user
    if invitation.recipient_id != current_user.id:
        return jsonify({'message': 'This invitation is not for you.'}), 403

    if invitation.status != 'pending':
        return jsonify({'message': 'This invitation has already been processed.'}), 400

    # Add user to group
    group = invitation.group
    if current_user not in group.members:
        group.members.append(current_user)

    # Update invitation status
    invitation.status = 'accepted'

    db.session.commit()

    return jsonify({'message': 'Invitation accepted! You have joined the group.'}), 200

# Reject invitation
@app.route('/invitations/<int:invitation_id>/reject', methods=['POST'])
@login_required
def reject_invitation(invitation_id):
    invitation = GroupInvitation.query.get_or_404(invitation_id)

    # Check if the invitation is for the current user
    if invitation.recipient_id != current_user.id:
        return jsonify({'message': 'This invitation is not for you.'}), 403

    if invitation.status != 'pending':
        return jsonify({'message': 'This invitation has already been processed.'}), 400

    # Update invitation status
    invitation.status = 'rejected'

    db.session.commit()

    return jsonify({'message': 'Invitation rejected.'}), 200

# Get group's pending invitations (for group owner)
@app.route('/groups/<int:group_id>/invitations', methods=['GET'])
@login_required
def get_group_invitations(group_id):
    group = Group.query.get_or_404(group_id)

    # Only group owner can view invitations
    if group.owner != current_user.id:
        return jsonify({'message': 'Only the group owner can view invitations.'}), 403

    invitations = GroupInvitation.query.filter_by(
        group_id=group_id,
        status='pending'
    ).all()

    result = []
    for inv in invitations:
        result.append({
            'id': inv.id,
            'recipient': {
                'id': inv.recipient.id,
                'username': inv.recipient.username,
                'nickname': inv.recipient.nickname
            },
            'created_at': inv.created_at.isoformat() if inv.created_at else None
        })

    return jsonify(result), 200

# Cancel invitation (for group owner)
@app.route('/invitations/<int:invitation_id>/cancel', methods=['DELETE'])
@login_required
def cancel_invitation(invitation_id):
    invitation = GroupInvitation.query.get_or_404(invitation_id)

    # Check if the user is the group owner
    if invitation.group.owner != current_user.id:
        return jsonify({'message': 'Only the group owner can cancel invitations.'}), 403

    if invitation.status != 'pending':
        return jsonify({'message': 'Only pending invitations can be cancelled.'}), 400

    db.session.delete(invitation)
    db.session.commit()

    return jsonify({'message': 'Invitation cancelled.'}), 200

##### Others

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
    try:
        data = request.get_json()  # Get the request data from Vue.js

        email = data.get('email')
        if not email:
            return jsonify({'success': False, 'message': 'Email is required'}), 400

        user = User.query.filter_by(email=email).first()

        if user:
            # Generate password reset token
            token = serializer.dumps(email, salt='reset-password')
            
            # Create frontend URL for password reset
            # Check multiple headers to determine the frontend URL
            origin = request.headers.get('Origin')
            referer = request.headers.get('Referer')
            
            # Default to production URL
            frontend_url = "https://goalbond.netlify.app"
            
            # Check if request is from localhost
            if origin and ('localhost' in origin or '127.0.0.1' in origin):
                frontend_url = origin
            elif referer and ('localhost' in referer or '127.0.0.1' in referer):
                # Extract base URL from referer
                from urllib.parse import urlparse
                parsed = urlparse(referer)
                frontend_url = f"{parsed.scheme}://{parsed.netloc}"
            elif request.host and ('localhost' in request.host or '127.0.0.1' in request.host):
                # If backend is running locally, assume frontend is too
                frontend_url = "http://localhost:8080"
            
            reset_link = f"{frontend_url}/reset_password?token={token}"
            
            # Log for debugging
            app.logger.info(f"Password reset requested from: Origin={origin}, Referer={referer}, Host={request.host}")
            app.logger.info(f"Generated reset link: {reset_link}")

            # Send reset email
            msg = Message('Password Reset Request', recipients=[email])
            msg.html = f'''
            <html>
                <body>
                    <h2>Password Reset Request</h2>
                    <p>Hello,</p>
                    <p>You have requested to reset your password for your GoalBond account.</p>
                    <p>Please click the link below to reset your password:</p>
                    <p><a href="{reset_link}" style="background-color: #B03052; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block;">Reset Password</a></p>
                    <p>Or copy and paste this link into your browser:</p>
                    <p>{reset_link}</p>
                    <p>This link will expire in 1 hour.</p>
                    <p>If you did not request this password reset, please ignore this email.</p>
                    <p>Best regards,<br>The GoalBond Team</p>
                </body>
            </html>
            '''
            msg.body = f'''
Hello,

You have requested to reset your password for your GoalBond account.

Please click the link below to reset your password:
{reset_link}

This link will expire in 1 hour.

If you did not request this password reset, please ignore this email.

Best regards,
The GoalBond Team
            '''
            mail.send(msg)

            return jsonify({'success': True, 'message': 'A password reset link has been sent to your email.'})

        else:
            return jsonify({'success': False, 'message': 'No account found with that email address.'})

    except Exception as e:
        app.logger.error(f"Error in forgot_password route: {str(e)}")
        return jsonify({'success': False, 'message': 'Something went wrong. Please try again later.'}), 500
       
@app.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    try:
        try:
            email = serializer.loads(token, salt='reset-password', max_age=3600)
        except (SignatureExpired, BadSignature) as e:
            return jsonify({'success': False, 'message': 'Invalid or expired token.'}), 400

        user = User.query.filter_by(email=email).first()

        if not user:
            return jsonify({'success': False, 'message': 'User not found for the given email.'}), 400

        new_password = request.json.get('password')
        if not new_password:
            return jsonify({'success': False, 'message': 'New password is required.'}), 400

        user.set_password(new_password)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Your password has been updated!'}), 200

    except Exception as e:
        app.logger.error(f"Error in reset_password: {str(e)}")
        return jsonify({'success': False, 'message': 'Something went wrong. Please try again later.'}), 500

    
    
# Run the application
if __name__ == '__main__':
    app.run(debug=False)
