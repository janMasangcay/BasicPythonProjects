import sqlite3

def createDB():
    connDb = sqlite3.connect('test.db')
    with connDb:
        connDb.cursor().execute("CREATE TABLE IF NOT EXISTS persons( \
            ID  INTEGER PRIMARY KEY AUTOINCREMENT, \
            fname TEXT, \
            lname TEXT, \
            email TEXT \
        )")
        connDb.commit()
    connDb.close()

def insertIntoDB():
    connDb = sqlite3.connect('test.db')
    with connDb:
        connDb.cursor().execute("INSERT INTO persons(fname, lname, email) VALUES (?,?,?)", \
            ('Jakul', 'Ero', 'jakulero@gmail.com'))
        connDb.cursor().execute("INSERT INTO persons(fname, lname, email) VALUES (?,?,?)", \
            ('Jill', 'Ero', 'jillero@gmail.com'))
        connDb.cursor().execute("INSERT INTO persons(fname, lname, email) VALUES (?,?,?)", \
            ('Kantot', 'Ero', 'kantotero@gmail.com'))
        connDb.commit()
    connDb.close()

def selectFromDB():
    connDb = sqlite3.connect('test.db')
    with connDb:
        cur = connDb.cursor()
        cur.execute('SELECT fname, lname, email FROM persons WHERE fname = "Jakul"')
        selectedPerson = cur.fetchall()    
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(selectedPerson[0][0], selectedPerson[0][1], selectedPerson[0][2])
        print(msg)


if __name__ == '__main__':
    createDB()
    insertIntoDB()
    selectFromDB()