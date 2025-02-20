import pymysql
db=pymysql.connect(host="localhost",user="root",password="roots",database="agriculture")
cursor=db.cursor()
select="select name,category,email from tbl_session"
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    name=results[0]
    category=results[1]
    email=results[2]
else:
    name="None"

print("""<!DOCTYPE html>
<header id='header'>
<h1><a href='index.py'>ONLINE FARMER's DIGITAL MARKET (AgroCulture)</a></h1>
<nav id='nav'>
<ul><li><a href='index.py'><span class='glyphicon glyphicon-home'></span> Home</a></li>""")
##<li><a href='myCart.py'><span class='glyphicon glyphicon-shopping-cart'>MyCart</a></li>
if(name!="None" and (category=="farmer" or category=="buyer")):
    print("<li><a href='market.py'><span class='glyphicon glyphicon-grain'>Digital-Market</a></li>")
    print("<li><a href='logout.py'><span class='glyphicon glyphicon-grain'>Logout</a></li>")
else:
    print("<li><a href='market.py'><span class='glyphicon glyphicon-grain'>Digital-Market</a></li>")
    print("<li><a href='login.py'>")
    print("<span class='glyphicon glyphicon-log-in'></span>Login</a></li>")
    print("<li><a href='register.py'>")
    print("<span class='glyphicon glyphicon-log-in'></span>Register</a></li>")
##<span class='<?php echo $logo; ?>'></span><?php echo' '. $loginProfile; ?></a></li>

##<li><a href='blogView.py'><span class='glyphicon glyphicon-comment'> BLOG</a></li>
print("""</ul></nav></header>
</body>
</html>""")
