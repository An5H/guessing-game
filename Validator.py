from tkinter import *
getStr = StringVar()
def strSplit():
    strg = getStr.get()
    print(strg)
    splitInput =  strg.split(' ')
    print(splitInput)
    checkStats()

#def checkStats():
    #finding elements of one list in another comes here

def takeInputs():
    ro = Tk()
    Top = Frame(ro, bd=2,  relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(ro, height=200)
    Form.pack(side=TOP, pady=20)
    takeInput = Entry(Form, textvariable=getStr, font=('Helvetica 16 bold italic', 15), width = 50)
    print(getStr.get())
    takeInput.grid(row=0, column = 0)
    lbl_title = Label(Top, text = "Enter your choices here", font=('Helvetica 16 bold italic', 15), fg = "white", bg = "#263D42")
    lbl_title.pack(fill=X)
    btn_Submit = Button(Form, text="Submit", width=20, font=('Helvetica 16 bold italic', 15), fg = "white", bg = "#263D42", command = strSplit)
    btn_Submit.grid(pady=25, row=3 )
    ro.mainloop()

    
    