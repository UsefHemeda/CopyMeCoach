from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False,)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)

class StudentAnswers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    style = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.foreignkey("user.id"))
