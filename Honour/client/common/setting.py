#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/12 20:38
# @Author    :Andy
# @FileName  :setting.py
# @Software: PyCharm
from pathlib import Path
from PySide6.QtCore import QStandardPaths

# change DEBUG to False if you want to compile the code to exe
DEBUG = True


YEAR = 2024
AUTHOR = "Andy"
VERSION = "Beta 1.0"
APP_NAME = "Honour"
HELP_URL = "https://space.bilibili.com/663055127?spm_id_from=333.1007.0.0"
FEEDBACK_URL = "https://space.bilibili.com/663055127?spm_id_from=333.1007.0.0"
RELEASE_URL = "https://space.bilibili.com/663055127?spm_id_from=333.1007.0.0"


if DEBUG:
    CONFIG_FOLDER = Path('AppData').absolute()
else:
    CONFIG_FOLDER = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)) / APP_NAME

CONFIG_FILE = CONFIG_FOLDER / "config.json"
