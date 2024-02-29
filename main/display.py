#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')

#pid_file = "/home/kali/display/pid/display.pid"

#if os.path.exists(pid_file):
#    print("Process is already running.")


#with open(pid_file, "w") as file:
#    file.write(str(os.getpid()))

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13_V4 Demo")

    epd = epd2in13_V4.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    time.sleep(1)

    # Drawing on the image
    logging.info("E-Paper refresh")
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)

        # read bmp file
    while True:
        try:
            
              
            logging.info("E-paper refresh")
            logging.info("2.read bmp file...")
            image = Image.open(os.path.join(picdir, 'skull.bmp'))
            epd.display(epd.getbuffer(image))
            time.sleep(5)
            
            logging.info("E-paper refresh")
            logging.info("2.read bmp file...")
            image = Image.open(os.path.join(picdir, 'hands.bmp'))
            epd.display(epd.getbuffer(image))
            time.sleep(5)
            
            logging.info("E-paper refresh")
            logging.info("2.read bmp file...")
            image = Image.open(os.path.join(picdir, 'sad.bmp'))
            epd.display(epd.getbuffer(image))
            time.sleep(5)
             

        except KeyboardInterrupt:
            logging.info("Ctrl+C pressed. Exiting...")
            break


    logging.info("Clear...")
    #epd.init()
    #epd.Clear(0xFF)

    logging.info("Goto Sleep...")
    epd.sleep()


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    exit()
