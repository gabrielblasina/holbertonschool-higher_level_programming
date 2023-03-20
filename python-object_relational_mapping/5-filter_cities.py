#!/usr/bin/python3
"""
script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name "
                "FROM states, cities "
                "WHERE cities.name IS NOT NULL "
                "AND states.id = cities.state_id "
                "AND states.name = '%s' "
                "ORDER BY cities.id ASC" % argv[4])
    show_rows = cur.fetchall()
    string = ', '.join([row[0] for row in show_rows])
    print(string)

    cur.close()
    db.close()
