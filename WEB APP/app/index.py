from .views import NameModelView
from .adminViews import SelectSeasonFormView

from flask_appbuilder.urltools import get_order_args, get_page_args, get_page_size_args
from flask_appbuilder import MultipleView, expose, has_access
from flask import redirect, url_for, request

from . import appbuilder
from functools import cmp_to_key

class DefaultView(MultipleView):

    route_base = ""
    default_view = "index"
    title = "Home"
    computed_views = None
    seasonSelect = None

    @expose("/", methods=["GET", "POST"])
    def index(self):

        if appbuilder.sm.current_user is None or not appbuilder.sm.current_user.is_authenticated:

            return redirect(url_for('AuthDBView.login'))

        if self.computed_views is None:

            self.computed_views = list(filter(lambda view : isinstance(view,NameModelView) or isinstance(view,SelectSeasonFormView), appbuilder.baseviews))

            for view in self.computed_views:

                if isinstance(view,SelectSeasonFormView):

                    self.seasonSelect = view

        if request.method == "POST":

            self.seasonSelect.this_form_post()

        filtered_views = list()

        for view in self.computed_views:

            if appbuilder.sm.has_access("can_list", view.__class__.__name__):

                filtered_views.append(view)

        sortedViews = sorted(filtered_views, key = cmp_to_key(lambda view1, view2 : view2.indexPriority - view1.indexPriority))
        result = self._list(sortedViews)
        return result
    
    @expose("/list/")
    @has_access
    def list(self):

        return self._list(self._views)

    def _list(self,views):    

        pages = get_page_args()
        page_sizes = get_page_size_args()
        orders = get_order_args()
        views_widgets = list()

        for view in views:

            if orders.get(view.__class__.__name__):

                order_column, order_direction = orders.get(view.__class__.__name__)

            else:

                order_column, order_direction = "", ""

            page = pages.get(view.__class__.__name__)
            page_size = page_sizes.get(view.__class__.__name__)
            views_widgets.append(
                view.getViewWidget() if isinstance(view,SelectSeasonFormView) else 
                view._get_view_widget(
                    filters = view._base_filters,
                    order_column = order_column,
                    order_direction = order_direction,
                    page = page,
                    page_size = page_size,
                )
            )

        self.update_redirect()

        return self.render_template(self.list_template, views = views, views_widgets = views_widgets, title = self.title)
    