import sqlite3

def createTable(sqlFilePath):
    try:
        conn = sqlite3.connect(sqlFilePath)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE prosecutor_report
                          (ID INT NOT NULL,
                           NAME TEXT NOT NULL,
                           PATH TEXT NOT NULL,
                           HASH_SHA_256,
                           MATCH TEXT,
                           TEXT TEXT,
                           METADATA TEXT)''')
        conn.commit() # Confirm the changes in the DB
        conn.close() # Close connection with the DB
        return True

    except:
        return False


def saveSQL(sqlFilePath, data):
    try:
        conn = sqlite3.connect(sqlFilePath)
        cursor = conn.cursor()
        cursor.executemany('''INSERT INTO prosecutor_report (ID, NAME, PATH, HASH_SHA_256, MATCH, TEXT, METADATA) VALUES (?, ?, ?, ?, ?, ?, ?)''', data)
        conn.commit() # Confirm the changes in the DB
        conn.close() # Close connection with the DB
        return True

    except:
        return False