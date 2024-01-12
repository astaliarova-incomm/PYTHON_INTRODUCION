import json
import os

class RecordProvider:
    def __init__(self, file_path='records.json'):
        self.file_path = file_path

    def read_json_records(self):
        """Read records from a JSON file and return a list."""
        records = []
        try:
            with open(self.file_path, 'r') as json_file:
                data = json.load(json_file)
                if isinstance(data, list):
                    records = data
                elif isinstance(data, dict):
                    records.append(data)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        return records

    def remove_file(self):
        """Remove the file if it exists."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

class NewsFeedTool:
    # ... (previous implementation)

    def process_json_records(self, record_provider):
        """Process records from a JSON file."""
        records = record_provider.read_json_records()

        # Process records here
        for record in records:
            print(f"Processing JSON record: {record}")

        # Remove the file after processing
        record_provider.remove_file()

# Example Usage:
news_feed_tool = NewsFeedTool()

# Add some records
news_feed_tool.add_news("News about", "Minsk")
news_feed_tool.add_private_ad("Special Offer", "2024-01-15")
news_feed_tool.add_custom_record("Custom Record", "Unique Custom Record")

# Create a RecordProvider instance and write records to a JSON file
json_record_provider = RecordProvider('records.json')
json_records = [
    {"type": "News", "text": "Breaking News", "city": "New York"},
    {"type": "Private Ad", "text": "Limited Time Offer", "expiration_date": "2024-01-20"},
    {"type": "Custom", "text": "Custom Record", "custom_rule": "New Rule"}
]
with open('records.json', 'w') as json_file:
    json.dump(json_records, json_file)

# Process records from the JSON file and remove the file
news_feed_tool.process_json_records(json_record_provider)
