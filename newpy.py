import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox

from database_module import *





root=Tk()
root.title("LOGIN WINDOW")
root.geometry("300x300")


def newuser_fun():
        def signup_fun():
                if(pn.get()!=cp.get()):
                        messagebox.showerror("Error","Passwords doesn't match")
                        un.delete(0,END)
                        pn.delete(0,END)
                        cp.delete(0,END)
                        un.focus()
                else:
                        sf=open("USERS.txt","a")
                        sf.write(un.get())
                        sf.write("\t")
                        sf.write(pn.get())
                        sf.write("\t")
                        sf.write(ssn.get())
                        sf.write("\n")
                        sf.close()
                        print("NEW USER SUCCEFULLY CREATED")
                        messagebox.showinfo("Sign up complete","New user created")
                        login_main()
                        un.delete(0,END)
                        pn.delete(0,END)
                        cp.delete(0,END)
                        un.focus()


        def signup_clear():
                un.delete(0,END)
                pn.delete(0,END)
                cp.delete(0,END)
                un.focus()

        sup=Tk()
        sup.title("SIGN UP")
        sup.geometry("300x300")
        Label(sup,text="NEW USER PAGE!",font=("TIMES",12),fg="red").grid(row=0,column=1)
        Label(sup,text="USER ID").grid(row=2,column=0)
        Label(sup,text="PASSWORD").grid(row=3,column=0)
        Label(sup,text="CONFIRM PASSWORD").grid(row=4,column=0)
        Label(sup,text="SSN").grid(row=5,column=0)
        un=Entry(sup)
        un.grid(row=2,column=1)
        pn=Entry(sup,show='*')
        pn.grid(row=3,column=1)
        cp=Entry(sup,show='*')
        cp.grid(row=4,column=1)
        ssn=Entry(sup)
        ssn.grid(row=5,column=1)
        Button(sup,text="SAVE",command=signup_fun).grid(row=7,column=0)
        Button(sup,text="CANCEL",command=signup_clear).grid(row=7,column=1)
        




      
def admin_fun():
        af=open("ADMIN.txt","r")
        if(af.mode=="r"):
            for line in af:
                name,pwd=line.split()
##    name=str(contents[0])
##    pwd=str(contents[1])
        af.close()
        if(name==u.get() and pwd==p.get()):
                print("ADMIN AUTHORIZED")
                admin_main()

        else:
                messagebox.showerror("Authorization Error","Incorrect Admin credentials")
        u.delete(0,END)
        p.delete(0,END)
        u.focus()

        
def login_fun():
    nlist=[]
    plist=[]
    ssnlist=[]
    lf=open("USERS.txt","r")
    if(lf.mode=='r'):
        for lines in lf:
            name,pwd,ssn_list=lines.split()
            nlist.append(name)
            plist.append(pwd)
            ssnlist.append(ssn_list)
    length=len(nlist) ##or,use length=len(plist)
    for i in range(length):
        if(nlist[i]==u.get()):
            if(plist[i]==p.get()):
                print("USER AUTHENTICATED")
                login_main()
                break
        
                
    else:
        print("USER DOESNT EXIST")
        messagebox.showerror("Error","User doesnt exist")
        u.delete(0,END)
        p.delete(0,END)
        u.focus()
    lf.close()


def forgot_fun():

        obj=Tk()
        obj.title("RECOVERY")
        obj.geometry("250x100")
        def showpass():
                nlist=[]
                plist=[]
                ssnlist=[]
                lf=open("USERS.txt","r")
                if(lf.mode=='r'):
                        for lines in lf:
                            name,pwd,ssn_file=lines.split()
                            nlist.append(name)
                            plist.append(pwd)
                            ssnlist.append(ssn_file)
                length=len(nlist) ##or,use length=len(plist)
                for i in range(length):
                        if(nlist[i]==nameent.get()):
                            if(ssnlist[i]==ssnent.get()):
                                print("Your password is '%s'"%plist[i])
                                break
        
                else:
                        print("USER DOESNT EXIST")
                        messagebox.showerror("Error","User doesnt exist")
                nameent.delete(0,END)
                ssnent.delete(0,END)
                nameent.focus()
                lf.close()


        
        Label(obj,text="NAME").grid(row=1,column=0)
        Label(obj,text="SSN").grid(row=2,column=0)
        nameent=Entry(obj)
        ssnent=Entry(obj)
        nameent.grid(row=1,column=1)
        ssnent.grid(row=2,column=1)
        Button(obj,text="RECOVER",command=showpass).grid(row=3,column=1)
        
        
        
        
        

            
        
    
    
Label(root,text="LOGIN TO CONTINUE!",font=("TIMES",12),fg="red").grid(row=0,column=1)
Label(root,text="USER ID").grid(row=2,column=0)
Label(root,text="PASSWORD").grid(row=3,column=0)
u=Entry(root)
u.grid(row=2,column=1)
p=Entry(root,show='*')
p.grid(row=3,column=1)
Button(root,text="LOGIN",command=login_fun).grid(row=4,column=0)
Button(root,text="ADMIN",command=admin_fun).grid(row=4,column=1)
Button(root,text="NEW USER",command=newuser_fun).grid(row=4,column=2)
Button(root,text="FORGOT PASSWORD",command=forgot_fun).grid(row=5,column=1)
root.mainloop()
     
        
       


