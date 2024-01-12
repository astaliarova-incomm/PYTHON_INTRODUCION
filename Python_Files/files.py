import datetime
import os

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_records(self):
        """Read records from the file and return a list."""
        records = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                records = file.readlines()
        return records

    def remove_file(self):
        """Remove the file if it exists."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

class NewsFeedTool:
    def __init__(self, file_path='news_feed.txt'):
        self.file_path = file_path
        self.file_reader = FileReader(file_path)

    def add_news(self, text, city):
        """Add a News record to the feed."""
        record_type = 'News'
        timestamp = self.get_current_timestamp()
        data = f"{timestamp} - {record_type}: {text}, City: {city}\n"
        self.write_to_file(data)

    def add_private_ad(self, text, expiration_date):
        """Add a Private Ad record to the feed."""
        record_type = 'Private Ad'
        days_left = self.calculate_days_left(expiration_date)
        timestamp = self.get_current_timestamp()
        data = f"{timestamp} - {record_type}: {text}, Expiration Date: {expiration_date}, Days Left: {days_left}\n"
        self.write_to_file(data)

    def add_custom_record(self, text, custom_rule):
        """Add a Custom record to the feed with a unique publishing rule."""
        record_type = 'Custom'
        timestamp = self.get_current_timestamp()
        data = f"{timestamp} - {record_type}: {text}, Custom Rule: {custom_rule}\n"
        self.write_to_file(data)

    def get_current_timestamp(self):
        """Get the current timestamp in the required format."""
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def calculate_days_left(self, expiration_date):
        """Calculate the number of days left until the expiration date."""
        today = datetime.date.today()
        expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
        days_left = (expiration_date - today).days
        return max(0, days_left)


    def write_to_file(self, data):
        """Write the data to the end of the file."""
        with open(self.file_path, 'a') as file:
            file.write(data)

    def process_file_records(self):
        """Process records from the file and remove the file."""
        records = self.file_reader.read_records()
        for record in records:
            # Process each record as needed
            print(f"Processing record: {record.strip()}")

        # Remove the file after processing
        self.file_reader.remove_file()

# Example Usage:
news_feed_tool = NewsFeedTool()

# Add some records
news_feed_tool.add_news("News about", "Minsk")
news_feed_tool.add_private_ad("Special Offer", "2024-01-15")
news_feed_tool.add_custom_record("Custom Record", "Unique Custom Record")

# Process records from the file and remove the file
news_feed_tool.process_file_records()
