from numpy import genfromtxt
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from nbastats import app
from nbastats.database import Player_Statistics, session

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@manager.command
def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=",", skip_header=1, usecols=np.arange(0,1434))
    
    try:
        for i in data.tolist():
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
        
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()

if __name__ == '__main__':
    manager.run()
