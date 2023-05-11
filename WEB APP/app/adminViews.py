from .views import NameModelView

from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterInFunction

from flask_appbuilder.fieldwidgets import Select2ManyWidget
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder import SimpleFormView

from wtforms.fields import SelectMultipleField
from functools import cmp_to_key

from flask import session
from . import appbuilder, db
from .models import Season, Competitor, Region, Category, Team, Slot

def get_displayed_season_ids():

    if session.get("displayed_season", None) is not None:

        return session["displayed_season"] if isinstance(session["displayed_season"], list) else [session["displayed_season"]]
    
    seasons = db.session.query(Season).all()

    return list(map(lambda season : season.id, seasons))

class AdminCompetitorView(NameModelView):
    
    datamodel = SQLAInterface(Competitor)
    related_views = []

    indexPriority = 50
    route_base = "/admin/competitorview"

    base_filters = [['season_id', FilterInFunction, get_displayed_season_ids]]
    list_columns = ['first_name', 'last_name', 'date_of_birth', 'season.name', 'region.name', 'team.name']

class AdminTeamView(NameModelView):
    
    datamodel = SQLAInterface(Team)
    related_views = [AdminCompetitorView]

    indexPriority = 70
    route_base = "/admin/teamview"

    base_filters = [['season_id', FilterInFunction, get_displayed_season_ids]]
    list_columns = ['name', 'name_of_institute', 'season.name', 'region.name', 'category.name']

class AdminSlotView(NameModelView):
    
    datamodel = SQLAInterface(Slot)
    related_views = []

    indexPriority = 60
    route_base = "/admin/slotview"

    base_filters = [['season_id', FilterInFunction, get_displayed_season_ids]]
    list_columns = ['name', 'season.name', 'region.name', 'category.name', 'team.name']
                                  
class AdminCategoryView(NameModelView):
    
    datamodel = SQLAInterface(Category)
    related_views = [AdminSlotView]

    indexPriority = 80
    route_base = "/admin/categoryview"
    
    base_filters = [['season_id', FilterInFunction, get_displayed_season_ids]]
    list_columns = ['name', 'number_of_competitors', 'season.name']
    
class AdminRegionView(NameModelView):
        
    datamodel = SQLAInterface(Region)
    related_views = [AdminCompetitorView, AdminSlotView]

    indexPriority = 90
    route_base = "/admin/regionview"

    list_columns = ['name']

class AdminSeasonView(NameModelView):
    
    datamodel = SQLAInterface(Season)
    related_views = [AdminTeamView, AdminCategoryView, AdminSlotView]

    indexPriority = 100
    route_base = "/admin/seasonview"

    list_columns = ['name', 'active']

class SeasonSelectForm(DynamicForm):

    def getSeasons():

        seasons = db.session.query(Season).all()
        seasons = list(map(lambda season : (season.id, season.__repr__()), seasons))        
        seasons = sorted(seasons,key = cmp_to_key(lambda season1, season2 : -1 if season1[1] > season2[1] else (0 if season1[1] == season2[1] else 1)))
        return seasons
    
    selectedSeason = SelectMultipleField("Season", coerce = int, widget = Select2ManyWidget(), choices = getSeasons, validate_choice = False)

class SelectSeasonFormView(SimpleFormView):

    indexPriority = 110
    form = SeasonSelectForm
    title = "Displayed Season"

    # Custome function to handle interaction with multiview on index page
    def getViewWidget(self):

        self._init_vars()
        form = self.form.refresh()

        self.form_get(form)
        widget = self._get_edit_widget(form = form)["edit"]
        return widget

    def form_get(self, form):

        form.selectedSeason.data = get_displayed_season_ids()

    def form_post(self, form):

        selectedSeasons = form.selectedSeason.data

        if selectedSeasons is None or len(selectedSeasons) == 0:

            seasons = db.session.query(Season).all()
            selectedSeasons = list(map(lambda season : season.id, seasons))
            
        session["displayed_season"] = selectedSeasons

def initAdminViews():

    appbuilder.add_view_no_menu(SelectSeasonFormView)

    appbuilder.add_view(
        AdminSeasonView, "Seasons", icon = "fa-folder-open-o", category = "Seasons"
    )

    appbuilder.add_view(
        AdminRegionView, "Regions", icon = "fa-folder-open-o", category = "AdminMenu"
    )

    appbuilder.add_view(
        AdminCategoryView, "Categories", icon = "fa-folder-open-o", category = "AdminMenu"
    )

    appbuilder.add_view(
        AdminTeamView, "Teams", icon = "fa-folder-open-o", category = "AdminMenu"
    )

    appbuilder.add_view(
        AdminSlotView, "Slots", icon = "fa-folder-open-o", category = "AdminMenu"
    )

    appbuilder.add_view(
        AdminCompetitorView, "Competitors", icon = "fa-folder-open-o", category = "AdminMenu"
    )
