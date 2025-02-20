#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
import os
form=cgi.FieldStorage()

try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="roots",database="agriculture")
    if(dbcon):
        cursor=dbcon.cursor()
        nid=form.getvalue('q')
        query="delete from tbl_natural_fertilizers where sno=%d"%(int(nid))
        res=cursor.execute(query)
        if(res==1):
            dbcon.commit()
            print("<script>alert('Deleted');location.href='viewnaturals.py';</script>")
        else:
            dbcon.rollback()
            print("<script>alert('Error in Deletion');location.href='viewnaturals.py';</script>")
    else:
        print("<script>alert('DB Error');location.href='adminhomepage.py';</script>")
except Exception as e:
    print(e)
