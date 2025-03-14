from config import get_db_connection
from app.models.models import User
from flask import jsonify


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
    def find_by_email(user_email):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, (user_email,))
            row = cursor.fetchone()
        connection.close()
        return User(*row) if row else None

    @staticmethod
    def find_all():
        connection = get_db_connection()
        users = []
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users LIMIT 25"
            cursor.execute(sql)
            rows = cursor.fetchall()
        connection.close()

        return [User(*row) for row in rows] if rows else []

    @staticmethod
    def delete(user):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = f"DELETE FROM users WHERE id = {user.id}"
            cursor.execute(sql)
            connection.commit()
        connection.close()

        return jsonify({"message": "User deleted successfully"}), 200

    @staticmethod
    def update(user):
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "UPDATE users SET email = %s WHERE id = %s"
            cursor.execute(sql, (user.email, user.id))
            connection.commit()
        connection.close()

        return jsonify({"message": "User update successfully"}), 200

