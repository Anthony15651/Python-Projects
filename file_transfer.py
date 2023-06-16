import datetime
import time
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        # Program Title
        self.master.title("File Transfer")

        # Creates button to select files from source directory and positions it
        self.sourceDir_btn = Button(text = 'Select Source', width = 20, command = self.sourceDir)
        self.sourceDir_btn.grid(row = 0, column = 0, padx = (20, 10), pady = (30, 0))

        # Creates entry for source directory selection and positions it
        self.source_dir = Entry(width = 75)
        self.source_dir.grid(row = 0, column = 1, columnspan = 2, padx = (20, 10), pady = (30, 0))

        # Creates button to select destination of files from directory and positions it
        self.destDir_btn = Button(text = 'Select Destination', width = 20, command = self.destDir)
        self.destDir_btn.grid(row = 1, column = 0, padx = (20, 10), pady = (15, 10))

        # Creates entry for destination directory selection and positions it
        self.destination_dir = Entry(width = 75)
        self.destination_dir.grid(row = 1, column = 1, columnspan = 2, padx = (20, 10), pady = (15, 10))

        # Creates button to transfer files
        self.transfer_btn = Button(text = 'Transfer Files',width = 20, command = self.transferFiles)
        self.transfer_btn.grid(row = 2, column = 1, padx = (200, 0), pady = (0, 15))

        # Creates an Exit button
        self.exit_btn = Button(text = 'Exit', width = 20, command = self.exit_program)
        self.exit_btn.grid(row = 2, column = 2, padx = (10, 40), pady = (0, 15))


    # Function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()

        # Clearing the path to allow for proper input
        self.source_dir.delete(0, END)

        # Inserts user selection into the source_dir Entry widget
        self.source_dir.insert(0, selectSourceDir)


    # Function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()

        # Clearing the path to allow for proper input
        self.destination_dir.delete(0, END)
        
        # Inserts user selection into the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)

    # Function to automatically transfer files that have been changed in the last 24 hours
    def transferFiles(self):

        # Setting timestamp of yesterday (time is in EPOCH / 86400 seconds per day)
        past = (time.time() - 86400)

        # Gets source and destination directory
        source = self.source_dir.get()
        destination = self.destination_dir.get()

        # Gets a list of files in the source directory
        source_files = os.listdir(source)
        for i in source_files:

            # Gets created date (checking for new files)
            c_time = os.path.getctime(source + '/' + i)

            # Gets modification date
            m_time = os.path.getmtime(source + '/' + i)

            # Compares dates to get result
            if (c_time > past) or (m_time > past):
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')
            else:
                print(i + ' has not been recently modified. It will not be transferred.')
                

    # Function to exit program
    def exit_program(self):
        root.destroy()

        


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
