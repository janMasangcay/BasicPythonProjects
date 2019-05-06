import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

def sortFiles(listOfFiles):
    txtList = []
    for item in listOfFiles:
        if item.endswith('.txt'):
            txtList.append(item)
    return txtList

def createDB():
    connDB = sqlite3.connect('test.db')
    with connDB:
        connDB.cursor().execute("CREATE TABLE IF NOT EXISTS FileWithTxt( \
            ID  INTEGER PRIMARY KEY AUTOINCREMENT, \
            filename TEXT \
        )")
        connDB.commit()
    connDB.close()

def insertIntoDB(sortedFiles):
    for item in sortedFiles:
        #print(item)
        connDb = sqlite3.connect('test.db')
        with connDb:
            connDb.cursor().execute("INSERT INTO FileWithTxt(filename) VALUES (?)", \
                (item,))
        connDb.commit()
        connDb.close()
    
def selectIntoDB():
    connDb = sqlite3.connect('test.db')
    with connDb:
        cur = connDb.cursor()
        cur.execute('SELECT * FROM FileWithTxt',)
        selectedFile = cur.fetchall()    
        for item in selectedFile:
            print("File Name: {}".format(item[1]))
        


if __name__ == '__main__':
    createDB()
    insertIntoDB(sortFiles(fileList))
    selectIntoDB()