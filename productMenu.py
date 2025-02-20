#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
print("""<!DOCTYPE html>
<html lang='en'>
<head><meta charset='UTF-8'>
<title>AgroCulture</title>
<meta http-equiv='content-type' content='text/html; charset=utf-8' />
<meta name='description' content='' />
<meta name='keywords' content='' />
<link href='bootstrap\css\bootstrap.min.css' rel='stylesheet'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>
<script src='bootstrap\js\bootstrap.min.js'></script>""")

print("""<link rel='stylesheet' href='login.css'/>
<script src='js/jquery.min.js'></script>
<script src='js/skel.min.js'></script>
<script src='js/skel-layers.min.js'></script>
<script src='js/init.js'></script>
<noscript>
<link rel='stylesheet' href='css/skel.css' />
<link rel='stylesheet' href='css/style.css' />
<link rel='stylesheet' href='css/style-xlarge.css' />
</noscript>""")

print("""</head>
<body class>""")
from menu import *

print("""<section id='main' class='wrapper style1 align-center' >
<div class='container'>
<h2>Welcome to digital market</h2>""")

print("""<h3>Select Filter</h3>
<form method='get' name='product'>
<center>
<div class='row'>
<div class='col-sm-4'></div>
<div class='col-sm-2'>
<div class='select-wrapper' style='width: auto' >
<select name='type' id='type' required style='background-color:white;color: black;'>
<option value='all' style='color: black;'>List All</option>
<option value='fruit' style='color: black;'>Fruit</option>
<option value='vegetable' style='color: black;'>Vegetable</option>
<option value='grain' style='color: black;'>Grains</option>
</select></div></div>
<div class='col-sm-2'>
<input class='button special' type='submit' name='submit' value='Go!' /></div>
<div class='col-sm-4'></div></div></center></form>""")

print("""<section id='two' class='wrapper style2 align-center'>
<div class='container'>""")
if(category=="farmer"):
    if(form.getvalue('submit')!="None" and form.getvalue('type')=="all"):
        sql="select * from product where email='%s' order by id desc"%(email)
    elif(form.getvalue('submit')!="None" and form.getvalue('type')=="fruit"):
        sql="select * from product where email='%s' and pcategory='Fruit' order by id desc"%(email)
    elif(form.getvalue('submit')!="None" and form.getvalue('type')=="vegetable"):
        sql="select * from product where email='%s' and pcategory='Vegetable' order by id desc"%(email)
    elif(form.getvalue('submit')!="None" and form.getvalue('type')=="grain"):
        sql="select * from product where email='%s' and pcategory='Grains' order by id desc"%(email)
    else:
        sql="select * from product where email='%s' order by id desc"%(email)
else:
    if(form.getvalue('submit')!="None" and form.getvalue('type')=="all"):
        sql="select * from product order by id desc"
    elif(form.getvalue('submit')!="None" and form.getvalue('type')=="fruit"):
        sql="select * from product where pcategory='Fruit' order by id desc"
    elif(form.getvalue('submit')!="None" and form.getvalue('type')=="vegetable"):
        sql="select * from product where pcategory='Vegetable' order by id desc"
    elif(form.getvalue('submit')!="None" and form.getvalue('type')=="grain"):
        sql="select * from product where pcategory='Grains' order by id desc"
    else:
        sql="select * from product order by id desc"

print("<div class='row'>")
if(cursor.execute(sql)>0):
    results=cursor.fetchall()
    for row in results:
        pid=row[0]
        pcat=row[4]
        pname=row[5]
        pcost=row[6]
        pic=row[9]
        print("""<div class='col-md-4'>
        <section>""")
        
        if(category=="farmer"):
            print("""<strong><h2 class='title' style='color:black; '>""")
            print(pname)
            print("</h2></strong>")
            
            print("<img class='image fit' src='upload_images/%s' height='220px;'  />"%(pic))
            print("""<div style='align: left'><blockquote>""")
            print("Category:")
            print(pcat)
            print("<br>")
            print("Price(per kg):")
            print(pcost)
            print("/-")
            print("<br>")
            print("<a href='edit-product.py?pid=%s'>"%(pid))
            print("<font color='blue'>Edit</font>")
            print("</a>")
            print("/")
            print("<a href='delete-product.py?pid=%s'>"%(pid))
            print("<font color='red'>Delete</font>")
            print("</a>")
        else:
            print("""<strong><h2 class='title' style='color:black; '>""")
            print(pname)
            print("</h2></strong>")
            print("<a href='view-product.py?pid=%s'>"%(pid))
            print("<img class='image fit' src='upload_images/%s' height='220px;'  /></a>"%(pic))
            print("""<div style='align: left'><blockquote>""")
            print("Category:")
            print(pcat)
            print("<br>")
            print("Price(per kg):")
            print(pcost)
            print("/-")
            print("<br>")
            
            select="select ifnull(avg(rating),0) from review where pid=%d"%(int(pid))
            cursor.execute(select)
            results=cursor.fetchone()
            avg=int(results[0])
            if(avg!=0):
                avg=round(avg,1)
                print("<b><font color='white'>Overall Rating: <font color='blue'>%s out of 10</font>"%(avg))
                print("&nbsp;<a href='review.py?pid=%s'>"%(pid))
                print("<font color='red'>View Reviews</font>")
                print("</a>")
            else:
                print("<b><font color='white'>Overall Rating: <font color='blue'>No ratings</font>")
                print("&nbsp;<a href='review.py?pid=%s'>"%(pid))
                print("<font color='red'>View Reviews</font>")
                print("</a>")
                
            print("<br><a href='view-product.py?pid=%s'>"%(pid))
            print("<font color='Red'>view details</font>")
            print("</a>")
        print("</section></div>")

print("""</div></section>
</header>
</section>""")
import footer
print("""</body>
</html>""")
