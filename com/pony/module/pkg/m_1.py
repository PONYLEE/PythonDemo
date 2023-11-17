#!/usr/bin/python
# -*- coding: UTF-8 -*-
import warnings

warnings.warn("the imp module is deprecated in favour of importlib; "
              "see the module's documentation for alternative uses",
              DeprecationWarning, stacklevel=2)

def module_func():
    """**DEPRECATED**

    :return:
    """
    return module_var1*2

module_var1 = 100

class Class1:
    class_var_1=2

    def __init__(self, obj_var_1):
        self.obj_var_1 = obj_var_1

    def getVarSum(self):
        return Class1.class_var_1 + self.obj_var_1

