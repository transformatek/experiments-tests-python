# -*- coding: utf-8 -*-
import pytest



def func(x):
    if x <= 0:
        raise ValueError("x needs to be larger than zero")


pytest.raises(ValueError, func, x=-2)