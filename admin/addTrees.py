#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-Type:text/html\n\r")
print("""
<html>
<head>
<meta charset="UTF-8">
<title>Natural Farming</title>
<link rel="stylesheet" type="text/css" href="css/style.css">


</head>
<body>



<form action="inserttrees.py" name="login" method="post" enctype="multipart/form-data">
<div id="page" style='width:100%;'>

<img src="header1.jpg" width="100%" height=150>

<div id="header">
<ul style='width:100%;'>
<li>
<a href="adminhomepage.py">Vegetables</a>
</li>


<li >
<a href="addCrops.py">Crops</a>
</li>
<li>
<a href="addNaturals.py">Natural Fertilizer</a>
</li>
<li>
<a href="addGreens.py">Greens</a>
</li>
<li class="current">
<a href="addTrees.py">Trees</a>
</li>


<li>
<a href="logout.py">Logout</a>
</li>
</ul>

</div>
<div id="body">
<div class="header">
<div style="z-index:1">
<br><br><br><br>
<table bgcolor="silver" align="center" width="500px" height="200px">
<tr>
<td align="center" colspan=2>
ADD TREES
</td>
</tr>
<tr><td>Name</td><td>
<input type="text" name="vname" style="width:300px"></td></tr>
<tr><td>Image</td><td>
<input type="file" name="vegimg"></td></tr>
<tr><td>Grows</td><td>
<textarea name="grows" rows=5 cols=40>
</textarea></td></tr>
<tr><td>Season</td><td>
<input type="text" name="season" style="width:300px"></td></tr>

<tr><td>Compost</td><td>
<textarea name="compost" rows=5 cols=40>
</textarea></td></tr>


<tr>
<td align="center" colspan=2>
<input type="submit" name="b" value="Add" style="width:150px;height:30px">
<a href="viewtrees.py"><input type="button" value="VIEW" style="width:150px;height:30px;background-color:teal;"></a>


</td>
</tr>		 
</table>


</div>

</div>




<div id="footer">
<img src="images/bottom.png" width="100%">
</div>

</div>
</div>
</form>







</body>
</html>""")
