# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:14:28 2018

@author:Sam 
"""
from mcpi.minecraft import Minecraft
sam = Minecraft.create()

x,y,z = sam.player.getTilePos()
sam.spawnEntity(x,y,z,53)
