# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:18:41 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
sam = Minecraft.create()

while True:
    sam.executeCommand("time add 10")
    time.sleep(0.01)