import sqlite3

fileList = ('information.doxc', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

txtFile = []
for file in fileList:
    if file.endswith(".txt"):
        txtFile.append(file)
#print(txtFile)

        
conn = sqlite3.connect("textFiles.db")

with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles \
                   (\
                   ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                   FileName TEXT \
                   )")
    conn.commit()
conn.close()


conn = sqlite3.connect("textFiles.db")

with conn:
    cursor = conn.cursor()
    for file in txtFile:
        cursor.execute("INSERT INTO tbl_textFiles (FileName) VALUES (?)", (file,))
    conn.commit()
conn.close()



conn = sqlite3.connect("textFiles.db")

with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT FileName FROM tbl_textFiles")
    files = cursor.fetchall()
   
    conn.commit()

conn.close()

print(files)




    
