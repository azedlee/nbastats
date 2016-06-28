import os.path
import json

from flask import request, Response, url_for, send_from_directory
from jsonschema import validate, ValidationError

from . import decorators
from nbastats import app
from .database import session, Player_Statistics

@app.route("/nbastats/players", methods=['GET'])
@decorators.accept("application/json")
def players_get():
    name_like = request.args.get("name_like")
    team_like = request.args.get("team_like")
    position_like = request.args.get("position_like")
    game_played_like = request.args.get("game_played_like")
    min_per_game_like = request.args.get("min_per_game_like")
    field_goal_percent_like = request.args.get("field_goal_percent_like")
    free_throw_percent_like = request.args.get("field_throw_percent_like") 
    three_made_like = request.args.get("three_made_like")
    three_percent_like = request.args.get("three_percent_like")
    three_per_game_like = request.args.get("three_per_game_like")
    pts_per_game_like = request.args.get("pts_per_game_like")
    o_reb_per_game_like = request.args.get("o_reb_per_game_like")
    d_reb_per_game_like = request.args.get("d_reb_per_game_like")
    reb_per_game_like = request.args.get("reb_per_game_like")
    ast_per_game_like = request.args.get("ast_per_game_like")
    steals_per_game_like = request.args.get("steals_per_game_like")
    blocks_per_game_like = request.args.get("blocks_per_game_like")
    to_per_game_like = request.args.get("to_per_game_like")
    fouls_per_game_like = request.args.get("fouls_per_game_like")
    tot_tech_like = request.args.get("tot_tech_like")
    plus_minus_rating_like = request.args.get("plus_minus_rating_like")
    
    players = session.query(Player_Statistics)
    if name_like:
        players = players.filter(Player_Statistics.name.contains(name_like))
    if team_like:
        players = players.filter(Player_Statistics.team.contains(team_like))
    if position_like:
        players = players.filter(Player_Statistics.position.contains(position_like))
    if game_played_like:
        players = players.filter(Player_Statistics.game_played.contains(game_played_like))
    if min_per_game_like:
        players = players.filter(Player_Statistics.min_per_game.contains(min_per_game_like))
    if field_goal_percent_like:
        players = players.filter(Player_Statistics.field_goal_percent.contains(field_goal_percent_like))
    if free_throw_percent_like:
        players = players.filter(Player_Statistics.free_throw_percent.contains(free_throw_percent_like))
    if three_made_like:
        players = players.filter(Player_Statistics.three_made.contains(three_made_like))
    if three_percent_like:
        players = players.filter(Player_Statistics.three_percent.contains(three_percent_like))
    if three_per_game_like:
        players = players.filter(Player_Statistics.three_per_game.contains(three_per_game_like))
    if pts_per_game_like:
        players = players.filter(Player_Statistics.pts_per_game.contains(pts_per_game_like))
    if o_reb_per_game_like:
        players = players.filter(Player_Statistics.o_reb_per_game.contains(o_reb_per_game_like))
    if d_reb_per_game_like:
        players = players.filter(Player_Statistics.d_reb_per_game.contains(d_reb_per_game_like))
    if reb_per_game_like:
        players = players.filter(Player_Statistics.reb_per_game.contains(reb_per_game_like))
    if ast_per_game_like:
        players = players.filter(Player_Statistics.ast_per_game.contains(ast_per_game_like))
    if steals_per_game_like:
        players = players.filter(Player_Statistics.steals_per_game.contains(steals_per_game_like))
    if blocks_per_game_like:
        players = players.filter(Player_Statistics.blocks_per_game.contains(blocks_per_game_like))
    if to_per_game_like:
        players = players.filter(Player_Statistics.to_per_game.contains(to_per_game_like))
    if fouls_per_game_like:
        players = players.filter(Player_Statistics.fouls_per_game.contains(fouls_per_game_like))
    if tot_tech_like:
        players = players.filter(Player_Statistics.tot_tech.contains(tot_tech_like))
    if plus_minus_rating_like:
        players = players.filter(Player_Statistics.plus_minus_rating.contains(plus_minus_rating_like))
    
    data = json.dumps([player.as_dictionary for player in players])
    return Response(data, 200, mimetype="application/json")

@app.route("/nbastats/players/<int:id>", methods=['GET'])
@decorators.accept("application/json")
def player_get(id):
    player = session.query(Player_Statistics).get(id)
    
    if not player:
        message = "Could not find player name: {}".format(id)
        data = json.dumps({"message": message})
        return Response(data, 404, mimetype="application/json")

    data = json.dumps(player.as_dictionary())
    return Response(data, 200, mimetype="application/json")

@app.route("/nbastats/players/points", methods=['GET'])
@decorators.accept("application/json")
def player_top_pts_get():
    name_like = request.args.get("name_like")
    team_like = request.args.get("team_like")
    position_like = request.args.get("position_like")
    pts_per_game_like = request.args.get("pts_per_game_like")
    
    players = session.query(Player_Statistics).order_by(Player_Statistics.pts_per_game).limit(5)
    
    if name_like:
        players = players.filter(Player_Statistics.name.contains(name_like))
    if team_like:
        players = players.filter(Player_Statistics.team.contains(team_like))
    if position_like:
        players = players.filter(Player_Statistics.position.contains(position_like))
    if pts_per_game_like:
        players = players.filter(Player_Statistics.pts_per_game.contains(pts_per_game_like))
    
    data = json.dumps([player.as_pts_dictionary for player in players])
    return Response(data, 200, mimetype="application/json")
    
@app.route("/nbastats/players/rebounds", methods=['GET'])
@decorators.accept("application/json")
def player_top_reb_get():
    name_like = request.args.get("name_like")
    team_like = request.args.get("team_like")
    position_like = request.args.get("position_like")
    reb_per_game_like = request.args.get("reb_per_game_like")
    
    players = session.query(Player_Statistics).order_by(Player_Statistics.reb_per_game).limit(5)
    
    if name_like:
        players = players.filter(Player_Statistics.name.contains(name_like))
    if team_like:
        players = players.filter(Player_Statistics.team.contains(team_like))
    if position_like:
        players = players.filter(Player_Statistics.position.contains(position_like))
    if reb_per_game_like:
        players = players.filter(Player_Statistics.reb_per_game.contains(reb_per_game_like))
    
    data = json.dumps([player.as_reb_dictionary for player in players])
    return Response(data, 200, mimetype="application/json")

@app.route("/nbastats/players/assists", methods=['GET'])
@decorators.accept("application/json")
def player_top_ast_get():
    name_like = request.args.get("name_like")
    team_like = request.args.get("team_like")
    position_like = request.args.get("position_like")
    ast_per_game_like = request.args.get("ast_per_game_like")
    
    players = session.query(Player_Statistics).order_by(Player_Statistics.ast_per_game).limit(5)
    
    if name_like:
        players = players.filter(Player_Statistics.name.contains(name_like))
    if team_like:
        players = players.filter(Player_Statistics.team.contains(team_like))
    if position_like:
        players = players.filter(Player_Statistics.position.contains(position_like))
    if ast_per_game_like:
        players = players.filter(Player_Statistics.ast_per_game.contains(ast_per_game_like))
    
    data = json.dumps([player.as_ast_dictionary for player in players])
    return Response(data, 200, mimetype="application/json")

@app.route("/nbastats/players/plus_minus_rating", methods=['GET'])
@decorators.accept("application/json")
def player_top_plus_minus_get():
    name_like = request.args.get("name_like")
    team_like = request.args.get("team_like")
    position_like = request.args.get("position_like")
    plus_minus_rating_like = request.args.get("plus_minus_rating_like")
    
    players = session.query(Player_Statistics).order_by(Player_Statistics.plus_minus_rating).limit(5)
    
    if name_like:
        players = players.filter(Player_Statistics.name.contains(name_like))
    if team_like:
        players = players.filter(Player_Statistics.team.contains(team_like))
    if position_like:
        players = players.filter(Player_Statistics.position.contains(position_like))
    if plus_minus_rating_like:
        players = players.filter(Player_Statistics.plus_minus_rating.contains(plus_minus_rating_like))
    
    data = json.dumps([player.as_plus_minus_dictionary for player in players])
    return Response(data, 200, mimetype="application/json")
