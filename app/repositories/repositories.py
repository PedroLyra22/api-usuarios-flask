from config import get_db_connection

class UserRepository:
    @staticmethod
    def create(user):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user.name, user.email, user.password))
            connection.commit()
        connection.close()