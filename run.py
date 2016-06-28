import numpy as np
import pandas as pd
import sqlalchemy as sa
import os
import sys

from flask_script import Manager

from nbastats import app
from nbastats.database import Player_Statistics, engine

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@manager.command
def Load(file_name):

    engine = sa.create_engine("postgresql://ubuntu:thinkful@localhost:5432/nbastats")
    
    df = pd.read_csv(file_name, skiprows=1, header=None)
    df.to_sql('playerstats', engine, if_exists='replace')

if __name__ == '__main__':
    manager.run()