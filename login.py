#import modules
import time

from tkinter import *
import os

# Designing window for registration
Name = ''



def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("700x700")

    global Name
    global username
    global password
    global Class1
    global Class2
    global Class3
    global Class4
    global Class5
    global Name_entry
    global username_entry
    global password_entry
    global Class1_entry
    global Class2_entry
    global Class3_entry
    global Class4_entry
    global Class5_entry
    Name= StringVar()
    username = StringVar()
    password = StringVar()
    Class1= StringVar()
    Class2= StringVar()
    Class3= StringVar()
    Class4= StringVar()
    Class5= StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    
    Name_lable = Label(register_screen, text="Name")
    Name_lable.pack()
    Name_entry = Entry(register_screen, textvariable=Name)
    Name_entry.pack()
    
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    
    Class1_label=Label(register_screen, text="Class1 your Handling *")
    Class1_label.pack()
    Class1_entry=Entry(register_screen, textvariable=Class1)
    Class1_entry.pack()
    
    Class2_label=Label(register_screen, text="Class2 your Handling 'if not type none'")
    Class2_label.pack()
    Class2_entry=Entry(register_screen, textvariable=Class2)
    Class2_entry.pack()
    
    Class3_label=Label(register_screen, text="Class3 your Handling 'if not type none'")
    Class3_label.pack()
    Class3_entry=Entry(register_screen, textvariable=Class3)
    Class3_entry.pack()
    
    Class4_label=Label(register_screen, text="Class4 your Handling 'if not type none'")
    Class4_label.pack()
    Class4_entry=Entry(register_screen, textvariable=Class4)
    Class4_entry.pack()
    
    Class5_label=Label(register_screen, text="Class5 your Handling 'if not type none'")
    Class5_label.pack()
    Class5_entry=Entry(register_screen, textvariable=Class5)
    Class5_entry.pack()
    
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_user).pack()


# Designing window for login 

def login():
    
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    #Label(login_screen, text="").pack()
    #Button(login_screen, text="Close", height=2, width=30, command=delete_login_screen).pack()
    
    

# Implementing event on register button

def register_user():
    
    Name_info=Name.get()
    username_info = username.get()
    password_info = password.get()
    Class1_info= Class1.get()
    Class2_info= Class2.get()
    Class3_info= Class3.get()
    Class4_info= Class4.get()
    Class5_info= Class5.get()

    file = open(username_info, "w")
    file.write(Name_info + "\n")
    file.write(username_info + "\n")
    file.write(password_info+"\n")
    file.write(Class1_info+"\n")
    file.write(Class2_info+"\n")
    file.write(Class3_info+"\n")
    file.write(Class4_info+"\n")
    file.write(Class5_info)
    
    file.close()
    
    Name_entry.delete(0,END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    register_screen.destroy()
    

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            l = open('Name.txt', 'w')
            l.write(verify[0])
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()
    



# Designing popup for login success

def login_sucess():
    '''    global login_success_screen

    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Login Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Welcome").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    '''
    global Name
    Name=str(Name)
    Name=Name[:-4]
    
    login_screen.destroy()
    main_screen.destroy()
    f=open('loginTrue.txt', 'w')
    f.write('True')
    rav = open('Name.txt','w')
    rav.write(Name)
    
# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_main_account_screen():
    main_screen.destroy()
    
def delete_login_screen():
    login_screen.destroy()
        


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(main_screen,text="Select Your Choice", width="300", height="2", font=("Calibri", 13)).pack()
    Label(main_screen,text="").pack()
    Button(main_screen,text="Login", height="2", width="30", command = login).pack()
    Label(main_screen,text="").pack()
    Button(main_screen,text="Register", height="2", width="30", command=register).pack()
    #Label(text="").pack()
    #Button(text="Close", height="2", width="30", command=delete_main_account_screen).pack()
    main_screen.mainloop()

















