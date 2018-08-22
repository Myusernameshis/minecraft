# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:08:27 2018

@author: Sam
"""
from mcpi.minecraft import Minecraft
sam = Minecraft.create()
x,y,z=sam.player.getTilePos()
name=input("請輸入姓名")
s=input("請輸入想說的話")
sam.postToChat("<"+name+">")
