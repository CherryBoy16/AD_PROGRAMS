from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import sqlite3
import pickle
import pyttsx3
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

app.secret_key = "your_secret_key"

# Load the trained model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for("login"))
    return render_template("signup.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session["user"] = username
            return redirect(url_for("verify"))
        else:
            return "Invalid credentials"
    return render_template("login.html")

# Verification route
@app.route("/verify", methods=["GET", "POST"])
def verify():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        headline = request.form["headline"]
        tfidf = vectorizer.transform([headline])
        prediction = model.predict(tfidf)[0]
        return render_template("result.html", headline=headline, prediction=prediction)
    return render_template("verify.html")

# Voice summary route
@app.route("/voice_summary", methods=["POST"])
def voice_summary():
    headline = request.json["headline"]
    summary = f"The headline is: {headline}"  # Mock summary (can be enhanced with NLP summarizers)
    engine = pyttsx3.init()
    engine.say(summary)
    engine.runAndWait()
    return jsonify({"message": "Summary spoken!"})

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
