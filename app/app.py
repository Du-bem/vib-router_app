from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages


DATABASE = "db/database.db"

@app.route("/")
def home():
    if "user" in session:
        return render_template("home_logged_in.html", user=session["user"])
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session["user"] = email
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials. Please try again.", "danger")
    return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    flash("Logged out successfully!", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)