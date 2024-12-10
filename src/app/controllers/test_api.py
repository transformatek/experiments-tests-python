# -*- coding: utf-8 -*-
from flask import request
from flask_appbuilder.api import BaseApi, ModelRestApi, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app import appbuilder, db
from app.models.test_model import Test


class TestModelApi(ModelRestApi):
    resource_name = "test"
    base_order = ("id", "desc")
    datamodel = SQLAInterface(Test)


appbuilder.add_api(TestModelApi)


class ExampleApi(BaseApi):
    @expose("/greeting")
    def greeting(self):
        """
        Simple Greeting Endpoint
        ---
        get:
          summary: Greeting API
          description: Returns a simple greeting message
          responses:
            200:
              description: Successful Response
              content:
                text/plain:
                  schema:
                    type: string
                    example: "hello"
        """

        return "hello"


appbuilder.add_api(ExampleApi)


class TestApi(BaseApi):
    resource_name = "test-test"

    @expose("", methods=["POST"])
    def add_test(self):
        """
        Add a new Test record
        ---
        post:
          summary: Create a new Test record
          description:
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    name:
                      type: string
                      example: "Example Name"
          responses:
            201:
              description: Test record created successfully
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
                        example: "Test record created successfully"
                      id:
                        type: integer
                        example: 1


        """
        data = request.get_json()

        if "name" not in data:
            return ({"error": "Field 'name' is required"}), 400

        test_record = Test(name=data["name"])
        db.session.add(test_record)
        db.session.commit()

        return ({"message": "Test record created successfully", "id": test_record.id}), 201


appbuilder.add_api(TestApi)
