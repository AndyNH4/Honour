#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/19 10:28
# @Author    :Andy
# @FileName  :application.py
# @Software: PyCharm
import sys

from PySide6.QtWidgets import QApplication

from Honour.client.common.setting import *
from Honour.client.common.share.const import *
from Honour.client.common.async_client import *


class HApplication(QApplication):
    """ Singleton application """
    def __init__(self):
        super().__init__(sys.argv)

        self.client = AsyncClient(config.get()['server']['ip'],
                                  config.get()['server']['port'],
                                  config.get()['server']['max_bytes'])


    async def check(self):
        result = await self.client.c2s({'type': C2S_CHECK, 'status': C2S_STATUS, 'version': VERSION})
        try:
            if result['code'] == S2C_NORMAL:
                if result['type'] == C2S_CHECK:
                    if result['status'] == S2C_STATUS:
                        # 验证通过
                        return True

                    else:
                        return result['info']
                else:
                    return False
            else:
                return False
        except KeyError:
            return False

    async def run(self):
        """ run """
        check = await self.check()
        if check:
            # 验证通过
            pass

        else:
            print(check)
            sys.exit(0)
