import mysql.connector
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"


# ---------- MySQL Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # change if needed
        user="root",  # your MySQL username
        password="",  # your MySQL password
        database="userdb"
    )


# ---------- HTML Templates ----------
login_page = """
<!DOCTYPE html>
<html>
<head><title>Login Page</title></head>
<body>
    <h2>Login</h2>
    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>

        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

admin_page = """
<h2>Welcome {{ session['username'] }} (Admin)</h2>
<p>This is the Admin Dashboard.</p>
<a href="{{ url_for('logout') }}">Logout</a>
"""

manager_page = """
<h2>Welcome {{ session['username'] }} (Manager)</h2>
<p>This is the Manager Dashboard.</p>
<a href="{{ url_for('logout') }}">Logout</a>
"""

user_page = """
<h2>Welcome {{ session['username'] }} (User)</h2>
<p>This is the User Dashboard.</p>
<a href="{{ url_for('logout') }}">Logout</a>
"""


# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and user["password"] == password:
            session["username"] = user["username"]
            session["role"] = user["role"]

            # Redirect based on role
            if user["role"] == "Admin":
                return redirect(url_for("admin_dashboard"))
            elif user["role"] == "Manager":
                return redirect(url_for("manager_dashboard"))
            else:
                return redirect(url_for("user_dashboard"))
        else:
            return render_template_string(login_page, error="Invalid credentials!")

    return render_template_string(login_page)


@app.route("/admin")
def admin_dashboard():
    if "role" in session and session["role"] == "Admin":
        return render_template_string(admin_page)
    return redirect(url_for("login"))


@app.route("/manager")
def manager_dashboard():
    if "role" in session and session["role"] == "Manager":
        return render_template_string(manager_page)
    return redirect(url_for("login"))


@app.route("/user")
def user_dashboard():
    if "role" in session and session["role"] == "User":
        return render_template_string(user_page)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
