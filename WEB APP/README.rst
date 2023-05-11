################################################################################
Webová aplikácia na prideľovanie slotov v medzinárodných súťažiach RoboCupJunior
################################################################################

Príkazy pre prvotné spustenie webovej aplikácie (NIEKEDY...)::

    setx FLASK_APP app/__init__.py
    flask fab create-admin
    flask run

Príkazy pre prvotné spustenie webovej aplikácie (DNES...)::

    setx FLASK_APP app/__init__.py
    flask --app "app:create_app('config')" fab create-admin
    flask --app "app:create_app('config')" run

V prípade, že niečo nefunguje (zmena mena / cesty priečinku), tak je potrebné postupovať nasledovne::

    1. Ak sa nachádza ".venv" medzi súbormi aplikácie, tak ho VYMAŽ (kľudne môžeš aj: "__pycache__").
    2. Ak náhodou nemáš nainštalované "poetry", tak ho nainštaluj do tohto priečinka cez terminál "poetry install".
    3. Vytvor si nový ENVIRONMENT cez "pyproject.toml" s použitím napr. VisualStudioCode, alebo terminálu.
    4. Môžeš inicializovať aplikáciu, vytvoriť si nového administrátora a zapnúť aplikáciu.

Webová aplikácia beží na::

    localhost:5000