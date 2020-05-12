#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
root = Tk()
root.title("Alex Dzul")
root.geometry("300x300")
app = Frame(root)
app.grid()
message = str("Hola Pythonízame")
lbl = Label(app, text = message)
lbl.grid()
root.mainloop()