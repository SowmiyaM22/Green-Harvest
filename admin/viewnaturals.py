#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
import os
try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="roots",database="agriculture")
    if(dbcon):
        cursor=dbcon.cursor()
        query="select * from tbl_natural_fertilizers"
       
        cursor.execute(query)
        result=cursor.fetchall()
        print("""<html>
        <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">

        <title>Natural Farming</title>
        <link rel="stylesheet" type="text/css" href="css/style.css">


        </head>
        <body>
        <form action="insertvegetables.py" name="login" method="post" enctype="multipart/form-data">
        <div id="page" style='width:100%;'>

        <img src="header1.jpg" width=100% height=150>

        <div id="header">
        <ul style='width:100%;'>
        <li class="current">
        <a href="adminhomepage.py">Vegetables</a>
        </li>


        <li>
        <a href="addCrops.py">Crops</a>
        </li>

        <li>
        <a href="addNaturals.py">Natural Fertilizer</a>
        </li>

        <li>
        <a href="addGreens.py">Greens</a>
        </li>
        <li>
        <a href="addTrees.py">Trees</a>
        </li>
        <li>
        <a href="addLoans.py">GovernmentLoans</a>
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
        <table bgcolor="silver" align="center" width="800px" height="">
        <tr>
        <td bgcolor="teal" align="center" colspan=8>
        NATURALS
        </td>
        </tr>
        <tr><td align="center">Name</td><td align="center">Description</td>
        <td align="center">Delete</td>
        </tr>""")
        for row in result:
            sno=row[0]
            name=row[1]
            description=row[2]
            print("<tr><td align='center'>%s</td>"%(name))
            print("<td align='center'>%s</td>"%(description))
            print("<td align='center'><a href='deletenatural.py?q=%d'>Delete</a></td>"%(int(sno)))
            print("</tr>")
        print("""</table>
                                         

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
    else:
        print("<script>alert('DB Error');location.href='adminhomepage.py';</script>")
except Exception as e:
    print("<script>alert('%s');location.href='adminhomepage.py';</script>"%(e))
    
