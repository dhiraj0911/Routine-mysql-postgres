import psycopg2



def createtable():
    conn=psycopg2.connect("dbname='My_Routine' user='postgres' password='2110' port='5432' host='localhost'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS My_Routine(Date TEXT, Time TEXT, Study TEXT, Hour TEXT, Note TEXT, Log TEXT,id SERIAL PRIMARY KEY)")
    conn.commit()
    conn.close()

def insert(Date, Time, Study, Hour, Note, Log):
    conn=psycopg2.connect("dbname='My_Routine' user='postgres' password='2110' port='5432' host='localhost'")
    cur=conn.cursor()
    cur.execute("INSERT INTO My_Routine VALUES(%s,%s,%s,%s,%s,%s)",(Date, Time, Study, Hour, Note, Log))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='My_Routine' user='postgres' password='2110' port='5432' host='localhost'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM My_Routine")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(Time):
    conn=psycopg2.connect("dbname='My_Routine' user='postgres' password='2110' port='5432' host='localhost'")
    cur=conn.cursor()
    cur.execute("DELETE From My_Routine WHERE Time=%s",(Time,))
    conn.commit()
    conn.close()

def search(Date='', Time='', Study='', Hour='', Note='', Log=''):
    conn=psycopg2.connect("dbname='My_Routine' user='postgres' password='2110' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM My_Routine WHERE Date=%s OR Time=%s OR Study=%s OR Hour=%s OR Note=%s OR Log=%s",(Date, Time, Study, Hour, Note, Log))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

createtable()