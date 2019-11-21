import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

i = 1
passing_imgnames = []
passing_imgrealnames = []
checkNames = []

li_urls = ['image_1.png', 'image_2.png', 'image_3.png', 'image_4.png',
           'image.gif']
li_names = ['tree', 'glasses', 'flower', 'masked man', 'earth']
reelList = [['Apple', 'Umbrella', 'Water Bottle'], ['Mango', 'Television', 'Chair'],

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ['Pencil', 'Pizza', 'Wire'], ['Cup', 'Window', 'Peach'], ['Strawberry', 'Ball', 'Pillow']]

r = tk.Tk()
r.title('KIDS LEARNING GAME!')
tk.Label(r, 
		 text="Welcome to the kids learning game.",
		 fg = "white",
		 bg = "#263D42",
		 font = "Helvetica 16 bold italic").pack()

canvas = tk.Canvas(r, height = 700, width = 700, bg = "#263D42" )
canvas.pack(expand = 'YES', fill = BOTH)
def takeInput():
    import Validator as v
    v.takeInputs()
    
def closeApp():
    d=messagebox.askquestion("Confirm","Are you sure?") 
    if(d == 'yes'):
        r.destroy()

def presentList(flag, getStr = ''):
    if(flag == 0):
        strg = 'Tree, Ball, glasses, Flower, Mango, Masked-man'
        canvas.create_text(1200,200,fill="White",font="Helvetica 14 bold italic", text= strg)
    else:    
            canvas.create_text(1200,230,fill="White",font="Helvetica 14 bold italic", text= getStr)

def insertInitialImages():
    startButton.destroy()
    quitButton.destroy()
    strHead = 'Make your choice here!'
    canvas.create_text(1200,150,fill="White",font="Helvetica 14 bold italic", text= strHead)
    presentList(0)
    
    startFunc()
    img = Image.open(li_urls[0])
    img = img.resize((350, 250), Image.ANTIALIAS)
    canvas.image1 = ImageTk.PhotoImage(img)
    canvas.create_image(300, 230, image = canvas.image1)
    
    img1 = Image.open(li_urls[1])
    img1 = img1.resize((350, 250), Image.ANTIALIAS)
    canvas.image2 = ImageTk.PhotoImage(img1)
    canvas.create_image(700, 230, image = canvas.image2)
    
    img3 = Image.open(li_urls[2])
    img3 = img3.resize((350, 250), Image.ANTIALIAS)
    canvas.image4 = ImageTk.PhotoImage(img3)
    canvas.create_image(300, 530, image = canvas.image4)
    
    img4 = Image.open(li_urls[3])
    img4 = img4.resize((350, 250), Image.ANTIALIAS)
    canvas.image5 = ImageTk.PhotoImage(img4)
    canvas.create_image(700, 530, image = canvas.image5)
    
def insertNewImages(img_names):
    img = Image.open(img_names[0])
    img = img.resize((350, 250), Image.ANTIALIAS)
    canvas.image1 = ImageTk.PhotoImage(img)
    canvas.create_image(300, 230, image = canvas.image1)
    
    img1 = Image.open(img_names[1])
    img1 = img1.resize((350, 250), Image.ANTIALIAS)
    canvas.image2 = ImageTk.PhotoImage(img1)
    canvas.create_image(700, 230, image = canvas.image2)
    
    img3 = Image.open(img_names[2])
    img3 = img3.resize((350, 250), Image.ANTIALIAS)
    canvas.image4 = ImageTk.PhotoImage(img3)
    canvas.create_image(300, 530, image = canvas.image4)
    
    img4 = Image.open(img_names[3])
    img4 = img4.resize((350, 250), Image.ANTIALIAS)
    canvas.image5 = ImageTk.PhotoImage(img4)
    canvas.create_image(700, 530, image = canvas.image5)
    
    while len(passing_imgnames):
        passing_imgnames.pop()
    
def itemShuffler(realList):
    strg = ''
    r1 = random.randint(0, 4)
    li = realList + reelList[r1]
    shuffledList = random.sample(li, len(li))
    for i in shuffledList:
       strg = strg + i.join(' ,')
    presentList(1, strg)
    while len(passing_imgrealnames) > 0:
        passing_imgrealnames.pop()
    
def displayListOfNames(takeNames):
    for i in takeNames:
        if takeNames.index(i) > 4:
            continue
        else:   
            checkNames.append(takeNames.index(i))
    for i in checkNames:
        if i > 4:
            continue
        else:
            passing_imgrealnames.append(li_names[i])
    while len(checkNames) > 0:
        checkNames.pop()
    itemShuffler(passing_imgrealnames)
    
def funcRandomSelector():
    for i in range(4):
        passing_imgnames.append(str(random.choice(li_urls)))
    displayListOfNames(passing_imgnames)
    insertNewImages(passing_imgnames) 
    
def startFunc():
    quitButton1 = tk.Button(r, text = "QUIT", padx= 8, pady = 10, fg = 'white', bg = '#263D42', command = closeApp)                          
    quitButton1.place(relx = 0.48, x = -3.5, y = 32.5, rely = 0.88)
    
    refreshButton = tk.Button(r, text = "REFRESH", padx= 8, pady = 10, fg = 'white', bg = '#263D42', command = funcRandomSelector)                          
    refreshButton.place(relx = 0.47, x = -3.5, y = 32.5, rely = 0.02)
    
    playButton = tk.Button(r, text = "PLAY", padx= 8, pady = 10, fg = 'white', bg = '#263D42', command = takeInput)                          
    playButton.place(relx = 0.765, x = -3.5, y = 32.5, rely = 0.02)

startButton = tk.Button(r, text = "START GAME", padx= 10, pady = 5, fg = 'white', bg = '#263D42', command = insertInitialImages)
startButton.place(relx = 0.45, rely = 0.7)

quitButton = tk.Button(r, text = "QUIT",padx= 10, pady = 5, fg = 'white', bg = '#263D42', command = closeApp) 
quitButton.place(relx = 0.53, rely = 0.7)

r.mainloop()
    
    
