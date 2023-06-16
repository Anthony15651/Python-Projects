

import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title('Web Page Generator')

        # Buttons
        self.btn = Button(self.master, text='Default HTML Page', width = 30, height = 2, command = self.defaultHTML)
        self.btn.grid(row = 2, column = 1, padx = (10, 10), pady = (10, 10))
        self.btn_Custom = Button(self.master, text = 'Submit Custom Text', width = 30, height = 2, command = self.customHTML)
        self.btn_Custom.grid(row = 2, column = 2, padx = (10, 10), pady = (10, 10))

        # Label
        self.lbl_Input = Label(self.master, text = 'Enter custom text or click the "Default HTML Page" button:')
        self.lbl_Input.grid(row = 0, column = 0, padx = (10, 10), pady = (10, 10))

        # Entry Box
        self.entry_Box = Entry(self.master)
        self.entry_Box.grid(row = 1, column = 0, columnspan = 3, padx = (10, 10), pady = (0, 0), sticky = E + W)

    # Function for default HTML page
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Function for custom HTML page
    def customHTML(self):
        htmlText = self.entry_Box.get() # Grabbing text from Entry box
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1></body></html>" # Building html
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html") # Opens window


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
