# -*- coding: utf-8 -*-

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app import appbuilder, db
from app.models.test_model import Test


class TestModelView(ModelView):
    # route_base = "/admin/test"
    datamodel = SQLAInterface(Test)
    list_columns = ["id", "name"]
    base_order = ("id", "desc")


db.create_all()
appbuilder.add_view(
    TestModelView,
    "Test",
    icon="fa fa-binoculars",
    category_icon="fa fa-binoculars",
    category="Test",
)
