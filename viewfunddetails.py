#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
import cgi
import pymysql
db=pymysql.connect(host="localhost",user="root",password="roots",database="agriculture")
cursor=db.cursor()
print("""
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>AgroCulture</title>
<meta http-equiv='content-type' content='text/html; charset=utf-8' />
<meta name='description' content='' />
<meta name='keywords' content='' />
<link href='bootstrap\css\bootstrap.min.css' rel='stylesheet'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>
<script src='bootstrap\js\bootstrap.min.js'></script>""")
##		<!--[if lte IE 8]><script src='css/ie/html5shiv.js'></script><![endif]-->
print("""<link rel='stylesheet' href='login.css'/>
<link rel='stylesheet' type='text/css' href='indexFooter.css'>
<script src='js/jquery.min.js'></script>
<script src='js/skel.min.js'></script>
<script src='js/skel-layers.min.js'></script>
<script src='js/init.js'></script>
<noscript>
<link rel='stylesheet' href='css/skel.css' />
<link rel='stylesheet' href='css/style.css' />
<link rel='stylesheet' href='css/style-xlarge.css' />
</noscript>""")
##		<!--[if lte IE 8]><link rel='stylesheet' href='css/ie/v8.css' /><![endif]-->
print("</head>")
from menu import *
print("<body>")



##		<!-- One -->
if(category=="farmer"):
    print("<section id='one' class='wrapper style1 align-center' style='height: auto;'>")
    print("<div class='container' style='margin-top:-100px;'>")
    print("<h2>Govt Scheme</h2>")
    print("<br />")
    print("""<div class='row 200%' style='border:1px solid #000000'>
    <table border=1><tr><td>#</td><td>Name</td><td>Acres</td><td>LandType</td><td>Category</td><td>Details</td><td>Amount</td><td>Interest</td></tr>
    """)
    
    query="select * from tbl_loans"
    cursor.execute(query)
    res=cursor.fetchall()
    cnt=0
    for row in res:
        cnt=cnt+1
        name=row[1]
        acres=row[2]
        landtype=row[3]
        category=row[4]
        details=row[5]
        amount=row[6]
        interest=row[7]
        print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>"%(cnt,name,acres,landtype,category))
        print("<td>%s</td><td>%s</td><td>%s</td></tr>"%(details,amount,interest))
    print("</table></div>")


   



   
    
    
    print("""</div>



    
    </section>""")



import footer
print("""</body>
</html>""")
