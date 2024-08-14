from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the database and define the database name
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # Create and configure the Flask app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'  # Keep this key safe and private
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    # Register blueprints for different routes
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    # Initialize the LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Define the user loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User  # Ensure User is imported here
        return User.query.get(int(user_id))

    # Create the database tables if they do not exist
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Created Database!')

    return app
