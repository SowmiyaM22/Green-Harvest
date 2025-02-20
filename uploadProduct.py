#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")

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
<script type='text/javascript' src='image_upload.js'></script>""")

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

print("""<section id='one' class='wrapper style1 align-center'>
<div class='container'>
<form method='POST' action='uploadProduct_action.py' enctype='multipart/form-data'>
<h2>Enter the Product Information here..!!</h2><br>
<center>
<img id='blah1' src='preview.jpg' alt='your image' />
<input type='file' name='productPic' class='form-control' required onchange='readURL1(this);' />
<br /></center>
<div class='row'>
<div class='col-sm-6'>
<div class='select-wrapper' style='width: auto' >
Product Category: <select name='ptype' id='ptype' required style='background-color:white;color: black;'>
<option value='' style='color: black;'>- Category -</option>
<option value='Fruit' style='color: black;'>Fruit</option>
<option value='Vegetable' style='color: black;'>Vegetable</option>
<option value='Grains' style='color: black;'>Grains</option>
</select></div></div>
<div class='col-sm-6'>
Product Name: <input type='text' name='pname' id='pname' value='' placeholder='Product Name' style='background-color:white;color: black;' />
</div><br>
<div class='col-sm-6'>
Quantity: <input type='number' name='quantity' id='quantity' value='' min='1' placeholder='Product quantity' style='background-color:white;color: black;' />
</div></div>
<br><div>
<textarea  name='pinfo' id='pinfo' rows='12'></textarea></div>
<br><div class='row'>
<div class='col-sm-6'>
Price: <input type='text' name='price' id='price' value='' placeholder='Price per kg' style='background-color:white;color: black;' /></div>
<div class='col-sm-6'>
<button class='button fit' style='width:auto; color:black;'>Submit</button></div>
</div></form>
</div></section>
<script>
CKEDITOR.replace( 'pinfo' );
</script>""")
import footer
print("""</body>
</html>""")
