#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/19 10:07
# @Author    :Andy
# @FileName  :game_client.py
# @Software: PyCharm
from Honour.client.common.config import *
from Honour.client.common.async_client import *


class GameClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.MAX_BYTES = config.get()['server']['max_bytes']
        self.client = AsyncClient(self.ip, self.port, self.MAX_BYTES)

if __name__ == "__main__":
    pass
