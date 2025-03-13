from flask import jsonify

class UserService:
    @staticmethod
    def check_login(user, login, password):
        check_login = user.email == login
        check_password = user.password == password

        if check_login and check_password:
            return jsonify({"message": "Login and password ok"}), 200
        else:
            return jsonify({"message": "Login and password dont match"}), 403
