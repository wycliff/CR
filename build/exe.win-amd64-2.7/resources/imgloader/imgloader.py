# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:57:22 2016

@author: Kenneth
"""

from PIL import Image, ImageTk
from constants.alprconstants import CANVAS_WIDTH, CANVAS_HEIGHT

"""
Loads program image resources
"""
import os

cwd = os.getcwd()

MAIN_BG = Image.open(cwd+'\\resources\\img\\alpr-main-bg.png')
    

def loadImage(path):
     img = Image.open(path)
     
     isbigger = isLargerThanCanvas(img.height, img.width, CANVAS_WIDTH, CANVAS_HEIGHT) 
     
     if (isbigger):
         resized = img.resize((CANVAS_WIDTH,CANVAS_HEIGHT), Image.ANTIALIAS)
         return ImageTk.PhotoImage(resized)         
         
     else:   
         return ImageTk.PhotoImage(img)

def isLargerThanCanvas(img_height, img_width, canvas_width, canvas_height):
    return (img_height * img_width) > (canvas_width * canvas_height)    