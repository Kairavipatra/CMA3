import os
from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render injects PORT env variable.
    app.run(host='0.0.0.0', port=port)
