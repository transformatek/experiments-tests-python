from flask import Flask, jsonify
from flask.wrappers import Response
from flask_appbuilder import SQLA, AppBuilder
from flask_migrate import Migrate
from sqlalchemy import MetaData

app = Flask(__name__)
app.config.from_object("config")


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
db = SQLA(app, metadata=metadata)

migrate = Migrate(app, db, render_as_batch=True)

appbuilder = AppBuilder(app, db.session)

app.response_class = Response


# Register views

if __name__ == "__main__":
    app.run(debug=True)

from . import controllers, models, views
