from flask import request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from Backend.app_init import app
from Backend.database import init_db


mongo = init_db(app)

def signup():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if not email or not username or not password:
        return jsonify({"message": "Missing fields!"}), 400

    existing_user = mongo.db.users.find_one({"email": email})
    if existing_user:
        return jsonify({"message": "Email already exists!"}), 400

    hashed_password = generate_password_hash(password)

    mongo.db.users.insert_one({
        "email": email,
        "username": username,
        "password": hashed_password
    })

    return jsonify({"message": "User registered successfully!"}), 201

def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = mongo.db.users.find_one({"email": email})
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "Invalid credentials!"}), 401

    session['user_id'] = str(user['_id'])
    return jsonify({"message": "Login successful!"}), 200

def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully!"}), 200
