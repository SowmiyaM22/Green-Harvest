#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *

print("""<!DOCTYPE HTML>
<html lang='en'>
<head>
<title>Profile:""")
print(name)
##<?php echo $_SESSION['Username']; ?>
print("""</title>
<meta charset='utf-8' />
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<meta name='viewport' content='width=device-width, initial-scale=1' />
<link href='bootstrap\css\bootstrap.min.css' rel='stylesheet'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>
<script src='bootstrap\js\bootstrap.min.js'></script>
<meta name='description' content='' />
<meta name='keywords' content='' />""")
##		<!--[if lte IE 8]><script src='css/ie/html5shiv.js'></script><![endif]-->
print("""<link rel='stylesheet' href='login.css'/>
<script src='js/jquery.min.js'></script>
<script src='js/skel.min.js'></script>
<script src='js/skel-layers.min.js'></script>
<script src='js/init.js'></script>
<link rel='stylesheet' href='css/skel.css' />
<link rel='stylesheet' href='css/style.css' />
<link rel='stylesheet' href='css/style-xlarge.css' />
</head>
<body>""")
from menu import *

select="select username,email,mobile,address,image from user where email='%s'"%(email)
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    name=results[0]
    email=results[1]
    phone=results[2]
    address=results[3]
    image=results[4]
    image="images/profileImages/%s"%(image)
print("""<section id='one' class='wrapper style1 align'>
<div class='inner'>
<div class='box'>
<header><center>""")
print("<span><img src='"+image+"' class='image-circle' class='img-responsive' height='200%'>")
print("</span>")
print("<br><h2>")
print(name)
print("""</h2>
<h4 style='color: black;'>""")
print(email)
print("""</h4><br>
</center>
</header>
<div class='row'>
<div class='col-sm-3'></div>""")
##<div class='col-sm-3'>
##<b><font size='+1' color='black'>RATINGS : </font></b>
##<font size='+1'>"""
####<?php echo $_SESSION['Rating'];?>
##</font></div>
print("""<div class='col-sm-3'>
<b><font size='+1' color='black'>Email ID : </font></b>
<font size='+1'>""")
print(email)
##<?php echo $_SESSION['Email'];?>
print("""</font></div>
<div class='col-sm-3'></div></div><br />
<div class='row'>
<div class='col-sm-3'></div>
<div class='col-sm-3'>
<b><font size='+1' color='black'>Mobile No : </font></b>
<font size='+1'>""")
print(phone)##<?php echo $_SESSION['Mobile'];?>
print("""</font></div>
<div class='col-sm-3'>
<b><font size='+1' color='black'>ADDRESS : </font></b>
<font size='+1'>""")
print(address)##<?php echo $_SESSION['Addr'];?>
print("""</font></div>
<div class='col-sm-3'></div></div>
<div class='12u$'><center>
<div class='row uniform'>

<div class='3u 12u$(large)'>
<a href='profileEdit.py' class='btn btn-danger' style='color:white;'>Edit Profile</a></div>

<div class='3u 12u$(large)'>
<a href='logout.py' class='btn btn-danger' style='color:white;'>LOG OUT</a>
</div></div>
</center>
</div></div></div>
</div>
</section>""")

##        <!-- Scripts -->
print("""<script src='assets/js/jquery.min.js'></script>
<script src='assets/js/jquery.scrolly.min.js'></script>
<script src='assets/js/jquery.scrollex.min.js'></script>
<script src='assets/js/skel.min.js'></script>
<script src='assets/js/util.js'></script>
<script src='assets/js/main.js'></script>
</body>
</html>""")
