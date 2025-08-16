from flask import Flask, redirect, request, jsonify, render_template, flash, url_for
from models import db, User
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv() # Load environment variables from .env file


app = Flask(__name__)

# Create an OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Database Creation
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///copyme.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()


# App routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.form == "POST":
        data = request.form
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")
        password = data.get("password")

        if User.query.filter_by(email = email).first():
            flash("Email alraedy registered!")
            return redirect(url_for("signup"))
        
        new_user = User(name = name, email = email, age = age)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    student_text = data.get("text", "")
    preferred_style = data.get("style", "casual")
    id = data.get("id", "")

    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a helpful coach. Respond in a {preferred_style} style."},
            {"role": "user", "content": student_text}
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)