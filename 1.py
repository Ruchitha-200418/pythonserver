from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',              # your MySQL username
    'password': '',  # your MySQL password
    'database': 'userform_db'    # database you created
}

@app.route('/')
def index():
    return render_template('2''.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Connect to MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert data into table
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()

    cursor.close()
    conn.close()

    return f"<h2>Data Saved ✅</h2><p>Name: {name}</p><p>Email: {email}</p>"

@app.route('/users')
def users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Fetch all users
    cursor.execute("SELECT id, name, email FROM users")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    # Display results in simple HTML
    rows = "".join([f"<p>{u[0]} | {u[1]} | {u[2]}</p>" for u in data])
    return f"<h2>All Users</h2>{rows}"

if __name__ == '__main__':
    app.run(debug=True)
