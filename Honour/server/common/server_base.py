#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/12 20:39
# @Author    :Andy
# @FileName  :server_base.py
# @Software: PyCharm
import json
import asyncio

from Honour.server.common.share.const import *

class ServerBase(object):
    def __init__(self, config, logger):
        self.config = config
        self.ip = self.config.get()['server']['ip']
        self.port = self.config.get()['server']['port']
        self.MAX_BYTES = self.config.get()['server']['max_bytes']
        self.logger = logger

    def reconfiguring(self):
        self.ip = self.config.get()['server']['ip']
        self.port = self.config.get()['server']['port']
        self.MAX_BYTES = self.config.get()['server']['max_bytes']

    async def handle_client(self, reader, writer):
        data = await reader.read(self.MAX_BYTES)
        msg = json.loads(data.decode())
        s2cmsg = {}

        ## to handle

        writer.write(json.dumps(s2cmsg))
        await writer.drain()

    async def run(self):
        server = await asyncio.start_server(self.handle_client, self.ip, self.port)
        print('Serving at:', self.ip, self.port)
        async with server:
            await server.serve_forever()


class ClientItem(object):
    def __init__(self, socket):
        self.socket = socket
        self.status = None
        self.account = None
