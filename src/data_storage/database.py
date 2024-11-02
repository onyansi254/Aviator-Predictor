import sqlite3  # Import SQLite for database operations

class Database:
    def __init__(self, db_name="aviator_data.db"):
        self.connection = sqlite3.connect(db_name)  # Connect to the database
        self.cursor = self.connection.cursor()  # Create a cursor for executing SQL commands
        self.create_table()  # Create the table if it doesn't exist

    def create_table(self):
        # SQL command to create the aviator_data table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS aviator_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each record
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Record insertion time
                crash_value REAL  -- Store crash-related data
            )
        ''')
        self.connection.commit()  # Save changes to the database

    def insert_data(self, crash_value):
        self.cursor.execute('INSERT INTO aviator_data (crash_value) VALUES (?)', (crash_value,))
        self.connection.commit()  # Save the change

    def get_data(self):
        self.cursor.execute('SELECT crash_value FROM aviator_data ORDER BY timestamp DESC LIMIT 100')
        return self.cursor.fetchall()  # Return the results as a list of tuples

    def close(self):
        self.connection.close()  # Close the database connection
