# -*- coding: utf-8 -*-
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import ModelRestApi,expose,BaseApi
from app import appbuilder
from app.models.test_model import Test
from app import appbuilder



class TestModelApi(ModelRestApi):
    resource_name = "test"
    base_order = ("id", "desc")
    datamodel = SQLAInterface(Test)


appbuilder.add_api(TestModelApi)



class ExampleApi(BaseApi):
    @expose('/greeting')
    def greeting(self):
        return "hello"
appbuilder.add_api(ExampleApi)