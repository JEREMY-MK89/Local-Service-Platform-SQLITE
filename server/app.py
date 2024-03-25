import os
from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_cors import CORS
from models import User, Service, Review

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

# Define WTForms for input validation
class ServiceForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=1, max=100)])
    category = StringField('Category', validators=[InputRequired(), Length(min=1, max=50)])

class ReviewForm(FlaskForm):
    content = TextAreaField('Content', validators=[InputRequired()])
    rating = IntegerField('Rating', validators=[InputRequired()])

# Your resources (API endpoints) go here
class Signup(Resource):
    def post(self):
        # Your signup logic here
        return jsonify({'message': 'Signup endpoint'}), 200

class Login(Resource):
    def post(self):
        # Your login logic here
        return jsonify({'message': 'Login endpoint'}), 200

class Logout(Resource):
    def delete(self):
        # Your logout logic here
        return jsonify({'message': 'Logout endpoint'}), 200

class CheckSession(Resource):
    def get(self):
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            if user:
                return jsonify(user.serialize())
        return jsonify({}), 204  # Return empty response with status code 204 if user not authenticated

class ServiceResource(Resource):
    def get(self, id):
        # Your get service logic here
        return jsonify({'message': f'Get service {id}'}), 200

    def post(self):
        # Your create service logic here
        form = ServiceForm(request.form)
        if form.validate():
            # Process form data and create service
            return jsonify({'message': 'Create service'}), 201
        return jsonify({'message': 'Validation error'}), 400

    def put(self, id):
        # Your update service logic here
        return jsonify({'message': f'Update service {id}'}), 200

    def delete(self, id):
        # Your delete service logic here
        return jsonify({'message': f'Delete service {id}'}), 200

# Add resources to API endpoints
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(ServiceResource, '/services/<int:id>', '/services')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
