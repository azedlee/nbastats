import unittest
import os
import shutil
import json
try: from urllib.parse import urlparse
except ImportError: from urlparse import urlparse # Py2 compatibility
from io import StringIO

import sys; print(list(sys.modules.keys()))
# Configure our app to use the testing databse
os.environ["CONFIG_PATH"] = "tuneful.config.TestingConfig"

from nbastats import app
from nbastats import models
from nbastats.utils import upload_path
from nbastats.database import Base, engine, session

class TestAPI(unittest.TestCase):
    """ Tests for the nbastats API """

    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        Base.metadata.create_all(engine)
    
    def get_empty_player(self):
        response = self.client.get("/api/player",
                                    headers=[("Accept", "application/json")])
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")
        
        data = json.loads(response.data.decode('UTF-8'))
        self.assertEqual(data, [])
    
    def get_player(self):
        pass
    
    def get_players(self):
        pass
    
    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)

        # Delete test upload folder
        shutil.rmtree(upload_path())
