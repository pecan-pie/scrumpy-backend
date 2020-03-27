import json
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from scrumpy.room import RoomList, Room
from scrumpy import models, app, api

# https://flask-restful.readthedocs.io/en/latest/quickstart.html#endpoints

api.add_resource(RoomList, '/room')
api.add_resource(Room, '/room/<room_id>')

if __name__ == '__main__':
    models.init_database()
    models.create_testdata()
    app.run(host='0.0.0.0', debug=True)
