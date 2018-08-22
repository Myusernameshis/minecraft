# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:19:08 2018

@author: Sam
"""

from mcpi.minecraft import Minecraft
sam = Minecraft.create()

x,y,z=sam.player.getTilePos()
sam.setSign(x,y,z,63,0,"W","","","L")