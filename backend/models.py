from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  # Import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Association table for the many-to-many relationship between users and groups
user_groups = db.Table('user_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class User(UserMixin, db.Model):  # Inherit from UserMixin
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)  # VARCHAR(64)
    email = db.Column(db.String(128), unique=True, nullable=False)     # VARCHAR(128)
    nickname = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(512), nullable=False)

    # Update the relationship to use back_populates
    groups = db.relationship('Group', secondary=user_groups, back_populates='members')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Goal(db.Model):
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=True)  # Allow goals to be associated with groups
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    deadline = db.Column(db.DateTime, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(100), nullable=False)

    # New columns for season and episode
    season = db.Column(db.Integer, nullable=True)
    episode = db.Column(db.Integer, nullable=True)
    
    # Progress tracking
    progress = db.Column(db.Integer, default=0)  # Progress percentage (0-100)

    # Relationship to group for eager loading
    group = db.relationship('Group', backref='group_goals', lazy='joined')
    
    def to_dict(self):
        group_data = None
        if self.group:
            group_data = {
                'id': self.group.id,
                'name': self.group.name,
                'members': [{'id': member.id, 'username': member.username} for member in self.group.members]
            }
        
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,  # Convert to ISO format
            'group_id': self.group_id,  # Include group_id here
            'deadline': self.deadline.isoformat() if self.deadline else None,        # Convert to ISO format
            'completed': self.completed,
            'has_deadline': self.deadline is not None,  # Check if deadline is set
            'is_group_goal': self.group_id is not None,  # Check if the goal is associated with a group
            'group': group_data,  # Include group data if applicable
            'category': self.category,
            'season': self.season,  # Include season if applicable
            'episode': self.episode,  # Include episode if applicable
            'progress': self.progress,  # Include progress percentage
        }

class Group(db.Model):
        __tablename__ = 'groups'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        owner = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        description = db.Column(db.Text, nullable=True)
        is_public = db.Column(db.Boolean, default=False)  # Public groups can be seen by other users, private groups require invitation

        # Update the relationship to use back_populates
        members = db.relationship('User', secondary=user_groups, back_populates='groups')
