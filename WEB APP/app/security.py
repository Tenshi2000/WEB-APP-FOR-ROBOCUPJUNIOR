import re
from flask_appbuilder.security.sqla.manager import SecurityManager

from .models import MyUser
from flask_babel import lazy_gettext

from flask_appbuilder.security.views import UserDBModelView

class MyUserDBModelView(UserDBModelView):
    
    """
        View that add DB specifics to User view.
        Override to implement your own custom view.
        Then override userdbmodelview property on SecurityManager.
    """

    show_fieldsets = [
        (
            lazy_gettext("User info"),
            {"fields": ["username", "active", "roles", "login_count"], "expanded": True},
        ),
        (
            lazy_gettext("Personal Info"),
            {"fields": ["first_name", "last_name", "email"], "expanded": True},
        ),
    ]

    user_show_fieldsets = [
        (
            lazy_gettext("User info"),
            {"fields": ["username", "active", "roles", "login_count"]},
        ),
        (
            lazy_gettext("Personal Info"),
            {"fields": ["first_name", "last_name", "email"], "expanded": True},
        ),
    ]

    add_columns = [
        "first_name",
        "last_name",
        "username",
        "active",
        "email",
        "roles",
        "region",
        "password",
        "conf_password",
    ]

    list_columns = [
        "first_name",
        "last_name",
        "username",
        "email",
        "active",
        "roles",
        "region",
    ]

    edit_columns = [
        "first_name",
        "last_name",
        "username",
        "active",
        "email",
        "roles",
        "region",
    ]

class MySecurityManager(SecurityManager):

    user_model = MyUser
    userdbmodelview = MyUserDBModelView

    def _has_access_builtin_roles(self, role, permission_name: str, view_name: str) -> bool:
        
        """
            Checks permission on builtin role. Added support for negative permissions.
        """

        builtin_pvms = self.builtin_roles.get(role.name, [])
        
        for pvm in builtin_pvms:

            _view_name = pvm[0]
            _permission_name = pvm[1]

            if re.match(_view_name, view_name) and re.match(_permission_name, permission_name):

                return True
            
            if re.match(_view_name, view_name) and re.match(_permission_name, "-" + permission_name):
                
                return False
            
        return False
