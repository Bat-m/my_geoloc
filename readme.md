Projet pour du tracking gps
et gestion data tracking (avec essai partition pgsql)

ce projet utilise python 3 et poetry ainsi qu'alembic en back
svelte en front

pour installer une librairie python:
poetry add */name-lib/*

poetry shell -> initliasier python virtuel

créer une nouvele revision dpour la migration
alembic revision -m "infos here"

générer la migration 
alembic upgrade head