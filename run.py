import numpy as np
import pandas as pd
import sqlalchemy as sa
import os
import sys

from flask_script import Manager

from sqlalchemy import create_engine

from nbastats import app
from nbastats.database import Player_Statistics, session

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

import csv
import psycopg2
@manager.command
def Data_Load(file_name):
    conn = psycopg2.connect("host='localhost' port='5432' dbname='nbastats' user='ubuntu' password='thinkful'")
    cur = conn.cursor()
    
    with open(file_name, 'rt', encoding="utf8") as csvfile:
        docreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in docreader:
            statement = """INSERT INTO playerstats_test VALUES ('%s', '%s', '%s', %s)""" % tuple(row[0:3])
            cur.execute(statement)
            conn.commit()

#@manager.command
#def Data_Load(file_name):
#    engine = create_engine(app.config["DATABASE_URI"])
#    
#    with open(file_name, 'rt', encoding="utf8") as csvfile:
#        docreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#        for row in docreader:
#            statement = "INSERT INTO playerstats " + \
#            "(name, team, position, game_played, min_per_game, field_goal_percent, free_throw_percent, three_made, three_percent, three_per_game, pts_per_game, o_reb_per_game, d_reb_per_game, reb_per_game, ast_per_game, steals_per_game, blocks_per_game, to_per_game, fouls_per_game, tot_tech, plus_minus_rating)" +\
#            "VALUES ('" +row[1]+"','" +(row[2])+"', '" +(row[3])+"', '" +(row[4])+"', '" +(row[5])+"', '" +(row[6])+"', '" +(row[7])+"', '" +(row[8])+"', '" +(row[9])+"', '" +(row[10])+"', '" +(row[11])+"', '" +(row[12])+"', '" +(row[13])+"', '" +(row[14])+"', '" +(row[15])+"', '" +(row[16])+"', '" +(row[17])+"', '" +(row[18])+"', '" +(row[19])+"', '" +(row[20])+"')"
#            
#            print(statement)
#            session.add(statement)
#            session.commit()

if __name__ == '__main__':
    manager.run()