#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/7 14:11
# @Author    :Andy
# @FileName  :asyncio_server.py
# @Software: PyCharm
import aiomysql

from Honour.server.common.const import *
from Honour.server.common.config import config
from Honour.server.common.server_base import *


class AsyncioServer(ServerBase):
    def __init__(self, config, logger):
        ServerBase.__init__(self, config, logger)

        self.conn = None
        self.cursor = None

        asyncio.run(self.load())

        """
            self.account dic
            {'id': AccountItem,}
        """
        self.account = {}
        sql = "select id, account, nickname from account"
        result = asyncio.run(self.select(sql))
        for item in result:
            self.account[item[0]] = item[1]

    async def load(self):
        self.conn = await aiomysql.connect(host='localhost', port=3306, user='root', password='root', db='honour')
        self.cursor = await self.conn.cursor()

    async def select(self, sql):
        try:
            await self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            pass

    async def handle_client(self, reader, writer):
        data = await reader.read(self.config.get()['server']['MAX_BYTES'])
        msg = json.loads(data.decode())
        s2cmsg = {}
        ## handle
        if msg['type'] == C2S_CHECK:
            if msg['status'] == C2S_STATUS:
                if msg['version'] == '':
                    s2cmsg = {
                        'code': S2C_NORMAL,
                        'type': C2S_CHECK,
                        'status': S2C_STATUS,
                        'sign': 123
                    }
                else:
                    s2cmsg = {
                        'code': S2C_NORMAL,
                        'type': C2S_CHECK,
                        'status': False,
                        'info': 'version to old'
                    }

            else:
                s2cmsg = {
                    'code': S2C_NORMAL,
                    'type': C2S_CHECK,
                    'status': False,
                    'info': 'key is wrong'
                }

        else:
            if msg['sign'] == 123:
                if msg['type'] == C2S_LOGIN:
                    pass

                elif msg['type'] == C2S_REGISTER:
                    pass

        writer.write(json.dumps(s2cmsg))
        await writer.drain()

    def shell(self):
        """ shell """
        pass


class AccountItem(object):
    def __init__(self, id, account, status, nickname, socket=None):
        self.id = id
        self.account = account
        self.status = status
        self.nickname = nickname
        self.socket = socket


if __name__ == "__main__":
    server = AsyncioServer(config, None)
    asyncio.run(server.run())
