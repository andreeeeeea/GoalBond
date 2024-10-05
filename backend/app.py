from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Goal
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db.init_app(app)

# Initialize the database
with app.app_context():
    db.create_all()

# Create a User
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'message': 'Missing username or email'}), 400

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201


# Get all Users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200
# Create a Goal
@app.route('/goals', methods=['POST'])
def create_goal():
    data = request.get_json()
    new_goal = Goal(title=data['title'], description=data['description'], user_id=data['user_id'])
    db.session.add(new_goal)
    db.session.commit()
    return jsonify(new_goal.to_dict()), 201

# Get all Goals
@app.route('/goals', methods=['GET'])
def get_goals():
    goals = Goal.query.all()
    return jsonify([goal.to_dict() for goal in goals]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
