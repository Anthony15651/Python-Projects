

import os
import time

def getDir():
    path = 'C:\\Users\\antho\\OneDrive\\Documents\\GitHub\\Tech-Academy-Projects\\Python-Projects' # Setting my "path" variable (any path can be used)
    dirList = os.listdir(path) # Creating a list of files from the path above 
    for i in dirList:
        """ This iterates through all files in dirList
        and determines their file type. """
        fileName, fileExtension = os.path.splitext(i)
        if fileExtension == '.txt': # If file type is ".txt", get the absolute path and time it was modified
            fullFile = fileName + fileExtension
            absolutePath = os.path.join(path,fullFile)
            lastModified = os.path.getmtime(absolutePath)
            localTime = time.ctime(lastModified)
            convertedTime = str(localTime)
            print('The absolute path is: ' + absolutePath)
            print('The file was last modified: ' + convertedTime)
        else: # If file is not ".txt", disregard
            continue












if __name__ == "__main__":
    getDir()
    
    
