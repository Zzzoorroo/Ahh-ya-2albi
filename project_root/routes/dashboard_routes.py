from flask import Blueprint, render_template, session, redirect, url_for, request, current_app
from werkzeug.utils import secure_filename
import os

from models.file_model import File
from models.database import db

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    files = File.query.all()
    return render_template("dashboard.html", files=files)


@dashboard_bp.route("/upload", methods=["GET", "POST"])
def upload():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        uploaded_file = request.files.get("file")
        if not uploaded_file:
            return render_template("upload.html", error="No file selected")

        filename = secure_filename(uploaded_file.filename)
        save_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        uploaded_file.save(save_path)

        # Save in DB
        file = File(filename=filename)
        db.session.add(file)
        db.session.commit()

        return redirect(url_for("dashboard.home"))

    return render_template("upload.html")

@dashboard_bp.route("/view/<int:file_id>")
def view_file(file_id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    

    file_record = File.query.get(file_id)
    if not file_record:
        return "File not found"
    
    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], file_record.filename)

    from data_processing.file_reader import load_file
    from data_processing.auto_charts import make_chart_data

    df = load_file(filepath)
    charts = make_chart_data(df)


    return render_template("charts.html", charts=charts, filename = file_record.filename)