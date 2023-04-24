from flask_appbuilder import Model

from sqlalchemy import Column, Date, ForeignKey, Integer, Boolean, String, Table, Text
from sqlalchemy.orm import relationship

class Season(Model):
    
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)

    def __repr__(self):
        
        return self.name

class Region(Model):
    
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)

    def __repr__(self):
        
        return self.name

########################Pravdepodobne nebudem potrebovať########################
class User(Model):
    
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50), unique = False, nullable = False)
    last_name = Column(String(50), unique = False, nullable = False)
    is_admin = Column(Boolean) #Nie som si ešte istý...
    mail = Column(Text(250), nullable = False)
    hashes_password = Column(String(50), unique = False, nullable = False)

    region_id = Column(Integer, ForeignKey("region.id"), nullable = False)
    region = relationship("Region")
    
    def __repr__(self):
        
        return "User has id: " + self.first_name
################################################################################

class Competitor(Model):
    
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50), unique = False, nullable = False)
    last_name = Column(String(50), unique = False, nullable = False)
    date_of_birth = Column(Date)

    team_id = Column(Integer, ForeignKey("team.id"), nullable = False)
    team = relationship("Team")

    region_id = Column(Integer, ForeignKey("region.id"), nullable = False)
    region = relationship("Region")
    
    def __repr__(self):
        
        return "Competitor has id: " + self.id

class Team(Model):
    
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)
    name_of_institute = Column(String(50), unique = False, nullable = False)

    season_id = Column(Integer, ForeignKey("season.id"), nullable = False)
    season = relationship("Season")

    def __repr__(self):
        
        return self.name

class Category(Model):
    
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)
    number_of_competitors = Column(Integer, nullable = False)

    team_id = Column(Integer, ForeignKey("team.id"), nullable = False)
    team = relationship("Team")

    season_id = Column(Integer, ForeignKey("season.id"), nullable = False)
    season = relationship("Season")

    def __repr__(self):
        
        return self.name

class Slot(Model):
    
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False) #Bez tohto riadku: LIST INDEX OUT OF RANGE!!!
    
    team_id = Column(Integer, ForeignKey("team.id"), nullable = True)
    team = relationship("Team")

    region_id = Column(Integer, ForeignKey("region.id"), nullable = True)
    region = relationship("Region")

    season_id = Column(Integer, ForeignKey("season.id"), nullable = False)
    season = relationship("Season")

    category_id = Column(Integer, ForeignKey("category.id"), nullable = False)
    category = relationship("Category")

    def __repr__(self):
        
        return self.id
