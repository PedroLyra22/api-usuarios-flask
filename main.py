from flask import Flask, request, jsonify
from app.repositories.repositories import UserRepository
from app.models.models import User
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return 'deu bom'

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    hashed_password = hashlib.sha256(data["password"].encode()).hexdigest()
    user = User(name=data["name"], email=data["email"], password=hashed_password)

    try:
        UserRepository.create(user)
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserRepository.find_by_id(user_id)

    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['GET'])
def get_all_users():
    users = UserRepository.find_all()
    return jsonify([user.__dict__ for user in users])

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = UserRepository.find_by_id(user_id)

    if user:
        return UserRepository.delete(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)