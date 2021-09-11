from tkinter import *

window = Tk()
WIDTH = '800'
HEIGHT = '600'
window.geometry(WIDTH+'x'+HEIGHT)

def SelectPreviousImage():
    global ImageFolder, imageName, n, label, photo
    if n <= 0:
        n = len(imageName) - 1
    else:
        n = n - 1
    ConfigurePhotoObject(ImageFolder + imageName[n])

def SelectNextImage():
    global ImageFolder, imageName, n, label, photo
    if n >= (len(imageName) - 1):
        n = 0
    else:
        n = n+1
    ConfigurePhotoObject(ImageFolder + imageName[n])

def ConfigurePhotoObject(filepath):
    global photo

    photo.configure(file = filepath)


ImageFolder = "gif/"
imageName = ['cat.gif', 'cat2.gif', 'dog2.gif', 'dog4.gif', 'froyo.gif', 'eclair.gif', 'gingerbread.gif']
n = 0
photo = PhotoImage(file = ImageFolder + imageName[n])
label = Label(window, image = photo)

previousButton = Button(window, text='prev', command = SelectPreviousImage)
nextButton = Button(window, text = 'next', command = SelectNextImage)

previousButton.pack(pady = 5)
nextButton.pack(pady = 5)
label.pack()

window.mainloop()
