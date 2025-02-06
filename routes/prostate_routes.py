from flask import Blueprint, render_template, request
import joblib
import numpy as np

# Define Blueprint
prostate_routes = Blueprint('prostate_routes ', __name__)

# Load the models
# prostate_cancer_model = joblib.load("models/prostate/prostate_cancer_prediction_model.pkl")
# prostate_stage_model = joblib.load("models/prostate/prostate_stage_prediction_model.pkl")

@prostate_routes .route("/")
def prostate_home():
    """Render the prostate cancer prediction home page."""
    return render_template("prostate.html")

@prostate_routes.route("/predict", methods=["POST"])
def predict_lung():
    """Handle prostate cancer and stage predictions."""
    try:
        # Extract features from the form
        features = [float(request.form[key]) for key in request.form.keys()]
        features_array = np.array([features])

        # Predictions
        cancer_prediction = prostate_cancer_model.predict(features_array)[0]
        stage_prediction = prostate_stage_model.predict(features_array)[0]

        # Render result page
        return render_template(
            "result.html",
            cancer=cancer_prediction,
            stage=stage_prediction,
            disease="Prostate Cancer"
        )
    except Exception as e:
        # Render an error page in case of failure
        return render_template("error.html", message=str(e))
