#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
pid=form.getvalue('pid')
delete="delete from product where id=%d"%(int(pid))
if(cursor.execute(delete)>0):
    db.commit()
    print("<script>alert('Product Removed');location.href='productmenu.py';</script>")
