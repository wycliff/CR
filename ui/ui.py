# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 22:30:24 2016

@author: Kenneth
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 12:19:43 2016

@author: Kenneth
"""

import tkFileDialog as tFD
import Tkinter as tk
from PIL import Image, ImageTk
from constants.alprconstants import ROOT_WIDTH, ROOT_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT
from fileops.getfilename import getFileName
from resources.imgloader import imgloader        
         

class MainWindow():
     groot = None
     frame_root = None
     imgloader=None
     file_name_list = []
     file_name_var = None
     x0, y0 = None, None
     listbox = None
     file_paths = None
     img_canvas = None
     canvas = None
     """
     Initializing MainWindow Class
     """
     def __init__(self, root):
         global groot, file_name_list, file_name_var, frame_root, listbox, img_canvas, canvas
         #initialise imgloader
         #imgloader = ImageConstants()
         
         #configure root
         root.minsize(width=ROOT_WIDTH, height=ROOT_HEIGHT)
         root.resizable(width=False, height=False)
         #center window on screen
         screen_width = root.winfo_screenwidth()
         screen_height = root.winfo_screenheight()
         posx = (screen_width/2)- (ROOT_WIDTH/2)
         posy = (screen_height/2)- (ROOT_HEIGHT/2)
         
        
         root.geometry('%dx%d+%d+%d' %(ROOT_WIDTH, ROOT_HEIGHT,posx, posy))
         
         # Adding the menu bar
         
         self.menubar = tk.Menu(root)
         #menus
         self.filemenu = tk.Menu(self.menubar, tearoff=0)
         self.helpmenu = tk.Menu(self.menubar, tearoff=0)
         
         self.menubar.add_cascade(label="File", menu=self.filemenu)
         self.menubar.add_cascade(label="Help", menu=self.helpmenu)
         
         self.filemenu.add_command(label="Load Image" ,command=self.IndLoadImage, )
         root.config(menu=self.menubar)
         
         
         #label for bg image, place before all other widgets
         self.img = imgloader.MAIN_BG
         
         self.bg_height = self.img.height
         self.bg_width = self.img.width
         
         self.bg = ImageTk.PhotoImage(self.img)
         self.bg_label = tk.Label(master=root, image=self.bg)
         self.bg_label.image = self.bg
         self.width_diff = ROOT_WIDTH-self.bg_width
         self.height_diff = ROOT_HEIGHT-self.bg_height
         self.bg_label.place(x=-150, y=-100)
         
         
         #add frames to window
         self.frame_posx, self.frame_posy = 600, 20
         self.frame_height, self.frame_width = ROOT_HEIGHT*0.55, ROOT_WIDTH*0.2
         
         self.frame_file_list = tk.Frame(root,
                                         bg="#e3e3e3",
                                         width=self.frame_width,
                                         height=self.frame_height,
                                         borderwidth=1)
         
         
         
         self.frame_file_list.place(x=self.frame_posx,y=self.frame_posy)
         
         
         
         self.btn_load_var = tk.StringVar()
         self.btn_load_var.set("Load")
         print self.frame_height, self.frame_width
         self.btn_load_options = {'txt':"Load",
                                  'command':self.IndLoadImage, 
                                  'x':10, 'y':235, 'anchor':tk.NW, 
                                  'bg':'#fff'}
         
         #create widgets
         self.btn_load = self.addButtonCommand(root=self.frame_file_list,
                                               **self.btn_load_options)  #key word arguments
         
         self.label_file_name_var = tk.StringVar()
         self.label_file_name_var.set("")
         file_name_var = self.label_file_name_var
         self.label_file_name_options = {'textvariable':self.label_file_name_var,
                                         'justify':tk.CENTER, 
                                         'bg':'white'}
         
         #self.label_file_name = tk.Label(master=self.frame_file_list, **self.label_file_name_options)
         #self.label_file_name = self.addLabel(root,"")
         #self.label_file_name.place(x=0,y=0)
         
         #test canvas
         self.canvas = tk.Canvas(master=root,
                                 width=500,
                                 height=400,
                                 bd=2, 
                                 relief=tk.SUNKEN)
         
         canvas = self.canvas
         img_canvas =  self.canvas.create_image(0,0,anchor=tk.NW, image=self.bg)
         self.canvas.place(x=0, y=0)
         
         
         #list box
         self.list = tk.Listbox(master=self.frame_file_list)
         self.list.place(x=0, y=0)
         #for x in [1,2,3,4]:
          #   self.list.insert(tk.END, x)
         
         #bind listbox to event listener
         self.list.bind('<<ListboxSelect>>', self.selection)
         
         listbox = self.list
         groot = root
         frame_root = self.frame_file_list
         #print self.frame_file_list.winfo_width()
         
#=======================End __init__=
#================listbox event handler=================================#

     def selection(self,event):
         global listbox, file_paths, img_canvas, canvas
         index = listbox.curselection()
         #print index[0]
         path = file_paths[index[0]]
         img_to_load = imgloader.loadImage(path)
        
                  
         
         canvas.delete(img_canvas)
         canvas.image = img_to_load
         canvas.create_image(0,0, anchor=tk.NW, image=img_to_load)
         
#        value = listbox.get(index)
 #       print value
     
     
#=======================Methods to Load Images================================#    
           
     def IndLoadImage(self):
         """Indirect method to load image; avoids use of lambda functions and global variables(partially)"""
         self.loadImage(self.groot)
     
     def loadImage(self,root):
         """Selects* image from directory and gets file name"""
         global file_name_var, frame_root, listbox, file_paths
         self.file_names = []
         self.files  = []
         self.file_list = []#full path name
         self.file_options = {'initialdir':'/',
                              'title':'Choose file(s) to load',
                              'filetypes':[('JPEG','*.jpg'),('Bitmap Image','*.bmp'),('PNG Images','*.png')]}
         
         self.file_tuple = tFD.askopenfilenames(parent=root, **self.file_options )
         #print self.file_tuple
         if self.file_tuple != '':
             for index, value in enumerate(self.file_tuple):
                 self.file_list.append(str(self.file_tuple[index]))
             #print self.file_list
             file_paths = self.file_list
             
             for f in self.file_list:
                 self.file_names.append(getFileName(f,'/'))
            # print (self.file_names)
            
             for name in self.file_names:
                 listbox.insert(tk.END, name)
             
             #for x in range(len(self.file_list)):
              #   self.files.append((self.file_list[x], self.file_names[x]))
             self.files = zip(self.file_list, self.file_names)
             #print self.files
#=======================End load image================================#
             
             

#====================Methods to add button========================#
     def addButton(self,root, txt):
         """Resusable code to add button to window"""
         self.btn_txt_var = tk.StringVar()
         self.btn_txt_var.set(txt)
         
         tk.Button(master=root, textvariable=self.btn_txt_var).pack()
         
     def addButtonCommand(self,root,txt,command, x=50, y=150, side=tk.BOTTOM, anchor=tk.NW, bg='#fff', fill=tk.BOTH):
         """Resusable code to add button with callback function to window"""
         self.btn_txt_var = tk.StringVar()
         self.btn_txt_var.set(txt)
         
         self.options={'textvariable':self.btn_txt_var, 'command':command, 'padx':10, 'anchor':tk.CENTER, 'bg':bg}
         
         tk.Button(master=root, **self.options).place(x=x,y=y)
         
#=================end addutton========================#    
         
         
         
#================add labels=================#
         
     def addLabel(self, root, txt):
          global file_name_var, x0, y0
          x0,y0=-10,10
          file_name_var.set(txt)
          tk.Label(master=root, textvariable=file_name_var, bg='white').place(x=x0+10, y=y0+10)
          x0, y0 = x0+10, y0+10
          
          
        
#=======================Class for Frames===========================#

