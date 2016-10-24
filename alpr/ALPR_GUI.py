# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:53:03 2016

@author: Wycliffe
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 20:31:11 2016

@author: Wycliffe
"""


from Tkinter import *
from PIL import Image, ImageTk


#Main window
root = Tk()
root.title("ALPR")
root.configure(background="#000")


#fixed size of the window
#root.maxsize(700,700) 
root.minsize(800,600) #width, height
root.resizable(width=FALSE, height=FALSE)
    

#adding canvas to the main  window
# Size of the canvas
canvas_width =500
canvas_height =400


canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.place(x=0,y=0)

canvas.configure(background="#fff")
sumn=None


#Loading image 
this_image = Image.open("C:/Users/Wycliffe/Desktop/snaps/test_004.jpg")

#If the image is bigger than it is resized else it remains the same way
if(this_image.width * this_image.height > canvas_width * canvas_height ):
    getImage=this_image.resize((canvas_width,canvas_height),Image.ANTIALIAS)#Withpath
else:       
    getImage=this_image
    
myImg = ImageTk.PhotoImage(getImage)
#myImg = ImageTk.PhotoImage(file="test_013.jpg")




def loader():
    #Load image into the canvas using canvas.create_image(x,y,anchor= ,image
    global sumn
    sumn = canvas.create_image(0,0, anchor=NW,image=myImg)
    
def remove():
    global sumn
    canvas.delete(sumn)
    
    
def close():
    root.destroy()
    

    
myButton1=Button(root,text="LOAD IMAGE", command=loader)
myButton1.place(x=600,y=300)  
          
myButton2=Button(root,text="REMOVE", command=remove)
myButton2.place(x=600,y=400) 
          
root.mainloop()

    