from flask import Blueprint, render_template, request
import joblib
import numpy as np

breast_routes = Blueprint('breast_routes', __name__)

# Load models
detection_model = joblib.load("models/breast/breast_cancer__model.pkl")
stage_model = joblib.load("models/breast/breast_stage_model.pkl")

@breast_routes.route("/")
def breast_home():
    """
    Render the Breast Cancer Prediction form.
    """
    return render_template("breast.html")

@breast_routes.route("/predict", methods=["POST"])
def predict_breast():
    try:
        # Ensure all 15 features are extracted
        feature_keys = [
            "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
            "smoothness_mean", "compactness_mean", "concavity_mean", 
            "concave_points_mean", "symmetry_mean", "radius_worst", 
            "texture_worst", "perimeter_worst", "area_worst", 
            "smoothness_worst", "compactness_worst"
        ]
        features = [float(request.form[key]) for key in feature_keys]
        features_array = np.array([features])

        # Make predictions
        cancer_prediction = detection_model.predict(features_array)[0]
        stage_prediction = stage_model.predict(features_array)[0]

        # Send results to result page
        return render_template("result.html", cancer=cancer_prediction, stage=stage_prediction)
    except Exception as e:
        return render_template("error.html", message=f"An error occurred: {str(e)}")
