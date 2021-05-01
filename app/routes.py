from flask import Blueprint

hello_world_bp = Blueprint("hello_word", __name__)

@hello_world_bp.route('/hello-world', methods=["GET"])
def get_hello_world(): 
    my_response = "Hello, World!"
    return my_response 

@hello_world_bp.route('/hello-world/JSON', methods=["GET"])
def hello_world_json(): 
    return {
        "name" : "CheezItMan!",
        "message" : "Heya!",
        "hobbies": ["Coding", "Writing", "Subversive Politics"],
    }, 201

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"] + [new_hobby]
    return response_body