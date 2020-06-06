from tkinter import *
import file1
def clicked():
    lbl.configure(text = " CLICKED"+txt.get())

window = Tk()
window.geometry('500x500')
window.title("Main Page")

label_1 = Label(window,text = "ENter Image Path")
label_1.grid(column = 3,row = 4)

path_t = Entry(root)

label_2 = Label(window,text = "ENter Species")
label_2.grid(column = 3,row = 14)


window.mainloop()
