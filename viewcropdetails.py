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
    print("<h2>Crop Details</h2>")
    print("<br />")
    print("""<div class='row 200%' style='border:1px solid #000000'>
    <table border=1><tr><td>#</td><td>Name</td><td>Image</td><td>Grows</td><td>Season</td><td>Compost</td></tr>
    """)
    
    query="select * from tbl_crops"
    cursor.execute(query)
    res=cursor.fetchall()
    cnt=0
    for row in res:
        cnt=cnt+1
        name=row[1]
        image=row[2]
        grows=row[3]
        season=row[4]
        compost=row[5]
        print("<tr><td>%s</td><td>%s</td><td><img src='admin/Fileupload/crops/%s' width=100 height=100></td><td>%s</td><td>%s</td><td>%s</td></tr>"%(cnt,name,image,grows,season,compost))
    print("</table></div>")
    print("<br><br><h2>Crop Greens</h2>")
    print("<br />")
    print("""<div class='row 200%' style='border:1px solid #000000'>
    <table border=1><tr><td>#</td><td>Name</td><td>Image</td><td>Grows</td><td>Season</td><td>Compost</td></tr>
    """)
    
    query="select * from tbl_greens"
    cursor.execute(query)
    res=cursor.fetchall()
    cnt=0
    for row in res:
        cnt=cnt+1
        name=row[1]
        image=row[2]
        grows=row[3]
        season=row[4]
        compost=row[5]
        print("<tr><td>%s</td><td>%s</td><td><img src='admin/Fileupload/greens/%s' width=100 height=100></td><td>%s</td><td>%s</td><td>%s</td></tr>"%(cnt,name,image,grows,season,compost))
    print("</table></div>")

    print("<br><br><h2>Crop Trees</h2>")
    print("<br />")
    print("""<div class='row 200%' style='border:1px solid #000000'>
    <table border=1><tr><td>#</td><td>Name</td><td>Image</td><td>Grows</td><td>Season</td><td>Compost</td></tr>
    """)
    
    query="select * from tbl_trees"
    cursor.execute(query)
    res=cursor.fetchall()
    cnt=0
    for row in res:
        cnt=cnt+1
        name=row[1]
        image=row[2]
        grows=row[3]
        season=row[4]
        compost=row[5]
        print("<tr><td>%s</td><td>%s</td><td><img src='admin/Fileupload/trees/%s' width=100 height=100></td><td>%s</td><td>%s</td><td>%s</td></tr>"%(cnt,name,image,grows,season,compost))
    print("</table></div>")

    print("<br><br><h2>Crop Vegetables</h2>")
    print("<br />")
    print("""<div class='row 200%' style='border:1px solid #000000'>
    <table border=1><tr><td>#</td><td>Name</td><td>Image</td><td>Grows</td><td>Season</td><td>Compost</td></tr>
    """)
    
    query="select * from tbl_vegetables"
    cursor.execute(query)
    res=cursor.fetchall()
    cnt=0
    for row in res:
        cnt=cnt+1
        name=row[1]
        image=row[2]
        grows=row[3]
        season=row[4]
        compost=row[5]
        print("<tr><td>%s</td><td>%s</td><td><img src='admin/Fileupload/vegetables/%s' width=100 height=100></td><td>%s</td><td>%s</td><td>%s</td></tr>"%(cnt,name,image,grows,season,compost))
    print("</table></div>")

    print("<br><br><h2>Natural Fertilizers</h2>")
    print("<br />")
    print("""<div class='row 200%' style='border:1px solid #000000'>
    <table border=1><tr><td>#</td><td>Name</td><td>Description</td></tr>
    """)
    
    query="select * from tbl_natural_fertilizers"
    cursor.execute(query)
    res=cursor.fetchall()
    cnt=0
    for row in res:
        cnt=cnt+1
        name=row[1]
        description=row[2]
        
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>"%(cnt,name,description))
    print("</table></div>")
    
    
    print("""</div>



    
    </section>""")



import footer
print("""</body>
</html>""")
