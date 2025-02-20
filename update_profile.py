#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import MySQLdb
import os
try:
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass
form=cgi.FieldStorage()
image=form['profilePic']
uname=form.getvalue('name')
pwd=form.getvalue('pwd')
mobile=form.getvalue('mobile')
address=form.getvalue('address')
address=address.replace("'","")
images="images/profileImages/"
if image.filename:
    fn=os.path.basename(image.filename)
    open("images/"+fn, 'wb').write(image.file.read())
    image=fn
else:
    image=form.getvalue('img_hide')
db=pymysql.connect(host="localhost",user="root",password="roots",database="agriculture")
cursor=db.cursor()
select="select name,category,email from tbl_session"
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    name=results[0]
    category=results[1]
    email=results[2]


update="update user set username='%s',password='%s',cpassword='%s',mobile='%s',image='%s',address='%s' where email='%s'"%(uname,pwd,pwd,mobile,image,address,email)
if(cursor.execute(update)>0):
    db.commit()
    print("<script>alert('Profile Updated Successfully');location.href='profileView.py';</script>")
else:
    db.rollback()
    print("<script>alert('Failed To Update! Try again Later.');location.href='profileView.py';</script>")
