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
        vid=form.getvalue('q')
        filename=form.getvalue('r')
        query="delete from tbl_trees where sno=%d"%(int(vid))
        res=cursor.execute(query)
        if(res==1):
            dbcon.commit()
            if(os.path.exists("Fileupload/Trees/%s"%(filename))):
                os.remove("Fileupload/Trees/%s"%(filename))
                print("<script>alert('File Deleted');location.href='viewtrees.py';</script>")
            else:
                print("<script>alert('Error in Deletion');location.href='viewtrees.py';</script>")
        else:
                print("<script>alert('Error in Deletion');location.href='viewtrees.py';</script>")
    else:
        print("<script>alert('DB Error');location.href='adminhomepage.py';</script>")
except Exception as e:
    print(e)

