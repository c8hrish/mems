import sqlite3
def create_db():
    con=sqlite3.connect(database="mems.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS members(memid INTEGER PRIMARY KEY AUTOINCREMENT, fname text, mname text, lname text, addr1 text, addr2 text, place text, tehs text, distr text, state text, country text, pinco text, contaNum text, altNum text, whatNum text, dob text, uid text, eid text, mothermname text, descr text, applid text, appldt text, check1 INTEGER, check2 INTEGER)")
    con.commit()

create_db()