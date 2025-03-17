import json

class UserService:
    @staticmethod
    def check_login(user, login, password):
        check_login = user.email == login
        check_password = user.password == password

        login = {'user':json.dumps(user.__dict__), 'check':False}

        if check_login and check_password:
            login['check'] = True
            return login
        else:
            return login
