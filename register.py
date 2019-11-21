from tkinter import *
import sqlite3

root = Tk()
root.title("Register")
width = 400
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythonProject.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `pythongame` (username TEXT, password TEXT, phoneNumber INTEGER, email TEXT)") 
    conn.commit()      
    
def Register():
    Database()
    dataInsert = []
    dataInsert.append(USERNAME.get())
    dataInsert.append(PASSWORD.get())
    dataInsert.append(PHONENUMBER.get())
    dataInsert.append(EMAIL.get())
    print(dataInsert)
    if USERNAME.get() == "" or PASSWORD.get() == "" or EMAIL.get() == "" or PHONENUMBER.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
        lbl_text.grid(row = 6, columnspan = 2)
    else:
        cursor.execute("INSERT INTO `pythongame` VALUES(?, ?, ?, ?)", dataInsert)
        conn.commit()
        USERNAME.set("")
        PASSWORD.set("")
        EMAIL.set("")
        PHONENUMBER.set("")
        HomeWindow()
    

def HomeWindow():
    cursor.close()
    conn.close()
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Registered!\n Now you can log in", font=('Helvetica 14 bold italic', 20), fg = "white", bg = "#263D42").pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

def Back():
    Home.destroy()
    root.destroy
    import login as lg
    
#==============================VARIABLES======================================
USERNAME = StringVar()
EMAIL = StringVar()
PHONENUMBER = IntVar()
PASSWORD = StringVar()

#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text = "Register", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Email:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_password = Label(Form, text = "Phone number:", font=('arial', 14), bd=15)
lbl_password.grid(row=2, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=3, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
username = Entry(Form, textvariable=EMAIL, font=(14))
username.grid(row=1, column=1)
username = Entry(Form, textvariable=PHONENUMBER, font=(14))
username.grid(row=2, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=3, column=1)

#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Register", width=45, command=Register)
btn_login.grid(pady=25, row=5, columnspan=2)
btn_login.bind('<Return>', Register)

root.resizable(0, 0)
root.mainloop()





