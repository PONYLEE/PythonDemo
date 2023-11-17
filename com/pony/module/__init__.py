#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包。
'''
# export PYTHONPATH=$PYTHONPATH:path/to/com
import sys
import support
from ..common import print_utils


support.print_func('pony')

from pkg.runoob import runoob1
runoob1()

# from .. common.print_utils import print_split_line
# import .. common.print_utils
# print_utils.print_split_line('test')
sys.path.append('D:\\idea_workspace\\PythonDemo\\com')