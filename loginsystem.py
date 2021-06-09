from posixpath import expanduser
from tkinter import*
from tkinter.font import BOLD
from tkinter.simpledialog import SimpleDialog
from typing import Counter
from tkinter import messagebox
import awesometkinter as atk
from tkinter import ttk
import mysql.connector
from awesometkinter import button

window = Tk()
window.geometry('580x580+0+0')
window.config(bg = 'powder blue')
window.title('Kothon')
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='fci'
)

def validation():
    name = un1_entry.get()
    pas = un2_entry.get()
    
    cur = db.cursor()
    formula = "SELECT * FROM student WHERE NAME = %s AND PAS = %s "
    value = (name, pas)
    cur.execute(formula, value)
    r = cur.fetchall()
    if not r:
        messagebox.showerror('Error', 'Information not matched...\n try again...')
    else:
        messagebox.showinfo('Success', 'You have successfully loged in...')
        
# #user name 
# def username():
#     name = un1_entry.get()
#     pas = un2_entry.get()
    
#     for user in users:
#         if name == user['u_name'] and pas == user['password']:
#             conf_lebel = Label(window, text='successfully loged in',padx=10, pady=10,font='18',)
#             conf_lebel.place(x = 130, y = 450, height=80,width=300)
#             messagebox.showinfo('success','You have successfully login')
#             break
        
#     else:
#         conf_lebel = Label(window, text='Invalid loged in',padx=10, pady=10,font='18',)
#         conf_lebel.place(x = 130, y = 450, height=80,width=300)
#         messagebox.showerror('Error','Invalid Info')
            

login_frame =atk.Frame3d(window, bg= 'pink')
login_frame.pack(side =TOP ,expand=True, fill=None, ipady=200)

t = Label(login_frame, text='Lutuputu login system', bg='pink', fg='black',font={BOLD},relief=RIDGE)
t.pack(side=TOP, fill=X ,padx=150,pady=20, ipady=5, ipadx=5)

#---lebel====

un_lebel = Label(login_frame, text='User name :',fg='Black', bg='pink')
un_lebel.place(x =100, y = 90)

pss_lebel = Label(login_frame, text='Password :', fg='black', bg='pink')
pss_lebel.place(x=100, y = 155)



#---entry===

un1_entry = ttk.Entry(login_frame,font={'times new roman',14, 'bold'})
un1_entry.place(x= 100, y = 120, height=28, width=260)

un2_entry = ttk.Entry(login_frame,font={'times new roman',14, 'bold'})
un2_entry.place(x = 100, y = 180,height=28, width=260)


##log in button
lg_btn = Button(login_frame, text='Log in', bg='black', fg='white', command=lambda:validation())
lg_btn.pack(side=BOTTOM,expand=True, fill=None, ipadx=40, ipady=5,)

cna_btn = Button(login_frame, text='Create a new accout', bg='pink', fg='black', activebackground='pink', activeforeground='black')
cna_btn.place(x = 78, y = 350 )
fp_btn = Button(login_frame, text='Forget password', bg='pink', fg='black', activebackground='pink', activeforeground='black')
fp_btn.place(x = 78, y = 380 )



window.mainloop()