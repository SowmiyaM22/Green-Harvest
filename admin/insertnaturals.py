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
        nfname=form.getvalue('nfname')
        description=form.getvalue('description')
        query="insert into tbl_natural_fertilizers(name,description) values('%s','%s')"%(nfname,description)
        res=cursor.execute(query)
        if(res==1):
            dbcon.commit()
            print("<script>alert('Addedd Successfully');location.href='viewnaturals.py';</script>")
        else:
            dbcon.rollback()
            print("<script>alert('Error in Adding');location.href='addNaturals.py';</script>")
    else:
        print("<script>alert('DB Error');location.href='adminhomepage.py';</script>")
except Exception as e:
    print(e)
    
