

from tkinter import *
import tkinter as tk

# Importing other StudentTracking Modules
import StudentTrackingMain
import StudentTrackingFunc

def LoadGUI(self):

    # Labels:
    self.lblFName = tk.Label(self.master, text = 'First Name: ')
    self.lblFName.grid(row = 0, column = 0, padx = (27, 0), pady = (10, 0), sticky = N + W)
    self.lblLName = tk.Label(self.master, text = 'Last Name: ')
    self.lblLName.grid(row = 2, column = 0, padx = (27, 0), pady = (10, 0), sticky = N + W)
    self.lblPhone = tk.Label(self.master, text = 'Phone Number: ')
    self.lblPhone.grid(row = 4, column = 0, padx = (27, 0), pady = (10, 0), sticky = N + W)
    self.lblEmail = tk.Label(self.master, text = 'Email Address: ')
    self.lblEmail.grid(row = 6, column = 0, padx = (27, 0), pady = (10, 0), sticky = N + W)
    self.lblCourse = tk.Label(self.master, text = 'Current Course: ')
    self.lblCourse.grid(row = 8, column = 0, padx = (27, 0), pady = (10, 0), sticky = N + W)
    self.lblStudent = tk.Label(self.master, text = 'Student: ')
    self.lblStudent.grid(row = 0, column = 2, padx = (0, 0), pady = (10, 0), sticky = N + W)

    # Text Boxes
    self.txtFName = tk.Entry(self.master, text = '')
    self.txtFName.grid(row = 1, column = 0, columnspan = 2, padx = (30, 40), pady = (0, 0), sticky = N + E + W)
    self.txtLName = tk.Entry(self.master, text = '')
    self.txtLName.grid(row = 3, column = 0, columnspan = 2, padx = (30, 40), pady = (0, 0), sticky = N + E + W)
    self.txtPhone = tk.Entry(self.master, text = '')
    self.txtPhone.grid(row = 5, column = 0, columnspan = 2, padx = (30, 40), pady = (0, 0), sticky = N + E + W)
    self.txtEmail = tk.Entry(self.master, text = '')
    self.txtEmail.grid(row = 7, column = 0, columnspan = 2, padx = (30, 40), pady = (0, 0), sticky = N + E + W)
    self.txtCourse = tk.Entry(self.master, text = '')
    self.txtCourse.grid(row = 9, column = 0, columnspan = 2, padx = (30, 40), pady = (0, 0), sticky = N + E + W)

    # Scrollbar / Listbox
    self.scrollbar = Scrollbar(self.master, orient = VERTICAL)
    self.lstList = Listbox(self.master, exportselection = 0, yscrollcommand = self.scrollbar.set)
    self.lstList.bind('<<ListboxSelect>>', lambda event: StudentTrackingFunc.OnSelect(self, event))
    self.scrollbar.config(command = self.lstList.yview)
    self.scrollbar.grid(row = 1, column = 5, rowspan = 9, padx = (10, 0), pady = (0, 0), sticky = N + E + S)
    self.lstList.grid(row = 1, column = 2, rowspan = 9, columnspan = 3, padx = (0, 0), pady = (0, 0), sticky = N + E + S + W)
    
    # Buttons
    self.btnSubmit = tk.Button(self.master, width = 12, height = 2, text = 'Submit', command = lambda: StudentTrackingFunc.AddToList(self))
    self.btnSubmit.grid(row = 10, column = 1, padx = (0, 0), pady = (20, 10), sticky = W)
    self.btnDelete = tk.Button(self.master, width = 12, height = 2, text = 'Delete', command = lambda: StudentTrackingFunc.OnDelete(self))
    self.btnDelete.grid(row = 10, column = 3, padx = (0, 0), pady = (20, 10), sticky = W)

    StudentTrackingFunc.CreateDB(self)
    StudentTrackingFunc.OnRefresh(self)

if __name__ == '__main__':
    pass
