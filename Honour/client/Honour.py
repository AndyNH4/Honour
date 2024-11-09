#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/7 13:47
# @Author    :Andy
# @FileName  :Honour.py
# @Software: PyCharm
import os
import sys
from pathlib import Path
from inspect import getsourcefile

os.chdir(Path(getsourcefile(lambda: 0)).resolve().parent)
