from tkinter import *

window = Tk()
TITLE = "Label 위젯 사용해보기"
WIDTH = "700"
HEIGHT = "500"

button = Button(window, text="파이썬 종료", fg="red", command=quit)

window.title(TITLE)
window.geometry(WIDTH +'x'+ HEIGHT)

button.pack()

window.mainloop()