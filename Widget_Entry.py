from tkinter import *

window = Tk()

TITLE = "Label 위젯 사용해보기"
WIDTH = "700"
HEIGHT = "500"

window.title(TITLE)
window.geometry(WIDTH +'x'+ HEIGHT)


entry = Entry(window, fg='black', bg='yellow', width = 30)
entry.get()
entry.pack()

window.mainloop()