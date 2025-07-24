from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import text

# Initialize the Flask application
app = Flask(__name__)

# Set up the database URI with pymysql
# Replace <username>, <password>, <host>, and <dbname> with your database details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:5282@localhost/inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable Flask-SQLAlchemy warning

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

#health check
with app.app_context():
    try:
        db.session.execute(text("SELECT 1"))  # Basic query to test connection
        print("Database connected successfully!")
        print("app created")
    except Exception as e:
        print(f"Database connection failed: {e}")
        

with app.app_context():
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)

