

from tkinter import *
import tkinter as tk

# Importing other StudentTracking Modules
import StudentTrackingGUI
import StudentTrackingFunc


# Creating subclass from tkinter's main frame class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):

        # Setting window size
        self.master = master
        self.master.minsize(600, 350)
        self.master.maxsize(600, 350)

        # Centering window on launch
        StudentTrackingFunc.CenterWindow(self, 600, 350)
        self.master.title('Student Tracking')
        self.master.configure(bg='#F0F0F0')

        # Window close when user hits "X"
        self.master.protocol('WM_DELETE_WINDOW', lambda: StudentTrackingFunc.AskQuit(self))
        arg = self.master

        # Load in the GUI
        StudentTrackingGUI.LoadGUI(self)

if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
