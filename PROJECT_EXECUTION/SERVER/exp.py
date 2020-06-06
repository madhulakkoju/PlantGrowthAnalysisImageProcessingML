from tkinter import filedialog
from tkinter import*
import tkinter as tk

from file1 import *
import tkinter.font as font
from PIL import Image, ImageTk
#import VotingClassifier as vote

#from DataSupport import *
#voteClassifier = vote.model(x_train,y_train)
#vote.test(voteClassifier,x_test,y_test)

def openfilename(): 
  
    # open file dialog box to select image 
    # The dialogue box has a title "Open" 
    filename = filedialog.askopenfilename(title ="Input Image")
    #global imagpath
    #imagpath = filename
    return filename 

def ButtonClicked(event):
    imagepath = openfilename()
    #imagepath.replace(
    open_img(imagepath)
    #imagepath = imagpath
    print(imagepath)
    master.im1 = Image.open(imagepath)
    featureset = FeatureExtract(imagepath)
    #pred = vote.predict(voteClassifier,[featureset])
    #print(pred)
    pred = " pred output "
    #w = Message( master,font = font.Font(size= 15), text= str("pred") ).grid(row = 10)
    Label(master,font = myfont, text=pred).grid(row=9,column = 1) 

'''
class DragManager():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            pass

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
'''
    


def open_img(x): 
    # Select the Imagename  from a folder  
    #x = openfilename() 
    
    # opens the image 
    img = Image.open(x) 
      
    # resize the image and apply a high-quality down sampling filter 
    img = img.resize((250, 250), Image.ANTIALIAS) 
  
    # PhotoImage class is used to add image to widgets, icons etc 
    img = ImageTk.PhotoImage(img) 
   
    # create a label 
    panel = Label(master, image = img)
      
    # set the image as img  
    panel.image = img 
    panel.grid(row = 2,column = 1) 


master = Tk(screenName=" Home " )
master.geometry("700x500")
master.title (' Home Page ')
myfont = font.Font(size = 20)
Label(master,font = myfont, text='Find the Image').grid(row=2,column = 1) 
'''
label = Label(canvas, image= image ).grid(row = 4)

dnd = DragManager()
dnd.add_dragable(label)
'''
#path = Entry(master,width="50") 
#path.place(width = 50,height = 10)


#path.grid(row=2, column=1) 



#btn = Button(master,text = " Open the image ",command = open_img()).grid(row = 2,columns = 3)



'''
frame = tk.Frame(master , bd=4, bg="grey")
frame.place(x=10, y=10)
make_draggable(frame)

notes = tk.Text(frame)
notes.pack()
'''



button = Button(master,text = " Predict ",bg = "green" ,fg = "black",width = 20)
button['font'] = myfont
button.grid(row = 6, column = 1)
#message = "Give the image path in this box to get the prediction ! " 
#w = Message( master, font = font.Font(size= 15) ,text= "PREDICT " ).grid(row = 0,column = 0)
#w1 = Message( master, font = font.Font(size= 15) ,text= "PLANT" ).grid(row = 0,column = 1)
w2 = Message( master, font = font.Font(size= 15) ,text= "Species" ).grid(row = 9)

Label(master,font = myfont, text='OUTPUT').grid(row=9) 

button.bind("<Button>",ButtonClicked)



master.mainloop()
