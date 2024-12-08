# -*- coding: utf-8 -*-

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Test(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return self.name
