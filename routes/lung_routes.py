from flask import Blueprint, render_template, request
import joblib
import numpy as np

# Define Blueprint
lung_routes = Blueprint('lung_routes', __name__)

# Load the models
lung_cancer_model = joblib.load("models/lung/lung_cancer_prediction_model.pkl")
lung_stage_model = joblib.load("models/lung/lung_stage_prediction_model.pkl")

@lung_routes.route("/")
def lung_home():
    """Render the lung cancer prediction home page."""
    return render_template("lung.html")

@lung_routes.route("/predict", methods=["POST"])
def predict_lung():
    """Handle lung cancer and stage predictions."""
    try:
        # Extract features from the form
        features = [float(request.form[key]) for key in request.form.keys()]
        features_array = np.array([features])

        # Predictions
        cancer_prediction = lung_cancer_model.predict(features_array)[0]
        stage_prediction = lung_stage_model.predict(features_array)[0]

        # Render result page
        return render_template(
            "result.html",
            cancer=cancer_prediction,
            stage=stage_prediction,
            disease="Lung Cancer"
        )
    except Exception as e:
        # Render an error page in case of failure
        return render_template("error.html", message=str(e))
