import os.path
import json

from flask import request, Response, url_for, send_from_directory
from jsonschema import validate, ValidationError

from . import decorators
from . import database
from nbastats import app
from .database import session, Player_Statistics

@app.route("/nbastats/players", methods=["GET"])
@decorators.accept("application/json")
def players_get():
    players = session.query(database.Player_Statistics.name).all()
    
    data = json.dumps([player.as_dictionary for player in players])
    return Response(data, 200, mimetype="application/json")

@app.route("/nbastats/player", methods=["GET"])
@decorators.accept("application/json")
def player_get(name):
    player = session.query(database.Player_Statistics).get(name)
    
    if not player:
        message = "Could not find player name: {}".format(name)
        data = json.dumps({"message": message})
        return Response(data, 404, mimetype="application/json")

    data = json.dumps(player.as_dictionary())
    return Response(data, 200, mimetype="application/json")