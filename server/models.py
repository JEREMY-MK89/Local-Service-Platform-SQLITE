from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    reviews = db.relationship("Review", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }

class Service(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    reviews = db.relationship("Review", back_populates="service")

    def __repr__(self):
        return f"Service(id={self.id}, name={self.name}, category={self.category})"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }

class Review(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    user = db.relationship("User", back_populates="reviews")
    service = db.relationship("Service", back_populates="reviews")

    def __repr__(self):
        return f"Review(id={self.id}, rating={self.rating}, comment={self.comment})"

    def serialize(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'comment': self.comment,
            'user_id': self.user_id,
            'service_id': self.service_id
        }
