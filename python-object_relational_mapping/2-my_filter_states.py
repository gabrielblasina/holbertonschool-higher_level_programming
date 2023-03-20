#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE "
                "name = '{}' ORDER BY id ASC".format(argv[4]))
    show_rows = cur.fetchall()
    for row in show_rows:
        if argv[4] == row[1]:
            print(row)

    cur.close()
    db.close()
