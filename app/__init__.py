from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development

def create_app(test_config=None):
    app = Flask(__name__)

    # DB Config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    # initialize sql object
    db.init_app(app)
    # tell igrate this is the application to work with
    migrate.init_app(app, db)
    from app.models.book import Book 
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)
    

    return app
