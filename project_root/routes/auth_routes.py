from flask import Blueprint, render_template, request, redirect, url_for
from models.user_model import User
from models.database import db


auth_bp = Blueprint('auth',__name__, url_prefix="/auth")

#registrqation route 
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    
    return render_template("register.html")

#Login Route
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #TODO : add athentification logic here
        pass
    return render_template("login.html")