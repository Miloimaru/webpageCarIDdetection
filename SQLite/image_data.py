import sqlite3


def create_data():
    try:
        with sqlite3.connect("Data_test1.db") as con:
            sql_cmd = """
            create table medal(
                ID integer primary key,
                image blob,
                car_ID integer,
                Province text,
                Date text
            )
            """
            con.execute(sql_cmd)
    except Exception as e:
        print("error -> {}".format(e))


if __name__ == '__main__':
    create_data()
