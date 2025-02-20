#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-Type:text/html\n\r")
print("""
<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	
	<title>Natural Farming</title>
	<link rel="stylesheet" type="text/css" href="css/style.css">
<script>
function validate()
{
if(document.login.uname.value=="" || document.login.upwd.value=="")
 {
 alert("Enter Empty Field");
 return false;
 }
 else
 {
 return true;
 }
}
</script>	
	
</head>
<body>
	<form action="verify.py" name="login" method="post">
	<div id="page">
	
     <img src="header22.jpg" width=900 height=200>
	 	
		<div id="header">
				<ul>
				<li class="current">
					<a href="index.py">Home</a>
				</li>
				<li>
					<a href="index.py">About</a>
				</li>
				<li>
					<a href="index.py">Products</a>
				</li>
				<li>
					<a href="index.py">Services</a>
				</li>
				<li>
					<a href="index.py">Contact</a>
				</li>
				<li>
					<a href="adminlogin.py">Login</a>
				</li>
			</ul>

		</div>
		<div id="body">
			<div class="header">
				<div style="z-index:1">
					<br><br><br><br><br><br>
			     <table bgcolor="silver" align="center" width="300px" height="200px">
				 <tr>
				 <td align="center" colspan=2>
				 ADMIN LOGIN
				 </td>
				 </tr>
<tr><td>Login Name</td><td>
<input type="text" name="uname"></td></tr>
<tr><td>Pass Word</td><td>
<input type="password" name="upwd"></td></tr>
		<tr>
				 <td align="center" colspan=2>
				 <input type="submit" name="b" value="SignIn" style="width:150px;height:30px" onClick="return validate();">
				 </td>
				 </tr>		 
				 </table>
				 
					
				</div>
				
			</div>
			
			

			
		<div id="footer">
		<img src="images/bottom.png" width="900">
						</div>
			
		</div>
	</div>
	</form>

</body>
</html>""")
