from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  # Import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):  # Inherit from UserMixin
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)  # VARCHAR(64)
    email = db.Column(db.String(128), unique=True, nullable=False)     # VARCHAR(128)
    password = db.Column(db.String(512), nullable=False)       

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
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    deadline = db.Column(db.DateTime, nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,  # Convert to ISO format
            'deadline': self.deadline.isoformat() if self.deadline else None,        # Convert to ISO format
            'completed': self.completed,
            'has_deadline': self.deadline is not None  # Check if deadline is set
        }
    
    
    




