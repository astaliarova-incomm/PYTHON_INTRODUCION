import datetime

class NewsFeedTool:
    def __init__(self, file_path='news_feed.txt'):
        self.file_path = file_path

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

# Example Usage:
news_feed_tool = NewsFeedTool()

# Add a News record
news_feed_tool.add_news("News about", "Minsk")

# Add a Private Ad record
news_feed_tool.add_private_ad("Special Offer", "2024-01-15")

# Add a Custom record
news_feed_tool.add_custom_record("Custom Record", "Unique Custom Record")

# Display the contents of the file
with open('news_feed.txt', 'r') as file:
    contents = file.read()
    print(contents)
