from tkinter import * 









Tk()
import tkinter as Tk

root = Tk()
root.title("Canvas")
root.geometry("800x400")

c = Canvas(root,height=500, width=800,
           bg="#860A35")

kepala = c.create_oval("100,50,600,450, fill='#39A7FF'")
                       
pipi = c.create_oval(200, 120, 600, 450,
                     fill='white')
c.pack 
root.mainloop()