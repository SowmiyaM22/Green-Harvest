#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
pid=form.getvalue('pid')
print("""<!DOCTYPE html>
<html>
<head>
<title>AgroCulture: Product</title>
<meta lang='eng'>
<meta charset='UTF-8'>
<title>AgroCulture</title>
<meta http-equiv='content-type' content='text/html; charset=utf-8' />
<meta name='description' content='' />
<meta name='keywords' content='' />
<link href='bootstrap\css\bootstrap.min.css' rel='stylesheet'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>
<script src='bootstrap\js\bootstrap.min.js'></script>""")
##		<!--[if lte IE 8]><script src='css/ie/html5shiv.js'></script><![endif]-->
print("""<script src='js/jquery.min.js'></script>
<script src='js/skel.min.js'></script>
<script src='js/skel-layers.min.js'></script>
<script src='js/init.js'></script>
<link rel='stylesheet' href='Blog/commentBox.css' />
<noscript>
<link rel='stylesheet' href='css/skel.css' />
<link rel='stylesheet' href='css/style.css' />
<link rel='stylesheet' href='css/style-xlarge.css' />
</noscript>
</head>
<body>""")

from menu import *

select="select * from product where id=%d"%(int(pid))
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    pic=results[9]
    ownername=results[2]
    pname=results[5]
    pcost=results[6]
    pinfo=results[8]
    
print("""<section id='main' class='wrapper style1 align-center'>
<div class='container'>
<div class='row'>
<div class='col-sm-4'>""")
print("<img class='image fit' src='upload_images/%s' alt='' />"%(pic))
print("</div>")

print("""<div class='col-12 col-sm-6'>
<p style='font: 50px Times new roman;'>""")
print(pname)
print("""</p>
<p style='font: 30px Times new roman;'>Product Owner :""")
print(ownername)

print("""</p>
<p style='font: 30px Times new roman;'>Price : """)
print(pcost)
print("</p>")
print("""</div></div><br />
<div class='row'>
<div class='col-12 col-sm-12' style='font: 25px Times new roman;'>""")
print(pinfo)
print("""</div></div></div>
<br /><br />
<div class='12u$'>
<center>

<div class='container'>
<b>Product Reviews
<div class='row'>""")

print("""<div class='col-0 col-sm-3'></div>
<div class='col-12 col-sm-6'>""")
print("""<div class='con'>""")
print("<table>")
select="select * from review where pid=%d"%(int(pid))
if(cursor.execute(select)>0):
    results=cursor.fetchall()
    for row in results:
        name=row[3]
        email=row[2]
        comment=row[5]
        rating=row[4]
        print("<tr><td>")
        print("Comment : "+comment)
        print("<br>")
        print("Rating : "+str(rating)+" out of 10")
        print("""</em></div>
        """)
        print("From: "+name)
        print("("+email+")")
        print("""<br />
        """)
        print("</td></tr>")
    print("</table>")
print("</div></div></div>")

if(category!="farmer"):
    print("""<div class='container'>
    <p style='font: 20px Times new roman; align: left;'>Rate this product</p>""")
    print("<form method='POST' action='reviewInput.py?pid=%s&pname=%s'>"%(pid,pname))
    print("""<div class='row'>
    <div class='col-sm-7'>
    <textarea style='background-color:white;color: black;' cols='25' rows='5'name='comment' placeholder='Write a review'></textarea>
    </div>
    <div class='col-sm-5'>
    <br />
    Rating: <input type='number' min='0' max='10' name='rating' value='0'/>
    </div></div>
    <div class='row'>
    <div class='col-sm-12'>
    <br />
    <input type='submit' />
    </div></div>
    </form>
    </div>""")
print("""</body>
</html>""")
