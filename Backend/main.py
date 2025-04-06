from flask import request
from .app_init import app  # Corrected import to use relative import
from .database import init_db, add_hotel, get_hotels, get_hotel_by_name, update_hotel, delete_hotel  # Corrected import to use relative import
from .auth import signup, login, logout  # Corrected import to use relative import

# Initialize the database
mongo = init_db(app)

# Auth routes
@app.route('/signup', methods=['POST'])
def signup_route():
    return signup()

@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/logout', methods=['POST'])
def logout_route():
    return logout()

# Hotel routes
@app.route('/hotels', methods=['POST'])
def add_hotel_route():
    hotel_data = request.get_json()
    add_hotel(hotel_data)
    return {"message": "Hotel added successfully"}, 201

@app.route('/hotels', methods=['GET'])
def get_hotels_route():
    hotels = get_hotels()
    return {"hotels": hotels}, 200

@app.route('/hotels/<string:name>', methods=['GET'])
def get_hotel_by_name_route(name):
    hotel = get_hotel_by_name(name)
    if hotel:
        return hotel, 200
    return {"message": "Hotel not found"}, 404

@app.route('/hotels/<string:name>', methods=['PUT'])
def update_hotel_route(name):
    update_data = request.get_json()
    result = update_hotel(name, update_data)
    if result.modified_count:
        return {"message": "Hotel updated successfully"}, 200
    return {"message": "Hotel not found or nothing changed"}, 404

@app.route('/hotels/<string:name>', methods=['DELETE'])
def delete_hotel_route(name):
    result = delete_hotel(name)
    if result.deleted_count:
        return {"message": "Hotel deleted successfully"}, 200
    return {"message": "Hotel not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)
