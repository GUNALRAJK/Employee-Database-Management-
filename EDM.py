import mysql.connector
 
#...To create database in MySQL host using MySQL workbench...
""" ---> its a command to hide a code to execute
con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788")

cur=con.cursor()
sql="create database Employee"
result=cur.execute(sql)
cur.fetchall()
print(result)
con.commit() """

#    ...To create table in Employee database...
"""
con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")

cur=con.cursor()
sql="create table employee(Sino int primary key auto_increment,Employee_id int unique,Employee_name varchar(30),dept varchar(20),salary int,dob varchar(10),address varchar(50),phno varchar(10))"
result=cur.execute(sql)
cur.fetchall()
print(result)
con.commit()
"""

def display():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    sql="select * from employee"
    cur.execute(sql)
    result=cur.fetchall()
    con.commit()
    print(result)

def create():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    n=[]
    n.append(int(input("Enter the Employee id: ")))
    n.append(input("Enter the Employee name: "))
    n.append(input("Enter the Employee dept: "))
    n.append(input("Enter the Employee salary: "))
    n.append(input("Enter the dob: "))
    n.append(input("Enter the address: "))
    n.append(input("Enter the phno: "))
    sql="insert into employee values(NULL,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,n)
    result=cur.fetchall()
    con.commit()
    con.close()
    print(n)
        
def update():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    n=int(input("\n1.Employee id \n2.Employee name\n \n3.Employee dept \n4.Employee salary \n5.dob \n6.address\n7.phno \n select your choise: "))
    if(n==1):
        i=[]
        i.append(int(input("Enter the update Employee_id")))
        i.append(int(input("Enter the pre Employee_id")))
        sql="update employee set Employee_id=(%s) where Employee_id=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==2):
        i=[]
        i.append(input("Enter the update Employee_name"))
        i.append(input("Enter the pre Employee_name"))
        sql="update employee set Employee_name=(%s) where Employee_name=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==3):
        i=[]
        i.append(input("Enter the new dept"))
        i.append(input("Enter the old dept"))
        sql="update employee set dept=(%s) where dept=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==4):
        i=[]
        i.append(input("Enter the update salary"))
        i.append(input("Enter the old salary"))
        sql="update employee set salary=(%s) where salary=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==5):       
        i=[]
        i.append(input("Enter the update dob"))
        i.append(input("Enter the pre dob"))
        sql="update employee set dob=(%s) where dob=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==6):
        i=[]
        i.append(input("Enter the update address"))
        i.append(input("Enter the pre address"))
        sql="update employee set address=(%s) where address=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==7):
        i=[]
        i.append(int(input("Enter the update phno")))
        i.append(int(input("Enter the pre phno")))
        sql="update employee set phno=(%s) where phno=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    else:
        print("...Invalid choice...")

def view():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    n=[]
    n.append(int(input("Enter your Employee id: ")))
    sql="select * from employee where Employee_id=(%s)"
    cur.execute(sql,n)
    result=cur.fetchall()
    print(result)
    con.close()

def delete():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    n=[]
    n.append(int(input("Enter the Employee id: ")))
    sql="delete from employee where Employee_id=(%s)"
    cur.execute(sql,n)
    con.commit()
    con.close()
    
m=0    
while(m!=6):
    print("\n1.view employee database \n2.create \n3.update \n4.delete \n5.view \n6.exit")
    m=int(input("Enter your choice:"))
    if m==1:
        display()
    elif m==2:
        create()
    elif m==3:
        update()
    elif m==4:
        delete()
    elif m==5:
        view()
    elif m==6:
        print("...Exist...")
    else:
        print("...Invaild choise...")
    



    
