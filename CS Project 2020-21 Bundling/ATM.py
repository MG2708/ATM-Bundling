#ATM using Tkinter

################################# IMPORTED MODULES #################################
import tkinter as tk
import time
import mysql.connector
from tkinter import *
import PIL
import sys
from tkinter import messagebox
import  tkinter.messagebox
from tkinter import BOTH, END, LEFT
import os
from os import path
from PIL import Image,ImageTk
import random

#Setting High DPI in Windows
try:
    from ctypes import windll
    windl.schore.SetProcessDpiAwareness(1)
except:
    pass
################################# BANKING SCREEN USING CLASS #################################

################################# CURRENT BALANCE #################################


current_balance=0.00

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        ################## INITIALIZING PAGES IN CONTAINER ##################
        for F in (StartPage, MenuPage,Withdraw_Page,Deposit_Page,Balance_Page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

########################## START PAGE ##########################
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#2d5986')
        self.controller = controller
        self.controller.title('M SECURITY ATM Simulator')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='assets/atm.png'))

        heading=tk.Label(self,text='M SECURITY ATM Simulator',font=('orbitron',45,'bold'),foreground='white',background='#2d5986')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#2d5986').pack()

        password_label=tk.Label(self,text=(f'Welcome {user_display_name} to M SECURITY ATM Simulator'),font=('orbitron',17),bg='#2d5986',fg='white').pack(pady=10)

        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self,text='Enter',font=('orbitron',12),command=next_page,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)

        def Quit():
            self.controller.destroy()

        def popup():
            response=messagebox.askyesno('Exit','Do you want to Quit?')

            if response == 1:
                return Quit()
            else:
                return

        quit1 = tk.Button(self,text='Quit',font=('orbitron',12),command=popup,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)


        dualtone_label=tk.Label(self, text='',font=('orbitron',13),fg='white',bg='#264d73',anchor='n')
        dualtone_label.pack(fill='both',expand='True')

        ################## BOTTOM FRAME #################################
        #Bottom Frame for Logos and time
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_pic=Image.open(file='assets/visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_pic)
        visa_label.pack(side='left')
        visa_label.image=visa_pic
        
        rupay_pic=Image.open(file='assets/rupay.png')
        rupay_label=tk.Label(bottom_frame,image=rupay_pic)
        rupay_label.pack(side='left')
        rupay_label.image=rupay_pic
        
        mastercard_pic=Image.open(file='assets/mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_pic)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_pic        

        ae_pic=Image.open(file='assets/american-express.png')
        ae_label=tk.Label(bottom_frame,image=ae_pic)
        ae_label.pack(side='left')
        ae_label.image=ae_pic

        def tick():
            current_time=time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label=tk.Label(bottom_frame,font=('orbitron',15))
        time_label.pack(side="right")
        tick()

        credits=tk.Label(bottom_frame,text='Created and Develped by Mudit Garg',font=('orbitron',15),justify='center').pack()



########################## MENU PAGE ##########################
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#2d5986')
        self.controller = controller
         
        headingLab1=tk.Label(self,
                            text="M SECURITY ATM Simulator",
                            font=('orbitron',45,'bold'),
                            foreground='white',
                            background='#2d5986')
        headingLab1.pack(pady=20)
        space_label=tk.Label(self, height=1,bg='#2d5986')
        space_label.pack()

        welcome_label=tk.Label(self,
                               text=f'Welcome {user_display_name} to M SECURITY ATM Simulator',
                               font=('orbitron',22),
                               fg='white',
                               bg='#2d5986')
        welcome_label.pack(pady=20)
        
        main_menu_label=tk.Label(self,
                                 text='Main Menu',
                                 font=('orbitron',20),
                                 fg='white',
                                 bg='#2d5986')
        main_menu_label.pack()

    
        selection_label=tk.Label(self,
                                 text="Please Make a Selection",
                                 font=('orbitron',14),
                                 fg='white',
                                 bg='#2d5986',
                                 anchor='w')
        selection_label.pack(fill='x', padx=10)

        button_frame=tk.Frame(self,bg='#264d73')
        button_frame.pack(fill='both',expand=True,pady=10)

        #withdraw
        def withdraw():
            controller.show_frame('Withdraw_Page')
            
        withdraw_button=tk.Button(button_frame,
                                text='Withdraw',
                                font=('orbitron',20),
                                command=withdraw,
                                relief='raised',
                                borderwidth=3,
                                width=20,
                                height=2)
        withdraw_button.grid(row=0, column=0, pady=16,padx=125)

        #deposit
        def deposit():
            controller.show_frame('Deposit_Page')
            
        deposit_button=tk.Button(button_frame,
                                text='Deposit',
                                font=('orbitron',20),
                                command=deposit,
                                relief='raised',
                                borderwidth=3,
                                width=20,
                                height=2)
        deposit_button.grid(row=1, column=0,pady=16,padx=125)

        #balance
        def balance():
            controller.show_frame('Balance_Page')
                        
        balance_button=tk.Button(button_frame,
                                text='Balance',
                                font=('orbitron',20),
                                command=balance,
                                relief='raised',
                                borderwidth=3,
                                width=20,
                                height=2)
        balance_button.grid(row=0,column=1, pady=40, padx=355)

        #exit
        def exit():
            controller.show_frame('StartPage')
                        
        exit_button=tk.Button(button_frame,
                                text='Exit',
                                font=('orbitron',20),
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=20,
                                height=2)
        exit_button.grid(row=1,column=1,pady=40, padx=355)

        ################## BOTTOM FRAME #################################
        #Bottom Frame for Logos and time
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_pic = Image.open(file='assets/visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic

        rupay_pic = Image.open(file='assets/rupay.png')
        rupay_label = tk.Label(bottom_frame, image=rupay_pic)
        rupay_label.pack(side='left')
        rupay_label.image = rupay_pic

        mastercard_pic = Image.open(file='assets/mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_pic)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_pic

        ae_pic = Image.open(file='assets/american-express.png')
        ae_label = tk.Label(bottom_frame, image=ae_pic)
        ae_label.pack(side='left')
        ae_label.image = ae_pic

        def tick():
            current_time=time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label=tk.Label(bottom_frame,font=('orbitron',15))
        time_label.pack(side="right")
        tick()

        credits=tk.Label(bottom_frame,text='Created and Develped by Mudit Garg',font=('orbitron',15),justify='center').pack()
        

########################## WITHDRAW PAGE ##########################
class Withdraw_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#2d5986')
        self.controller = controller
        #self.controller.title('Withdraw Amount')
        heading=tk.Label(self,text='M SECURITY ATM Simulator',font=('orbitron',45,'bold'),foreground='white',background='#2d5986')
        heading.pack(pady=25)
        choose_amount_label=tk.Label(self,text='Choose the amount you want to withdraw',font=('orbitron',13),fg='white',bg='#2d5986')
        choose_amount_label.pack()
        button_frame=tk.Frame(self,bg='#264d73')
        button_frame.pack(fill='both',expand='True')

        def withdraw(amount):
            global current_balance
            if amount>current_balance:
                messagebox.showwarning('WARNING','Not sufficient funds!')
                other_amount_entry.delete(0,END)
            else:

                current_balance -= amount
                messagebox.showinfo('TRANSACTION','Done Successfully!')
                other_amount_entry.delete(0,END)
                controller.shared_data['Balance'].set(current_balance)
                mydb=mysql.connector.connect(host="156.67.222.190",user="u518149110_admin",password="Ke460qIg~4t")
                mycursor=mydb.cursor()
                mycursor.execute("u518149110_atm")
                mycursor.execute(f"update users set balance ={current_balance} where accid = {username1} ")
                mydb.commit()

                controller.show_frame('MenuPage')



        one_hundred_button=tk.Button(button_frame, text='₹ 100',font=('orbitron',20),command=lambda:withdraw(100), relief='raised', width=20,height=2)
        one_hundred_button.grid(row=0, column=0, pady=10,padx=125)

        five_hundred_button=tk.Button(button_frame, text='₹500', font=('orbitron',20), command=lambda:withdraw(500), relief='raised', width=20,height=2)
        five_hundred_button.grid(row=1, column=0, pady=10,padx=125)

        one_thousand_button=tk.Button(button_frame, text='₹ 1000',font=('orbitron',20),command=lambda:withdraw(1000), relief='raised', width=20,height=2)
        one_thousand_button.grid(row=2,column=0, pady=10,padx=125)

        two_thousand_button=tk.Button(button_frame,text='₹ 2000', font=('orbitron',20),command=lambda:withdraw(2000),relief='raised', width=20,height=2)
        two_thousand_button.grid(row=3,column=0, pady=10,padx=125)

        three_thousand_button=tk.Button(button_frame,text='₹ 3000',font=('orbitron',20),command=lambda:withdraw(3000), relief='raised',width=20,height=2)
        three_thousand_button.grid(row=0,column=1,pady=10,padx=355)     

        five_thousand_button=tk.Button(button_frame,text='₹ 5000',font=('orbitron',20),command=lambda:withdraw(5000),relief='raised', width=20, height=2)
        five_thousand_button.grid(row=1,column=1,pady=10,padx=355) 

        ten_thousand_button=tk.Button(button_frame,text='₹ 10000', font=('orbitron',20),command=lambda:withdraw(10000),relief='raised', width=20, height=2)
        ten_thousand_button.grid(row=2,column=1,pady=10,padx=355)

        #Other Amount Withdraw
        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,textvariable=cash, font=('orbitron',20),width=20,justify='center')
        other_amount_entry.grid(row=3,column=1,pady=10,padx=355,ipady=25)

        other_amount_heading=tk.Button(button_frame,text='Other amount in Ruppees',font=('orbitron',15),borderwidth=0,relief='sunken',activeforeground='white',activebackground='#2d5986',bg='#2d5986',fg='white')
        other_amount_heading.grid(row=4,column=1)

        def other_amount(_):
            global current_balance
            try:
                val=int(cash.get())

                if int(cash.get())>current_balance:
                    messagebox.showwarning('WARNING','Not sufficient funds!')
                    other_amount_entry.delete(0,END)
                elif int(cash.get())<0:
                    messagebox.showwarning('WARNING','Invalid Input!')
                    other_amount_entry.delete(0,END)
                else:

                    current_balance -= int(cash.get())
                    controller.shared_data['Balance'].set(current_balance)
                    cash.set('')
                    messagebox.showinfo('TRANSACTION','Done Successfully!')
                    controller.show_frame('MenuPage')
                    mydb=mysql.connector.connect(host="156.67.222.190",user="u518149110_admin",password="Ke460qIg~4t")
                    mycursor=mydb.cursor()
                    mycursor.execute("u518149110_atm")
                    mycursor.execute(f"update users set balance ={current_balance} where accid = {username1} ")
                    mydb.commit()
            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')

        other_amount_entry.bind('<Return>',other_amount)

        ################## BOTTOM FRAME #################################
        #Bottom Frame for Logos and time
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_pic = Image.open(file='assets/visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic

        rupay_pic = Image.open(file='assets/rupay.png')
        rupay_label = tk.Label(bottom_frame, image=rupay_pic)
        rupay_label.pack(side='left')
        rupay_label.image = rupay_pic

        mastercard_pic = Image.open(file='assets/mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_pic)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_pic

        ae_pic = Image.open(file='assets/american-express.png')
        ae_label = tk.Label(bottom_frame, image=ae_pic)
        ae_label.pack(side='left')
        ae_label.image = ae_pic

        def tick():
            current_time=time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label=tk.Label(bottom_frame,font=('orbitron',15))
        time_label.pack(side="right")
        tick()

        credits=tk.Label(bottom_frame,text='Created and Develped by Mudit Garg',font=('orbitron',15),justify='center').pack()

########################## DEPOSIT PAGE ##########################
class Deposit_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#2d5986')
        self.controller = controller
        #self.controller.title('Deposit Amount')
        heading=tk.Label(self,text='M SECURITY ATM Simulator',font=('orbitron',45,'bold'),foreground='white',background='#2d5986')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#2d5986').pack()

        enter_amount_label=tk.Label(self,text='Enter the amount you want to deposit',font=('orbitron',13),bg='#2d5986',fg='white').pack(pady=10)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('orbitron',12),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            try:
                val=int(cash.get())
                if int(val)<0:
                    messagebox.showwarning('WARNING','Improper Amount Entered!')
                    cash.set('')
                else:
                    current_balance += int(val)
                    messagebox.showinfo('DEPOSITION','Done Successfully!')
                    controller.shared_data['Balance'].set(current_balance)
                    controller.show_frame('MenuPage')
                    cash.set('')
                    mydb=mysql.connector.connect(host="156.67.222.190",user="u518149110_admin",password="Ke460qIg~4t")
                    mycursor=mydb.cursor()
                    mycursor.execute("Use u518149110_atm")
                    mycursor.execute(f"update users set balance ={current_balance} where accid = {username1} ")
                    mydb.commit()

            except ValueError:
                messagebox.showwarning('WARNING','Invadlid Input!')
                cash.set('')


        enter_button=tk.Button(self,text='Enter',font=('orbitron',13),command=deposit_cash,relief='raised',borderwidth=3,width=23,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self, bg='#264d73')
        two_tone_label.pack(fill='both', expand=True)

        ################## BOTTOM FRAME #################################
        #Bottom Frame for Logos and time
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_pic = Image.open(file='assets/visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic

        rupay_pic = Image.open(file='assets/rupay.png')
        rupay_label = tk.Label(bottom_frame, image=rupay_pic)
        rupay_label.pack(side='left')
        rupay_label.image = rupay_pic

        mastercard_pic = Image.open(file='assets/mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_pic)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_pic

        ae_pic = Image.open(file='assets/american-express.png')
        ae_label = tk.Label(bottom_frame, image=ae_pic)
        ae_label.pack(side='left')
        ae_label.image = ae_pic

        def tick():
            current_time=time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label=tk.Label(bottom_frame,font=('orbitron',15))
        time_label.pack(side="right")
        tick()

        credits=tk.Label(bottom_frame,text='Created and Develped by Mudit Garg',font=('orbitron',15),justify='center').pack()

########################## BALANCE PAGE ##########################
class Balance_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#2d5986')
        self.controller = controller
        #self.controller.title('Balance Amount')
        heading=tk.Label(self,text='M SECURITY ATM Simulator',font=('orbitron',45,'bold'),foreground='white',background='#2d5986')
        heading.pack(pady=25)

        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(current_balance)

        balance_label = tk.Label(self, textvariable=self.balance_var, font=('orbitron',13),fg='white', bg='#2d5986', anchor='w')
        balance_label.pack()

        button_frame=tk.Label(self,bg='#264d73')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Menu',font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Exit',command=exit,font=('orbitron',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=5)

        ################## BOTTOM FRAME #################################
        #Bottom Frame for Logos and time
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_pic = Image.open(file='assets/visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_pic)
        visa_label.pack(side='left')
        visa_label.image = visa_pic

        rupay_pic = Image.open(file='assets/rupay.png')
        rupay_label = tk.Label(bottom_frame, image=rupay_pic)
        rupay_label.pack(side='left')
        rupay_label.image = rupay_pic

        mastercard_pic = Image.open(file='assets/mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_pic)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_pic

        ae_pic = Image.open(file='assets/american-express.png')
        ae_label = tk.Label(bottom_frame, image=ae_pic)
        ae_label.pack(side='left')
        ae_label.image = ae_pic

        def tick():
            current_time=time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label=tk.Label(bottom_frame,font=('orbitron',15))
        time_label.pack(side="right")
        tick()

        credits=tk.Label(bottom_frame,text='Created and Develped by Mudit Garg',font=('orbitron',15),justify='center' ).pack()

    def on_balance_changed(self, *args):
        self.balance_var.set('Current Balance: $'+str(self.controller.shared_data['Balance'].get()))

    ########################## CLASS  DEFINE FUNCTION ##########################
def abcd():

        app = SampleApp()
        app.mainloop()


########################## REGISTER/LOGIN ##########################


def password_not_recognised():
  messagebox.showwarning('WARNING',('Invalid Password!'))

################## ABOUT SCREEN ##################
def about():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("About")
  screen3.geometry("500x100+600+250")
  screen3.iconphoto(False,tk.PhotoImage(file='assets/atm.png'))
  Label(screen3, text = "Created and Developed by Mudit Garg\n GUI Development in Python using Tkinter \n with Mysql database at Backend \n\n © Mudit Garg 2020 \n ",font = ("orbitron", 10,'bold')).pack()

################## WARNING_SCREEN ##################
def user_not_found():
  messagebox.showwarning('WARNING',('No AccountID Found !'))

################## REGISTER USER SCREEN ##################
def register_user():
  global username_info
  username_info = str(rand)
  password_info = password.get()
  name_info     = name.get()

  ################## MYSQL DATABASE ##################
  global mycursor
  mydb=mysql.connector.connect(host='156.67.222.190',user='u518149110_admin',password='Ke460qIg~4t')
  mycursor=mydb.cursor()
  mycursor.execute("create database if not exists u518149110_atm")
  mycursor.execute("use u518149110_atm")
  mycursor.execute("create table if not exists users(accid int(10) primary key,name varchar(30),password char(20),balance char(30))")
  mydb.commit()

  mycursor.execute('select accid from users')
  values=mycursor.fetchall()

  b=[]
  for i in values:
      b.append(i[0])
  if username_info in b:
    messagebox.showwarning('WARNING',('AccountID already exists!'))
    #username_entry.delete(0,END)
    password_entry.delete(0,END)
    name_entry.delete(0,END)
  elif name_info=='' :
        messagebox.showwarning('WARNING',('No Name Given!'))
        password_entry.delete(0,END)
  elif password_info=='' :
        messagebox.showwarning('WARNING',('No Password Given!'))
  else:
        balance_inti='0.00'
        password_entry.delete(0, END)
        name_entry.delete(0, END)
        screen1.destroy()
        mycursor.execute("insert into users values('"+username_info+"','"+name_info+"','"+password_info+"','"+balance_inti+"')")
        mydb.commit()
        messagebox.showinfo('Registration',('Done Successfully!'))


################## LOGIN VERIFY SCREEN ##################
def login_verify():
  global current_balance
  global username1
  global name_display
  global user_display_name
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  mydb=mysql.connector.connect(host='156.67.222.190',user='u518149110_admin',password='Ke460qIg~4t')
  mycursor=mydb.cursor()
  #mycursor.execute("create database if not exists u518149110_atm")
  mycursor.execute("use u518149110_atm")

  mycursor.execute("select accid from users ")
  values=mycursor.fetchall()
  user_acc=[]
  for i in values:
    user_acc.append(i[0])

  if username1.isalpha():
        messagebox.showwarning('WARNING',('Wrong Input!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)

  elif str(username1)=='':
        messagebox.showwarning('WARNING',('No Accound ID Given!'))
        password_entry1.delete(0,END)
  elif str(username1).isspace():
        messagebox.showwarning('WARNING',('No Accound ID Given!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)
  elif username1.isalnum():
      if username1.isdigit():

          if int(username1) in user_acc:

              mycursor.execute(f"select password from users where accid = {username1} ")
              values=mycursor.fetchall()
              mydb.commit()
              user_pass=[]
              for i in values:
                  user_pass.append(i[0])

              user_pass_1=str(user_pass[0])

              if password1=='':
                  messagebox.showwarning('WARNING',('No Password Given!'))
                  username_entry1.delete(0, END)
                  password_entry1.delete(0,END)
              elif password1 == str(user_pass_1) :
                  mycursor.execute(f"select name from users where accid={username1}")
                  values=mycursor.fetchall()
                  user_name=[]
                  for i in values:
                    user_name.append(i[0])
                  user_display_name=str(user_name[0])
                  #login_sucess()
                  mydb=mysql.connector.connect(host='156.67.222.190',user='u518149110_admin',password='Ke460qIg~4t')
                  mycursor=mydb.cursor()
                  #mycursor.execute("create database if not exists u518149110_atm")
                  mycursor.execute("use u518149110_atm")

                  mycursor.execute(f'select balance from users where accid ={username1}')
                  values=mycursor.fetchall()
                  user_balance=[]
                  for i in values:
                    user_balance.append(i[0])
                  user_balance_1=float(user_balance[0])
                  current_balance=user_balance_1

                  screen2.destroy()
                  screen.destroy()
                  abcd()
              elif password1!= str(user_pass_1):
                  password_not_recognised()
          else:
              user_not_found()
      else:
          user_not_found()

  else:
        user_not_found()

################## REGISTER DISPLAY SCREEN ##################
def register():
  global screen1
  global password_entry
  global username_entry
  global rand
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250+600+250")
  screen1.iconphoto(False,tk.PhotoImage(file='assets/atm.png'))

  global username
  global password
  global name

  global username_entry
  global password_entry
  global name_entry

  username = StringVar()
  password = StringVar()
  name     = StringVar()

  Label(screen1, text = "Please enter details below",font = ("orbitron", 10)).pack()

  Label(screen1, text = "").pack()
  Label(screen1, text = "Name",font = ("orbitron", 10)).pack()
  name_entry = Entry(screen1,font = ("Times",15), textvariable = name)
  name_entry.pack()

  Label(screen1, text = "Account ID",font = ("orbitron", 10)).pack()
  rand=random.randint(1,100000)
  username=Label(screen1, text = rand,font = ("Times", 15)).pack()
  #username_entry = Entry(screen1, textvariable = username)
  #username_entry.pack()

  Label(screen1, text = "Pin",font = ("orbitron", 10)).pack()
  password_entry =  Entry(screen1,font = ("Times",15), textvariable = password)
  password_entry.config(fg='black',show='●')
  password_entry.pack()

  Label(screen1, text = "").pack()
  Button(screen1, text = "Register",font = ("orbitron", 10), width = 10, height = 1, command = register_user).pack()

################## LOGIN DISPLAY SCREEN ##################
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250+600+250")
  screen2.iconphoto(False,tk.PhotoImage(file='assets/atm.png'))
  Label(screen2, text = "Please enter details below to login",font = ("orbitron", 10)).pack()
  Label(screen2, text = "").pack()

  global username_verify
  global password_verify

  username_verify = StringVar()
  password_verify = StringVar()


  global username_entry1
  global password_entry1

  Label(screen2, text = "Account ID",font = ("orbitron", 10)).pack()
  username_entry1 = Entry(screen2,font = ("Times",15) ,textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Pin",font = ("orbitron", 10)).pack()
  password_entry1 = Entry(screen2,font = ("Times",15), textvariable = password_verify)
  password_entry1.config(fg='black',show='●')
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login",font = ("orbitron", 10), width = 10, height = 1, command = login_verify).pack()

################## REGISTER/LOGIN SCREEN #################################
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250+550+200")
  screen.title("M SECURITY ATM Simulator")
  screen.iconphoto(False,tk.PhotoImage(file='assets/atm.png'))
  #screen.bind('<Return>')
  Label(text = "M SECURITY", bg = "grey", width = "300", height = "2", font = ("orbitron", 13,'bold')).pack()
  Label(text = "").pack()
  Button(text = "Login", font = ("orbitron", 10),height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register", font = ("orbitron", 10),height = "2", width = "30", command = register).pack()
  Label(text = "").pack()
  Button(text = "About", font = ("orbitron", 10),height = "2", width = "30", command = about).pack()

  screen.mainloop()

main_screen()
