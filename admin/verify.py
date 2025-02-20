#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-Type:text/html\n\r")
import cgi
form=cgi.FieldStorage()
uname=form.getvalue('uname')
upwd=form.getvalue('upwd')
if(uname=='Admin' and upwd=='Admin'):
	print("<script>alert('Login Success');location.href='adminhomepage.py';</script>")
else:
	print("<script>alert('Login Error');location.href='index.py';</script>")



