from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user_model import User
from models.database import db


auth_bp = Blueprint('auth',__name__, url_prefix="/auth")

#registrqation route 
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        existing = User.query.filter_by(username=username).first()
        if existing:
            return render_template("register.html", error="Username already exists")
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    return render_template("register.html")

#Login Route
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        #Find user
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session["user_id"]= user.id
            session['username'] = user.username
            return redirect(url_for("dashboard.home"))
        else:
            return render_template("login.html", error="Invalid username or password")
        
    return render_template("login.html")