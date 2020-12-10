from tkinter import *

root = Tk()
root.title(Github sign in)

l1 = Label(root, text="Welcome to the GitHub login application!!")
l1.config(font =("Arial",19)
          
l2 = Label(root, text="username:")
l2.config(font =("Arial",12))
l3 = Label(root, text="password:")
l3.config("Arial",12)
          
username = StringVar()
password = StringVar()
          
e1 = Entry(root, textvariable=username)
e2 = Entry(root, textvariable=password,show="*")
          
def Submit():
    password_show = f("Your password is:{password.get}")
    username_show = f("Your password is:{username.get}")
          
    label_password = (root, text=password_show)
    label_username = (root, text=username_show)
          
           
login_button = Button(root, text="SUBMIT",command=Submit)
           
l1.grid()

l2.grid(row=0, column=0)
e1.grid(row=0, column=1)
           
l3.grid(row=1, column=0)
e2.grid(row=1, column=1)
           
login_button.grid(row=4, column=0)
          
root.mainloop()
