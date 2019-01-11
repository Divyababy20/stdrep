#python program for
#create,update and view reminders
#import tkinter library for gui application
import tkinter as tk
top = tk.Tk()
# import the MySQL connector and other modules
import mysql.connector
from tkinter import*
from tkinter import messagebox
import time
import datetime

num1=StringVar()
rdate=StringVar()
revent=StringVar()
#open a database connection
con=mysql.connector.connect(user="root", password="dbsys", database="reminder", host="localhost", port=3306)
if(con.is_connected()):
	pass
cur = con.cursor()
cur.execute("""CREATE TABLE events(rdate date,revent varchar(40))""")
con.commit()
con.close()
def remdate():
        try:
                i=0
                num1=(datetime.datetime.now().strftime("%Y-%m-%d"))				
                dat=str(num1)
                cur.execute("select revent from events where Date =%(value)s ",{'value': dat})		
                eve = cur.fetchall()
                for  row in eve:			
                        messagebox.showinfo("Todays Events:",row[i])	
                        i+=1
        except mysql.connector.Error as error:
                pass
		
remdate()	
		
def insert():
	try:
		print(rdate.get())
		cur.execute("insert into events values(%s,'%s')" %(rdate.get(),revent.get()))
		con.commit()
		messagebox.showinfo("success","record inserted")
	except mysql.connector.Error as error :
		print("Failed to insert into MySQL table {}".format(error))
	finally:
		dates.delete(0, END)
		entry1.delete(0, END)
		
def Update():
	try:
		A=rdate.get()
		B=revent.get()
		cur.execute("Update events set(Event=%(value2)s)",{'value2':B})
		con.commit()
		messagebox.showinfo("success","record Updated")
	except mysql.connector.Error as error :
		print("Failed to Update into MySQL table {}".format(error))
	finally:
		dates.delete(0, END)
		entry1.delete(0, END)	

def view():
    try:
                
        cur.execute("select * from events")
        #Fetch all the rows from the query
        result=cur.fetchall()
        #store the fetched result in a file
        f=open('details.txt','w')
        for data in result:
            f.write(str(data)+'\n')
        f.close()
        con.close()
        #make a subprocess module to open software and file that contain all details of remd table
        import subprocess as sp
        pName='notepad.exe'
        fName='detail.txt'
        sp.Popen([pName,fName])
    except mysql.connector.Error as error :
        print("Failed to view MySQL table {}".format(error))
           	
		

#Designing GUI
top.title("Reminder status")
top.geometry('500x200')

#create tkinter label widget
label1=Label(top, text='Rdate(yymmdd)')
dates=Entry(top,textvariable=rdate)
label2=Label(top, text='Revent')

#create tkinter entry widget
entry1=Entry(top, textvariable=revent)

#create tkinter button widget
button1=Button(top, text='Insert',command =insert)
button2=Button(top, text='Update',command =Update)
button3=Button(top, text='View',command =view)

#placing each widget in positions using grid
label1.grid(row=1, column=0)
dates.grid(row=1, column=1)
label2.grid(row=2, column=0)
entry1.grid(row=2, column=1)
button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
top.mainloop()


    
         
             
             


    
         
             
             


    
         
             
             
