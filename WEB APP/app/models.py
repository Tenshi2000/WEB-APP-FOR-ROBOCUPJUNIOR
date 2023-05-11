from flask_appbuilder import Model

from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Date, ForeignKey, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

class Season(Model):
    
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)
    active = Column(Boolean, nullable = True, default = False)

    def __repr__(self):
        
        return self.name

class Region(Model):
    
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)

    def __repr__(self):
        
        return self.name

class MyUser(User):
    
    __tablename__ = "ab_user"

    region_id = Column(Integer, ForeignKey("region.id"), nullable = True)
    region = relationship("Region")

class Competitor(Model):
    
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50), unique = False, nullable = False)
    last_name = Column(String(50), unique = False, nullable = False)
    date_of_birth = Column(Date)

    season_id = Column(Integer, ForeignKey("season.id"), nullable = False)
    season = relationship("Season")

    team_id = Column(Integer, ForeignKey("team.id"), nullable = False)
    team = relationship("Team")

    region_id = Column(Integer, ForeignKey("region.id"), nullable = False)
    region = relationship("Region")

    def __repr__(self):
        
        return self.first_name + " " + self.last_name

class Team(Model):

    __table_args__ = (UniqueConstraint('season_id', 'name', name = 'unique_season_id_name'),) # Pridal som toto a odstránil UNIQUE = TRUE z "name".

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    name_of_institute = Column(String(50), unique = False, nullable = False)

    season_id = Column(Integer, ForeignKey("season.id"), nullable = False)
    season = relationship("Season")

    region_id = Column(Integer, ForeignKey("region.id"), nullable = False)
    region = relationship("Region")

    category_id = Column(Integer, ForeignKey("category.id"), nullable = False)
    category = relationship("Category")

    def __repr__(self):
        
        return self.name

class Category(Model):
    
    __table_args__ = (UniqueConstraint('season_id', 'name', name = 'unique_season_id_name'),) # Pridal som toto a odstránil UNIQUE = TRUE z "name".

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    number_of_competitors = Column(Integer, nullable = False)

    season_id = Column(Integer, ForeignKey("season.id"), nullable = False)
    season = relationship("Season")

    def __repr__(self):
        
        return self.name + " " + self.season.name

class Slot(Model):
    
    __table_args__ = (UniqueConstraint('season_id', 'name', name = 'unique_season_id_name'),) # Pridal som toto a odstránil UNIQUE = TRUE z "name".

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    
    team_id = Column(Integer, ForeignKey("team.id"), nullable = True, default = None)
    team = relationship("Team")

    region_id = Column(Integer, ForeignKey("region.id"), nullable = False)
    region = relationship("Region")

    season_id = Column(Integer, ForeignKey("season.id"), nullable = False)
    season = relationship("Season")

    category_id = Column(Integer, ForeignKey("category.id"), nullable = False)
    category = relationship("Category")

    def __repr__(self):
        
        return self.name
