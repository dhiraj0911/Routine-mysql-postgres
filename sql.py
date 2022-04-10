import mysql.connector as connector

def connect():
    con=connector.connect(host="localhost",
    user="root",
    password="4664",
    database="start")
    cur = con.cursor()
    cur.execute('create table if not exists neo(date varchar(20), time varchar(20), study varchar(20), hour int(10),note varchar(20)')

def insert(date,time,study,hour,note):
    con=connector.connect(host="localhost",
    user="root",
    password="4664",
    database="start")
    query="insert into neo(date,time,study,hour,note)values('{}','{}','{}',{},'{}')".format(date,time,study,hour,note)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    con.close()

def view():
    con=connector.connect(host="localhost",
    user="root",
    password="4664",
    database="start")
    cur = con.cursor()
    cur.execute("SELECT * FROM neo")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete(time):
    con=connector.connect(host="localhost",
    user="root",
    password="4664",
    database="start")
    cur = con.cursor()
    cur.execute("DELETE FROM neo WHERE time=%s",(time))
    con.commit()
    con.close()

def search(date='' , time='' , study='' , hour='' , note=''):
    con=connector.connect(host="localhost",
    user="root",
    password="4664",
    database="start")
    cur = con.cursor()
    cur.execute("SELECT * FROM Routine WHERE Date=%s OR Time=%s OR Study=%s OR Hour=%s OR Note=%s" , (date , time , study , hour , note))
    rows = cur.fetchone()
    con.commit()
    con.close()
    return rows