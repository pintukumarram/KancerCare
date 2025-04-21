import pickle
import os

def load_cancer_model(model_path):
    """Loads a machine learning model from the given file path."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    return model
