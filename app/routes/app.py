from flask import Flask, Blueprint, render_template

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

# ✅ Create and register the Flask app
app = Flask(__name__)
app.register_blueprint(app_bp)
if __name__ == '__main__':
    app.run(debug=True)

