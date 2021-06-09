from os import name
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from typing import Literal, ValuesView
import PIL
from PIL import ImageTk
from PIL import Image
from awesometkinter import frame
from tkinter import messagebox
import mysql.connector 

root = Tk()
root.geometry('1080x780+0+0')
root.title("Create an new account")
root.config(background='#5B4F5F')


db = mysql.connector.connect(

    host='localhost',
    user = 'root',
    passwd = '',
    database = 'fci'
)

cur = db.cursor()

def insert(name, pas, bod, country, email):
    id = ''

    formula = ("INSERT INTO student (id,name, pas, bod, country, email) VALUES (%s,%s,%s,%s,%s,%s)")
    values = (id, name, pas, bod, country, email)
    cur.execute(formula, values)
    db.commit()

#function
def get_info():
    name = user_e.get()
    pas = pss_e.get()
    country = country_e.get()
    bod = bod_e.get()
    email = email_e.get()
    if name != '' and pas != '' and email != '':
        insert(name, pas, bod, country, email)
        messagebox.showinfo('Success','You have successfully resigterd')
    else:
        messagebox.showerror('Error', 'Enter all required field')

def clear_entry():
    user_e.delete(0, END)
    pss_e.delete(0, END)
    country_e.delete(0, END)
    bod_e.delete(0, END)
    email_e.delete(0, END)
    



#-----Frame---
login_frame = Frame(root,)
login_frame.pack(side=BOTTOM,expand=True, fill=None,)

fimg = Image.open(r'D:\Git\login_system_gui\logo1.png') 
fimg = fimg.resize((650,650))
f_img = ImageTk.PhotoImage(fimg)
f_img_leb = Label(login_frame,image=f_img, bg='#5A505F')
f_img_leb.pack(side =TOP ,expand=True, fill='both')

#entry ==========

user_e = Entry(login_frame,bg='#E167ED', bd=2, relief=RIDGE, fg='white', font=('havetica',10,''))
user_e.place(x = 300 , y = 190, width=180, height=28 )

pss_e =Entry(login_frame,bg='#E167ED', bd=2, relief=RIDGE, font=('havetica',10,''), fg='white')
pss_e.place(x = 300 , y = 258,width=180, height=28)

date = ['2000','2001', '2002', '2003']

bod_e = ttk.Combobox(login_frame, values=date, )
bod_e.place(x = 300 , y = 326,width=180, height=28)
bod_e.current(0)

country_list = ['Bangladesh','Saoudi Arab','Turky','USA', 'UAE',]
country_e = ttk.Combobox(login_frame, values=country_list)
country_e.place(x =300, y = 394,width=180, height=28) 
country_e.current(0)

email_e = Entry(login_frame,bg='#E167ED', bd=2, relief=RIDGE, font=('havetica',10,''), fg='white')
email_e.place(x = 300 , y = 460,width=180, height=28)

#---label----
user_l = Label(login_frame, text="User name",bg='#A5DAF5', fg='white', bd=2, padx=10, pady= 5, font=('',10,'bold'))
user_l.place(x = 200 , y = 190,height=26, width=70  )

pss_l = Label(login_frame,text="Password",bg='#A5DAF5', fg='white', bd=2, padx=10, pady= 5,font=('',10,'bold'))
pss_l.place(x = 200 , y = 258,height=26, width=70)

bod_l = Label(login_frame,text="B o D",bg='#A5DAF5', fg='white', bd=2, padx=10, pady= 5,font=('',10,'bold'))
bod_l.place(x = 200 , y = 326,height=26, width=70)

country_l = Label(login_frame,text="Country",bg='#A5DAF5', fg='white', bd=2, padx=10, pady= 5,font=('',10,'bold'))
country_l.place(x =200, y = 394,height=26, width=70) 

email_l = Label(login_frame,text="Email",bg='#A5DAF5', fg='white', bd=2, padx=10, pady= 5,font=('',10,'bold'))
email_l.place(x = 200 , y = 462,height=26, width=70)

####_____btn_____

sbtn = Button(login_frame,command=lambda:get_info(), text='Submit',bg='#5A505F',activeforeground='#A5DAF5',activebackground='#E167ED', fg='#A5DAF5', bd=2, padx=10, pady= 5,font=('',10,'bold'), relief=RAISED)
sbtn.place(x= 230, y = 580, height=27, width=70)

cbtn = Button(login_frame,command=lambda:clear_entry(), text='Clear',bg='#5A505F',activeforeground='#A5DAF5',activebackground='#E167ED', fg='#A5DAF5', bd=2, padx=10, pady= 5,font=('',10,'bold'), relief=RAISED)
cbtn.place(x= 350, y = 580, height=27, width=70)


root.mainloop()