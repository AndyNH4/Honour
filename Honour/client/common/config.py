#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/7 14:20
# @Author    :Andy
# @FileName  :config.py
# @Software: PyCharm
import json
from enum import Enum

from .setting import APP_NAME, CONFIG_FOLDER, CONFIG_FILE


class Language(Enum):
    """ Language enumeration """

    CHINESE_SIMPLIFIED = "zh"
    CHINESE_TRADITIONAL = "hk"
    ENGLISH = "en"
    AUTO = "Auto"


class Theme(Enum):
    """ Theme enumeration """

    LIGHT = "Light"
    DARK = "Dark"
    AUTO = "Auto"


class Config(object):
    def __init__(self):

        self.config = {}

        self.load()

    def get(self, key, default=None):
        return self.config.get(key, default)

    def load(self):
        """ load config """
        try:
            with open(CONFIG_FILE, encoding="utf-8") as f:
                cfg = json.load(f)
        except:
            cfg = {"server": {"ip": "127.0.0.1","port": 12127}}

        self.config = cfg

    def save(self):
        """ save config """
        CONFIG_FOLDER.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)


config = Config()
