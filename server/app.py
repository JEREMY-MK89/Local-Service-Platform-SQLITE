from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Service, Review 
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app)
db.init_app(app)

class ReviewForm(FlaskForm):
    rating = IntegerField('Rating', validators=[InputRequired(), NumberRange(min=1, max=5)])
    comment = TextAreaField('Comment')

# Routes for user authentication (sign up, log in, log out)
@app.route('/signup', methods=['POST'])
def signup():
    # Implement user signup logic here
    return jsonify({'message': 'User signed up successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
    # Implement user login logic here
    return jsonify({'message': 'User logged in successfully'}), 200

@app.route('/logout', methods=['GET'])
def logout():
    # Implement user logout logic here
    return jsonify({'message': 'User logged out successfully'}), 200

# Routes for services (GET, POST, PATCH, DELETE)
@app.route('/services', methods=['GET'])
def get_services():
    # Implement logic to get all services
    services = Service.query.all()
    return jsonify([service.serialize() for service in services]), 200

@app.route('/services', methods=['POST'])
def create_service():
    # Implement logic to create a new service
    return jsonify({'message': 'Service created successfully'}), 201

@app.route('/services/<int:service_id>', methods=['PATCH'])
def update_service(service_id):
    # Implement logic to update a service
    return jsonify({'message': 'Service updated successfully'}), 200

@app.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    # Implement logic to delete a service
    return jsonify({'message': 'Service deleted successfully'}), 200

# Routes for reviews (GET, POST, PATCH, DELETE)
@app.route('/services/<int:service_id>/reviews', methods=['GET'])
def get_reviews(service_id):
    # Implement logic to get all reviews for a service
    reviews = Review.query.filter_by(service_id=service_id).all()
    return jsonify([review.serialize() for review in reviews]), 200

@app.route('/services/<int:service_id>/reviews', methods=['POST'])
def create_review(service_id):
    # Implement logic to create a new review for a service
    return jsonify({'message': 'Review created successfully'}), 201

@app.route('/services/<int:service_id>/reviews/<int:review_id>', methods=['PATCH'])
def update_review(service_id, review_id):
    # Implement logic to update a review for a service
    return jsonify({'message': 'Review updated successfully'}), 200

@app.route('/services/<int:service_id>/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(service_id, review_id):
    # Implement logic to delete a review for a service
    return jsonify({'message': 'Review deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
