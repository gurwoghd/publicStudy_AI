from tkinter import *

window = Tk()
TITLE = "Label 위젯 사용해보기"
WIDTH = "700"
HEIGHT = "500"

window.title(TITLE)
window.geometry(WIDTH +'x'+ HEIGHT)


label1 = Label(window, text="Let's get Started!")
label2 = Label(window, text="말하는대로", font=("궁서체", 30), fg="blue")
label3 = Label(window, text = "행복은 지금이다", bg = "magenta", width=20, height=5, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()

