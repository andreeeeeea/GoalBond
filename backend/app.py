from dotenv import load_dotenv
import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from flask_cors import CORS

# Import models
from models import db, User, Goal

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = 'BellaEOpisicaGrasa2000'  # Change this to a strong secret key

# Enable CORS
cors = CORS()
cors.init_app(app, resources={r"/*": {"origins": "*"}})
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize the database
with app.app_context():
    db.create_all()  # Ensure all tables are created

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# User Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username, email=email)
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

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):  # Adjust based on how you hash passwords
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid username or password"}), 401


# User Logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful!'}), 200

# Create a Goal
@app.route('/goals', methods=['POST'])
def create_goal():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    user_id = data.get('user_id')  # User ID to associate the goal with a user

    if not title or not user_id:
        return jsonify({'message': 'Missing title or user_id'}), 400

    # Check if the user exists
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    # Create the new goal
    new_goal = Goal(title=title, description=description, user_id=user_id)
    db.session.add(new_goal)
    db.session.commit()

    return jsonify({'message': 'Goal created successfully!'}), 201

# Get all Goals
@app.route('/goals', methods=['GET'])
def get_goals():
    user_id = request.args.get('user_id')  # Optional user ID to filter goals by user

    if user_id:
        # Filter goals by user
        goals = Goal.query.filter_by(user_id=user_id).all()
        if not goals:
            return jsonify({'message': 'No goals found for this user'}), 404
    else:
        # Retrieve all goals
        goals = Goal.query.all()

    return jsonify([{
        'id': goal.id,
        'title': goal.title,
        'description': goal.description,
        'user_id': goal.user_id
    } for goal in goals]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
