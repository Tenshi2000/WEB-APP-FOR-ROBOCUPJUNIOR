################################################################################
Webová aplikácia na prideľovanie slotov v medzinárodných súťažiach RoboCupJunior
################################################################################

Príkazy pre prvotné spustenie webovej aplikácie::

    setx FLASK_APP app/__init__.py
    flask fab create-admin
    flask run

Webová aplikácia beží na::

    localhost:5000