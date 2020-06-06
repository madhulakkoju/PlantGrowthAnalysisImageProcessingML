from tkinter import *
from file1 import *
import tkinter.font as font
from PIL import Image
import VotingClassifier as vote

from DataSupport import *
voteClassifier = vote.model(x_train,y_train)
vote.test(voteClassifier,x_test,y_test)

def ButtonClicked(event):
    imagepath = path.get()
    #imagepath.replace(
    print(imagepath)
    master.im1 = Image.open(imagepath)
    featureset = FeatureExtract(imagepath)
    pred = vote.predict(voteClassifier,[featureset])
    print(pred)
    w = Message( master,font = font.Font(size= 15), text= str(pred) ).grid(row = 10,column = 1)

master = Tk(screenName=" Home " )
master.geometry("700x500")
master.title (' Home Page ')
myfont = font.Font(size = 20)
Label(master,font = myfont, text='Image Path  ').grid(row=2) 

path = Entry(master,width="50") 
path.place(width = 50,height = 10)


path.grid(row=2, column=1) 

button = Button(master,text = " Predict ",bg = "green" ,fg = "black",width = 20)
button['font'] = myfont
button.grid(row = 6, column = 1)
#message = "Give the image path in this box to get the prediction ! " 
#w = Message( master, font = font.Font(size= 15) ,text= "PREDICT " ).grid(row = 0,column = 0)
#w1 = Message( master, font = font.Font(size= 15) ,text= "PLANT" ).grid(row = 0,column = 1)
w2 = Message( master, font = font.Font(size= 15) ,text= "Species" ).grid(row = 10,column = 0)
button.bind("<Button>",ButtonClicked)



master.mainloop()
