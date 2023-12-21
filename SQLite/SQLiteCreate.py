import sqlite3


def create_table():
    try:
        with sqlite3.connect("Table") as con:
            sql_cmd = """
            create table medal(
                ID integer primary key,
                name text
            )
            """
            con.execute(sql_cmd)
    except Exception as e:
        print("error -> {}".format(e))


if __name__ == '__main__':
    create_table()
