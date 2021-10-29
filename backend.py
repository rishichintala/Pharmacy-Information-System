import sqlite3
#backend

def medicineData():
    conn=sqlite3.connect("management.db")
    cur.execute("CREATE TABLE IF NOT EXISTS management(id INTEGER PRIMARY KEY,MedId text,MedName text,DoM text,DoE text,Prices text)")
    conn.commit()
    conn.close()

def addMedRec(MedId , MedName , DoM , DoE , Prices ):
    conn=sqlite3.connect("management.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO management VALUES (NULL,?,?,?,?,?)", (MedId , MedName , DoM , DoE , Prices ))
    conn.commit()
    conn.close()

def viewData():
    conn=sqlite3.connect("management.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM management")
    row=cur.fetchall()
    conn.close()
    return row

def deleteRec(id):
    conn=sqlite3.connect("management.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM management WHERE id=?",(id, ))
    conn.commit()
    conn.close()

def searchData(MedId="" , MedName="" , DoM="" , DoE="" , Prices="" ):
    conn=sqlite3.connect("management.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM management WHERE MedId=? OR MedName=? OR DoM=? OR DoE=? OR Prices=? ",(MedId,MedName,DoM,DoE,Prices))
    row=cur.fetchall()
    conn.close()
    return row


def dataUpdate(id,MedId="" , MedName="" , DoM="" , DoE="" , Prices="" ):
    conn=sqlite3.connect("management.db")
    cur=conn.cursor()
    cur.execute("UPDATE management SET  MedId=?,MedName=?, DoM=?,DoE=?,Prices=?,WHERE id=?",(MedId,MedName,DoM,DoE,Prices,id))
    conn.commit()
    conn.close()


