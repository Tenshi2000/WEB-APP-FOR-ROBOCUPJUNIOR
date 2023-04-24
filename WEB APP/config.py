import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

# ------------------------------ #
# DATABASE FOR WEB APP:          #
# ------------------------------ #

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
#SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'

# ------------------------------ #
# LANGUAGES FOR WEB APP:         #
# ------------------------------ #

BABEL_DEFAULT_LOCALE = "en"

LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "es": {"flag": "es", "name": "Spanish"},
    "de": {"flag": "de", "name": "German"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ru": {"flag": "ru", "name": "Russian"},
}

# ------------------------------ #
# GLOBALS FOR GENERAL APP's:     #
# ------------------------------ #

UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"
IMG_SIZE = (150, 150, True)

AUTH_TYPE = 1
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"

APP_NAME = "BAKALÁRSKA PRÁCA: WEB PRE ROBOCUPJUNIOR"
# APP_THEME = ""                    # default
APP_THEME = "cyborg.css"            # COOL
# APP_THEME = "slate.css"           # COOL
# APP_THEME = "cerulean.css"        # COOL
# APP_THEME = "spacelab.css"        # NICE
# APP_THEME = "amelia.css"          # IDK
# APP_THEME = "cosmo.css"           # IDK
# APP_THEME = "flatly.css"          # IDK
# APP_THEME = "journal.css"         # IDK
# APP_THEME = "readable.css"        # IDK
# APP_THEME = "simplex.css"         # IDK
# APP_THEME = "united.css"          # IDK
