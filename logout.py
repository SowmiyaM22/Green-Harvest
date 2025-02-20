#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
delete="delete from tbl_session where email='%s'"%(email)
if(cursor.execute(delete)>0):
    db.commit()
    print("<script>location.href='index.py';</script>")
