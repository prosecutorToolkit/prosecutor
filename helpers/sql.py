import sqlite3

def createScanReportTable(sqlFilePath):
    conn = sqlite3.connect(sqlFilePath)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE scan_report
                        (ID INT NOT NULL,
                        NAME TEXT NOT NULL,
                        PATH TEXT NOT NULL,
                        HASH_SHA_256,
                        MATCH TEXT,
                        CUT_TEXT TEXT,
                        TEXT TEXT,
                        METADATA TEXT,
                        WR TEXT)''') # white row
    conn.commit()
    conn.close()

def getHeaderFromSQL(sqlFilePath):
    conn = sqlite3.connect(sqlFilePath)
    cursor = conn.cursor()
    cursor.execute('''SELECT TIME_REPORT, CASEDATA, TARGETFOLDER, MERCLE, FORMATSLIST, SHOWNQUERY, MISSPELLINGS FROM report_data''')
    return cursor.fetchall()

def saveHeaderInTable(sqlFilePath, data):
    conn = sqlite3.connect(sqlFilePath)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE report_data
                        (TIME_REPORT TEXT,
                        CASEDATA TEXT,
                        TARGETFOLDER TEXT,
                        MERCLE TEXT,
                        FORMATSLIST TEXT,
                        SHOWNQUERY TEXT,
                        MISSPELLINGS TEXT)''')
    conn.commit()
    cursor.execute('''INSERT INTO report_data (TIME_REPORT, CASEDATA, TARGETFOLDER, MERCLE, FORMATSLIST, SHOWNQUERY, MISSPELLINGS) VALUES (?, ?, ?, ?, ?, ?, ?)''', data)
    conn.commit()
    conn.close()

def saveIgnoredFilesInDB(sqlFilePath, ignoredFilesList):
    conn = sqlite3.connect(sqlFilePath)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE ignored_files
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        FILE TEXT,
                        EXT TEXT,
                        PATH TEXT)''')
    conn.commit()
    cursor.executemany('''INSERT INTO ignored_files (FILE, EXT, PATH) VALUES (?, ?, ?)''', ignoredFilesList)
    conn.commit()
    conn.close()


def getScanReportData(sqlFilePath):
    conn = sqlite3.connect(sqlFilePath)
    cursor = conn.cursor()
    cursor.execute('''SELECT ID, NAME, PATH, HASH_SHA_256, MATCH, CUT_TEXT, WR, METADATA FROM scan_report''')
    return cursor.fetchall()

def getIgnoredFilesData(sqlFilePath):
    conn = sqlite3.connect(sqlFilePath)
    cursor = conn.cursor()
    cursor.execute('''SELECT ID, FILE, EXT, PATH FROM ignored_files''')
    return cursor.fetchall()

def saveSQL(sqlFilePath, data):
    conn = sqlite3.connect(sqlFilePath)
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO scan_report (ID, NAME, PATH, HASH_SHA_256, MATCH, CUT_TEXT, TEXT, METADATA) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', data)
    conn.commit() # Confirm the changes in the DB
    conn.close() # Close connection with the DB