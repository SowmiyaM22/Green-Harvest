#!C:\Users\Sowmiya\AppData\Local\Programs\Python\Python312-32/python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
import os
try:
    import msvcrt # Microsoft Visual C/C++ runtime lib
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
   pass

form=cgi.FieldStorage()

try:
    dbcon=pymysql.connect(host="localhost",user="root",passwd="roots",database="agriculture")
    if(dbcon):
        cursor=dbcon.cursor()
        vname=form.getvalue('vname')
        imagename=form['vgimg']
        grows=form.getvalue('grows')
        season=form.getvalue('season')
        compost=form.getvalue('compost')
        if imagename.filename:
            fn=os.path.basename(imagename.filename)
            #Below line will upload files in specified folder named it as "files"
            open("FileUpload/vegetables/"+fn,'wb').write(imagename.file.read())
            file_name=imagename.filename
            iquery="insert into tbl_vegetables(name,image,grows,season,compost) values('%s','%s','%s','%s','%s')"%(vname,file_name,grows,season,compost)
            res=cursor.execute(iquery)
            if(res==1):
                dbcon.commit()
                print("<script>alert('Addedd Successfully');location.href='viewvegetables.py';</script>")
            else:
                dbcon.commit()
                print("<script>alert('Error in Adding');location.href='viewvegetables.py';</script>")
            
            
            

    else:
        print("<script>alert('DB Error');location.href='adminhomepage.py';</script>")
except Exception as e:
    print(e)
    
        


