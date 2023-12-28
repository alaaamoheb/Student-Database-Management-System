import mysql.connector

def studentData():
    try:
        with mysql.connector.connect(host="localhost", user="root", password="1234") as con:
            cur = con.cursor()
            # Create the 'project' database if it doesn't exist
            cur.execute("CREATE DATABASE IF NOT EXISTS project")
            cur.execute("USE project")
            # Create the 'Application' table if it doesn't exist
            cur.execute("CREATE TABLE IF NOT EXISTS Application(id INTEGER PRIMARY KEY AUTO_INCREMENT, StudentID TEXT, FirstName TEXT, LastName TEXT, DateOfBirth TEXT, Age TEXT, Gender TEXT, Address TEXT, Mobile TEXT)")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def addStudentRecord(StudentID, FirstName, LastName, DateOfBirth, Age, Gender, Address, Mobile):
    try:
        with mysql.connector.connect(host="localhost", user="root", password="1234") as con:
            cur = con.cursor()
            cur.execute("USE project")
            cur.execute("INSERT INTO Application (StudentID, FirstName, LastName, DateOfBirth, Age, Gender, Address, Mobile) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                        (StudentID, FirstName, LastName, DateOfBirth, Age, Gender, Address, Mobile))
    except mysql.connector.Error as err:
        print(f"Error: {err}")




def viewStudentData():
    con = mysql.connector.connect(host="localhost", user="root", password="1234")
    cur = con.cursor()
    cur.execute("USE project")
    cur.execute("SELECT * FROM Application")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteStudentRecord(id):
    con = mysql.connector.connect(host="localhost", user="root", password="1234")
    cur = con.cursor()
    cur.execute("USE project")
    cur.execute("DELETE FROM Application WHERE id=%s", (id,))
    con.commit()
    con.close()

def searchStudentData(StudentID, FirstName, LastName, DateOfBirth, Age, Gender, Address, Mobile):
    con = mysql.connector.connect(host="localhost", user="root", password="1234")
    cur = con.cursor()
    cur.execute("USE project")
    cur.execute("SELECT * FROM Application WHERE StudentID=%s OR FirstName=%s OR LastName=%s OR DateOfBirth=%s OR Age=%s OR Gender=%s OR Address=%s OR Mobile=%s",
                (StudentID, FirstName, LastName, DateOfBirth, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows

def updateStudentRecord(id, StudentID="", FirstName="", LastName="", DateOfBirth="", Age="", Gender="", Address="", Mobile=""):
    con = mysql.connector.connect(host="localhost", user="root", password="1234")
    cur = con.cursor()
    cur.execute("USE project")
    cur.execute("UPDATE Application SET StudentID=%s, FirstName=%s, LastName=%s, DateOfBirth=%s, Age=%s, Gender=%s, Address=%s, Mobile=%s WHERE id=%s",
                (StudentID, FirstName, LastName, DateOfBirth, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()
