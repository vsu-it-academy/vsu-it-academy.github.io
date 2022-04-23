from tkinter import *
from tkinter import messagebox as mb
 
 
def check():
    answer = mb.askyesno(
        title="Вопрос", 
        message="Введите уровень:")
    if answer:
        s = entry.get()
        entry.delete(0, END)
 
 
root = Tk()
entry = Entry()
entry.pack(pady=0)
Button(text='Передать', command=check).pack()
 
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.mainloop()