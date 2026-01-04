#!/usr/bin/python3
"""
Creates the database alx_book_store in a MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # CONNECT TO MYSQL SERVER
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # replace with your MySQL password if any
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # CREATE DATABASE (NO SELECT OR SHOW USED)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # CLOSE CONNECTION
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
