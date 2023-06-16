

import sqlite3

pplValues = (('Jean-Baptiste Zorg','Human',122), ('Korben Dallas','Meat Popsicle',100), ("Ak'not", 'Mangalore', -5))

with sqlite3.connect(':memory:') as conn:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Roster (Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES (?, ?, ?)", pplValues)
#    c.execute("SELECT * FROM Roster")
#    for row in c.fetchall():
#        print(row)
    c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    c.execute("SELECT * FROM Roster WHERE Species = 'Human'")
    for row in c.fetchall():
        print(row)

    
