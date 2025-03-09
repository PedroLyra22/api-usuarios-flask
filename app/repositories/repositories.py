from config import get_db_connection
from app.models.models import User


class UserRepository:
    @staticmethod
    def create(user):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user.name, user.email, user.password))
            connection.commit()
        connection.close()

    @staticmethod
    def find_by_id(user_id):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(sql, (user_id,))
            row = cursor.fetchone()
        connection.close()
        return User(*row) if row else None

    @staticmethod
    def delete(user):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, (user.id,))
            connection.commit()
        connection.close()
