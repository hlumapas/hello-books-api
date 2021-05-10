from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()
# postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development

def create_app(test_config=None):
    app = Flask(__name__)

    # DB Config/connecting
    if not test_config: 
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') 
    else: 
        app.config["TESTING"] = True 
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI') 

    # initialize sql object
    db.init_app(app)
    # tell igrate this is the application to work with
    migrate.init_app(app, db)
    # import the book model 
    from app.models.book import Book 

    # import the books blueprint and registed the blueprint
    from .routes import books_bp
    app.register_blueprint(books_bp)
    

    return app
