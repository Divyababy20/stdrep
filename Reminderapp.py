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
	#messagebox.showinfo("success","Connected")
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
		#print(dat)
                cur.execute("select revent from events where Date =%(value)s ",{'value': dat})		
                eve = cur.fetchall()
                for  row in eve:
			lS=Label(top,fg="blue")
			lS.config(text="Todays Events:  "+row[i])	
			lS.grid(row=1, column=2)
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
		e1.delete(0, END)
		
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
		e1.delete(0, END)	
)	

def Delete():
	try:
		A=rdate.get()
		B=revent.get()
		cur.execute("Delete from  events ")
		con.commit()
		messagebox.showinfo("success","record Deleted")
	except mysql.connector.Error as error :
		print("Failed to Delete into MySQL table {}".format(error))
	finally:
		dates.delete(0, END)
		e1.delete(0, END)			
		
#Designing GUI
top.title("Reminder status")
top.geometry('500x200')

#insert
l1=Label(top, text='Date(yymmdd)')
dates=Entry(top,textvariable=rdate)
l2=Label(top, text='Event(description)')
e1=Entry(top, textvariable=revent)
b1=Button(top, text='Insert',command =insert)

#update
lU=Label(top, text='Date( yymmdd )')
datesU=Entry(top,textvariable=rdate)
l2U=Label(top, text='Event(description)')
e2U=Entry(top, textvariable=revent)
bU=Button(top, text='Update',command =Update)

#DElete
lD=Label(top, text='Date( yymmdd )')
datesD=Entry(top,textvariable=rdate)
bD=Button(top, text='Delete',command =Delete)
#View
b4=Button(top, text='Refresh',command =remdate)

l21=Label(top, text='ADD EVENT',fg="red")
l22=Label(top, text='UPDATE EVENT',fg="red")
l23=Label(top, text='DELETE EVENT',fg="red")

l21.grid(row=3, column=2)
l1.grid(row=4, column=0)
dates.grid(row=4, column=1)
l2.grid(row=5, column=0)
e2.grid(row=5, column=1)
b1.grid(row=6, column=2)

l22.grid(row=8, column=2)
lU.grid(row=9, column=0)
datesU.grid(row=9, column=1)
l2U.grid(row=10, column=0)
e2U.grid(row=10, column=1)
bU.grid(row=11, column=2)

l23.grid(row=13, column=2)
lD.grid(row=14, column=0)
datesD.grid(row=14, column=1)
bD.grid(row=15, column=2)
b4.grid(row=17, column=2)
top.mainloop()

    
         
             
             


    
         
             
             


    
         
             
             
