# -*- coding: utf-8 -*-
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import ModelRestApi
from app import appbuilder
from app.models.test_model import Test
from app import appbuilder



class TestModelApi(ModelRestApi):
    resource_name = "test"
    base_order = ("id", "desc")
    datamodel = SQLAInterface(Test)


appbuilder.add_api(TestModelApi)