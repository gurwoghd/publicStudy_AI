from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^6")

window = Tk()
TITLE = '윈도 창 연습'
WIDTH = '400'
HEIGHT = '100'

window.title(TITLE)
window.geometry(WIDTH + 'x' + HEIGHT)

photo = PhotoImage(file ="gif/dog.gif")
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

entry = Entry(window, fg='black', bg='yellow', width=30)
entry.pack()

window.mainloop()
