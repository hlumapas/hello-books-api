from app import db

class Book(db.Model):
    # dont need to use __init__ function (constructor)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    
    # how do you know where to put this function? 
    # my initial thought was to put it in the routes file 
    def to_json(self): 
        return {
            "id": self.id,
            "title": self.title, 
            "description": self.description
        }