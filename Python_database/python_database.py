import sqlite3
from Python_Classes.classes import NewsFeedTool


class DatabaseManager:
    def __init__(self, database_path='news_feed.db'):
        self.database_path = database_path
        self.connection = self.create_connection()

    def create_connection(self):
        """Create a connection to the SQLite database."""
        connection = None
        try:
            connection = sqlite3.connect(self.database_path)
            print(f"Connected to the database: {self.database_path}")
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
        return connection

    def create_tables(self):
        """Create tables for different record types if they don't exist."""
        if self.connection:
            cursor = self.connection.cursor()

            # Create News table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    text TEXT,
                    city TEXT
                )
            ''')

            # Create Private Ad table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS private_ad (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    text TEXT,
                    expiration_date TEXT,
                    days_left INTEGER
                )
            ''')

            # Create Custom table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS custom (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    text TEXT,
                    custom_rule TEXT
                )
            ''')

            self.connection.commit()

    def save_news_record(self, timestamp, text, city):
        """Save a News record to the database."""
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO news (timestamp, text, city) VALUES (?, ?, ?)', (timestamp, text, city))
            self.connection.commit()

    def save_private_ad_record(self, timestamp, text, expiration_date, days_left):
        """Save a Private Ad record to the database."""
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO private_ad (timestamp, text, expiration_date, days_left) VALUES (?, ?, ?, ?)',
                           (timestamp, text, expiration_date, days_left))
            self.connection.commit()

    def save_custom_record(self, timestamp, text, custom_rule):
        """Save a Custom record to the database."""
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute('INSERT INTO custom (timestamp, text, custom_rule) VALUES (?, ?, ?)', (timestamp, text, custom_rule))
            self.connection.commit()

    def check_duplicate(self, table_name, field_name, value):
        """Check if a record with the same value already exists in the specified table and field."""
        if self.connection:
            cursor = self.connection.cursor()
            query = f'SELECT COUNT(*) FROM {table_name} WHERE {field_name} = ?'
            cursor.execute(query, (value,))
            count = cursor.fetchone()[0]
            return count > 0

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection to the database closed.")

# Example Usage:
news_feed_tool = NewsFeedTool()

# Initialize the DatabaseManager
db_manager = DatabaseManager()

# Create tables for different record types if they don't exist
db_manager.create_tables()

# Add some records
news_feed_tool.add_news("News about", "Minsk")
news_feed_tool.add_private_ad("Special Offer", "2024-01-15")
news_feed_tool.add_custom_record("Custom Record", "Unique Custom Record")

# Process records from the file and remove the file
news_feed_tool.process_file_records()

# Save records to the database
news_records = news_feed_tool.get_news_records()
private_ad_records = news_feed_tool.get_private_ad_records()
custom_records = news_feed_tool.get_custom_records()

for record in news_records:
    if not db_manager.check_duplicate('news', 'text', record['text']):
        db_manager.save_news_record(record['timestamp'], record['text'], record['city'])
    else:
        print(f"Duplicate record found for News: {record}")

for record in private_ad_records:
    if not db_manager.check_duplicate('private_ad', 'text', record['text']):
        db_manager.save_private_ad_record(record['timestamp'], record['text'], record['expiration_date'], record['days_left'])
    else:
        print(f"Duplicate record found for Private Ad: {record}")

for record in custom_records:
    if not db_manager.check_duplicate('custom', 'text', record['text']):
        db_manager.save_custom_record(record['timestamp'], record['text'], record['custom_rule'])
    else:
        print(f"Duplicate record found for Custom: {record}")

# Close the database connection
db_manager.close_connection()
