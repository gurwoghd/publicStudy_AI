from tkinter import *
from tkinter import messagebox

def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요")

window = Tk()

TITLE = "Checkbutton 연습"
WIDTH = "800"
HEIGHT = "600"

window.title(TITLE)
window.geometry(WIDTH+'x'+HEIGHT)

chk = IntVar()
cb1 = Checkbutton(window, text="클릭하세요", variable = chk, command = myFunc)
cb1.pack()
window.mainloop()