import json

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app import models
from flask import jsonify


ROOMS = {
    "meeting1": "tolles meeting",
}


def abort_if_room_doesnt_exist(room_id):
    if room_id not in ROOMS:
        abort(404, message="Room {} doesn't exist".format(room_id))


parser = reqparse.RequestParser()
parser.add_argument('room')


class RoomList(Resource):
    def get(self):
        return jsonify(json_list=[i.serialize for i in models.Room.query.all()])


class Room(Resource):
    def get(self, room_id):
        abort_if_todo_doesnt_exist(room_id)
        return ROOMS[room_id]

    def put(self, roomname):
        args = parser.parse_args()
        room = {'room': args['room']}
        ROOMS[roomname] = room
        return room, 201

    def delete(self, room_id):
        abort_if_todo_doesnt_exist(room_id)
        del ROOMS[room_id]
        return '', 204
