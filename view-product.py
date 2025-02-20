#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
from db import *
print("""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>AgroCulture</title>
<meta http-equiv='content-type' content='text/html; charset=utf-8' />
<meta name='description' content='' />
<meta name='keywords' content='' />
<link href='bootstrap\css\bootstrap.min.css' rel='stylesheet'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>
<script src='bootstrap\js\bootstrap.min.js'></script>
<script type='text/javascript' src='image_upload.js'></script>
""")

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
</noscript>
<script src='https://cdn.ckeditor.com/4.8.0/full/ckeditor.js'></script>""")

print("</head><body>")
from menu import *
pid=form.getvalue('pid')
select="select * from product where id=%d"%(int(pid))
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    pid=results[0]
    email=results[1]
    name=results[2]
    phone=results[3]
    pcategory=results[4]
    pname=results[5]
    pcost=results[6]
    quantity=results[7]
    pdesc=results[8]
    pic=results[9]
print("""<section id='one' class='wrapper style1 align-center'>
<div class='container'>""")
print("<form method='POST' action='order.py?pid=%s' enctype='multipart/form-data'>"%(pid))
print("<h2>Enter the Product Information here..!!</h2><br>")
print("<center>")
print("<img id='blah1' src='upload_images/%s' alt='your image'  width=500 height=300/>"%(pic))

print("""<div class='row'>
<div class='col-sm-6'>
<div class='select-wrapper' style='width: auto' >""")
print("Product Category: <input type='text' name='ptype' id='ptype' value='%s' readonly style='background-color:white;color: black;'>"%(pcategory))
print("""</div></div>
<div class='col-sm-6'>""")
print("Product Name: <input type='text' name='pname' readonly id='pname' value='%s' placeholder='Product Name' style='background-color:white;color: black;' />"%(pname))
print("""</div><br>
<div class='col-sm-6'>""")
print("Select Quantity: <input type='number' name='quantity' id='quantity'  required min='1' placeholder='min 1kg' style='background-color:white;color: black;' />")
print("""</div></div>
<br><div>""")
print("<textarea  name='pinfo' readonly>%s</textarea>"%(pdesc))
print("</div>")
print("<br><br>")
print("""<div class='row'>
<div class='col-sm-6'>""")
print("Price(per kg): <input type='text' name='price' id='price' readonly  value='%s' placeholder='Price per kg' style='background-color:white;color: black;' /></div>"%(pcost))
print("</div>")
print("<br>")


print("<font color='red' size='25'>Owner Details:</font>")
print("<br>")
print("<br>")
print("<font color='white' size='5'>")
print(name)
print("<br>")
print("<br>")
print(email)
print("<br>")
print("<br>")
print(phone)
print("<br>")


print("""<br><br>
<button class='button fit' style='width:auto; color:blue;'>Place Order</button>""")
print("""</form>
</div></section>
<script>
CKEDITOR.replace( 'pinfo' );
</script>""")
import footer
print("""</body>
</html>""")
