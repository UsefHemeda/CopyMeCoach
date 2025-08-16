from flask import Flask, redirect, request, jsonify, render_template
from models import db, User
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

#intialize flask
app = Flask(__name__, template_folder=os.path.join("..", "frontend", "templates"), static_folder=os.path.join("..", "frontend"))

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

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

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
