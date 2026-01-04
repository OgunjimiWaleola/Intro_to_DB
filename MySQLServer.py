#!/usr/bin/python3
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)

finally:
    try:
        cursor.close()
        connection.close()
    except Exception:
        pass
