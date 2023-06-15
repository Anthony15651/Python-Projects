

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Importing other StudentTracking Modules
import StudentTrackingMain
import StudentTrackingGUI


#
def CenterWindow(self, W, H):
    
    # Getting user screen width / height
    ScreenWidth = self.master.winfo_screenwidth()
    ScreenHeight = self.master.winfo_screenheight()

    # Calculate X and Y coords to center the app on the user's screen
    X = int((ScreenWidth/2) - (W/2))
    Y = int((ScreenHeight/2) - (H/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(W, H, X, Y))
    return centerGeo

# Catch if the user clicks on the "X" to close the window
def AskQuit(self):
    if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
        # Closes the app if the user does not cancel
        self.master.destroy()
        os._exit(0)

#
def CreateDB(self):
    conn = sqlite3.connect('StudentTracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_Students (\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );')
        conn.commit()
    conn.close()
    FirstRun(self)

#
def FirstRun(self):
    data = ('John','Doe','John Doe','111-111-1111','jdoe@email.com','Sociology 101')
    conn = sqlite3.connect('StudentTracking.db')
    with conn:
        cur = conn.cursor()
        cur, count = CountRecords(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_Students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course)VALUES (?,?,?,?,?,?)""", data)
            conn.commit()
    conn.close()


#
def CountRecords(cur):
    count = ''
    cur.execute("""SELECT COUNT(*) FROM tbl_Students""")
    count = cur.fetchone() [0]
    return cur, count

# Selects items in the listbox
def OnSelect(self, event):
    # Calling the event is the self.lstList widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('StudentTracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email, col_course \
            FROM tbl_Students \
            WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple which is sliced into 4 parts
        # using data[] during the iteration
        for data in varBody:
            self.txtFName.delete(0, END)
            self.txtFName.insert(0, data[0])
            self.txtLName.delete(0, END)
            self.txtLName.insert(0, data[1])
            self.txtPhone.delete(0, END)
            self.txtPhone.insert(0, data[2])
            self.txtEmail.delete(0, END)
            self.txtEmail.insert(0, data[3])
            self.txtCourse.delete(0, END)
            self.txtCourse.insert(0, data[4])

#
def AddToList(self):
    varFName = self.txtFName.get()
    varLName = self.txtLName.get()
    # Normalizing data to keep it consistent within the DB
    varFName = varFName.strip()
    varLName = varLName.strip()
    varFName = varFName.title()
    varLName = varLName.title()
    varFullName = ('{} {}'.format(varFName, varLName))
    print('varFullName: {}'.format(varFullName))
    varPhone = self.txtPhone.get().strip()
    varEmail = self.txtEmail.get().strip()
    varCourse = self.txtCourse.get().strip()
    
    # Ensures email is entered correctly
    if not '@' or not '.' in varEmail:
        print('Incorrect email format!')
        
    # Ensures all fields are filled out
    if (len(varFName) > 0) and (len(varLName) > 0) and (len(varPhone) > 0) and (len(varEmail) > 0) and (len(varCourse) > 0):
        conn = sqlite3.connect('StudentTracking.db')
        with conn:
            cursor = conn.cursor()

            # Checks the DB for existance of 'fullname'. If so,
            # we will alert the user and disregard request
            cursor.execute("""SELECT COUNT (col_fullname) \
                FROM tbl_Students \
                WHERE col_fullname = '{}'""".format(varFullName))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                print('chkName: {}'.format(chkName))
                cursor.execute("""INSERT INTO tbl_Students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",(varFName,varLName,varFullName,varPhone,varEmail,varCourse))
                self.lstList.insert(END, varFullName)
                OnClear(self)
            else:
                messagebox.showerror('Name Error', "'{}' already exists in the database! Please choose a different name.".format(varFullName))
                OnClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('Missing Text Error','Please ensure that there is data in all five fields.')

#
def OnDelete(self):
    varSelect = self.lstList.get(self.lstList.curselection()) # Listbox's selected value
    conn = sqlite3.connect('StudentTracking.db')
    with conn:
        cur = conn.cursor()

        # Checks count to ensure that this is not the last record
        # in the db (can't delete the last record or we get an error)
        cur.execute("""SELECT COUNT (*) FROM tbl_Students""")
        count = cur.fetchone() [0]
        if count > 1:
            confirm = messagebox.askokcancel('Delete Confirmation', 'All information associated with, ({}) \n will be permenantly deleted from the database. \n\nProceed with the deletion request?'.format(varSelect))
            if confirm:
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_Students \
                        WHERE col_fullname = '{}'""".format(varSelect))
                OnDeleted(self) # Call the function to clear all textboxes and the selected index of listbox
                conn.commit()
        else:
            confirm = messagebox.showerror('Last Record Error', '({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).'.format(varSelect, varSelect))
    conn.close()

# Deletes the fields
def OnDeleted(self):
    self.txtFName.delete(0, END)
    self.txtLName.delete(0, END)
    self.txtPhone.delete(0, END)
    self.txtEmail.delete(0, END)
    self.txtCourse.delete(0, END)
    try:
        index = self.lstList.curselection()[0]
        self.lstList.delete(index)
    except IndexError:
        pass

#
def OnClear(self):
    self.txtFName.delete(0, END)
    self.txtLName.delete(0, END)
    self.txtPhone.delete(0, END)
    self.txtEmail.delete(0, END)
    self.txtCourse.delete(0, END)

#
def OnRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList.delete(0, END)
    conn = sqlite3.connect('StudentTracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_Students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_Students""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList.insert(0,str(item))
                i += 1
    conn.close()

                
if __name__ == '__main__':
    pass
