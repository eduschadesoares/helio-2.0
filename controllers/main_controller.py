import sys
sys.path.append('../')
import tkinter
from tkinter import ttk

class Main_controller():
    def __init__(self, app, db):
        self.app = app
        self.db = db


        app.table.bind('<<TreeviewSelect>>', self.printageral)

        app.mainloop()

    def printageral(self, _):
         print(self.app.table.selection())





