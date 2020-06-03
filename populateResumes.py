import Dependencies
import ResumeGenerator
import pyodbc

connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-HOLIG319;'
                      'Database=DBMS;'
                      'Trusted_Connection=yes;'
                      'MARS_Connection = YES;')

cur = connection.cursor()
memberList = cur.execute("SELECT MEMBER_ID FROM MEMBER").fetchall()

if memberList:
    memberList = [i[0] for i in memberList]
memberList.sort()

for memberID in memberList:
    print(memberID)
    values = Dependencies.clientInfo(memberID)
    resume_values = Dependencies.structureDetails(values)
    ResumeGenerator.create_resume(resume_values)