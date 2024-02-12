from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Halaman Login")
root.geometry('500x300')

judul = Label(root,
              text='Login',
              font=('Arial',18,'bold')
              )
judul.pack()

username = Label(root,
                 text='username')
username.pack()

input_user = Entry(root,width=20)
input_user.pack()

password = Label(root,
                 text='password')
password.pack()

input_user = Entry(root,width=20,show="#")
input_user.pack() 

def pesan() :
    tkinter.messagebox.showinfo("info","Login berhasil")
    
tombol = Button(root,
                text="Log in",
                width=7,
                command=pesan)
tombol.pack()

root.mainloop()