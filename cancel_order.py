#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
oid=form.getvalue('oid')
status=form.getvalue('status')
update="update order_details set status='%s' where id=%d"%(status,int(oid))
if(cursor.execute(update)>0):
    db.commit()
    if(status=="Delivered"):
        print("<script>alert('order Delivered successfully');location.href='orderdetails.py';</script>")
    else:
        print("<script>alert('order cancelled successfully');location.href='orderdetails.py';</script>")
else:
    print("<script>alert('Failed! Try Again Later');location.href='orderdetails.py';</script>")
