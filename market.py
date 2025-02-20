#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
import cgi
form=cgi.FieldStorage()
userid=form.getvalue('userid')
usertype=form.getvalue('usertype')
select="select name,category from tbl_session where email='%s' and category='%s'"%(userid,usertype)
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    name=results[0]
    category=results[1]
else:
    print("<script>alert('you must login first');location.href='login.py';</script>")
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
    print("<section id='one' class='wrapper style1 align-center' style='height: 600px;'>")
    print("<div class='container' style='margin-top:-100px;'>")
    print("<h2>Welcome to Digital Market</h2>")
    print("<br />")
    print("""<div class='row 200%'>
    <section class='4u 12u$(small)'>
    <a href='profileView.py'><img src='profileDefault.png'></a>
    <p>Your Profile</p>
    </section>
    <section class='4u 12u$(small)'>
    <a href='uploadProduct.py'><img src='upload.png' width='50'></a>
    <p>Upload Product</p>
    </section>
    <section class='4u$ 12u$(small)'>
    <a href='productmenu.py'><img src='product.png'></a>
    <p>Our products</p>
    </section>
    </div>
    

    <div class='row 200%'>
    <section class='4u 12u$(small)'>
    <a href='orderdetails.py'><img src='order.png' width='50'></a>
    <p>Order Details</p>
    </section>
    <section class='4u$ 12u$(small)'>
    <a href='viewreviews.py'><img src='review.png' width='100'></a>
    <p>Reviews</p>
    </section>
    </div>


<div class='row 200%'>
    <section class='4u 12u$(small)'>
    <a href='viewcropdetails.py'><img src='images/crops.png' width='50' height='50'></a>
    <p>Crops Details</p>
    </section>
    
    </div>

    
    </div>



    
    </section>""")
else:
    print("<section id='one' class='wrapper style1 align-center' style='height: 600px'>")
    print("<div class='container'>")
    print("<h2>Welcome to Digital Market</h2>")
    print("<br /><br />")
    print("""<div class='row 200%'>
    <section class='4u 12u$(small)'>
    <a href='profileView.py'><img src='profileDefault.png'></a>
    <p>Your Profile</p>
    </section>
    <section class='4u 12u$(small)'>
    <a href='productMenu.py' name='catSearch'><img src='search.png'></a>
    <p>Search according to your needs</p>
    </section>
    <section class='4u$ 12u$(small)'>
    <a href='orderdetails.py'><img src='order.png' width='50'></a>
    <p>Order Details</p>
    </section>
    </div>
    </div>
    </section>""")


import footer
print("""</body>
</html>""")
