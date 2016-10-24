# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:18:14 2016

@author: Kenneth
"""
import Tkinter as tk
from ui.ui import MainWindow

dependency = 'Tkinter'

try:
    __import__(dependency)
except ImportError as e:
    print str(e)+' :'+dependency+' '+'is probably not installed on the system'


root = tk.Tk()
root.title("Automatic License Plate Recognition")

app = MainWindow(root)


root.mainloop()
