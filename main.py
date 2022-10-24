global dealerid
global userid
global adminid
from collections import UserDict
import sqlite3
conn=sqlite3.connect("cabsbooking.db")
c=conn.cursor()


def dealerreg():
      car_dealarname=input("Enter Your Name : -")
      car_dealarpassword =input("Enter your password :- ")
      car_dealaremail=input("Enter your email :- ")
      car_dealarphone=input("Enter your phone number :-")
      dins="INSERT INTO car_dealar(car_dealarname,car_dealarpassword,car_dealaremail,car_dealarphone) VALUES('"+car_dealarname+"','"+car_dealarpassword+"','"+car_dealaremail+"','"+car_dealarphone+"')"
      c.execute(dins)
      conn.commit()
      init()
     
def userreg():
      user_name=input("Enter Your Name : -")
      user_password  =input("Enter your password :- ")
      user_email =input("Enter your email :- ")
      user_phone=input("Enter your phone number :-")
      data=c.execute("SELECT * FROM users WHERE user_email ='"+user_email+"'")
      t=len(data.fetchall())
      if(t==0):
         uins="INSERT INTO users(user_name, user_password,user_email,user_phone) VALUES('"+user_name+"','"+user_password+"','"+user_email+"','"+user_phone+"')"
         c.execute(uins)
         conn.commit()
         print("user register sucessfully !")
         init()
        
      else:
        print("user already registered !!")
        userreg()


def dealerlogin():
     global dealerid
     car_dealarname=input("Enter Your Name : -")
     car_dealarpassword =input("Enter your password :- ")
     data=c.execute("SELECT * FROM car_dealar WHERE car_dealarname='"+car_dealarname+"' and car_dealarpassword ='"+car_dealarpassword+"' ")
     d=data.fetchall()
     for a in d:
          dealerid=a[0]
     t=len(d)
     if(t==1):
        print("login success ")
        dealerfeature()
     else:
        print("invalid username and password !")
        dealerlogin()




def dealerfeature():
       global dealerid
       print("1 Add CAB \n 2 View CAB \n 3 Delete CAB \n 4 update CAB \n 5 logout")
       dl=int(input("Enter your choice :- "))
       if dl==1:
           addcab()
       elif dl==2:
           viewcab()
       elif dl==3:
           deletecab()
       elif dl==4:
          pass
       elif dl==5:
          del dealerid
          init()

def addcab():
      global dealerid
      cab_name=input("Enter CAB Name : -")
      cab_number= input("Enter CAB Number : -")
      cab_type =input("Enter CAB TYPE  :- ")
      cab_model =input("Enter CAB MODEL :- ")
      cab_delarid= dealerid
      cab_from =input("Enter your Source :- ")
      cab_to=input("Enter your destination :-") 
      addc="INSERT INTO cabs(cab_name,cab_number,cab_type,cab_model,cab_delarid,cab_from,cab_to) VALUES('"+cab_name+"','"+cab_number+"','"+ cab_type+"','"+cab_model+"','"+str(cab_delarid)+"','"+cab_from+"','"+cab_to+"')"
      c.execute(addc)
      conn.commit()
      print("CAB CREATED ! ")
      dealerfeature()
      
def viewcab():
    global dealerid
    data="SELECT c.cab_id ,c.cab_name,c.cab_number,c.cab_type,c.cab_model,d.car_dealarname ,c.cab_from,c.cab_to FROM cabs as c inner join car_dealar as d on c.cab_delarid=d.car_dealarid WHERE c.cab_delarid='"+str(dealerid)+"' "
    cabdata=c.execute(data)
    finaldata=cabdata.fetchall()
    print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}{7:<15}".format("cab_id","cab_name"," cab_number"," cab_type","cab_model","cab_delarid","cab_from","cab_to"))
    for d in finaldata:
         print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}{7:<15}".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]))

    dealerfeature() 


def deletecab():
    global dealerid
    cbid=input("Enter the cab id :- ")
    data="DELETE FROM cabs WHERE cab_id='"+cbid+"' and cab_delarid='"+str(dealerid)+"'"
    c.execute(data)
    conn.commit()
    print("cab delete successfully !..s")
    dealerfeature()


def userlogin():
    global userid
    user_name=input("Enter Your User_Name : - ")
    user_password=input("Enter your User_Password : -")
    data=c.execute("SELECT * FROM users WHERE user_name='"+user_name+"' and user_password='"+ user_password+"'")
    d=data.fetchall()
    for a in d:
        userid=a[0]
    
    t=len(d)
    if t==1:
        print("login successfull ! ")
        userfeature()
    else:
        print("Failed to login ! try again")
        userlogin()

    
def userfeature():
    global userid
    print(" 1 View all CAB \n 2 Search CAB \n 3 change password \n 3 logout")
    userc=int(input("Enter your choice :- "))
    if userc==1:
        displaycab()
    elif userc==2:
        cab_from=input("Enter your source of travelling :- ")
        cab_to=input("Enter your destination of travelling :- ")
        displaycab(cab_from,cab_to)
    elif userc==3:
       changepass()
    else:
        del userid
        init()
       
    

def displaycab(cab_from='',cab_to=''):
    if cab_from!="" and cab_to!="":
         data="SELECT c.cab_id ,c.cab_name,c.cab_number,c.cab_type,c.cab_model,d.car_dealarname ,c.cab_from,c.cab_to FROM cabs as c inner join car_dealar as d on c.cab_delarid=d.car_dealarid  WHERE cab_from='"+cab_from+"' and cab_to='"+cab_to+"'"
         cabdata=c.execute(data)
         finaldata=cabdata.fetchall()
         print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}{7:<15}".format("cab_id","cab_name"," cab_number"," cab_type","cab_model","cab_delarid","cab_from","cab_to"))
         for d in finaldata:
          print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}{7:<15}".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]))
    else:
        data="SELECT c.cab_id ,c.cab_name,c.cab_number,c.cab_type,c.cab_model,d.car_dealarname ,c.cab_from,c.cab_to FROM cabs as c inner join car_dealar as d on c.cab_delarid=d.car_dealarid "
        cabdata=c.execute(data)
        finaldata=cabdata.fetchall()
        print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}{7:<15}".format("cab_id","cab_name"," cab_number"," cab_type","cab_model","cab_delarid","cab_from","cab_to"))
        for d in finaldata:
            print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}{5:<15}{6:<15}{7:<15}".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]))

        userfeature()
   
def changepass():
    global userid
    oldpass=input("input Enter your old password :- ")
    data=c.execute("SELECT *FROM users WHERE user_password='"+oldpass+"' and user_id ='"+str(userid)+"'")
    d=data.fetchall()
    t=len(d)
    if t==1:
        newpass=input("Enter your new password :- ")
        conformpass=input("Enter your conformpass :- ")
        if(newpass==conformpass):
           upd="update users set user_password='"+newpass+"' where user_id='"+str(userid)+"'"
           c.execute(upd)
           conn.commit()
           print("password update successfully !....")
           userfeature()

        else:
           print("newpassword and old password not matching !!!!!")
           userfeature()
    else:
        print("invalid old password !! please Enter correct old password !!")
        userfeature()
    

def adminlogin():
    global adminid
    admin_username=input("Enter your username for login :- ")
    admin_password=input("Enter your password :- ")
    data=c.execute("SELECT * FROM admin WHERE admin_username='"+admin_username+"' AND admin_password='"+admin_password+"'")
    d=data.fetchall()
    for a in d:
        adminid=a[0]
    t=len(d)
    if t==1:
        print("login successfully !")
    else:
        print("please valid username and password...")
    pass

def init():
 print(' Hello \n 1 Delar Registration \n 2 delar login \n 3 user Registration \n 4 user login \n 5 admin login \n 6 exit')
 userinput=int(input("Enter Your Choice :- "))
 if userinput==1:
     dealerreg()
 elif userinput==2:
     dealerlogin()
 elif userinput==3:
     userreg()
 elif userinput==4:
     userlogin()
 elif userinput==5:
     adminlogin() 
 else:
       exit()   
   



init()