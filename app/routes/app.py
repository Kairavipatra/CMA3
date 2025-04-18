from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

db = SQLAlchemy()

app_bp = Blueprint('app', __name__)

@app_bp.route('/')
def home():
    return render_template('index.html')

@app_bp.route('/blog.html')
def blog():
    return render_template('blog.html')

@app_bp.route('/contact.html')
def contact():
    return render_template('contact.html')

@app_bp.route('/dog-walking.html')
def dog_walking():
    return render_template('dog-walking.html')

@app_bp.route('/food.html')
def food():
    return render_template('food.html')

@app_bp.route('/grooming.html')
def grooming():
    return render_template('grooming.html')

@app_bp.route('/services.html')
def services():
    return render_template('services.html')

@app_bp.route('/shop.html')
def shop():
    return render_template('shop.html')

@app_bp.route('/toys.html')
def toys():
    return render_template('toys.html')

@app_bp.route('/vet.html')
def vet():
    return render_template('vet.html')

@app_bp.route('/foster-care.html')
def foster_care():
    return render_template('foster-care.html')

# ✅ Create the Flask app
app = Flask(__name__)
app.config.from_object('config.Config')  # Make sure your config points to PostgreSQL

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(app_bp)

# ✅ Apply migrations at startup (works on free Render plan)
if __name__ == '__main__':
    with app.app_context():
        upgrade()  # This runs "flask db upgrade"
    app.run(debug=True)
