#########################################################################################################
Názov bakalárskej práce: Webová aplikácia na prideľovanie slotov v medzinárodných súťažiach RoboCupJunior
#########################################################################################################
Autor: Erik Mihálik
#########################################################################################################

############################################################################################################################################################################################

Príkazy pre prvotné spustenie webovej aplikácie::

    setx FLASK_APP app/__init__.py
    flask --app "app:create_app('config')" fab create-admin
    flask --app "app:create_app('config')" run

Webová aplikácia beží na::

    localhost:5000

POZOR: V prípade, že sa niečo pokazilo (zmenalo sa meno priečinku / cesta k priečinku), tak je potrebné postupovať nasledovne::

    1. Ak sa nachádza v priečinku ".venv" medzi súbormi aplikácie, tak ho VYMAŽTE (kľudne môžete vymazať aj: "__pycache__").
    2. Ak náhodou nemáte nainštalované "poetry", tak ho nainštalujte do tohto priečinka (do terminálu zadajte: "poetry install").
    3. Vytvorte si nový ENVIRONMENT pomocou "pyproject.toml" s použitím napr. VisualStudioCode (tlačítko), alebo terminálu (príkazy).
    4. Teraz by už mali fungovať príkazy, ktoré používate zvyčajne, teda príkazy na inicializáciu webovej aplikácie, vytvorenie nového administrátora a spustenie webovej aplikácie.

############################################################################################################################################################################################

Dokladám aj databázový súbor "app.db" s testovacími dátami pre prípad, že by Ste si chceli otestovať moju webovú aplikáciu. Tu sú dôležité informácie::

    1. Prihlasovacie údaje pre administrátora systému:

        Prihlasovacie meno: Administrator
        Prihlasovacie heslo: 1
    
    2. Prihlasovacie údaje pre manažérov systému:

        Prihlasovacie meno: Slovakia
        Prihlasovacie heslo: 1

        Prihlasovacie meno: Czechia
        Prihlasovacie heslo: 1

V prípade, že by Ste si chceli vytvoriť vlastný databázový súbor, tak stačí vymazať databázový súbor "app.db" a použiť "Príkazy pre prvotné spustenie webovej aplikácie" (spomenuté vyššie).

############################################################################################################################################################################################