from flask import Flask, render_template
from routes.breast_routes import breast_routes
from routes.lung_routes import lung_routes
from routes.prostate_routes import prostate_routes
from routes.colorectal_routes import colorectal_routes

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(breast_routes, url_prefix='/breast')
app.register_blueprint(lung_routes, url_prefix='/lung')
app.register_blueprint(prostate_routes, url_prefix='/prostate')
app.register_blueprint(colorectal_routes, url_prefix='/colorectal')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
