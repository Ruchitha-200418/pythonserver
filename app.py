from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # your MySQL username
        password="",  # your MySQL password
        database="studentdb"      # your database name
    )


# ---------- Home Page ----------
@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template("index.html", students=students)


# ---------- Add Student ----------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        birthday = request.form["birthday"]
        phone = request.form["phone"]
        course = request.form["course"]
        address = request.form["address"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (name, email, birthday, phone, course, address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, email, birthday, phone, course, address))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("add.html")


# ---------- Edit Student ----------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        birthday = request.form["birthday"]
        phone = request.form["phone"]
        course = request.form["course"]
        address = request.form["address"]

        cursor.execute("""
            UPDATE students
            SET name=%s, email=%s, birthday=%s, phone=%s, course=%s, address=%s
            WHERE id=%s
        """, (name, email, birthday, phone, course, address, id))

        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    conn.close()
    return render_template("edit.html", student=student)


# ---------- Delete Student ----------
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
