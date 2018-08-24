# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:21:54 2018

@author: NTPU
"""
from time import sleep
from mcpi.minecraft import Minecraft
sam = Minecraft.create()
sleep(2)
myID=sam.getPlayerEntityID("sam0617")
sam.postToTitle(myID,"§天亮了","§you are a human")
