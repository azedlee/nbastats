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

@manager.command
def Load(file_name):
    
    engine = create_engine(app.config["DATABASE_URI"])
    df = pd.read_csv(file_name, sep=',', index_col=False, header=None)
    df.to_sql('playerstats', engine, if_exists='append')

@manager.command
def Load_Data(file_name):
    data = np.genfromtxt(file_name, delimiter=",", skip_header=1, usecols=np.arange(0,22), 
                        names=True, converters={0: lambda s: str(s)})
    
    try:
        for i in data:
            record = Player_Statistics(**{
                    'name' : i[0],
                    'team' : i[1],
                    'position' : i[2],
                    'game_played' : i[3],
                    'min_per_game' : i[4],
                    'field_goal_percent' : i[5],
                    'free_throw_percent' : i[6],
                    'three_made' : i[7],
                    'three_percent' : i[8],
                    'three_per_game' : i[9],
                    'pts_per_game' : i[10],
                    'o_reb_per_game' : i[11],
                    'd_reb_per_game' : i[12],
                    'reb_per_game' : i[13],
                    'ast_per_game' : i[14],
                    'steals_per_game' : i[15],
                    'blocks_per_game' : i[16],                    
                    'to_per_game' : i[17],
                    'fouls_per_game' : i[18],
                    'tot_tech' : i[19],
                    'plus_minus_rating' : i[20]
            })
            session.add(record)
            print(i)
            session.commit()
    except:
        print("Unexpected error:",sys.exc_info())
        session.rollback()

import csv
@manager.command
def Data_Load(file_name):
    with open(file_name, 'rb') as csvfile:
        docreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in docreader:
            statement = "INSERT INTO ImportCSVTable " + \
            "(name, team, position, game_played, min_per_game, field_goal_percent, free_throw_percent, three_made, three_percent, three_per_game, pts_per_game, o_reb_per_game, d_reb_per_game, reb_per_game, ast_per_game, steals_per_game, blocks_per_game, to_per_game, fouls_per_game, tot_tech, plus_minus_rating)" +\
            "VALUES ('%s', '%s', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')" % (tuple(row[0:20]))

if __name__ == '__main__':
    manager.run()