#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-Type:text/html\n\n")
import cgi
import pymysql
form=cgi.FieldStorage()
Id=form.getvalue('Id')
password=form.getvalue('password')
db=pymysql.connect(host="localhost",user="root",password="roots",database="agriculture")
if db:
    cursor=db.cursor()
    if Id=='000' and password=='Admin':
        try:
            insertQuery="insert into admin(Id,password) values(%d,'%s')"%(int(Id),password)
            print(insertQuery)
            cursor.execute(insertQuery)
            db.commit()
            print("<script>alert('Login Success');location.href='wheat.py';</script>")
        except:
            db.rollback()
##            print("<script>alert('Invalid');location.href='index.py';</script>")
##    else:
##        selectQuery="select * from registration where fid=%d and password='%s'"%(int(fid),password)
##        if cursor.execute(selectQuery)>0:
##            try:
##                result=cursor.fetchone()
##                fid=result[0]
##                password=result[4]
##                insertQuery="insert into sign(fid,password) values(%d,'%s')"%(int(fid),password)
##                print(insertQuery)
##                cursor.execute(insertQuery)
##                db.commit()
##                print("<script>alert('Login Success');location.href='home.py?fid=%s';</script>"%(int(fid)))
##            except:
##                db.rollback()
##                print("<script>alert('Invalid Credentials');location.href='index.py';</script>")            
##            #print "<script>alert('Login Success');location.href='userhomepage.py';</script>"
##        else:
##            print("<script>alert('Invalid Credentials');location.href='index.py';</script>")
else:
    print("Error in Connecting with Server")
