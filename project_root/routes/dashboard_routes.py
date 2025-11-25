import os
from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from models.database import db
from models.file_model import File
from werkzeug.utils import secure_filename


dashboard_bp = Blueprint('dashboard',__name__, url_prefix="/dashboard")



@dashboard_bp.route("/")
def dashboard_home():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    
    #Get all uploaded files
    files = File.query.order_by(File.upload_time.desc()).all()

    return render_template("dashboard.html", username=session.get('username'), files=files)

@dashboard_bp.route("/view/<int:file_id>")
def view_file(file_id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    
    #Find file record
    file_rec = File.query.get(file_id)
    if not file_rec:
        if not file_rec:
            return "File not found"
        
    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], file_rec.filename)

    #Load file
    from data_processing.file_reader import load_file
    from data_processing.auto_charts import make_chart_data

    df = load_file(filepath)
    if df is None:
        return "Error loading file"
    
    charts = make_chart_data(df)

    #Send to frontend
    return render_template("charts.html", charts=charts, filename=file_rec.filename)

@dashboard_bp.route("/upload", methods=["GET", "POST"])
def upload_file():
    ...