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
    
    def tearDown(self):
        """ Test teardown """
        session.close()
        Base.metadata.drop_all(engine)
