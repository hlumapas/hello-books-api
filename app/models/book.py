from app import db

class Book(db.Model):
    # dont need to use __init__ function (constructor)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    