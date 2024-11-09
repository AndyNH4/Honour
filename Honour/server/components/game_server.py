#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/12 20:40
# @Author    :Andy
# @FileName  :game_server.py
# @Software: PyCharm
from Honour.server.common.server_base import *

class GameServer(ServerBase):
    def __init__(self, config, logger):
        ServerBase.__init__(self, config, logger)
