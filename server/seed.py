from flask_sqlalchemy import SQLAlchemy
from model import db, User, Service, Review

def seed_data():
    # Create users
    user1 = User(username='user1', password_hash='password1')
    user2 = User(username='user2', password_hash='password2')
    user3 = User(username='user3', password_hash='password3')

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # Create services
    service1 = Service(name='Clinic A', category='Clinic')
    service2 = Service(name='Salon B', category='Salon')
    service3 = Service(name='Shopping Mall C', category='Shopping Mall')

    db.session.add_all([service1, service2, service3])
    db.session.commit()

    # Create reviews
    review1 = Review(content='Great service!', rating=5, service_id=service1.id, user_id=user1.id)
    review2 = Review(content='Average experience.', rating=3, service_id=service2.id, user_id=user2.id)
    review3 = Review(content='Poor service quality.', rating=2, service_id=service3.id, user_id=user3.id)

    db.session.add_all([review1, review2, review3])
    db.session.commit()

if __name__ == '__main__':
    seed_data()
