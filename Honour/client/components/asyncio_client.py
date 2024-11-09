#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/19 10:07
# @Author    :Andy
# @FileName  :asyncio_client.py
# @Software: PyCharm
from Honour.client.common.config import *
from Honour.client.common.async_client import *


class HonourClient(AsyncClient):
    def __init__(self):
        AsyncClient.__init__(self, config.get()['server']['ip'],
                                   config.get()['server']['port'],
                                   config.get()['server']['max_bytes'])

    async def request(self, message):
        try:
            return self.c2s(message)
        except:
            return {}


if __name__ == "__main__":
    honour = HonourClient()
