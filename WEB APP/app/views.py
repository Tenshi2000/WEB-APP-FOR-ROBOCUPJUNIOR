from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Season, User, Competitor, Region, Category, Team, Slot

class UserView(ModelView):
    
    datamodel = SQLAInterface(User)
    related_views = []
    
    list_columns = ['first_name', 'last_name', 'is_admin', 'mail', 'region.name']

class CompetitorView(ModelView):
    
    datamodel = SQLAInterface(Competitor)
    related_views = []

    list_columns = ['first_name', 'last_name', 'date_of_birth', 'team.name', 'region.name']

class SlotView(ModelView):
    
    datamodel = SQLAInterface(Slot)
    related_views = []

    list_columns = ['name', 'team.name', 'region.name', 'season.name', 'category.name']

class CategoryView(ModelView):
    
    datamodel = SQLAInterface(Category)
    related_views = [SlotView]

    list_columns = ['name', 'number_of_competitors', 'team.name', 'season.name']

class TeamView(ModelView):
    
    datamodel = SQLAInterface(Team)
    related_views = [CompetitorView, CategoryView, SlotView]

    list_columns = ['name', 'name_of_institute', 'season.name']

class RegionView(ModelView):
        
    datamodel = SQLAInterface(Region)
    related_views = [UserView, CompetitorView, SlotView]

    list_columns = ['name']

class SeasonView(ModelView):
    
    datamodel = SQLAInterface(Season)
    related_views = [TeamView, CategoryView, SlotView]

    list_columns = ['name']

db.create_all()

appbuilder.add_view(
    SeasonView, "Seasons", icon="fa-folder-open-o", category="Seasons"
)

appbuilder.add_view(
    RegionView, "Regions", icon="fa-folder-open-o", category="MainMenu"
)

appbuilder.add_view(
    TeamView, "Teams", icon="fa-folder-open-o", category="MainMenu"
)

appbuilder.add_view(
    CategoryView, "Categories", icon="fa-folder-open-o", category="MainMenu"
)

appbuilder.add_view(
    SlotView, "Slots", icon="fa-folder-open-o", category="MainMenu"
)

appbuilder.add_view(
    UserView, "Users", icon="fa-folder-open-o", category="MainMenu"
)

appbuilder.add_view(
    CompetitorView, "Competitors", icon="fa-folder-open-o", category="MainMenu"
)
