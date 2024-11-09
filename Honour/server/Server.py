#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2024/10/7 14:07
# @Author    :Andy
# @FileName  :Server.py
# @Software: PyCharm
import os
import sys
from pathlib import Path
from inspect import getsourcefile

os.chdir(Path(getsourcefile(lambda: 0)).resolve().parent)

from Honour.server.common.logger import *
from Honour.server.common.config import config
from Honour.server.components.game_server import *
from Honour.server.components.asyncio_server import *

server = AsyncioServer(config, Logger('log.txt'))
asyncio.run(server.run())
