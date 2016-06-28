import unittest
import os
import json
try: from urllib.parse import urlparse
except ImportError: from urlparse import urlparse # Py2 compatibility

# Configure our app to use the testing databse
os.environ["CONFIG_PATH"] = "nbastats.config.TestingConfig"

from nbastats import app
from nbastats.database import Base, engine, session, Player_Statistics

class TestAPI(unittest.TestCase):
    """ Tests for the nbastats API """

    def setUp(self):
        """ Test setup """
        self.client = app.test_client()
        Base.metadata.create_all(engine)
    
    def test_get_empty_player(self):
        response = self.client.get("/nbastats/players",
                                    headers=[("Accept", "application/json")])
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")
        
        data = json.loads(response.data.decode('UTF-8'))
        self.assertEqual(data, [])
    
    def test_get_player(self):
        playerA = Player_Statistics(name="Player A",
                                            game_played = 75,
                                            pts_per_game = 18.7)
        
        session.add(playerA)
        session.commit()
        
        response = self.client.get("/nbastats/players/{}".format(playerA.id),
                                    headers=[("Accept", "application/json")])
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")
        
        playerA = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(playerA["name"], "Player A")
        self.assertEqual(playerA["game_played"], 75)
        self.assertEqual(playerA["pts_per_game"], 18.7)
    
    def test_get_players(self):
        playerA = Player_Statistics(name="Player A",
                                            game_played = 82,
                                            pts_per_game = 20.0)
        playerB = Player_Statistics(name="Player B",
                                            game_played = 75,
                                            pts_per_game = 18.7)

        session.add_all([playerA, playerB])
        session.commit()
        
        response = self.client.get("/nbastats/players",
                                    headers=[("Accept", "application/json")])

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(len(data), 2)

        playerA = data[0]
        self.assertEqual(playerA["name"], "Player A")
        self.assertEqual(playerA["game_played"], 82)
        self.assertEqual(playerA["pts_per_game"], 20.0)

        playerB = data[1]
        self.assertEqual(playerB["name"], "Player B")
        self.assertEqual(playerB["game_played"], 75)
        self.assertEqual(playerB["pts_per_game"], 18.7)
    
    def test_get_five_players(self):
        playerA = Player_Statistics(name="Player 1",
                                    team="CLE",
                                    position="C",
                                    pts_per_game=20.0)
        playerB = Player_Statistics(name="Player 2",
                                    team="CLE",
                                    position="PF",
                                    pts_per_game=15.0)
        playerC = Player_Statistics(name="Player 3",
                                    team="CLE",
                                    position="SF",
                                    pts_per_game=10.0)
        playerD = Player_Statistics(name="Player 4",
                                    team="CLE",
                                    position="SG",
                                    pts_per_game=5.0)
        playerE = Player_Statistics(name="Player 5",
                                    team="CLE",
                                    position="PG",
                                    pts_per_game=2.5)
        
        session.add_all([playerA, playerB, playerC, playerD, playerE])
        session.commit()
        
        response = self.client.get("/nbastats/players/points",
                                    headers=[("Accept", "application/json")])
        
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(len(data), 5)
        
        playerA = data[0]
        self.assertEqual(playerA['name'], "Player 1")
        self.assertEqual(playerA['team'], 'CLE')
        self.assertEqual(playerA['position'], 'C')
        self.assertEqual(playerA['pts_per_game'], 20.0)
        
        playerB = data[1]
        self.assertEqual(playerB['name'], 'Player 2')
        self.assertEqual(playerB['team'], 'CLE')
        self.assertEqual(playerB['position'], 'PF')
        self.assertEqual(playerB['pts_per_game'], 15.0)
        
        playerC = data[2]
        self.assertEqual(playerC['name'], 'Player 3')
        self.assertEqual(playerC['team'], 'CLE')
        self.assertEqual(playerC['position'], 'SF')
        self.assertEqual(playerC['pts_per_game'], 10.0)
        
        playerD = data[3]
        self.assertEqual(playerD['name'], 'Player 4')
        self.assertEqual(playerD['team'], 'CLE')
        self.assertEqual(playerD['position'], 'SG')
        self.assertEqual(playerD['pts_per_game'], 5.0)
        
        playerE = data[4]
        self.assertEqual(playerE['name'], 'Player 5')
        self.assertEqual(playerE['team'], 'CLE')
        self.assertEqual(playerE['position'], 'PG')
        self.assertEqual(playerE['pts_per_game'], 2.5)
        
    def tearDown(self):
        """ Test teardown """
        session.close()
        Base.metadata.drop_all(engine)
