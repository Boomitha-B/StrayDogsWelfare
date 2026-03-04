import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG

def test_connection():
    print("Testing connection to MySQL...")
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record[0]}")
            cursor.close()
            connection.close()
            print("Connection test PASSED!")
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        print("ACTION REQUIRED: Please check your 'db_config.py' file and ensure your MySQL server is running.")

if __name__ == "__main__":
    test_connection()
