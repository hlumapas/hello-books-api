from app import db
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from .models.book import Book 

books_bp = Blueprint("books", __name__, url_prefix="/books")

# helper function to change book_id into int
def is_int(value): 
    try:
        return int(value)
    except ValueError: 
        return False

#refactored way 
@books_bp.route("", methods=["GET"], strict_slashes=False)
def books_index():
    # inherits class method called query it has a .all function
    books = Book.query.all()
    books_response = []
    # each book is an instance of the Book model 
    for book in books: 
        books_response.append(book.to_json())

    # have to use jsonify bc books_response is a list
    # flask knows how to make dict into json 
    return jsonify(books_response,200)

@books_bp.route("", methods=["POST"], strict_slashes=False)
def books():
    # request_body is a local vairable that hold the contents of the HTTP request 
    # get_json() converts the request JSON body to a python dictionary
    request_body = request.get_json()

    #create new instance of Book model 
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])
    
    # pass in the new book that you want to add, kinda like staging in git
    db.session.add(new_book) 
    # want to commit that change and make it happen
    db.session.commit()

    # need to return a response
    return {
        "success": True,
        "message": f"Book {new_book.title} has been created"
    }, 201

@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_single_book(book_id):
    # make sure to check if id given is an int
    # can make this into a helper function
    if not is_int(book_id): 
        return {
            "message": f"ID {book_id} must be an integer",
            "success": False 
        }, 400 

    # try to find the book with given id
    # need to find Book instance based on book_id
    book = Book.query.get(book_id)

    # need a way to verify if the book_id is even a book in the database
    if request.method == "GET":
        if book: #if its truthy and this prevents a crash if book id not found
            return book.to_json(), 200 

        return {
            "message": f"Book with id {book_id} does not exist!",     
            "success": False
        }, 404
    elif request.method == "PUT":
        form_data = request.get_json()

        book.title = form_data["title"]
        book.description = form_data["description"]
        
        db.session.commit()

        return make_response(f"Book #{book.id} successfully updated")

    elif request.method == "DELETE": 
        # telling the database to delete this 
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book #{book_id} successfully deleted")

# hello_world_bp = Blueprint("hello_word", __name__)

# @hello_world_bp.route('/hello-world', methods=["GET"])
# def get_hello_world(): 
#     my_response = "Hello, World!"
#     return my_response 

# @hello_world_bp.route('/hello-world/JSON', methods=["GET"])
# def hello_world_json(): 
#     return {
#         "name" : "CheezItMan!",
#         "message" : "Heya!",
#         "hobbies": ["Coding", "Writing", "Subversive Politics"],
#     }, 201

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"] + [new_hobby]
#     return response_body