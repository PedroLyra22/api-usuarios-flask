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

if __name__ == '__main__':
    app.run(debug=True)