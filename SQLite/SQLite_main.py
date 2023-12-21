import sqlite3


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


def readBlobData(Id):
    try:
        sqliteConnection = sqlite3.connect('../SQLite/Data_test1.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from medal where ID = ?"""
        cursor.execute(sql_fetch_blob_query, (Id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0])
            photo = row[1]

            print("Storing employee image and resume on disk \n")
            photoPath = "../static/ReadImageFormSQLite/" + 'Image' + ".jpg"
            writeTofile(photo, photoPath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


if __name__ == '__main__':
    readBlobData(3)
