from tkinter import *

def name_and_surname():
    file_for_saving = open("data.txt","w")
    written = file_for_saving.writelines(str("First Name: %s\nLast Name: %s" % (name_1.get(), surname_2.get())))
    file_for_saving.close()

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

name_1 = Entry(master)
surname_2 = Entry(master)

name_1.grid(row=0, column=1)
surname_2.grid(row=1, column=1)

Button(master, text='Exit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Save',command = name_and_surname).grid(row=3, column=1, sticky=W, pady=4)

mainloop()

