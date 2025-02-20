import cgi
form=cgi.FieldStorage()
import pymysql
db=pymysql.connect(host="localhost",user="root",password="roots",database="agriculture")
cursor=db.cursor()
select="select name,category,email from tbl_session"
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    name=results[0]
    category=results[1]
    email=results[2]

