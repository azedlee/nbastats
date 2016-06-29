import numpy as np
import pandas as pd
import sqlalchemy as sa
import os
import sys
import csvkit

from flask_script import Manager

from sqlalchemy import create_engine

from nbastats import app
from nbastats.database import Player_Statistics

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@manager.command
def Load(file_name):
    
    engine = create_engine(app.config["DATABASE_URI"])
    df = pd.read_csv(file_name, index_col=False, skiprows=1, header=None)
    df.to_sql('playerstats', engine, if_exists='append')

if __name__ == '__main__':
    manager.run()