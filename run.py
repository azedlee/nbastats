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
    conn = psycopg2.connect("host='ec2-23-21-148-9.compute-1.amazonaws.com' port='5432' dbname='d3gntcc7ejvold' user='zmdkdpsjliuemk' password='NLy9RzlvAtKyw5OZ50Xn7neP4P'")
    # For localhost
    # conn = psycopg2.connect("host='localhost' port='5432' dbname='nbastats' user='ubuntu' password='thinkful'")
    cur = conn.cursor()

    with open(file_name, 'rt', encoding="utf8") as csvfile:
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        docreader = csv.reader(csvfile, delimiter=',')
        if has_header:
            next(docreader)
        for row in docreader:
            #print(tuple(row[0:5]))
            row[0] = int(row[0])
            row[4] = int(row[4])
            row[5] = float(row[5])
            row[6] = float(row[6])
            row[7] = float(row[7])
            row[8] = int(row[8])
            row[9] = float(row[9])
            row[10] = float(row[10])
            row[11] = float(row[11])
            row[12] = float(row[12])
            row[13] = float(row[13])
            row[14] = float(row[14])
            row[15] = float(row[15])
            row[16] = float(row[16])
            row[17] = float(row[17])
            row[18] = float(row[18])
            row[19] = float(row[19])
            row[20] = int(row[20])
            row[21] = int(row[21])
            #print(row[0:21])
            #print(isinstance(row[0], int))
            statement = """INSERT INTO playerstats VALUES (%s, '%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % tuple(row[0:22])
            print(statement)
            cur.execute(statement)
            conn.commit()

if __name__ == '__main__':
    manager.run()