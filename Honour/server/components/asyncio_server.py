#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/7 14:11
# @Author    :Andy
# @FileName  :asyncio_server.py
# @Software: PyCharm
from importlib.metadata import pass_none

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
        sql = "select id, account, nickname from account;"
        result = asyncio.run(self.select(sql))
        for item in result:
            self.account[item[0]] = AccountItem(item[0], item[1], FREE, item[2])

    # 初始化数据库
    async def load(self):
        """ load """
        self.conn = await aiomysql.connect(host='localhost', port=3306, user='root', password='root', db='honour')
        self.cursor = await self.conn.cursor()

    # 执行mysql数据库查询
    async def select(self, sql):
        """ select """
        try:
            await self.cursor.execute(sql)
            return self.cursor.fetchall()._result
        except Exception as e:
            pass

    # 关闭服务器
    async def close(self):
        """ close """
        self.conn.close()

    # 处理客户端请求
    async def handle_client(self, reader, writer):
        """ handle client """
        data = await reader.read(self.config.get()['server']['MAX_BYTES'])
        msg = json.loads(data.decode())
        s2cmsg = {}

        # handle

        # 验证信息
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
            # 验证数字签名
            if msg['sign'] == 123:
                if msg['type'] == C2S_LOGIN:
                    pass

                elif msg['type'] == C2S_REGISTER:
                    pass

        writer.write(json.dumps(s2cmsg))
        await writer.drain()

    # 命令提示符
    def shell(self):
        """ shell """
        while True:
            message = input()
            # 帮助
            if message == 'help':
                pass

            # 关于
            elif message == 'about':
                pass

            # 关闭命令提示符
            elif message == 'quit':
                break

            # 关闭服务器
            elif message == 'stop':
                asyncio.run(self.close())
                break

            # 重启服务器
            elif message == 'reboot':
                pass

            # 查询服务器数据
            elif message[:5] == 'select':
                pass

            # 具体命令帮助
            elif message[:3] == 'help':
                if message == 'help':
                    pass

                elif message == 'about':
                    pass

                elif message == 'stop':
                    pass

                elif message == 'reboot':
                    pass

                elif message == 'select':
                    pass

                else:
                    pass

            else:
                print('位置命令')


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
