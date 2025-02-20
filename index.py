#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
print("""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>Agro web vision</title>
<meta http-equiv='content-type' content='text/html; charset=utf-8' />
<meta name='description' content='' />
<meta name='keywords' content='' />
<link href='bootstrap\css\bootstrap.min.css' rel='stylesheet'>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js'></script>
<script src='bootstrap\js\bootstrap.min.js'></script>""")
##		<!--[if lte IE 8]><script src='css/ie/html5shiv.js'></script><![endif]-->
print("""<link rel='stylesheet' href='login.css'/>
<script src='js/jquery.min.js'></script>
<script src='js/skel.min.js'></script>
<script src='js/skel-layers.min.js'></script>
<script src='js/init.js'></script>
<noscript>
<link rel='stylesheet' href='css/skel.css' />
<link rel='stylesheet' href='css/style.css' />
<link rel='stylesheet' href='css/style-xlarge.css' />
</noscript>
<link rel='stylesheet' href='indexfooter.css' />""")
##		<!--[if lte IE 8]><link rel='stylesheet' href='css/ie/v8.css' /><![endif]-->
print("</head>")
import menu

##		<!-- Banner -->
print("""<section id='banner' class='wrapper'>
<div class='container'>
<h2>Agro web vision</h2>
<p>Your Product Our Market</p>
<br><br>""")

print("</section>")

##		<!-- One -->
print("""<section id='one' class='wrapper style1 align-center'>
<div class='container'>
<header><h2>Agro web vision</h2>
<p>Explore the new way of trading...</p>
</header>
<div class='row 200%'>
<section class='4u 12u$(small)'>
<a href='market.py'>
<font color='white'><i class='icon big rounded fa-clock-o'></i>
<p>Digital Market</p></font></a>
</section>
<section class='4u 12u$(small)'>
<a href='market.py'>
<font color='white'><i class='icon big rounded fa-search'></i>
<p>Search According to Your Needs</p></font></a>

</section>
<section class='4u$ 12u$(small)'>
<a href='register.py'>
<font color='white'><i class='icon big rounded fa-user'></i>
<p>Register with us</p></font></a>
</section>
</div>
</div>
</section>""")


##		<!-- Footer -->
print("""<footer class='footer-distributed' style='background-color:black' id='aboutUs'>
<center>
<h1 style='font: 35px calibri;'>About Us</h1>
</center>
<div class='footer-left'>
<h3 style='font-family: 'Times New Roman', cursive;'>AgroCulture &copy; </h3>""")

print("""<br />
<p style='font-size:20px;color:white'>Your product Our market !!!</p>
<br /></div>
<div class='footer-center'>
<div>
<i class='fa fa-map-marker'></i>
<p style='font-size:20px'>COLLEGE NAME<span>City Pincode</span></p>
</div>
<div>
<i class='fa fa-phone'></i>
<p style='font-size:20px'>Contact No</p>
</div>
<div>
<i class='fa fa-envelope'></i>
<p style='font-size:20px'><a href='mailto:' style='color:white'>mail id</a></p>
</div></div>
<div class='footer-right'>
<p class='footer-company-about' style='color:white'>
<span style='font-size:20px'><b>About AgroCulture</b></span>
AgroCulture is e-commerce trading platform for grains & grocerries...
</p>
<div class='footer-icons'>
<a  href='#'><i style='margin-left: 0;margin-top:5px;'class='fa fa-facebook'></i></a>
<a href='#'><i style='margin-left: 0;margin-top:5px' class='fa fa-instagram'></i></a>
<a href='#'><i style='margin-left: 0;margin-top:5px' class='fa fa-youtube'></i></a>
</div></div>
</footer>

<script>
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

var modal1= document.getElementById('id02');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal1) {
        modal1.style.display = 'none';
    }
}

</script>
</body>
</html>""")
