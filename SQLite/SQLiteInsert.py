import sqlite3
from datetime import datetime, date


def insert_table():
    try:
        photo = convert_photo()
        with sqlite3.connect("Data_test1.db") as con:
            con.execute("INSERT INTO medal(ID, image, Date) VALUES(?,?,?)",
                        (4, photo, date(2023, 12, 12)))
    except Exception as e:
        print("error -> {}".format(e))


def convert_photo():
    filename = "../static/images/Test4.jpg"
    with open(filename, 'rb') as file:
        photo = file.read()

    return photo


if __name__ == '__main__':
    insert_table()
