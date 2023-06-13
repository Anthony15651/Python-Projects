

import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png' \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

def createTable(): # Creates a new table with two fields (Primary Int / String)
    conn = sqlite3.connect('Assignment.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_name( \
        personID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_1 STRING)')
    conn.commit()
    conn.close()

def getTxtFiles(): # Iterates through files to find ".txt" files and add them to DB
    conn = sqlite3.connect('Assignment.db')
    cur = conn.cursor()
    for file in fileList:
        if file.endswith('.txt'):
            cur.execute('INSERT INTO tbl_name (col_1) \
                VALUES (?)', (file,))
            conn.commit()
        else:
            continue
    conn.close()

def printFiles(): # Legibly prints qualifying text files for the user
    conn = sqlite3.connect('Assignment.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_name WHERE col_1 LIKE '%.txt'")
    txtFiles = cur.fetchall()
    for i in txtFiles:
        msg = 'Here is your text file: {}'.format(i[1])
        print(msg)
    conn.close()
    



if __name__ == '__main__':
    createTable()
    getTxtFiles()
    printFiles()
