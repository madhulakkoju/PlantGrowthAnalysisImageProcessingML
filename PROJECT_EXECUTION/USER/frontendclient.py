# Importing Tkinter related modules for GUI purposes
from tkinter import filedialog
from tkinter import*
import tkinter.font as font
import tkinter as tk
# importing Socket and select for Networking purposes
import socket, select
from time import gmtime, strftime
from random import randint
# Importing PIL for Image Manipulations
from PIL import Image, ImageTk
# Plant Species Data considered as a Dictionary.
treedict={  "acer campestre" : "Acer campestre, known as the field maple, is a flowering plant species in the family Sapindaceae.It has been widely planted, and is introduced outside its native range in Europe campestre - downy fruit\nleiocarpum (Opiz) Wallr" ,"ulmus rubra" : "Ulmus rubra, the slippery elm, is a species of elm native to eastern North America \nfulva, published by French botanist André Michaux in 1803, is still widely used in dietary-supplement and alternative-medicine information.",
        "quercus montana" : "Quercus montana, the chestnut oak, is a species of oak in the white oak group, Quercus sect. Quercus. It is native to the eastern United States, where it is one of the most important ridgetop\n trees from southern Maine southwest to central Mississippi, with an outlying northwestern population in southern Michigan. \nIt is also sometimes called rock oak because of its presence in montane and other rocky habitats."
        ,"maclura pomifera":"Maclura pomifera, commonly known as the Osage orange, hedge, or hedge apple tree.This is a small deciduous tree or large shrub, typically growing to 8 to 15 metres (30–50 ft) tall. "
        ,"catalpa speciosa" :"Catalpa speciosa, commonly known as the northern catalpa,\n hardy catalpa, western catalpa, cigar tree, catawba-tree, or bois chavanon, is a species of Catalpa native to the midwestern United States."
        ,"asimina triloba" :"Asimina triloba, the papaw, pawpaw, paw paw, or paw-paw, among many regional names, is a small deciduous tree native to the eastern United States and Canada, producing a large, yellowish-green to brown fruit."}
# This method returns the plant species data from treedict.
def gets(x,rows):
    x = x[2:].split(' ')
    name =  x[0].lower()+" " + x[1].lower()
    return treedict[name]
# openfilename() method creates a Dialog box and returns the
# path of the item selected by the user.
def openfilename(): 
    filename = filedialog.askopenfilename(title ="Input Image")
    return filename
# Method used to display the user selected Image
def open_img(x): 
    img = Image.open(x) 
    # resize the image and apply a high-quality down sampling filter 
    img = img.resize((250, 250), Image.ANTIALIAS) 
    # PhotoImage class is used to add image to widgets, icons etc 
    img = ImageTk.PhotoImage(img) 
    # create a label 
    panel = Label(master, image = img)
    # set the image as img  
    panel.image = img 
    panel.grid(row = 5,column = 1)

#Defining an Event Button Clicked to guide the execution through the necessary path
def ButtonClicked(event):
    #  Dialog Box Opened 
    imagepath = openfilename()
    #Taking the image path for the path obtained from the dialogbox
    open_img(imagepath)
    myfile = open(imagepath, 'rb')
    # Image Retrieved from the path given in Dialog box 
    bytes = myfile.read()
    size = len(bytes)
    # Image read as a series of bytes 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = 6666
    server_address = (HOST, PORT)
    # Issuing a connect request to the Server with address : server_address 
    sock.connect(server_address)
    # Connection Successful
    # Sending Image data as Byte Stream 
    sock.sendall(bytes)
    # image sent to server
    # ---- SERVER PROCESS EXECUTES
    # Receiving the data from the server 
    answer = sock.recv(4096)
    # Data received from the server in the form of byte String
    print (answer, "  is received ")
    # Closing the Connection  
    # data recieved from server
    sock.close()
    # Successfully Terminated the Server Connection 
    # print(imagepath)
    global myfont
    # Creating a textbox for output
    output = Text(master=master,font=myfont)
    output. grid(row=12,column = 1,columnspan = 5,rowspan = 5)
    output.insert(tk.END, str(answer)+"\n\n" +gets(str(answer),13) )
    # insering the Outputdata to the text box
    return

# Client Execution Starts
print("\n\nCLIENT LOG\n\n")

try:
    # Creating a GUI window
    master = Tk(screenName=" Home ")
    master.configure(bg = "white")
    #width, height = master.winfo_screenwidth(), master.winfo_screenheight()
    #Defining size attributes to the GUI window
    master.geometry("900x700")
    master.title (' Home Page ')
    myfont = font.Font(size = 15)
    # Adding some related info on the Window
    Label(master, text='PLANT GROWTH ANALYSIS ',bg = "white",font = font.Font(weight="bold",size = 20) ).grid(row=1,columnspan = 10)
    Label(master,font = myfont, text='An application where you can find a Plant species and the plant-leaf Growth Phase ',bg = "white").grid(row=3 ,columnspan = 10 ) 
    Label(master,font = myfont, text='                         Using an Image                      ',bg = "white").grid(row=4 ,columnspan = 10 ) 
    Label(master,font = myfont, text='                                                                    ',bg = "white").grid(row=5 ,columnspan = 10 ) 
    
    Label(master,font = myfont, text='OUTPUT :                ',bg = "white").grid(row=12)
    Label(master,font = myfont, text='                                                                    ',bg = "white").grid(row=11 ,columnspan = 10 ) 
    # Adding a button for Initiating User Execution process.
    button = Button(master,text = " SelectImage ",bg = "green" ,fg = "black",width = 15)
    button['font'] = myfont
    button.grid(row = 7,column = 1)
    button.bind("<Button>",ButtonClicked)
    # Button Clicked Event is used to do the needed execution
    master.mainloop()
finally :
    pass






