from tkinter import *

window = Tk()

def ShowResult():
    global heightEntry, weightEntry, resultEntry

    height = float(heightEntry.get())/100
    weight = float(weightEntry.get())
    result = round(weight / height ** 2, 2)
    resultEntry.delete(0, END)
    resultEntry.insert(0, str(result))

height = Label(window, text="키")
weight = Label(window, text="몸무게")
heightEntry = Entry(window, width = 20)
weightEntry = Entry(window, width = 20)
ProgramName = Label(window, text="BMI Chart", font=("견고딕", 30), width = 10)
resultButton = Button(window, text="결과 보기", command = ShowResult)
bmi = Label(window, text="bmi지수")
resultEntry = Entry(window, width = 20)

height.grid(row = 0, column = 0)
weight.grid(row = 1, column = 0)
heightEntry.grid(row = 0, column = 1, sticky = E+S)
weightEntry.grid(row = 1, column = 1, sticky = E+S)
ProgramName.grid(row = 0, column = 2, rowspan = 2, sticky = W + E + N + S)
resultButton.grid(row = 2, column = 1)
bmi.grid(row = 3, column = 0)
resultEntry.grid(row = 3, column = 1, columnspan = 2, sticky = W + E + N + S)

window.mainloop()
