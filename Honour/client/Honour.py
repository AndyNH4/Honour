#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/7 13:47
# @Author    :Andy
# @FileName  :Honour.py
# @Software: PyCharm
import os
import sys
import asyncio
from pathlib import Path
from inspect import getsourcefile

os.chdir(Path(getsourcefile(lambda: 0)).resolve().parent)

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QLocale, QTranslator

from common.config import config
from common.setting import APP_NAME
from common.application import HApplication

app = HApplication()
asyncio.run(app.run())
