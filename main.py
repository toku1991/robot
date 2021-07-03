from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import credentials
import cv2

root = Tk()

login = Frame(root, height=600, width=300, )
main = Frame(root, height=600, width=300, bg="BLACK")
lmain = Label(main)
lmain.grid(row=0, column=0)

cap = cv2.VideoCapture('http://192.168.137.100:8080')

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def up(event):
    print('forward')

def down(event):
    print('backwards')

def left(event):
    print('left')

def right(event):
    print('right')

def mouseclick(event):
    print('fire')

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def submit():
    cur = credentials.mydb.cursor()
    cur.execute("select * from login where username=%s and password = %s",
                (username_entry.get(), password_entry.get()))
    row = cur.fetchone()
    if row == None:
        print('row')
    else:
        print('hello')
        login.destroy()
        root.bind("<Up>", up)
        root.bind("<Down>", down)
        root.bind("<Left>", left)
        root.bind("<Right>", right)
        root.bind("<Button-1>", mouseclick)


        main.pack();

# create username label and entry
username_label = Label(login, text='username', font=('bold', 10))
username_entry = Entry(login)

# create password label and entry
password_label = Label(login, text='password', font=('bold', 10))
password_entry = Entry(login, show="*")

#create button
login_button = Button(login, text='login', command=submit)

username_label.pack()
username_entry.pack()

password_label.pack()
password_entry.pack()

login_button.pack()

login.pack()

show_frame()
root.mainloop()