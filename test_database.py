#Create a test script to confirm the database works

from src.data_storage.database import Database

db = Database()
db.insert_data(5.67)  # Insert a test crash value
print("Data:", db.get_data())  # Retrieve and print data to confirm
db.close()



# run: python test_database.py

