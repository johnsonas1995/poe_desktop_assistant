from tkinter import Tk
from app import App

def start():
    try:
        root = Tk()
        App(root)
        root.mainloop()
    except Exception as e:
        print(e)
        

start()