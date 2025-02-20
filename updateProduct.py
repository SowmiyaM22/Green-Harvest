#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-type:text/html\r\n\r\n")
import os
import cgi
try:
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass
form=cgi.FieldStorage()
image=form['productPic']

if image.filename:
    fn=os.path.basename(image.filename)
    open("upload_images/"+fn, 'wb').write(image.file.read())
    image=fn
else:
    image=form.getvalue('img_hide')
pid=form.getvalue('pid')
pcategory=form.getvalue('ptype')
pname=form.getvalue('pname')
quantity=form.getvalue('quantity')
desc=form.getvalue('pinfo')
##to eliminate single quotations
desc=desc.replace("'","")
price=form.getvalue('price')
import pymysql
db=pymysql.connect(host="localhost",user="root",password="roots",database="agriculture")
cursor=db.cursor()
select="select name,category,email from tbl_session"
if(cursor.execute(select)>0):
    results=cursor.fetchone()
    name=results[0]
    category=results[1]
    email=results[2]
    select="select mobile from user where email='%s'"%(email)
    if(cursor.execute(select)>0):
        results=cursor.fetchone()
        mobile=results[0]
insert="update product set email='%s',name='%s',phone='%s',pcategory='%s',pname='%s',pcost=%d,quantity=%d,pdesc='%s',pic='%s' where id=%d"%(email,name,int(mobile),pcategory,pname,int(price),int(quantity),desc,image,int(pid))
if(cursor.execute(insert)>0):
    db.commit()
    print("<script>alert('Product Updated Successfully');location.href='productmenu.py';</script>")
else:
    db.rollback()
    print("<script>alert('Failed To Update! Try again Later.');location.href='productmenu.py';</script>")
