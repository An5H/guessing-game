from tkinter import *
from PIL import Image, ImageTk
r = Tk()
r.title("Welcome to KidsGame")
r.geometry('400x400')
Label(r, 
		 text="Welcome to the kids learning game.",
		 fg = "white",
		 bg = "#263D42",
		 font = "Helvetica 16 bold italic").pack()
canvas = Canvas(r, height = 700, width = 700, bg = "#263D42" )
canvas.pack(expand = 'YES', fill = BOTH)

def App():
    img = Image.open('loginimg.png')
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(570, 100, image = canvas.image, anchor = 'nw')
        
    Register = Button(r, text = "Register", padx = 8, pady = 10, fg = 'white', bg = '#263D42', command = invokeRegister) 
    Register.place(relx = 0.53, rely = 0.9, anchor = W)

    AlreadyAUser = Button(r, text = "Already a user ?", padx = 8, pady = 10, fg = 'white', bg = '#263D42', command = invokeLogin)                        
    AlreadyAUser.place(relx = 0.5, rely = 0.9, anchor = E)
    
def invokeRegister():
    import register as rg
    
def invokeLogin():
    import login as lg
App()
r.mainloop()