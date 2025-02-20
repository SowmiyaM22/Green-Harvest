#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
comment=form.getvalue('comment')
rating=form.getvalue('rating')
pid=form.getvalue('pid')
pname=form.getvalue('pname')
insert="insert into review values(%d,'%s','%s','%s',%d,'%s')"%(int(pid),pname,email,name,int(rating),comment)
if(cursor.execute(insert)>0):
    db.commit()
    print("<script>alert('comment successfully');location.href='review.py?pid=%s'</script>"%(pid))
else:
    print("<script>alert('Failed! Try Again Later');location.href='review.py?pid=%s'</script>"%(pid))
