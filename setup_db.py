import mysql.connector
from db_config import DB_CONFIG

def setup_database():
    # 1. Connect to MySQL Server (without selecting a DB yet)
    config_root = DB_CONFIG.copy()
    if 'database' in config_root:
        del config_root['database']

    print("Connecting to MySQL Server...")
    try:
        conn = mysql.connector.connect(**config_root)
        if conn.is_connected():
            print("Connected successfully.")
            cursor = conn.cursor()

            # 2. Read the schema.sql file
            print("Reading schema.sql...")
            with open('schema.sql', 'r') as f:
                sql_file = f.read()

            # 3. Execute each command
            commands = sql_file.split(';')
            
            for command in commands:
                if command.strip():
                    try:
                        cursor.execute(command)
                        print(f"Executed command: {command[:40]}...")
                    except mysql.connector.Error as err:
                        print(f"Warning/Error: {err}")

            conn.commit()
            print("\n✅ Database and Tables created successfully!")
            
            cursor.close()
            conn.close()
            
    except mysql.connector.Error as err:
        print(f"❌ Connection Error: {err}")
        print("Please check your password in db_config.py")

if __name__ == "__main__":
    setup_database()
