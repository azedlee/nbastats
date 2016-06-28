from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from nbastats import app

engine = create_engine(app.config["DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Player_Statistics(Base):
    __tablename__ = 'playerstats'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(1024))
    team = Column(String(1024))
    position = Column(String(128))
    game_played = Column(Integer)
    min_per_game = Column(Float)
    field_goal_percent = Column(Float)
    free_throw_percent = Column(Float)    
    three_made = Column(Integer)
    three_percent = Column(Float)
    three_per_game = Column(Float)
    pts_per_game = Column(Float)
    o_reb_per_game = Column(Float)
    d_reb_per_game = Column(Float)
    reb_per_game = Column(Float)
    ast_per_game = Column(Float)
    steals_per_game = Column(Float)
    blocks_per_game = Column(Float)
    to_per_game = Column(Float)
    fouls_per_game = Column(Float)
    tot_tech = Column(Integer)
    plus_minus_rating = Column(Integer)
    
    def as_dictionary(self):
        return {
            "name" : self.name,
            "team" : self.team,
            "position" : self.position,
            "game_played" : self.game_played,
            "min_per_game" : self.min_per_game,
            "field_goal_percent" : self.field_goal_percent,
            "free_throw_percent" : self.free_throw_percent,
            "three_made" : self.three_made,
            "three_percent" : self.three_percent,
            "three_per_game" : self.three_per_game,
            "pts_per_game" : self.pts_per_game,
            "o_reb_per_game" : self.o_reb_per_game,
            "d_reb_per_game" : self.d_reb_per_game,
            "reb_per_game" : self.reb_per_game,
            "ast_per_game" : self.ast_per_game,
            "steals_per_game" : self.steals_per_game,
            "blocks_per_game" : self.blocks_per_game,                    
            "to_per_game" : self.to_per_game,
            "fouls_per_game" : self.fouls_per_game,
            "tot_tech" : self.tot_tech,
            "plus_minus_rating" : self.plus_minus_rating
        }
    
    def as_pts_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "team": self.team,
            "position": self.position,
            "pts_per_game": self.pts_per_game
        }
        
    def as_reb_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "team": self.team,
            "position": self.position,
            "reb_per_game": self.reb_per_game
        }
    
    def as_ast_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "team": self.team,
            "position": self.position,
            "ast_per_game": self.ast_per_game
        }
    def as_plus_minus_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "team": self.team,
            "position": self.position,
            "plus_minus_rating": self.plus_minus_rating
        }
            
Base.metadata.create_all(engine)