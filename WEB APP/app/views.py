from flask_appbuilder import ModelView
from . import appbuilder

class NameModelView(ModelView):

    indexPriority= 0

    def prefill_form(self, form, pk):

        item = self.datamodel.get(pk, self._base_filters)
        self.edit_title = item.__repr__()

    def _show(self, pk):

        item = self.datamodel.get(pk, self._base_filters)
        self.show_title = item.__repr__()
        return super()._show(pk)

def initViews():

    from .managerViews import initManagerViews
    from .adminViews import initAdminViews
    
    from .index import DefaultView
    appbuilder.add_link("Home", "/", baseview = DefaultView)

    initAdminViews()
    initManagerViews()
    