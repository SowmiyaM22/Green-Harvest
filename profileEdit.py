#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *

print("""<!DOCTYPE HTML>
<html lang='en'>
<head>
<title>Profile:""")
print(name)
print("""</title>
<meta charset='utf-8' />
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<meta name='viewport' content='width=device-width, initial-scale=1' />
<link href='bootstrap\css\bootstrap.min.css' rel='stylesheet'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>
<script src='bootstrap\js\bootstrap.min.js'></script>
<link rel='stylesheet' href='assets/css/main.css' />
</head>
<body class='subpage'>""")
print("<center>")

select="select username,email,mobile,address,image,password from user where email='%s'"%(email)
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    name=results[0]
    email=results[1]
    phone=results[2]
    address=results[3]
    image=results[4]
    pwd=results[5]

image1="images/profileImages/%s"%(image)
print("""<section id='post' class='wrapper bg-img' data-bg='banner2.jpg'>
<div class='inner'>
<div class='box'>
<header>
<span class='image left'>""")
print("<form method='post' action='update_profile.py' enctype='multipart/form-data'>")
print("<img src='"+image1+"' class='img-circle' class='img-responsive' height='200px'></span>")
print("<input type='hidden' name='img_hide' value='%s'>"%(image))
print("<br><input type='file' name='profilePic' id='profilePic'><h2>")
print(name)
print("""</h2>
<h4>""")
print(email)
print("""</h4>
<br>

<br>
</header>""")
print("<table cellpadding='10'>")
print("<tr><td>Name:</td><td><input type='text' name='name' id='name' value='%s' placeholder='Full Name' required /></td><tr>"%(name))
print("<tr><td>Password:</td><td><input type='text' name='pwd'  value='%s' required /></td><tr>"%(pwd))
print("<tr><td>Mobile:</td><td><input type='text' name='mobile' id='mobile' value='%s' placeholder='Mobile No' required/></td></tr>"%(phone))
print("<tr><td>Address</td><td><textarea name='address'  required/>%s</textarea></td></tr>"%(address))
print("<tr><td></td><td><input type='submit' class = 'button special' value='Update Profile' />&nbsp;&nbsp;<input type='submit' class = 'button special' value='Back' formaction='profileView.py'></td></tr>")
print("</table>")
print("""</form>
</div></div>
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
