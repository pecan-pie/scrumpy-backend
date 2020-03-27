import json
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import app
from app.room import RoomList, Room
from app import models

# https://flask-restful.readthedocs.io/en/latest/quickstart.html#endpoints

app.api.add_resource(RoomList, '/room')
app.api.add_resource(Room, '/room/<room_id>')

if __name__ == '__main__':
    models.init_database()
    models.create_testdata()
    app.app.run(host='0.0.0.0', debug=True)
