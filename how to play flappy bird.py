import cv2
from tkinter import *
from PIL import Image,ImageTk
root1 = Tk ( )
root1.title ( 'How to Play Flappy Bird Game ' )
root1.geometry ( '800x500+360+150' )
root1.configure ( bg = "white" )
root1.resizable ( False , False )

ima = cv2.imread("C:/Users/sujal/PycharmProjects/new_Python_Project/images/how to play flappy bird.png" )
imgr1 = cv2.resize ( ima , (800 , 470) )
img_rgb1 = cv2.cvtColor ( imgr1 , cv2.COLOR_BGR2RGB )
img_tk = ImageTk.PhotoImage ( Image.fromarray ( img_rgb1 ) )

Label( root1,image = img_tk).place(x=0,y=5)

root1.mainloop()