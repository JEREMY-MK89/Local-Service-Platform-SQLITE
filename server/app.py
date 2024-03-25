from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_cors import CORS
from flask_migrate import Migrate
import os  # Import os module

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server/db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)  # Generate a new secret key every time the application runs

db = SQLAlchemy(app)  # Initialize SQLAlchemy instance with the app context
migrate = Migrate(app, db)
api = Api(app)

class ServiceForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=1, max=100)])
    category = StringField('Category', validators=[InputRequired(), Length(min=1, max=50)])

class ReviewForm(FlaskForm):
    content = TextAreaField('Content', validators=[InputRequired()])
    rating = IntegerField('Rating', validators=[InputRequired()])

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
        return jsonify({}), 204

class ServiceResource(Resource):
    def get(self, id=None):
        if id:
            service = Service.query.get(id)
            if service:
                return jsonify(service.serialize()), 200
            return jsonify({'message': 'Service not found'}), 404
        else:
            services = Service.query.all()
            return jsonify([service.serialize() for service in services]), 200

    def post(self):
        form = ServiceForm(request.form)
        if form.validate():
            name = form.name.data
            category = form.category.data
            service = Service(name=name, category=category)
            db.session.add(service)
            db.session.commit()
            return jsonify({'message': 'Service created successfully', 'service_id': service.id}), 201
        return jsonify({'message': 'Validation error'}), 400

    def put(self, id):
        # Your update service logic here
        service = Service.query.get(id)
        if not service:
            return jsonify({'message': 'Service not found'}), 404
        form = ServiceForm(request.form)
        if form.validate():
            service.name = form.name.data
            service.category = form.category.data
            db.session.commit()
            return jsonify({'message': 'Service updated successfully'}), 200
        return jsonify({'message': 'Validation error'}), 400

    def delete(self, id):
        service = Service.query.get(id)
        if service:
            db.session.delete(service)
            db.session.commit()
            return jsonify({'message': 'Service deleted successfully'}), 200
        return jsonify({'message': 'Service not found'}), 404

api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(ServiceResource, '/services', '/services/<int:id>')

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the home page'})

@app.route('/dashboard')
def dashboard():
    return jsonify({'message': 'Welcome to the dashboard'})

@app.route('/profile')
def profile():
    return jsonify({'message': 'Welcome to the profile'})

@app.route('/navigation')
def navigation():
    return jsonify({'message': 'This is a UI element for navigation'})

if __name__ == '__main__':
    app.run(debug=True)
