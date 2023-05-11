import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from sqlalchemy import event
from sqlalchemy.engine import Engine

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

db = SQLA()
appbuilder = AppBuilder()

def create_app(config):

    app = Flask(__name__)

    with app.app_context():

        app.config.from_object(config)
        db.init_app(app)

        from . import models
        db.create_all()
        
        from .index import DefaultView
        from .views import initViews

        appbuilder.indexview = DefaultView
        appbuilder.init_app(app, db.session)
        
        initViews()
        appbuilder.post_init()

    return app

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
