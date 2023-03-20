#!/usr/bin/python3
"""
script that lists all cities from the
database hbtn_0e_4_usa
"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM states, cities "
                "WHERE cities.name IS NOT NULL "
                "AND states.id = cities.state_id "
                "ORDER BY cities.id ASC")
    show_rows = cur.fetchall()
    for row in show_rows:
        print(row)

    cur.close()
    db.close()
