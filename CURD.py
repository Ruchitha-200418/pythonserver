import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="your_database"
)


# Create
cursor.callproc('CreateUser', ('John Doe', 'john@example.com'))
conn.commit()

# Read
cursor.callproc('ReadUsers')
for result in cursor.stored_results():
    rows = result.fetchall()
    for row in rows:
        print(row)

# Update
cursor.callproc('UpdateUser', (1, 'John Smith', 'johnsmith@example.com'))
conn.commit()

# Delete
cursor.callproc('DeleteUser', (1,))
conn.commit()

cursor.close()
conn.close()



