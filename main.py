import csv
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ohlc_db']
collection = db['ohlc_collection']
file_path = "./stockData.csv"

# Read CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read the header row
    # Iterate over each row in the CSV file
    for row in reader:
        # Create a new document for each row
        document = {
            'epoch':float(row[1]),
            'date': row[2],
            'open': float(row[3]),
            'high': float(row[4]),
            'low': float(row[5]),
            'close': float(row[6]),
            'volume':float(row[7])
        }
        # Insert the document into the collection
        collection.insert_one(document)

# Close the MongoDB connection
client.close()
