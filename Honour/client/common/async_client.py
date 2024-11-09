#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/12 20:38
# @Author    :Andy
# @FileName  :async_client.py
# @Software: PyCharm
import json
import asyncio


class AsyncClient(object):
    def __init__(self, ip, port, MAX_BYTES):
        self.ip = ip
        self.port = port
        self.MAX_BYTES = MAX_BYTES

    async def c2s(self, message):
        """ c2s接口 """
        reader, writer = await asyncio.open_connection(self.ip, self.port)
        data = json.dumps(message).encode()
        writer.write(data)
        await writer.drain()

        message = await reader.read(self.MAX_BYTES)
        return json.loads(message.decode())
