

import sqlite3

peopleValues = (('Ron' , 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

# Gets data from user
#FName = input('Enter your first name: ')
#LName = input('Enter your last name: ')
#Age = int(input('Enter your age: '))
#personData = (FName, LName, Age)

with sqlite3.connect('test_database.db') as conn:
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES (?, ?, ?)", peopleValues) 

# Selecting all First/Last Names for people over 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    # This fetches all rows at one time.
#    for row in c.fetchall():
#        print(row)


    # If we wanted to loop over our results instead of fetching them all at once,
    # we can use this method.
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
