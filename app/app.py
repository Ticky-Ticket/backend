from utils.db import Database
import pprint


if __name__=="__main__" :
    db = Database()
    db.execute("DROP TABLE IF EXISTS tickets")
    db.execute("DROP TABLE IF EXISTS roles")
    db.execute("DROP TABLE IF EXISTS history")
    db.execute('''CREATE TABLE tickets (
        id SERIAL,
        client INTEGER NOT NULL,
        asignee INTEGER NOT NULL ) ''')
    db.execute('''INSERT INTO tickets (client, asignee)
        VALUES (%s, %s)''', 1, 2)
    db.execute('''INSERT INTO tickets (client, asignee)
        VALUES (%s, %s)''', 2, 3)
    db.execute('''INSERT INTO tickets (client, asignee)
        VALUES (%s, %s)''', 1, 3)
    res = db.fetch("SELECT * from tickets")
    if res : 
        for r in res : 
            pprint.pprint(r)
    else : 
        print("No result returned") 
