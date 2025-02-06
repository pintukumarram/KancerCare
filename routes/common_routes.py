from flask import Blueprint, render_template

common_routes = Blueprint('common_routes', __name__)

@common_routes.route("/history")
def history():
    # Load history from database or file
    history_data = []  # Example data
    return render_template("history.html", history=history_data)

@common_routes.route("/result")
def result():
    # Placeholder for result redirection
    return render_template("result.html")
