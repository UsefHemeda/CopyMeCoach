from flask import Flask, redirect, request, jsonify, render_template
from models import db, User
from openai import OpenAI
from dotenv import load_dotenv
import os

<<<<<<< HEAD
load_dotenv()
=======
load_dotenv() # <-- reads .env and loads variables into the environment
>>>>>>> f90ae11fc1d0a0fe394983bb9b3d8dc3436fde9f

app = Flask(
    __name__,
    template_folder=os.path.join("..", "frontend", "templates"),
    static_folder=os.path.join("..", "frontend")
)

# Database Creation
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///copyme.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Create an OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# App routes
@app.route("/")
def home():
    return render_template("home.html")

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
