#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
logging.basicConfig(level=logging.DEBUG)

try:
    epd = epd2in13_V4.EPD()
    epd.init()
    epd.Clear(0xFF)

    epd.sleep()


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    exit()
