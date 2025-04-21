from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from models import db, History
from utils.load_model import load_cancer_model


common_routes = Blueprint('common_routes', __name__)

@common_routes.route('/predict', methods=['POST'])
@login_required
def predict():
    cancer_type = request.form.get('cancer_type')
    input_data = request.form.to_dict()

    model = load_cancer_model(cancer_type)
    prediction = model.predict([list(map(float, input_data.values()))])[0]

    history_entry = History(
        user_id=current_user.id,
        cancer_type=cancer_type,
        input_data=str(input_data),
        prediction_result=str(prediction)
    )
    db.session.add(history_entry)
    db.session.commit()

    return render_template('result.html', prediction=prediction)

@common_routes.route('/history')
@login_required
def history():
    user_history = History.query.filter_by(user_id=current_user.id).order_by(History.timestamp.desc()).all()
    return render_template('history.html', history=user_history)
