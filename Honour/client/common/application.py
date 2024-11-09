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
from Honour.client.components.asyncio_client import *


class Application(QApplication):
    """ Singleton application """
    def __init__(self):
        super(Application, self).__init__()

        self.client = HonourClient()


    def check(self):
        result = self.client.request({'type': C2S_CHECK, 'status': C2S_STATUS, 'version': VERSION})
        if result['code'] == S2C_NORMAL:
            if result['type'] == C2S_CHECK:
                if result['status'] == S2C_STATUS:
                    pass

                else:
                    print(result['info'])
                    sys.exit()
        else:
            print('服务器异常')
