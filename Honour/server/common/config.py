#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/7 14:14
# @Author    :Andy
# @FileName  :config.py
# @Software: PyCharm
import json

from .setting import APP_NAME, CONFIG_FOLDER, CONFIG_FILE


class Config(object):
    def __init__(self):

        self.config = None
        self.load()

    def get(self):
        return self.config

    def load(self):
        """ load config """
        try:
            with open('./ServerData/config.json', encoding="utf-8") as f:
                self.config = json.load(f)
        except:
            self.config = {"server": {"ip": "127.0.0.1","port": 12127,"max_bytes": 1024}}

    def save(self):
        """ save config """
        CONFIG_FOLDER.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)


config = Config()