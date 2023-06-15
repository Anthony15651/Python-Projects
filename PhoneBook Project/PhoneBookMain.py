

from tkinter import *
import tkinter as tk


# Importing the other PhoneBook
# modules so that they may be called
import PhoneBookGUI
import PhoneBookFunc


# Frame is the Tkinter frame class that
# our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):

        # Define our master frame configuration
        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)

        # This CenterWindow method will center
        # the app on the user's screen
        PhoneBookFunc.CenterWindow(self, 500, 300)
        self.master.title('My Tkinter Phone Book')
        self.master.configure(bg='#F0F0F0')

        # This protocol method is a tkinter built-in method to catch
        # if the user clicks the upper corner "X" on Windows OS
        self.master.protocol('WM_DELETE_WINDOW', lambda: PhoneBookFunc.AskQuit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # keeping my code compartmentalized and clutter free.
        PhoneBookGUI.LoadGUI(self)
        
if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
