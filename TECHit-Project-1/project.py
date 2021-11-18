#SJSU CMPE 138 Fall 2021 TEAM3

from sqlite3.dbapi2 import Cursor
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import scrolledtext
#from functools import partial
import sqlite3
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import date
from DBCreation import BuildDB
from DBDefaultData import addAllData
from datetime import date
from passwordHash import *
import logging

BuildDB()
addAllData()

#--------------------------------LOGGING FUNCTIONALITY----------------------------------#
logging.basicConfig(filename='TECHitLog.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(lineno)d:%(funcName)s:%(message)s')

x=''

def login():
    pwCheck = 0;
    try:
        #global row1
        #db = cx_Oracle.connect('system/lata')

        #cursor=db.cursor()
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        #flag= True
        
        #cursor=db.cursor()
        cursor.execute("select * from employee where username=?",(usernameEntry.get(),))
        row1 = cursor.fetchone()
        global x
        x=usernameEntry.get()
        
        
        #flag=False
        

        #sql="select * from employee where username='%s' and password='%s' "
        #args=(usernameEntry.get(),passwordEntry.get())
        #cursor.execute(sql % args)
        
        cursor.execute("select * from employee, Engineer where engr_id=e_id and username=?",(usernameEntry.get(),))
        row2=cursor.fetchone()
        cursor.execute("select * from employee, Dept_manager where m_id=e_id and username=?",(usernameEntry.get(),))
        row3=cursor.fetchone()
        cursor.execute("select * from employee, Database_Administrator where dba_id=e_id and username=?",(usernameEntry.get(),))
        row4=cursor.fetchone()
        cursor.execute("select * from employee, Technician where tech_id=e_id and username=?",(usernameEntry.get(),))
        row5=cursor.fetchone()
        
        dbPW = ""
        if row1: 
            dbPW = row1[5]
        
        pwCheck = verifyPassword(passwordEntry.get(),dbPW)

        #row1 = cursor.fetchone()
        if row1 and pwCheck:
            messagebox.showinfo('info','login success')
            logging.info('Login:{} has logged in'.format(usernameEntry.get()))


        else:
            messagebox.showinfo('info','login failed')
            logging.error('Failed login: Attempt to login using {} username'.format(usernameEntry.get(),))
        
        db.commit()
     
    except ValueError as v:
        messagebox.showerror('Error','Please check data you have entered')
        
    except sqlite3.DatabaseError as e:
        db.rollback()
        messagebox.showerror("Failure ", e)
        

    except Exception as u:
        messagebox.showerror('Error', 'Enter All Details')
        
    else:
        #ageEntry.delete(0,END)
        passwordEntry.delete(0,END)
        usernameEntry.delete(0,END)
            #lnEntry.delete(0,END)
            #fnEntry.delete(0,END)
            #e_idEntry.delete(0,END)
        usernameEntry.focus()  
        if db is not None:
            db.close()

    if row2 and pwCheck:
        dash.deiconify()
        root.withdraw()
    elif row3 and pwCheck:
        mang.deiconify()
        root.withdraw()
    elif row4 and pwCheck:
        dba.deiconify()
        root.withdraw()
    elif row5 and pwCheck:
        tech.deiconify()
        root.withdraw()

    
def fun1():
    global x

def fun():
    print(x)

#print(flag)

def add_tick():
    addtick.deiconify()
    dash.withdraw()
    t_idEntry.focus_set()

def register():
    reg.deiconify()
    root.withdraw()
    fnEntry.focus_set()
    #messagebox.showinfo('info',"hello")

def uptech():
    updatetech.deiconify()
    tech.withdraw()
    

def back():
    reg.withdraw()
    dash.withdraw()
    tech.withdraw()
    mang.withdraw()
	#delst.withdraw()
	#grst.withdraw()
    root.deiconify()
    usernameEntry.focus_set()
    fnEntry.focus_set()

def back1():
    addtick.withdraw()
    dash.deiconify()
    t_idEntry.focus_set()


def back2():
    vieteng.withdraw()
    dash.deiconify()

def back3():
    viettech.withdraw()
    tech.deiconify()

def back4():
    vieassteng.withdraw()
    tech.deiconify()

def back5():
    updatetech.withdraw()
    tech.deiconify()


def add_emp():
    #messagebox.showinfo('info',"hello")
    db = None
    
    try:
        db=sqlite3.connect('login.db')
        #db.execute("PRAGMA foreign_keys = 1")
        cursor=db.cursor()
        #cursor = db.cursor()
        #all1 = 'select e_id from employee'
       # cursor.execute(all1)
        
        cursor.execute("select e_id from employee")
        eid_list = cursor.fetchall()
        e_id = int(e_idEntry.get())
        fname = fnEntry.get()
        lname = lnEntry.get()
        age = int(ageEntry.get())
        username = usernameEntry1.get()
        hashPW = hashPassword(passwordEntry1.get())
        password = hashPW
        role=rolechoosen.get()
        typ= typchoosen.get()
        eid_flag= True
        fname_flag=True
        lname_flag= True
        username_flag= True
        age_flag= True
        password_flag= True
        

        if (e_id,) in eid_list:
            messagebox.showerror("Error"," This e_id Number Already Exists")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            #e_idEntry.delete(0, END)
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
            eid_flag = False
            #e_idEntry.focus_set()
            
        elif (e_id,) is None or e_id<=0:
            messagebox.showerror("Error"," Only Positive e_id Number ")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            #e_idEntry.delete(0, END)
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
            eid_flag = False
            #e_idEntry.focus_set()

        else:
            eid_flag = True



        if any(i.isdigit() for i in fname):
            messagebox.showerror("Error", "Name cannot contain Digits")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            #fnEntry.delete(0, END)
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
            fname_flag = False
            #fnEntry.focus_set()
            
        elif(len(fname)<2):
            messagebox.showerror("Error", "Name should contain minimum 2 character ")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            #fnEntry.delete(0, END)
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
            fname_flag = False
            #fnEntry.focus_set()
            
        else:
            fname_flag = True



        if any(i.isdigit() for i in lname):
            messagebox.showerror("Error", "Name cannot contain Digits")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            #lnEntry.delete(0, END)
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
            lname_flag = False
            #lnEntry.focus_set()
            
        elif(len(lname)<2):
            messagebox.showerror("Error", "Name should contain minimum 2 character ")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            #lnEntry.delete(0, END)
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
            lname_flag = False
            #lnEntry.focus_set()
            
        else:
            lname_flag = True


          
        if(len(username)<3):
            messagebox.showerror("Error", "Name should contain minimum 2 character ")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            #usernameEntry1.delete(0, END)
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
            username_flag = False
            #usernameEntry1.focus_set()          
        else:
            username_flag = True




        if(len(passwordEntry1.get())<3):
            messagebox.showerror("Error", "Password should contain minimum 2 character ")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            passwordEntry1.delete(0, END)
            username_flag = False
            passwordEntry1.focus_set()          
        else:
            password_flag = True




   
        if (age,) is None or e_id<=0:
            messagebox.showerror("Error"," Only Positive age ")
            logging.error('Failure to register as {} '.format(username,))
            #winsound.Beep(200,1000)
            #ageEntry.delete(0, END)
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
            age_flag = False
            #ageEntry.focus_set()

        else:
            age_flag = True


        if lname_flag == True and fname_flag == True and age_flag == True and username_flag == True and password_flag == True and eid_flag == True :
            #sql = "insert into employee values('%s', '%s','%d','%d','%s','%s')"
            #args = ( lname, fname, age, e_id, username,password)
            #cursor.execute(sql % args)
            #db.commit()
            #cursor.execute("Insert into employee values (?,?,?,?,?,?)",(lname, fname, age, e_id, username,password))
            today = date.today()
            dateT = today.strftime("%m/%d/%y")
            cursor.execute("INSERT INTO EMPLOYEE Values (?,?,?,?,?,?,?,?,?,?)",(fname,lname,age,e_id,username,password,'1','Engineering',dateT,None))
            db.commit()
            msg = str(cursor.rowcount) +" Account created records inserted"
            messagebox.showinfo("Success ", msg)
            logging.info('Registration: {} {} ({}) has been added as {} to database '.format(fname,lname,username,role,))
            if role=='Engineer':
                cursor.execute("Insert into Engineer Values (?,?)",(e_id,None))
                db.commit()
            elif role =='DBA':
                cursor.execute("Insert into Database_Administrator Values (?)",(e_id,))
                db.commit()
            elif role=='Technician A':
                cursor.execute("Insert into Technician Values (?)",(e_id,))
                db.commit()
                cursor.execute("Insert into Level_A_Technician Values (?)",(e_id,))
                db.commit()
            elif role=='Technician B':
                cursor.execute("Insert into Technician Values (?)",(e_id,))
                db.commit()
                cursor.execute("Insert into Level_B_Technician Values (?)",(e_id,))
                db.commit()
            elif role =='Manager':
                cursor.execute("Insert into Dept_manager Values (?)",(e_id,))
                db.commit()

            
            if typ =='Hourly':
                cursor.execute("Insert into Hourly_Employee Values (?,?)",(e_id,None))
                db.commit()

            elif typ=='Salaried':
                cursor.execute("Insert into Salaried_Employee Values (?,?)",(e_id,None))
                db.commit()


    except ValueError as v:
        messagebox.showerror('Error','Please enter e_id as Integer, fname and lname as Character and age as Integer')
        logging.error('Failure to register as {} '.format(username,))
        ageEntry.delete(0,END)
        passwordEntry1.delete(0,END)
        usernameEntry1.delete(0,END)
        lnEntry.delete(0,END)
        fnEntry.delete(0,END)
        e_idEntry.delete(0,END)
        e_idEntry.focus()
        
    except sqlite3.DatabaseError as e:
        db.rollback()
        messagebox.showerror("Failure ", e)
        logging.error('Failure to register as {} '.format(username,))
        ageEntry.delete(0,END)
        passwordEntry1.delete(0,END)
        usernameEntry1.delete(0,END)
        lnEntry.delete(0,END)
        fnEntry.delete(0,END)
        e_idEntry.delete(0,END)
        e_idEntry.focus()
        if db is not None:
            db.rollback()
        
    except Exception as u:
        messagebox.showerror('Error', 'Enter All Details')
        logging.error('Failure to register as {} '.format(username,))
        ageEntry.delete(0,END)
        passwordEntry1.delete(0,END)
        usernameEntry1.delete(0,END)
        lnEntry.delete(0,END)
        fnEntry.delete(0,END)
        e_idEntry.delete(0,END)
        e_idEntry.focus()
        
    else:
        if lname_flag== True and fname_flag == True and age_flag == True and username_flag == True and password_flag == True and eid_flag == True:
            ageEntry.delete(0,END)
            passwordEntry1.delete(0,END)
            usernameEntry1.delete(0,END)
            lnEntry.delete(0,END)
            fnEntry.delete(0,END)
            e_idEntry.delete(0,END)
            e_idEntry.focus()
        resetTechTree(cursor)
        resetEngineerTree(cursor)
        #resetDbaTree(cursor)
        if db is not None:
            db.close()
        


def addtickengr():
    #messagebox.showinfo('info',"hello")
    db = None
    
    try:
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        #cursor = db.cursor()
        #all1 = 'select e_id from employee'
        #cursor.execute(all1)
        
        cursor.execute("select t_id from Ticket")
        tid_list = cursor.fetchall()
        t_id = int(t_idEntry.get())
        status = m.get()
        level = n.get()
        #p = int(ageEntry.get())
        priority = l.get()
        description = des_engEntry.get()
        tid_flag= True
        status_flag=True
        level_flag= True
        priority_flag= True
        descripion_flag= True
        #password_flag= True

        if (t_id,) in tid_list:
            messagebox.showerror("Error"," This t_id Number Already Exists")
            logging.error('Failed to add ticket with ID {}'.format(t_id,))
			#winsound.Beep(200,1000)
            #e_idEntry.delete(0, END)
            #levelchoosen.delete(0,END)
            #prioritychoosen.delete(0,END)
            #statuschoosen.delete(0,END)
            #lnEntry.delete(0,END)
            des_engEntry.delete(0,END)
            t_idEntry.delete(0,END)
            t_idEntry.focus()
            tid_flag = False
            #e_idEntry.focus_set()

        elif (t_id,) is None or t_id<=0:
            messagebox.showerror("Error"," Only Positive t_id Number ")
            logging.error('Failed to add ticket with ID {}'.format(t_id,))
			#winsound.Beep(200,1000)
            #e_idEntry.delete(0, END)
            #statuschoosen.delete(0,END)
            #prioritychoosen.delete(0,END)
            #levelchoosen.delete(0,END)
            #lnEntry.delete(0,END)
            des_engEntry.delete(0,END)
            t_idEntry.delete(0,END)
            t_idEntry.focus()
            tid_flag = False
            #e_idEntry.focus_set()

        else:
            tid_flag = True


        if tid_flag == True and status_flag == True and level_flag == True and priority_flag == True and descripion_flag == True:
            #sql = "insert into employee values('%s', '%s','%d','%d','%s','%s')"
            #args = ( lname, fname, age, e_id, username,password)
            #cursor.execute(sql % args)
            #db.commit()
            #cursor.execute("Insert into employee values (?,?,?,?,?,?)",(lname, fname, age, e_id, username,password))
            today = date.today()
            dateT = today.strftime("%m/%d/%y")
            global x
            cursor.execute("select e_id from employee where username=?",(x,))
            tt=cursor.fetchone()
            cursor.execute("INSERT INTO Ticket Values (?,?,?,?,?,?,?,?,?)",(t_id,status,level,priority,description,'Engineering',tt[0],None,dateT))
            resetEngineerTree(cursor)
            resetTickTree(cursor)
            db.commit()
            
            msg = str(cursor.rowcount) +" Ticket is added"
            messagebox.showinfo("Success ", msg)
            logging.info('Engineer with ID {} added ticket with ID {}'.format(tt[0],t_id))
            

    except ValueError as v:
        messagebox.showerror('Error','Please enter the correct datatype')
        logging.error('Failed to add ticket with ID {}'.format(t_id,))
        #statuschoosen.delete(0,END)
        #levelchoosen.delete(0,END)
        #prioritychoosen.delete(0,END)
        #lnEntry.delete(0,END)
        des_engEntry.delete(0,END)
        t_idEntry.delete(0,END)
        t_idEntry.focus()
        tid_flag = False
            
    except sqlite3.DatabaseError as e:
        db.rollback()
        messagebox.showerror("Failure ", e)
        logging.error(' Failed to add ticket with ID {}'.format(t_id,))
        #levelchoosen.delete(0,END)
        #prioritychoosen.delete(0,END)
        #statuschoosen.delete(0,END)
        #lnEntry.delete(0,END)
        des_engEntry.delete(0,END)
        t_idEntry.delete(0,END)
        t_idEntry.focus()
        tid_flag = False
        if db is not None:
            db.rollback()
        
    except Exception as u:
        messagebox.showerror('Error', 'Enter All Details')
        logging.error('Failed to add ticket with ID {}'.format(t_id,))
        #levelchoosen.delete(0,END)
        #prioritychoosen.delete(0,END)
        #statuschoosen.delete(0,END)
        #lnEntry.delete(0,END)
        des_engEntry.delete(0,END)
        t_idEntry.delete(0,END)
        t_idEntry.focus()
        tid_flag = False
        
    else:
        if tid_flag == True and status_flag == True and level_flag == True and priority_flag == True and descripion_flag == True:
            #levelchoosen.delete(0,END)
            #statuschoosen.delete(0,END)
            #prioritychoosen.delete(0,END)
            #lnEntry.delete(0,END)
            des_engEntry.delete(0,END)
            t_idEntry.delete(0,END)
            t_idEntry.focus()
            tid_flag = False
            
        if db is not None:
            db.close()



def show_vieteng():
    vieteng.deiconify()
    dash.withdraw()
    #x=usernameEntry.get()

    db = None
    
    try:
        stdata.delete(1.0, END)
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        global x
        cursor.execute("select t_id, status, level, priority, description, e_id from employee as x, Engineer as y, Ticket as z  where y.engr_id=x.e_id and z.engr_id=y.engr_id and x.username = ?",(x,))
        data=cursor.fetchall()
        msg=''
        for d in data:
            msg=msg + "\t t_id: "+str(d[0])+ "\t\t status: "+ d[1]+ "\t\t level: "+d[2]+"\t\t priority: "+ d[3]+ "\t\t description: "+d[4]+"\t\t engr_id: "+ str(d[5])+'\n'+( '*'*140)+ '\n'
        stdata.insert(INSERT, msg)

    except sqlite3.DatabaseError as e:
        messagebox.showerror("issue : ",e)
    except Exception as e :
        print("Exception", e)
    finally :
        if db is not None:
            db.close() 


def viewalltechtick():
    viettech.deiconify()
    tech.withdraw()
    #messagebox("hello")

    db = None
    
    try:
        stdata1.delete(1.0, END)
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        global x
        cursor.execute("select * from Ticket")
        data=cursor.fetchall()
        msg=''
        for d in data:
            msg=msg + " t_id: "+str(d[0])+ " \t status: "+ d[1]+ " \t level: "+d[2]+" \t priority: "+ d[3]+ " \t description: "+d[4]+" \t engr_id: "+ str(d[6])+" \t department: "+d[5]+" \t tech_id: "+str(d[7])+'\n'+( '*'*140)+ '\n'
        stdata1.insert(INSERT, msg)

    except sqlite3.DatabaseError as e:
        messagebox.showerror("issue : ",e)
    except Exception as e :
        print("Exception", e)
    finally :
        if db is not None:
            db.close() 

    

def viewassigntechtick():
    vieassteng.deiconify()
    tech.withdraw()
    #x=usernameEntry.get()

    db = None
    
    try:
        stdata2.delete(1.0, END)
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        global x
        #print(x)
        cursor.execute("select t_id, status, level, priority, description, z.tech_id, engr_id from employee as x, Technician as y, Ticket as z  where y.tech_id=x.e_id and z.tech_id=y.tech_id and x.username = ?",(x,))
        data=cursor.fetchall()
        msg=''
        for d in data:
            msg=msg + " t_id: "+str(d[0])+ " \t status: "+ d[1]+ " \t level: "+d[2]+" \t priority: "+ d[3]+ " \t description: "+d[4]+" \t engr_id: "+ str(d[6])+" \t tech_id: "+ str(d[5])+'\n'+( '*'*140)+ '\n'
        stdata2.insert(INSERT, msg)

    except sqlite3.DatabaseError as e:
        messagebox.showerror("issue : ",e)
    except Exception as e :
        print("Exception", e)
    finally :
        if db is not None:
            db.close() 
            

def upttick():
  
    #x=usernameEntry.get()
    db = None
    
    try:

        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        t_id = int(tickupEntry.get())
        status = statustechchoosen.get()
        global x
        cursor.execute("select t_id from Ticket as x, employee as e where x.tech_id=e.e_id and username=? ",(x,))
        t_idlist=cursor.fetchall()

        cursor.execute("select t_id from Ticket as x, employee as e where x.tech_id=e.e_id and x.status ='Open' ")
        t_idlist1=cursor.fetchall()



        t_id_flag= True
        status_flag=True

        if (t_id,) not in t_idlist:
            messagebox.showerror("Error"," Please Enter your t_id")
            logging.error('Failed to close ticket with ID {}'.format(t_id,))
			#winsound.Beep(200,1000)
            #e_idEntry.delete(0, END)
            #levelchoosen.delete(0,END)
            #prioritychoosen.delete(0,END)
            #statuschoosen.delete(0,END)
            #lnEntry.delete(0,END)
            tickupEntry.delete(0,END)
            tickupEntry.focus()
            t_id_flag = False

        elif (t_id,) not in t_idlist1:
            messagebox.showerror("Error"," The t_id is already closed")
            logging.error('Failed to close ticket with ID {}'.format(t_id,))
			#winsound.Beep(200,1000)
            #e_idEntry.delete(0, END)
            #levelchoosen.delete(0,END)
            #prioritychoosen.delete(0,END)
            #statuschoosen.delete(0,END)
            #lnEntry.delete(0,END)
            tickupEntry.delete(0,END)
            tickupEntry.focus()
            t_id_flag = False

        else:
            t_id_flag=True

        if  t_id_flag == True and status_flag == True:
            sql_query="""update Ticket set status= ? where t_id=?"""
            data= (status,t_id)
            cursor.execute(sql_query,data)
            resetTickTree(cursor)
            cursor.execute("select e_id from Ticket as x, employee as e where x.tech_id=e.e_id and username=? and x.t_id=? ",(x,t_id))
            tech_id=cursor.fetchall()
            db.commit()
            messagebox.showinfo("Success","Record Updated")
            logging.info('Technician with ID {} updated ticket with id {} to closed'.format(t_id,tech_id[0]))
            

    except ValueError:
        messagebox.showerror('Error', 'Please Enter the detail correctly')
        tickupEntry.delete(0,END)

    except sqlite3.DatabaseError as e:
        messagebox.showerror('Issue',e)
        db.rollback()
        
    except UnboundLocalError:
        pass
    except Exception:
        #messagebox.showerror('Error', 'Please Enter All Details')
        pass

    else:
        if t_id_flag and status_flag:
            tickupEntry.delete(0, END)
            
        if db is not None:
            db.close()






    
    





#def validateLogin(username, password):
#	print("username entered :", username.get())
#	print("password entered :", password.get())
#	return

#window
root = Tk()  
root.geometry('888x500')  
root.title('TechHit')

my_img= ImageTk.PhotoImage(Image.open("helloworld.jpg"))
my_label=Label(root,image=my_img)
my_label.pack()
my_label.place(x=0,y=0)

#username label and text entry box
usernameLabel = Label(root, text="User Name",font='Arial 20',borderwidth=5,padx=20)
#usernameLabel.grid(row=0, column=0)
usernameLabel.pack()
usernameLabel.place(x=300,y=100)
usernamee = StringVar()
usernameEntry = Entry(root, textvariable=usernamee,font='Arial 20',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
usernameEntry.pack(pady=2)
usernameEntry.place(x=550,y=100)
print(usernameEntry.get())


#password label and password entry box
passwordLabel = Label(root,text="Password",font='Arial 20',borderwidth=5,padx=30)
#passwordLabel.grid(row=1, column=0)  
passwordLabel.pack(pady=2)
passwordLabel.place(x=300,y=200)
passworde = StringVar()
passwordEntry = Entry(root, textvariable=passworde, show='*',font='Arial 20',borderwidth=5) 
#passwordEntry.grid(row=1, column=1) 
passwordEntry.pack(pady=2)
#validateLogin = partial(validateLogin, username, password)
passwordEntry.place(x=550,y=200)

#login button
usernameEntry.focus_set()
loginButton = Button(root, text="Login", command=login,font='Arial 20',padx=20,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
loginButton.pack(pady=2)
loginButton.place(x=350,y=300)

#register button
registerButton = Button(root, text="Register", command=register,font='Arial 20',padx=30,fg='blue',borderwidth=5) 
registerButton.pack(pady=2)
registerButton.place(x=550,y=300)







#register page
reg = Toplevel(root)
reg.title("REGISTER")
reg.geometry("888x500")
reg.withdraw()

my_img1= ImageTk.PhotoImage(Image.open("xyz.jpg"))
my_label1=Label(reg,image=my_img1)
my_label1.pack()
my_label1.place(x=0,y=0)

#Labels
firstname = Label(reg, text="First Name",font='Arial 11',borderwidth=5,padx=1)
firstname.pack()
firstname.place(x=20,y=50)
#fn = StringVar()
#fnEntry = Entry(reg, textvariable=fn,font='Arial 11',borderwidth=5)
fnEntry = Entry(reg, font='Arial 11', borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
fnEntry.pack(pady=2)
fnEntry.place(x=120,y=50)

lastname = Label(reg, text="Last Name",font='Arial 11',borderwidth=5,padx=1)
lastname.pack()
lastname.place(x=450,y=50)
#ln = StringVar()
#lnEntry = Entry(reg, textvariable=ln,font='Arial 11',borderwidth=5)  
lnEntry = Entry(reg, font='Arial 11',borderwidth=5) 
#usernameEntry.grid(row=0, column=1)
lnEntry.pack(pady=2)
lnEntry.place(x=550,y=50)

age = Label(reg, text="Age",font='Arial 11',borderwidth=5,padx=25)
age.pack()
age.place(x=20,y=150)
#age = StringVar()
ageEntry = Entry(reg,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
ageEntry.pack(pady=2)
ageEntry.place(x=120,y=150)

e_id = Label(reg, text="e_id",font='Arial 11',borderwidth=5,padx=25)
e_id.pack()
e_id.place(x=450,y=150)
#age = StringVar()
e_idEntry = Entry(reg,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
e_idEntry.pack(pady=2)
e_idEntry.place(x=550,y=150)

username1 = Label(reg, text="User Name",font='Arial 11',borderwidth=5,padx=1)
username1.pack()
username1.place(x=20,y=250)
#age = StringVar()
usernameEntry1 = Entry(reg,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
usernameEntry1.pack(pady=2)
usernameEntry1.place(x=120,y=250)

password1 = Label(reg, text="Password",font='Arial 11',borderwidth=5,padx=5)
password1.pack()
password1.place(x=450,y=250)
#age = StringVar()
passwordEntry1 = Entry(reg,font='Arial 11', show='*',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
passwordEntry1.pack(pady=2)
passwordEntry1.place(x=550,y=250)


op = tkinter.StringVar()
role1 = Label(reg, text="Role Type",font='Arial 11',borderwidth=5,padx=5)
role1.pack()
role1.place(x=20,y=350)
rolechoosen = ttk.Combobox(reg, width = 27, textvariable=op, state='readonly')
rolechoosen['values']=('Engineer','DBA','Technician A','Technician B','Manager')
rolechoosen.pack(pady=2)
rolechoosen.place(x=120,y=350)
rolechoosen.current()

om = tkinter.StringVar()
typ1 = Label(reg, text="Emp_Type",font='Arial 11',borderwidth=5,padx=5)
typ1.pack()
typ1.place(x=450,y=350)
typchoosen = ttk.Combobox(reg, width = 27, textvariable=om, state='readonly')
typchoosen['values']=('Hourly','Salaried')
typchoosen.pack(pady=2)
typchoosen.place(x=550,y=350)
typchoosen.current()



#register button to save to the database
regstbutton = Button(reg, text="Register",font='Arial 20', command= add_emp ,padx=20,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
regstbutton.pack(pady=2)
regstbutton.place(x=50,y=420)

#back button
backButton = Button(reg, text="Back",font='Arial 20', command= back, padx=30, fg='blue', borderwidth=5) 
backButton.pack(pady=2)
backButton.place(x=550,y=420)






#Detail page Engineer
dash = Toplevel(root)
dash.title("Engineer")
dash.geometry("888x500")
dash.withdraw()

my_img2= ImageTk.PhotoImage(Image.open("pqr.jpeg"))
my_label2=Label(dash,image=my_img2)
my_label2.pack()
my_label2.place(x=0,y=0)

#Buttons
addbutton = Button(dash, text="ADD TICKET",font='Arial 20', command=add_tick, padx=50,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
addbutton.pack(pady=2)
addbutton.place(x=350,y=30)

'''mangbutton = Button(dash, text="Manager",font='Arial 20' ,padx=44,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
mangbutton.pack(pady=2)
mangbutton.place(x=350,y=130)'''

viewbutton = Button(dash, text="VIEW MY TICKET",font='Arial 20', command=show_vieteng ,padx=20,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
viewbutton.pack(pady=2)
viewbutton.place(x=350,y=230)

'''dbabutton = Button(dash, text="DataBaseAdmin",font='Arial 20' ,padx=1,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
dbabutton.pack(pady=2)
dbabutton.place(x=350,y=330)'''

backbutton1 = Button(dash, text="Log Out",font='Arial 20', command= back ,padx=80,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
backbutton1.pack(pady=2)
backbutton1.place(x=350,y=430)


#inside view button
vieteng = Toplevel(dash)
vieteng.title("Engineer")
vieteng.geometry("888x500")
vieteng.withdraw()

my_img4= ImageTk.PhotoImage(Image.open("abcd.png"))
my_label4=Label(vieteng,image=my_img4)
my_label4.pack()
my_label4.place(x=0,y=0)

stdata = scrolledtext.ScrolledText(vieteng, height = 25, width = 120, font = "TkDefaultFont")
stdata.pack(pady=2)
stdata.place(x=20,y=20)


backbutton3 = Button(vieteng, text="Back",font='Arial 20', command= back2 ,padx=80,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
backbutton3.pack(pady=2)
backbutton3.place(x=350,y=430)



#inside the engineerdash and inside that addticket

addtick = Toplevel(dash)
addtick.title("Engineer")
addtick.geometry("888x467")
addtick.withdraw()

my_img3= ImageTk.PhotoImage(Image.open("lmn.jpeg"))
my_label3=Label(addtick,image=my_img3)
my_label3.pack()
my_label3.place(x=0,y=0)


t_id = Label(addtick, text="t_id",font='Arial 11',borderwidth=5,padx=30)
t_id.pack()
t_id.place(x=20,y=100)
#age = StringVar()
t_idEntry = Entry(addtick,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
t_idEntry.pack(pady=2)
t_idEntry.place(x=150,y=100)


status_eng = Label(addtick, text="Status",font='Arial 11',borderwidth=5,padx=25)
status_eng.pack()
status_eng.place(x=450,y=100)

#opt = ['open']
#clicked= StringVar()
#clicked.set(opt[0])
m = tkinter.StringVar()
statuschoosen = ttk.Combobox(addtick, width = 27, textvariable=m, state='readonly')
statuschoosen['values']=('Open')
#age = StringVar()
#status_engEntry = Entry(addtick,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
statuschoosen.pack(pady=2)
statuschoosen.place(x=580,y=100)
statuschoosen.current()
#statuschoosen.bind("<<comboboxselected>>",addtickengr)


level_eng = Label(addtick, text="Level",font='Arial 11',borderwidth=5,padx=25)
level_eng.pack()
level_eng.place(x=20,y=200)

#opt1 = ['A','B']
#clicked1= StringVar()
#clicked1.set(opt1[0])
n = tkinter.StringVar()
levelchoosen = ttk.Combobox(addtick, width = 27, textvariable=n, state='readonly')
levelchoosen['values']=('A','B')


#level_engEntry = Entry(addtick,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
#level_engEntry.pack(pady=2)
#level_engEntry.place(x=150,y=200)

levelchoosen.pack(pady=2)
levelchoosen.place(x=150,y=200)
levelchoosen.current()
#levelchoosen.bind("<<comboboxselected>>",addtickengr)


priority_eng = Label(addtick, text="Priority",font='Arial 11',borderwidth=5,padx=25)
priority_eng.pack()
priority_eng.place(x=450,y=200)
#age = StringVar()
#opt2 = ['High','Low']
l = tkinter.StringVar()
prioritychoosen = ttk.Combobox(addtick, width = 27, textvariable=l, state='readonly')
prioritychoosen['values']=('High','Low')
#priority_engEntry = Entry(addtick,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
prioritychoosen.pack(pady=2)
prioritychoosen.place(x=580,y=200)
prioritychoosen.current()
#prioritychoosen.bind("<<comboboxselected>>",addtickengr)



des_eng = Label(addtick, text="Description",font='Arial 11',borderwidth=5,padx=8)
des_eng.pack()
des_eng.place(x=20,y=300)
#age = StringVar()
des_engEntry = Entry(addtick,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
des_engEntry.pack(pady=2)
des_engEntry.place(x=150,y=300)


t_idEntry.focus_set()
ADDbutton = Button(addtick, text="ADD",font='Arial 20', command=addtickengr, padx=20,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
ADDbutton.pack(pady=2)
ADDbutton.place(x=50,y=400)

backButton2 = Button(addtick, text="Back",font='Arial 20', command= back1, padx=30, fg='blue', borderwidth=5) 
backButton2.pack(pady=2)
backButton2.place(x=550,y=400)










##########################################################################################################
def resetEngineerTree(cursorTemp):
    #reseting engview in view technicians
    cursorTemp.execute("SELECT DISTINCT f_name,l_name,age,e_id,username,start_date,proj_name from Employee join Engineer on e_id=engr_id")
    engineers = cursorTemp.fetchall()
    for i in eTree.get_children():
        eTree.delete(i)
    for engineer in engineers:
        eTree.insert('',END,value=(engineer[0],engineer[1],engineer[2],engineer[3],engineer[4],engineer[5],engineer[6]),tags=('row',))
    logging.info('Engineer view tree updated')

def resetTechTree(cursorTemp):
    #reseting treeview in view technicians
    cursorTemp.execute("select F_name,L_name,age,e_id,username,start_date from Employee join Technician on e_id=tech_id")
    technicians = cursorTemp.fetchall()
    #nestedQ1 = "select count(t_id) from Technician as c left join Ticket as d on c.tech_id=d.tech_id where c.tech_id=a.techA_id group by c.tech_id"
    cursorTemp.execute("select a.techA_id,(select count(t_id) from Technician as c left join Ticket as d on c.tech_id=d.tech_id where c.tech_id=a.techA_id group by c.tech_id) from Level_A_Technician as a left join Level_A_Ticket as b on a.techA_id=b.techA_id group by a.techA_id")
    aTechs = cursorTemp.fetchall()
    cursorTemp.execute("select a.techB_id,(select count(t_id) from Technician as c left join Ticket as d on c.tech_id=d.tech_id where c.tech_id=a.techB_id group by c.tech_id) from Level_B_Technician as a left join Level_B_Ticket as b on a.techB_id=b.techB_id group by a.techB_id")
    bTechs = cursorTemp.fetchall()
    aTechIds = [(id[0]) for id in aTechs]
    bTechIds = [(id[0]) for id in bTechs]
    
    for i in techT.get_children():
        techT.delete(i)
    for tech in technicians:
        if tech[3] in aTechIds: 
            for id in aTechs:
                if(id[0]==tech[3]):
                    idA = id[1]
            techT.insert('',END,value=(tech[0],tech[1],tech[2],tech[3],tech[4],tech[5],'A',idA),tags=('row',))
            
        elif tech[3] in bTechIds:
            for id in bTechs:
                if(id[0]==tech[3]):
                    idB = id[1]
            techT.insert('',END,value=(tech[0],tech[1],tech[2],tech[3],tech[4],tech[5],'B',idB),tags=('row',))
    logging.info('Technician view tree updated')

def resetDbaTree(cursorTemp):
    cursorTemp.execute("select F_name,L_name,age,e_id,username,start_date from Employee join Database_Administrator on e_id=dba_id")
    dbas = cursor.fetchall()
    for i in dTree.get_children():
        dTree.delete(i)
    
    for dba in dbas:
        dTree.insert('',END,value=(dba[0],dba[1],dba[2],dba[3],dba[4],dba[5]),tags=('row',))
    logging.info('DBA view tree updated')

def resetTickTree(cursorTemp):
    cursorTemp.execute("SELECT DISTINCT t_id,status,level,priority,description,engr_id,tech_id,submitted_on from Ticket")
    tickets = cursorTemp.fetchall()
    for i in tTree.get_children():
        tTree.delete(i)
    
    for ticket in tickets:
        tTree.insert('',END,value=(ticket[0],ticket[1],ticket[2],ticket[3],ticket[4],ticket[5],ticket[6],ticket[7]))
    logging.info('Ticket view tree updated')
    
   

def resetProjTree(cursorTemp):
    cursorTemp.execute("SELECT DISTINCT Project.proj_name,Project.description,count(engr_id) as Workers FROM Project left join Engineer on Project.proj_name=Engineer.proj_name group by Project.proj_name,description")
    projects = cursorTemp.fetchall()
    for i in project_tree.get_children():
        project_tree.delete(i)
    
    for project in projects:
        project_tree.insert('',END,value=(project[0],project[1],project[2]))
    logging.info('Project view tree updated')
        
def viewEmployees():
    mang.withdraw()
    mEmp.deiconify()
    db=sqlite3.connect('login.db')
    db.execute("PRAGMA foreign_keys = 1")
    cursor=db.cursor()
    resetTechTree(cursor)
    resetEngineerTree(cursor)
    #dbaTree(cursor)
    resetProjTree(cursor)
    db.commit()
    db.close()

def assignPtoE():
    try:
        db=sqlite3.connect('login.db')
        db.execute("PRAGMA foreign_keys = 1")
        cursor=db.cursor()
        
        cursor.execute("select engr_id,proj_name from engineer where engr_id=?",(engEntry.get(),))
        rowEng = cursor.fetchone()
     
    except ValueError as v:
        messagebox.showerror('Error','Please check data you have entered')
    except Exception as u:
        messagebox.showerror('Error', 'Enter all Details')
        engEntry.delete(0,END)
        projEntry.delete(0,END)
        projEntry.focus()
        
    else:
        if rowEng is not None:
            if rowEng[1] is None:
                try:
                    cursor.execute("Update engineer set proj_name=? where engr_id=?",(projEntry.get(),engEntry.get()))
                except ValueError as v:
                    messagebox.showerror('Error','Please check data you have entered')
                    logging.error('Project {} not assigned to Engineer with ID of {} (Invalid data)'.format(projEntry.get(),engEntry.get()))
                except sqlite3.DatabaseError as e:
                    db.rollback()
                    messagebox.showerror("Failure ",'Project might not exist')
                    logging.error('Project {} not assigned to Engineer with ID of {} (Invalid Project)'.format(projEntry.get(),engEntry.get()))
                except Exception as u:
                    messagebox.showerror('Error', 'Enter all Details')
                    logging.error('Project {} not assigned to Engineer with ID of {} (Missing details)'.format(projEntry.get(),engEntry.get()))
                    engEntry.delete(0,END)
                    projEntry.delete(0,END)
                    projEntry.focus()
                else:
                    messagebox.showinfo('info','Chosen Engineer assigned project')
                    cursor.execute("SELECT DISTINCT Project.proj_name,Project.description,count(engr_id) as Workers FROM Project left join Engineer on Project.proj_name=Engineer.proj_name group by Project.proj_name,description")
                    result = cursor.fetchall()
                    
                    for i in project_tree.get_children():
                        project_tree.delete(i)
                    for i in result:
                        project_tree.insert('',END,value=(i[0],i[1],i[2]))
                    logging.info('Project {} assigned to Engineer with ID of {}'.format(projEntry.get(),engEntry.get()))
                    resetEngineerTree(cursor)

            else:
                messagebox.showerror('error','Chosen Engineer is already working on a project')
                logging.error('Project {} not assigned to Engineer with ID of {} (Engineer can only work on one project)'.format(projEntry.get(),engEntry.get()))
        else:
            messagebox.showerror('Error','Chosen Engineer might not exist')
            logging.error('Project {} not assigned to Engineer with ID of {} (Engineer does not exist)'.format(projEntry.get(),engEntry.get()))
  
        db.commit()
        engEntry.delete(0,END)
        projEntry.delete(0,END)
        projEntry.focus() 
        if db is not None:
            db.close()
                 
def backProj():
    mProj.withdraw()
    mang.deiconify()

def mangProjects():
    #manager projects window
    mang.withdraw()
    mProj.deiconify()
    db=sqlite3.connect('login.db')
    db.execute("PRAGMA foreign_keys = 1")
    cursor=db.cursor()
    resetProjTree(cursor)
    db.commit()
    db.close()
    
def mangTickets():
    mang.withdraw()
    mTick.deiconify()
    db=sqlite3.connect('login.db')
    db.execute("PRAGMA foreign_keys = 1")
    cursor=db.cursor()
    resetTickTree(cursor)
    db.commit()
    db.close()
    
def backTickets():
    mTick.withdraw()
    mang.deiconify()
    
def checkTechLevel(cursor,id):
    level = ''
    try:
        cursor.execute("select * from Technician where tech_id=? ",(id,))
        tech = cursor.fetchone()
    except ValueError as v:
        messagebox.showerror('Error','Please check data you have entered')
    except Exception as u:
        messagebox.showerror('Error', 'Enter all Details')
        tickEntry.delete(0,END)
        techEntry.delete(0,END)
        tickEntry.focus()
    else:
        if tech is not None:
            cursor.execute("select * from Level_A_Technician")
            aTechs = cursor.fetchall()
            aTechIds = [techs[0] for techs in aTechs]
    
            if (int(id) in aTechIds):
                level = 'A'
            else: 
                level = 'B'
        
        return level
    
def assignTicktoTech():
    try:
        db=sqlite3.connect('login.db')
        db.execute("PRAGMA foreign_keys = 1")
        cursor=db.cursor()
        #techEntry
        #tickEntry
        
        cursor.execute("select * from Ticket where t_id=? ",(tickEntry.get(),))
        ticks = cursor.fetchone()
        
            
    except ValueError as v:
        messagebox.showerror('Error','Please check data you have entered')
        logging.error('Ticket {} failed to be assigned to technician'.format(tickEntry.get(),))
    except Exception as u:
        messagebox.showerror('Error', 'Enter all Details')
        tickEntry.delete(0,END)
        techEntry.delete(0,END)
        tickEntry.focus()
    else:
        if ticks is not None:
            lev=ticks[2]
            if ticks[7] is None:
                levelOfTechnician = checkTechLevel(cursor,techEntry.get())
                if levelOfTechnician=='':
                    messagebox.showerror('Error','Technician might not exist')
                    logging.error('Ticket {} failed to be assigned to technician (Tech does not exist)'.format(tickEntry.get(),))
                elif levelOfTechnician != lev:
                    messagebox.showerror('Error','Ticket level does not match Technician Level')
                    logging.error('Ticket {} failed to be assigned to technician (Mismatching levels)'.format(tickEntry.get(),))
                else: 
                    try:
                        if lev == 'A':
                            cursor.execute("Update Level_A_Ticket set techA_id=? where ticketA_id=?",(techEntry.get(),tickEntry.get()))
                        else:
                            cursor.execute("Update Level_B_Ticket set techB_id=? where ticketB_id=?",(techEntry.get(),tickEntry.get()))
                        cursor.execute("Update Ticket set tech_id=? where t_id=?",(techEntry.get(),tickEntry.get()))
                    except sqlite3.DatabaseError as e:
                        db.rollback()
                        messagebox.showerror("Failure ",e) 
                        logging.error('Ticket {} failed to be assigned to technician (DB Error)'.format(tickEntry.get(),))
                    else:
                        messagebox.showinfo("info","Technician assigned ticket")  
                        logging.info('Ticket {} assigned to Technician {}'.format(tickEntry.get(),techEntry.get()))
                        cursor.execute("SELECT DISTINCT t_id,status,level,priority,description,engr_id,tech_id,submitted_on from Ticket")
                        results = cursor.fetchall()
                        for i in tTree.get_children():
                            tTree.delete(i)
                        for i in results:
                            tTree.insert('',END,value=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                            
                        resetTechTree(cursor)
   
            else:
                messagebox.showerror('Error','Chosen Ticket is being worked on')
                logging.error('Ticket {} failed to be assigned to technician (Ticket already being worked on)'.format(tickEntry.get(),))
                
        else:
            messagebox.showerror('Error','Chosen ticket might not exist')
            logging.error('Ticket {} failed to be assigned to technician (Ticket does not exist)'.format(tickEntry.get(),))
  
        db.commit()
        techEntry.delete(0,END)
        tickEntry.delete(0,END)
        tickEntry.focus() 
        if db is not None:
            db.close()
    
def ticketTree():
    #frame around tree
    tree_frame = Frame(mTick)
    tree_frame.pack(pady=10)
    #creating tree and column
    ticket_tree = ttk.Treeview(tree_frame,columns=("tid","status","level","prio","desc","engr_id","tech_id","submitted"),show='headings',selectmode="browse")
    ticket_tree.column("tid",anchor=CENTER,width=111)
    ticket_tree.column("status",anchor=CENTER,width=111)
    ticket_tree.column("level",anchor=CENTER,width=111)
    ticket_tree.column("prio",anchor=CENTER,width=111)
    ticket_tree.column("desc",anchor=CENTER,width=111)
    ticket_tree.column("engr_id",anchor=CENTER,width=111)
    ticket_tree.column("tech_id",anchor=CENTER,width=111)
    ticket_tree.column("submitted",anchor=CENTER,width=111)
    ticket_tree.pack()
    #style of tree
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",background="#D3D3D3",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
    style.map('Treeview',background=[('selected', "#347083")])
    #headers
    ticket_tree.heading("tid",text="Ticket ID",anchor=CENTER)
    ticket_tree.heading("status",text="Status",anchor=CENTER)
    ticket_tree.heading("level",text="Level",anchor=CENTER)
    ticket_tree.heading("prio",text="Priority",anchor=CENTER)
    ticket_tree.heading("desc",text="Description",anchor=CENTER)
    ticket_tree.heading("engr_id",text="Created by:Engr ID",anchor=CENTER)
    ticket_tree.heading("tech_id",text="Worked on by:Tech ID",anchor=CENTER)
    ticket_tree.heading("submitted",text="Date of Creation",anchor=CENTER)
    #insertion from db to tree
    db=sqlite3.connect('login.db')
    cursor=db.cursor()
    cursor.execute("SELECT DISTINCT t_id,status,level,priority,description,engr_id,tech_id,submitted_on from Ticket")
    tickets = cursor.fetchall()
    count = 0
    for ticket in tickets:
        ticket_tree.insert('',END,value=(ticket[0],ticket[1],ticket[2],ticket[3],ticket[4],ticket[5],ticket[6],ticket[7]))
        count+=1
    db.commit()
    db.close()
    #tree scroll config
    ticket_tree.grid(row=100,column=0,columnspan=100,sticky='nsew')
    scroll = ttk.Scrollbar(mEmp, orient=VERTICAL, command=ticket_tree.yview)
    ticket_tree.configure(yscroll=scroll.set)
    scroll.grid(row=0, column=1, sticky='ns')
    
    #buttons, assigning ticket to technician using id
    #Assign button
    assignButton = Button(mTick, text="Assign",font='Arial 20', command= assignTicktoTech ,padx=20,fg='blue',borderwidth=5)  
    assignButton.pack(pady=2)
    assignButton.place(x=600,y=300)
    
    #back button
    tickBack = Button(mTick, text="Back",font='Arial 20', command= backTickets,padx=20,fg='blue',borderwidth=5) 
    tickBack.pack()
    tickBack.place(x=600,y=400)
    
    return ticket_tree
    
    
    
def backEng():
    mvEng.withdraw()
    mEmp.deiconify()
    
def backViewEmp():
    mEmp.withdraw()
    mang.deiconify()
    
def viewEngs():
    mEmp.withdraw()
    mvEng.deiconify()
    
def engTree():
    #frame around tree
    tree_frame = Frame(mvEng)
    tree_frame.pack(pady=20)
    #creating tree and column
    engineer_tree = ttk.Treeview(tree_frame,columns=("fname","lname","age","id","username","start_date","proj"),show='headings',selectmode="browse",height=10)
    engineer_tree.column("fname",anchor=CENTER,width=126)
    engineer_tree.column("lname",anchor=CENTER,width=126)
    engineer_tree.column("age",anchor=CENTER,width=126)
    engineer_tree.column("id",anchor=CENTER,width=126)
    engineer_tree.column("username",anchor=CENTER,width=126)
    engineer_tree.column("start_date",anchor=CENTER,width=126)
    engineer_tree.column("proj",anchor=CENTER,width=126)
    engineer_tree.pack(side=LEFT)
    #style of tree
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3")
    style.map('Treeview',background=[('selected', "#347083")])
    #headers
    engineer_tree.heading("fname",text="First Name",anchor=CENTER)
    engineer_tree.heading("lname",text="Last Name",anchor=CENTER)
    engineer_tree.heading("age",text="Age",anchor=CENTER)
    engineer_tree.heading("id",text="ID",anchor=CENTER)
    engineer_tree.heading("username",text="Username",anchor=CENTER)
    engineer_tree.heading("start_date",text="Started on",anchor=CENTER)
    engineer_tree.heading("proj",text="Works on Project",anchor=CENTER)
    
    engineer_tree.tag_configure('row', background="white")
    sb = Scrollbar(tree_frame,orient=VERTICAL)
    sb.pack(side=RIGHT,fill=Y)
    engineer_tree.config(yscrollcommand=sb.set)
    ttk.Treeview(tree_frame).pack(expand=True,fill='y')
    
    #insertion from db to tree
    db=sqlite3.connect('login.db')
    db.execute("PRAGMA foreign_keys = 1")
    cursor=db.cursor()
    cursor.execute("SELECT DISTINCT f_name,l_name,age,e_id,username,start_date,proj_name from Employee join Engineer on e_id=engr_id")
    engineers = cursor.fetchall()
    count = 0
    for engineer in engineers:
        engineer_tree.insert('',END,value=(engineer[0],engineer[1],engineer[2],engineer[3],engineer[4],engineer[5],engineer[6]),tags=('row',))
        count+=1
    db.commit()
    db.close()
    
    #back button
    pBack = Button(mvEng, text="Back",font='Arial 20', command= backEng,padx=20,fg='blue',borderwidth=5) 
    pBack.pack()
    #pBack.place(x=350,y=400)
    return engineer_tree

    
def viewTechs():
    mEmp.withdraw()
    mvTech.deiconify()
    
def backTech():
    mvTech.withdraw()
    mEmp.deiconify()

def techTree():
    #frame around tree
    tree_frame = Frame(mvTech)
    tree_frame.pack(pady=20)
    #creating tree and column
    tech_tree = ttk.Treeview(tree_frame,columns=("fname","lname","age","id","username","start_date","level","tickets_amt"),show='headings',selectmode="browse",height=10)
    tech_tree.column("fname",anchor=CENTER,width=111)
    tech_tree.column("lname",anchor=CENTER,width=111)
    tech_tree.column("age",anchor=CENTER,width=111)
    tech_tree.column("id",anchor=CENTER,width=111)
    tech_tree.column("username",anchor=CENTER,width=111)
    tech_tree.column("start_date",anchor=CENTER,width=111)
    tech_tree.column("level",anchor=CENTER,width=111)
    tech_tree.column("tickets_amt",anchor=CENTER,width=111)
    tech_tree.pack(side=LEFT)
    #style of tree
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3")
    style.map('Treeview',background=[('selected', "#347083")])
    #headers
    tech_tree.heading("fname",text="First Name",anchor=CENTER)
    tech_tree.heading("lname",text="Last Name",anchor=CENTER)
    tech_tree.heading("age",text="Age",anchor=CENTER)
    tech_tree.heading("id",text="ID",anchor=CENTER)
    tech_tree.heading("username",text="Username",anchor=CENTER)
    tech_tree.heading("start_date",text="Started on",anchor=CENTER)
    tech_tree.heading("level",text="Level",anchor=CENTER)
    tech_tree.heading("tickets_amt",text="Num of tickets",anchor=CENTER)
    
    tech_tree.tag_configure('row', background="white")
    sb = Scrollbar(tree_frame,orient=VERTICAL)
    sb.pack(side=RIGHT,fill=Y)
    tech_tree.config(yscrollcommand=sb.set)
    ttk.Treeview(tree_frame).pack(expand=True,fill='y')
    
    #insertion from db to tree
    db=sqlite3.connect('login.db')
    db.execute("PRAGMA foreign_keys = 1")
    cursor=db.cursor()
    cursor.execute("select F_name,L_name,age,e_id,username,start_date from Employee join Technician on e_id=tech_id")
    technicians = cursor.fetchall()
   
    cursor.execute("select a.techA_id,(select count(t_id) from Technician as c left join Ticket as d on c.tech_id=d.tech_id where c.tech_id=a.techA_id group by c.tech_id) from Level_A_Technician as a left join Level_A_Ticket as b on a.techA_id=b.techA_id group by a.techA_id")
    aTechs = cursor.fetchall()
    cursor.execute("select a.techB_id,(select count(t_id) from Technician as c left join Ticket as d on c.tech_id=d.tech_id where c.tech_id=a.techB_id group by c.tech_id) from Level_B_Technician as a left join Level_B_Ticket as b on a.techB_id=b.techB_id group by a.techB_id")
    bTechs = cursor.fetchall()
    
    aTechIds = [(id[0]) for id in aTechs]
    bTechIds = [(id[0]) for id in bTechs]
    
    for tech in technicians:
        if tech[3] in aTechIds: 
            for id in aTechs:
                if(id[0]==tech[3]):
                    idA = id[1]
            tech_tree.insert('',END,value=(tech[0],tech[1],tech[2],tech[3],tech[4],tech[5],'A',idA),tags=('row',))
            
        elif tech[3] in bTechIds:
            for id in bTechs:
                if(id[0]==tech[3]):
                    idB = id[1]
            tech_tree.insert('',END,value=(tech[0],tech[1],tech[2],tech[3],tech[4],tech[5],'B',idB),tags=('row',))
        
    db.commit()
    db.close()
    
    #back button
    pBack = Button(mvTech, text="Back",font='Arial 20', command= backTech,padx=20,fg='blue',borderwidth=5) 
    pBack.pack()
    #pBack.place(x=350,y=400
    
    return tech_tree

def viewDBAs():
    mEmp.withdraw()
    mvDBA.deiconify()

def backDBA():
    mvDBA.withdraw()
    mEmp.deiconify()

def dbaTree():
    #frame around tree
    tree_frame = Frame(mvDBA)
    tree_frame.pack(pady=20)
    #creating tree and column
    dba_tree = ttk.Treeview(tree_frame,columns=("fname","lname","age","id","username","start_date"),show='headings',selectmode="browse",height=10)
    dba_tree.column("fname",anchor=CENTER,width=148)
    dba_tree.column("lname",anchor=CENTER,width=148)
    dba_tree.column("age",anchor=CENTER,width=148)
    dba_tree.column("id",anchor=CENTER,width=148)
    dba_tree.column("username",anchor=CENTER,width=148)
    dba_tree.column("start_date",anchor=CENTER,width=148)
    
    dba_tree.pack(side=LEFT)
    #style of tree
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",background="#D3D3D3",foreground="black",fieldbackground="#D3D3D3")
    style.map('Treeview',background=[('selected', "#347083")])
    #headers
    dba_tree.heading("fname",text="First Name",anchor=CENTER)
    dba_tree.heading("lname",text="Last Name",anchor=CENTER)
    dba_tree.heading("age",text="Age",anchor=CENTER)
    dba_tree.heading("id",text="ID",anchor=CENTER)
    dba_tree.heading("username",text="Username",anchor=CENTER)
    dba_tree.heading("start_date",text="Started on",anchor=CENTER)
    
    
    dba_tree.tag_configure('row', background="white")
    sb = Scrollbar(tree_frame,orient=VERTICAL)
    sb.pack(side=RIGHT,fill=Y)
    dba_tree.config(yscrollcommand=sb.set)
    ttk.Treeview(tree_frame).pack(expand=True,fill='y')
    
    #insertion from db to tree
    db=sqlite3.connect('login.db')
    db.execute("PRAGMA foreign_keys = 1")
    cursor=db.cursor()
    cursor.execute("select F_name,L_name,age,e_id,username,start_date from Employee join Database_Administrator on e_id=dba_id")
    dbas = cursor.fetchall()
    
    for dba in dbas:
        dba_tree.insert('',END,value=(dba[0],dba[1],dba[2],dba[3],dba[4],dba[5]),tags=('row',))
        
    db.commit()
    db.close()
    
    #back button
    pBack = Button(mvDBA, text="Back",font='Arial 20', command= backDBA,padx=20,fg='blue',borderwidth=5) 
    pBack.pack()
    #pBack.place(x=350,y=400
    
    return dba_tree


#Managerwindow
mang= Toplevel(root)
mang.title("Manager")
mang.geometry("888x500")
mang.withdraw()
my_img100= ImageTk.PhotoImage(Image.open("pqr.jpeg"))
my_label100=Label(mang,image=my_img100)
my_label100.pack()
my_label100.place(x=0,y=0)

#Manager buttons
#view employee info button
mangButton1 = Button(mang, text="View Employee Info", command=viewEmployees,font='Arial 20',padx=20,fg='blue',borderwidth=5) 
mangButton1.pack(pady=2)
mangButton1.place(x=350,y=100)
#employee view page
mEmp = Toplevel(mang)
mEmp.title("View all employees")
mEmp.geometry("888x500")
mEmp.withdraw()
my_img101= ImageTk.PhotoImage(Image.open("lmn.jpeg"))
my_label101=Label(mEmp,image=my_img101)
my_label101.pack()
my_label101.place(x=0,y=0)

#buttons on employee view page
#view engineers
viewEmpButton1 = Button(mEmp, text="View Engineers Info", command=viewEngs,font='Arial 20',padx=20,fg='blue',borderwidth=5) 
viewEmpButton1.pack(pady=2)
viewEmpButton1.place(x=350,y=100)
#engineer view page
mvEng = Toplevel(mEmp)
mvEng.title("View all Engineers")
mvEng.geometry("888x500")
mvEng.withdraw()
eTree=engTree()

#view technicians
viewEmpButton2 = Button(mEmp, text="View Technicians Info", command=viewTechs,font='Arial 20',padx=20,fg='blue',borderwidth=5) 
viewEmpButton2.pack(pady=2)
viewEmpButton2.place(x=350,y=200)
#technician view page
mvTech = Toplevel(mEmp)
mvTech.title("View all Technicians")
mvTech.geometry("888x500")
mvTech.withdraw()
techT = techTree()


#view DBAs
viewEmpButton3 = Button(mEmp, text="View DBAs Info", command=viewDBAs,font='Arial 20',padx=20,fg='blue',borderwidth=5) 
viewEmpButton3.pack(pady=2)
viewEmpButton3.place(x=350,y=300)
#DBA view page
mvDBA = Toplevel(mEmp)
mvDBA.title("View all DBAs")
mvDBA.geometry("888x500")
mvDBA.withdraw()
dTree = dbaTree()

#back button
viewBack = Button(mEmp, text="Back",font='Arial 20', command= backViewEmp,padx=20,fg='blue',borderwidth=5) 
viewBack.pack(pady=2)
viewBack.place(x=350,y=400)



#assign/view projects button
mangButton2 = Button(mang, text="Assign/view projects", command=mangProjects,font='Arial 20',padx=20,fg='blue',borderwidth=5) 
mangButton2.pack(pady=2)
mangButton2.place(x=350,y=200)
#proj page
mProj = Toplevel(mang)
mProj.title("Assign/view projects")
mProj.geometry("888x500")
mProj.withdraw()

#frame around tree
tree_frame = Frame(mProj)
tree_frame.pack(pady=10)
#creating tree and column
project_tree = ttk.Treeview(tree_frame,columns=("pname","desc","workers"),show='headings',selectmode="browse")
project_tree.column("pname",anchor=CENTER,width=296)
project_tree.column("desc",anchor=CENTER,width=296)
project_tree.column("workers",anchor=CENTER,width=296)
project_tree.pack()
#style of tree
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",background="#D3D3D3",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
style.map('Treeview',background=[('selected', "#347083")])
#headers
project_tree.heading("pname",text="Project Names",anchor=CENTER)
project_tree.heading("desc",text="Description",anchor=CENTER)
project_tree.heading("workers",text="Num of Workers",anchor=CENTER)
#insertion from db to tree
db=sqlite3.connect('login.db')
cursor=db.cursor()
cursor.execute("SELECT DISTINCT Project.proj_name,Project.description,count(engr_id) as Workers FROM Project left join Engineer on Project.proj_name=Engineer.proj_name group by Project.proj_name,description")
projects = cursor.fetchall()
count = 0
for project in projects:
    project_tree.insert('',END,value=(project[0],project[1],project[2]))
    count+=1
db.commit()
db.close()
#tree scroll config
project_tree.grid(row=100,column=0,columnspan=100,sticky='nsew')
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=project_tree.yview)
project_tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

#buttons, assigning project to eng using id, 
#project entry
assignProj = Label(mProj, text="Project ",font='Arial 20',borderwidth=5,padx=20)
assignProj.pack()
assignProj.place(x=0,y=300)
chosenProj = StringVar()
projEntry = Entry(mProj, textvariable=chosenProj,font='Arial 20',borderwidth=3)  
projEntry.pack(pady=2)
projEntry.place(x=200,y=300)
#engineer entry
assignEng = Label(mProj, text="Engineer ID",font='Arial 20',borderwidth=5,padx=20)
assignEng.pack()
assignEng.place(x=0,y=350)
engEntry = Entry(mProj,font='Arial 20',borderwidth=3)  
engEntry.pack(pady=2)
engEntry.place(x=200,y=350)
engEntry.delete(0,END)
projEntry.delete(0,END)
projEntry.focus()  
assignButton = Button(mProj, text="Assign",font='Arial 20', command= assignPtoE ,padx=20,fg='blue',borderwidth=5)  
assignButton.pack(pady=2)
assignButton.place(x=600,y=300)
#back button
pBack = Button(mProj, text="Back",font='Arial 20', command= backProj,padx=20,fg='blue',borderwidth=5) 
pBack.pack(pady=2)
pBack.place(x=600,y=400)



#assign/view tickets
mangButton3 = Button(mang, text="Assign/view tickets", command=mangTickets,font='Arial 20',padx=20,fg='blue',borderwidth=5) 
mangButton3.pack(pady=2)
mangButton3.place(x=350,y=300)
#tickets page
mTick = Toplevel(mang)
mTick.title("Assign/view tickets")
mTick.geometry("888x500")
mTick.withdraw()
tTree = ticketTree()
#Ticket entry
assignTick = Label(mTick, text="Ticket ID",font='Arial 20',borderwidth=5,padx=20)
assignTick.pack()
assignTick.place(x=0,y=300)
chosenTick = StringVar()
tickEntry = Entry(mTick, textvariable=chosenTick,font='Arial 20',borderwidth=3)  
tickEntry.pack(pady=2)
tickEntry.place(x=200,y=300)
#Technician entry
assignTech = Label(mTick, text="Technician ID",font='Arial 20',borderwidth=5,padx=20)
assignTech.pack()
assignTech.place(x=0,y=350)
techEntry = Entry(mTick,font='Arial 20',borderwidth=3)  
techEntry.pack(pady=2)
techEntry.place(x=200,y=350)


#back
mangButton100 = Button(mang, text="Log Out",font='Arial 20', command= back ,padx=80,fg='blue',borderwidth=5)  
mangButton100.pack(pady=2)
mangButton100.place(x=350,y=400)

##########################################################################################################

#-------------VIVEK CODE------------------------------------------------
def backdba():
    reg.withdraw()
    dba.withdraw()
    # dba.destroy()
    root.deiconify()
    usernameEntry.focus_set()
    fnEntry.focus_set()

def backdba1():
    viewemployee.withdraw()
    dba.deiconify()

def backdba2():
    removeemployee.withdraw()
    dba.deiconify()

def go_to_remove_gui():
    removeemployee.deiconify()
    dba.withdraw()
def remove_emp():
    # messagebox.showinfo('info',"hello")
    db = None

    try:
        db = sqlite3.connect('login.db')
        db.execute("PRAGMA foreign_keys = 1")
        cursor = db.cursor()
        # cursor = db.cursor()
        # all1 = 'select e_id from employee'
        # cursor.execute(all1)

        cursor.execute("select e_id from employee")
        eid_list = cursor.fetchall()
        e_id = int(idEntry.get())
        e_id_flag=True
        #print(e_id)
        if (e_id,) not in eid_list:
            # winsound.Beep(200,1000)
            # e_idEntry.delete(0, END)
            messagebox.showerror('Error','Please enter valid e_id')
            logging.error('Employee with ID {} failed to be deleted'.format(e_id,))
            idEntry.delete(0, END)
            idEntry.focus()
            e_id_flag=False
        else:
            e_id_flag=True

        if e_id_flag:
            cursor.execute('Delete from employee where e_id=?',(e_id,))
            db.commit()
    
            messagebox.showinfo("success","record deleted")
            logging.error('Employee with ID {} deleted from database'.format(e_id,))
            

    except ValueError as v:
        # messagebox.showerror('Error', 'Please enter e_id as Integer, fname and lname as Character and age as Integer')
        idEntry.delete(0, END)
        idEntry.focus()

    except sqlite3.DatabaseError as e:
        db.rollback()
        messagebox.showerror("Failure ", e)
        logging.error('Employee with ID {} failed to be deleted'.format(e_id,))
        idEntry.delete(0, END)
        idEntry.focus()
        if db is not None:
            db.rollback()

    except Exception as u:
        messagebox.showerror('Error', 'Enter All Details')
        logging.error('Employee with ID {} failed to be deleted'.format(e_id,))
        idEntry.delete(0, END)
        idEntry.focus()

        if db is not None:
            db.close()

def show_all_employee():
    viewemployee.deiconify()
    dba.withdraw()
    # x=usernameEntry.get()

    db = None

    try:
        employeedata.delete(1.0, END)
        db = sqlite3.connect('login.db')
        db.execute("PRAGMA foreign_keys = 1")
        cursor = db.cursor()
        # global x
        cursor.execute(
            "select * from employee",
            )
        data = cursor.fetchall()
        msg = ''
        for d in data:
            msg = msg + "\t f_name: " + d[0] + "\t\t l_name: " + d[1] + "\t\t age: " + str(d
                                                                                           [2]) + "\t\t username: " + \
                  d[4] + "\t\t e_id: " + str(d[3]) + "\t\t d_no: " + str(d[6]) + "\t\t d_name: " + d[7] + '\n' + ('*' * 140) + '\n'
        employeedata.insert(INSERT, msg)

    except sqlite3.DatabaseError as e:
        messagebox.showerror("issue : ", e)
    except Exception as e :
        print("Exception", e)
    finally :
        if db is not None:
            db.close()

        def show_all_employee():
            viewemployee.deiconify()
            dba.withdraw()
            # x=usernameEntry.get()

            db = None

            try:
                employeedata.delete(1.0, END)
                db = sqlite3.connect('login.db')
                cursor = db.cursor()
                global x
                cursor.execute(
                    "select * from employee",
                    (x,))
                data = cursor.fetchall()
                msg = ''
                for d in data:
                    msg = msg + "\t f_name: " + d[0] + "\t\t l_name: " + d[1] + "\t\t age: " + str(
                        d[2]) + "\t\t username: " + \
                          d[4] + "\t\t e_id: " + str(d[3]) + "\t\t d_no: " + str(d[6]) + "\t\t d_name: " + d[
                              7] + '\n' + ('*' * 140) + '\n'
                stdata.insert(INSERT, msg)

            except sqlite3.DatabaseError as e:
                messagebox.showerror("issue : ", e)
            except Exception as e:
                print("Exception", e)
            finally:
                if db is not None:
                    db.close()

                def show_all_employee():
                    viewemployee.deiconify()
                    dba.withdraw()
                    # x=usernameEntry.get()

                    db = None

                    try:
                        employeedata.delete(1.0, END)
                        db = sqlite3.connect('login.db')
                        cursor = db.cursor()
                        global x
                        cursor.execute(
                            "select * from employee",
                            (x,))
                        data = cursor.fetchall()
                        msg = ''
                        for d in data:
                            msg = msg + "\t f_name: " + d[0] + "\t\t l_name: " + d[1] + "\t\t age: " + str(
                                d[2]) + "\t\t username: " + \
                                  d[4] + "\t\t e_id: " + str(d[3]) + "\t\t d_no: " + str(d[6]) + "\t\t d_name: " + d[
                                      7] + '\n' + ('*' * 140) + '\n'
                        employeedata.insert(INSERT, msg)

                    except sqlite3.DatabaseError as e:
                        messagebox.showerror("issue : ", e)
                    except Exception as e:
                        print("Exception", e)
                    finally:
                        if db is not None:
                            db.close()

                        def show_all_employee():
                            viewemployee.deiconify()
                            dba.withdraw()
                            # x=usernameEntry.get()

                            db = None

                            try:
                                employeedata.delete(1.0, END)
                                db = sqlite3.connect('login.db')
                                cursor = db.cursor()
                                global x
                                cursor.execute(
                                    "select t_id, status, level, priority, description, e_id from employee as x, Engineer as y, Ticket as z  where y.engr_id=x.e_id and z.engr_id=y.engr_id and x.username = ?",
                                    (x,))
                                data = cursor.fetchall()
                                msg = ''
                                for d in data:
                                    msg = msg + "\t t_id: " + str(d[0]) + "\t\t status: " + d[1] + "\t\t level: " + d[
                                        2] + "\t\t priority: " + d[3] + "\t\t description: " + d[
                                              4] + "\t\t engr_id: " + str(
                                        d[5]) + '\n' + ('*' * 140) + '\n'
                                employeedata.insert(INSERT, msg)

                            except sqlite3.DatabaseError as e:
                                messagebox.showerror("issue : ", e)
                            except Exception as e:
                                print("Exception", e)
                            finally:
                                if db is not None:
                                    db.close()

    # try:
    #     stdata.delete(1.0,

#dbawindow
dba= Toplevel(root)
dba.title("DataBaseAdministrator")
dba.geometry("888x500")
dba.withdraw()

my_imgdba= ImageTk.PhotoImage(Image.open("pqr.jpeg"))
my_labeldba=Label(dba,image=my_img2)
my_labeldba.pack()
my_labeldba.place(x=0,y=0)

#inside view button on dba
viewemployee = Toplevel(dba)
viewemployee.title("DataBaseAdmin")
viewemployee.geometry("888x500")
viewemployee.withdraw()

viewemployees = Button(dba, text="VIEW EMPLOYEES",font='Arial 20', command=show_all_employee ,padx=20,fg='blue',borderwidth=5)
#loginButton.grid(row=4, column=0)
viewemployees.pack(pady=2)
viewemployees.place(x=350,y=130)

'''dbabutton = Button(dash, text="DataBaseAdmin",font='Arial 20' ,padx=1,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
dbabutton.pack(pady=2)
dbabutton.place(x=350,y=330)'''

backbuttondba = Button(dba, text="Log Out",font='Arial 20', command= backdba ,padx=80,fg='blue',borderwidth=5)
#loginButton.grid(row=4, column=0)
backbuttondba.pack(pady=2)
backbuttondba.place(x=350,y=430)

my_imgdba1= ImageTk.PhotoImage(Image.open("abcd.png"))
my_labeldba1=Label(viewemployee,image=my_imgdba1)
my_labeldba1.pack()
my_labeldba1.place(x=0,y=0)

employeedata = scrolledtext.ScrolledText(viewemployee, height = 25, width = 120, font = "TkDefaultFont")
employeedata.pack(pady=2)
employeedata.place(x=20,y=20)

backbuttondba1 = Button(viewemployee, text="Back",font='Arial 20', command= backdba1 ,padx=80,fg='blue',borderwidth=5)
#loginButton.grid(row=4, column=0)
backbuttondba1.pack(pady=2)
backbuttondba1.place(x=350,y=430)

#inside delete on dba ---------------------------------------------------------------------------
removeemployee = Toplevel(dba)
removeemployee.title("DataBaseAdmin")
removeemployee.geometry("888x500")
removeemployee.withdraw()

removeemployees = Button(dba, text="REMOVE EMPLOYEE",font='Arial 20', command=go_to_remove_gui ,padx=20,fg='blue',borderwidth=5)
#loginButton.grid(row=4, column=0)
removeemployees.pack(pady=2)
removeemployees.place(x=340,y=280)

#remove employee page
# rememp = Toplevel(root)
# rememp.title("Remove Employee")
# rememp.geometry("888x500")
# rememp.withdraw()

my_imgrem= ImageTk.PhotoImage(Image.open("xyz.jpg"))
my_labelrem=Label(removeemployee,image=my_imgrem)
my_labelrem.pack()
my_labelrem.place(x=0,y=0)

rem_id = Label(removeemployee, text="Employee ID",font='Arial 11',borderwidth=5,padx=25)
rem_id.pack()
rem_id.place(x=20,y=200)
#age = StringVar()
idEntry = Entry(removeemployee,font='Arial 11',borderwidth=5)
#usernameEntry.grid(row=0, column=1)
idEntry.pack(pady=2)
idEntry.place(x=120,y=200)

#delete button to save to the database
rembutton = Button(removeemployee, text="Remove",font='Arial 20', command= remove_emp ,padx=20,fg='blue',borderwidth=5)
#loginButton.grid(row=4, column=0)
rembutton.pack(pady=2)
rembutton.place(x=50,y=400)

backbuttondba2 = Button(removeemployee, text="Back",font='Arial 20', command= backdba2 ,padx=80,fg='blue',borderwidth=5)
#loginButton.grid(row=4, column=0)
backbuttondba2.pack(pady=2)
backbuttondba2.place(x=350,y=430)

#print(rem_id)
#remove dba ends ----------------------------------------------------------------------------------


# ------------------------VIVEK CODE ENDS-------------------------------------------------------------------------------------------------------------------------

#technician window
tech= Toplevel(root)
tech.title("Technician")
tech.geometry("888x500")
tech.withdraw()


my_img5= ImageTk.PhotoImage(Image.open("a.jpeg"))
my_label5=Label(tech,image=my_img5)
my_label5.pack()
my_label5.place(x=0,y=0)


#Buttons
viewalltickbutton = Button(tech, text="View All Ticket",font='Arial 20', command=viewalltechtick ,padx=60,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
viewalltickbutton.pack(pady=2)
viewalltickbutton.place(x=350,y=10)

viewassigntickbutton = Button(tech, text="View Assigned Ticket",font='Arial 20',command=viewassigntechtick,padx=20,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
viewassigntickbutton.pack(pady=2)
viewassigntickbutton.place(x=350,y=150)

updatemytickbutton = Button(tech, text="Update Ticket",font='Arial 20', command=uptech, padx=65,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
updatemytickbutton.pack(pady=2)
updatemytickbutton.place(x=350,y=290)

backbutton4 = Button(tech, text="Log Out",font='Arial 20', command= back ,padx=100,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
backbutton4.pack(pady=2)
backbutton4.place(x=350,y=430)



#inside viewall button
viettech =Toplevel(tech)
viettech.title("Technician")
viettech.geometry("888x500")
viettech.withdraw()

my_img6= ImageTk.PhotoImage(Image.open("a.jpeg"))
my_label6=Label(viettech,image=my_img6)
my_label6.pack()
my_label6.place(x=0,y=0)


stdata1 = scrolledtext.ScrolledText(viettech, height = 25, width = 120, font = "TkDefaultFont")
stdata1.pack(pady=2)
stdata1.place(x=20,y=20)


backbutton5 = Button(viettech, text="Back",font='Arial 20', command= back3 ,padx=80,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
backbutton5.pack(pady=2)
backbutton5.place(x=350,y=430)

#inside viewassign button
vieassteng=Toplevel(tech)
vieassteng.title("Technician")
vieassteng.geometry("888x500")
vieassteng.withdraw()

my_img7= ImageTk.PhotoImage(Image.open("a.jpeg"))
my_label7=Label(vieassteng,image=my_img7)
my_label7.pack()
my_label7.place(x=0,y=0)

stdata2 = scrolledtext.ScrolledText(vieassteng, height = 25, width = 120, font = "TkDefaultFont")
stdata2.pack(pady=2)
stdata2.place(x=20,y=20)

backbutton6 = Button(vieassteng, text="Back",font='Arial 20', command= back4 ,padx=80,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
backbutton6.pack(pady=2)
backbutton6.place(x=444,y=430)


#inside updatebutton
updatetech=Toplevel(tech)
updatetech.title("Technician")
updatetech.geometry("888x500")
updatetech.withdraw()

my_img8= ImageTk.PhotoImage(Image.open("a.jpeg"))
my_label8=Label(updatetech,image=my_img8)
my_label8.pack()
my_label8.place(x=0,y=0)

tickup = Label(updatetech, text="t_id",font='Arial 11',borderwidth=5,padx=30)
tickup.pack()
tickup.place(x=20,y=100)

tickupEntry = Entry(updatetech,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
tickupEntry.pack(pady=2)
tickupEntry.place(x=150,y=100)

status_tech = Label(updatetech, text="Status",font='Arial 11',borderwidth=5,padx=25)
status_tech.pack()
status_tech.place(x=450,y=100)

w = tkinter.StringVar()
statustechchoosen = ttk.Combobox(updatetech, width = 27, textvariable=w, state='readonly')
statustechchoosen['values']=('Close')
#age = StringVar()
#status_engEntry = Entry(addtick,font='Arial 11',borderwidth=5)  
#usernameEntry.grid(row=0, column=1)
statustechchoosen.pack(pady=2)
statustechchoosen.place(x=580,y=100)
statustechchoosen.current()


upttickbutton= Button(updatetech, text="Update",font='Arial 20' , command=upttick, padx=80,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
upttickbutton.pack(pady=2)
upttickbutton.place(x=100,y=430) 

backbutton7 = Button(updatetech, text="Back",font='Arial 20', command= back5 ,padx=80,fg='blue',borderwidth=5) 
#loginButton.grid(row=4, column=0) 
backbutton7.pack(pady=2)
backbutton7.place(x=444,y=430)   


root.mainloop()