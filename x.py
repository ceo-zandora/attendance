import sqlite3
import sys

# Connect to the database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT statement to get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

# Fetch the table names
table_names = cursor.fetchall()

# Redirect standard output to a file
sys.stdout = open('out.txt', 'w')

# Loop through the table names
for table in table_names:
    # Execute a SELECT statement to get all data from the table
    cursor.execute("SELECT * FROM {}".format(table[0]))
    # Fetch the data
    rows = cursor.fetchall()
    # Print the table name and data
    print("Table: {}".format(table[0]))
    for row in rows:
        print(row)

# Close the cursor and connection
cursor.close()
conn.close()

# Restore standard output
sys.stdout = sys.__stdout__
