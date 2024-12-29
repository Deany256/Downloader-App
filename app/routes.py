from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        url = request.form["url"]
        video_details = {
            'url': url,
            'title': 'Sample Video',
            'thumbnail': 'https://via.placeholder.com/150'
        }
        return redirect(url_for('main.download', **video_details))
    return render_template("dashboard.html")

@main_bp.route("/download")
@login_required
def download():
    video_details = {
        'title': request.args.get('title'),
        'thumbnail': request.args.get('thumbnail'),
        'url': request.args.get('url')
    }
    return render_template("download.html", video=video_details)