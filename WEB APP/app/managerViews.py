from .views import NameModelView

from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterInFunction

from flask import g
from . import appbuilder, db
from .models import Season, Competitor, Region, Category, Team, Slot

def get_user_region_id():

    return [g.user.region.id] if g.user.region is not None else []

def get_active_season_id():

    seasons = db.session.query(Season).filter(Season.active == "1").all()
    
    return list(map(lambda season : season.id, seasons))

class CompetitorView(NameModelView):
    
    datamodel = SQLAInterface(Competitor)
    related_views = []

    indexPriority = 1

    base_filters = [['region_id', FilterInFunction, get_user_region_id],
                    ['season_id', FilterInFunction, get_active_season_id]]
    list_columns = ['first_name', 'last_name', 'date_of_birth', 'season.name', 'region.name', 'team.name']

    add_form_query_rel_fields = {"region": [['id', FilterInFunction, get_user_region_id]], 
                                 "team": [['region_id', FilterInFunction, get_user_region_id],
                                          ['season_id', FilterInFunction, get_active_season_id]], 
                                 "season": [['id', FilterInFunction, get_active_season_id]]}
    edit_form_query_rel_fields = add_form_query_rel_fields

class TeamView(NameModelView):
    
    datamodel = SQLAInterface(Team)
    related_views = [CompetitorView]

    indexPriority= 10    

    base_filters = [['region_id', FilterInFunction, get_user_region_id],
                    ['season_id', FilterInFunction, get_active_season_id]]
    list_columns = ['name', 'name_of_institute', 'season.name', 'region.name', 'category']

    add_form_query_rel_fields = {"region": [['id', FilterInFunction, get_user_region_id]], 
                                 "season": [['id', FilterInFunction, get_active_season_id]],
                                 "category": [['season_id', FilterInFunction, get_active_season_id]],} 
    edit_form_query_rel_fields = add_form_query_rel_fields

class SlotView(NameModelView):
    
    datamodel = SQLAInterface(Slot)
    related_views = []

    indexPriority = 5
    edit_columns = ['team']

    base_filters = [['region_id', FilterInFunction, get_user_region_id],
                    ['season_id', FilterInFunction, get_active_season_id]]
    list_columns = ['name', 'season.name', 'region.name', 'category.name', 'team.name']

    edit_form_query_rel_fields = {"team": [['region_id', FilterInFunction, get_user_region_id],
                                          ['season_id', FilterInFunction, get_active_season_id]]}

def initManagerViews():

    appbuilder.add_view(
        TeamView, "Teams", icon = "fa-folder-open-o", category = "MainMenu"
    )

    appbuilder.add_view(
        SlotView, "Slots", icon = "fa-folder-open-o", category = "MainMenu"
    )

    appbuilder.add_view(
        CompetitorView, "Competitors", icon = "fa-folder-open-o", category = "MainMenu"
    )
