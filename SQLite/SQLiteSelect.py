import sqlite3


def select_table():
    try:
        with sqlite3.connect("Table") as con:
            sql_cmd = """
                select * from medal
            """
            for row in con.execute(sql_cmd):
                print(row)
    except Exception as e:
        print("error -> {}".format(e))


if __name__ == '__main__':
    select_table()
