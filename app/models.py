
from flask import current_app as app
from app import db

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    room_id = db.Column(
        db.Integer,
        db.ForeignKey('room.id'),
        nullable=False
        )
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
        )
    
    ticket_id = db.Column(
        db.Integer,
        db.ForeignKey('ticket.id'),
        nullable=False
        )

    vote = db.Column(db.Integer, nullable=True)
    
def init_database():
    db.create_all()


def create_testdata():
    db.session.add(User(name="user1"))
    db.session.add(User(name="user2"))
    db.session.add(User(name="user3"))
    db.session.add(Ticket(name="ticket1"))
    db.session.add(Ticket(name="ticket2"))
    db.session.add(Ticket(name="ticket3"))
    db.session.add(Room(name="room1"))
    db.session.add(Room(name="room2"))

    # fertig
    db.session.commit()