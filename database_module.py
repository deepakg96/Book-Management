import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox

conn=sqlite3.connect("DATABASE.db")
cursor=conn.cursor()
#uncomment the below line while running the program for the first time
##cursor.execute('''CREATE TABLE BOOKS(ID text PRIMARY KEY NOT NULL,NAME text NOT NULL,AUTHOR int NOT NULL,GENRE text NOT NULL,LANGUAGE text NOT NULL,COST real NOT NULL,PUBLISHED_DATE text NOT NULL)''')
conn.commit()
print("Database loaded successfully")



#for admin,
def admin_main():
        admin=Tk()
        admin.title("ADMIN PANEL")
        admin.geometry("415x300")
        
        def insert_book():
                conn=sqlite3.connect("DATABASE.db")
                cursor=conn.cursor()
                bid=str(bookid.get())
                bname=str(bookname.get())
                bauthor=str(author.get())
                bgenre=str(genre.get())
                blang=str(lang.get())
                bcost=int(cost.get())
                bdate=str(date.get())
                #inserting values to the database
                bookdata=[(bid,bname,bauthor,bgenre,blang,bcost,bdate)]
                cursor.executemany("INSERT INTO BOOKS VALUES(?,?,?,?,?,?,?)",bookdata)
                conn.commit()
                messagebox.showinfo("Database operation","Successfully added a book")
                bookid.delete(0,END)
                bookname.delete(0,END)
                author.delete(0,END)
                genre.delete(0,END)
                lang.delete(0,END)
                cost.delete(0,END)
                date.delete(0,END)
                bookid.focus()

        
        def display_book():
                conn=sqlite3.connect("DATABASE.db")
                cursor=conn.cursor()
                print("\nDetails in the DATABASE")
                showdata=cursor.execute("SELECT * FROM BOOKS ORDER BY NAME")
                for row in showdata:
                        print("\nBOOK ID : ",row[0])
                        print("BOOK NAME : ",row[1])
                        print("AUTHOR : ",row[2])
                        print("GENRE : ",row[3])
                        print("LANGUAGE : ",row[4])
                        print("COST(INR) : ",row[5])
                        print("PUBLISHED DATE : ",row[6])
                bookid.delete(0,END)
                bookid.focus()

                
        def search_book():
                conn=sqlite3.connect("DATABASE.db")
                cursor=conn.cursor()
                bid=str(bookid.get())
                print("\nThe deatils of the book with id = "+ bid) 
                showdata=cursor.execute("SELECT * FROM BOOKS WHERE ID='%s'"%bid)
                for row in showdata:
                        print("\nBOOK ID : ",row[0])
                        print("BOOK NAME : ",row[1])
                        print("AUTHOR : ",row[2])
                        print("GENRE : ",row[3])
                        print("LANGUAGE : ",row[4])
                        print("COST(INR) : ",row[5])
                        print("PUBLISHED DATE : ",row[6])
                bookid.delete(0,END)
                bookid.focus()
                
                
        def remove_book():
                conn=sqlite3.connect("DATABASE.db")
                cursor=conn.cursor()
                bid=str(bookid.get())
                cursor.execute("DELETE FROM BOOKS WHERE ID='%s'"%bid)
                conn.commit()
                messagebox.showinfo("Database operation","Successfully removed a book")
                bookid.delete(0,END)
                bookid.focus()
        
        
        def cancel_book():
                bookid.delete(0,END)
                bookname.delete(0,END)
                author.delete(0,END)
                genre.delete(0,END)
                lang.delete(0,END)
                cost.delete(0,END)
                date.delete(0,END)
                bookid.focus()

        def logout():
                admin.quit()
                messagebox.showinfo("Admin page","You successfully logged out")

        Label(admin,text="WELCOME ADMIN!",font=("TIMES",13),fg="red").grid(row=0,column=1)
        Label(admin,text="BOOK ID").grid(row=1,column=0)
        Label(admin,text="BOOK NAME").grid(row=2,column=0)
        Label(admin,text="AUTHOR").grid(row=3,column=0)
        Label(admin,text="GENRE").grid(row=4,column=0)
        Label(admin,text="LANGUAGE").grid(row=5,column=0)
        Label(admin,text="COST").grid(row=6,column=0)
        Label(admin,text="PUBLISHED DATE").grid(row=7,column=0)
        Label(admin,text="*BOOK ID is sufficient for search/delete operations",font=("TIMES",8),fg="blue").grid(row=8,column=1)
        bookid=Entry(admin)
        bookid.grid(row=1,column=1)
        bookname=Entry(admin)
        bookname.grid(row=2,column=1)
        author=Entry(admin)
        author.grid(row=3,column=1)
        genre=Entry(admin)
        genre.grid(row=4,column=1)
        lang=Entry(admin)
        lang.grid(row=5,column=1)
        cost=Entry(admin)
        cost.grid(row=6,column=1)
        date=Entry(admin)
        date.grid(row=7,column=1)
        Button(admin,text="Insert",command=insert_book).grid(row=1,column=3)
        Button(admin,text="Search",command=search_book).grid(row=2,column=3)
        Button(admin,text="Remove",command=remove_book).grid(row=3,column=3)
        Button(admin,text="Display",command=display_book).grid(row=4,column=3)
        Button(admin,text="Cancel",command=cancel_book).grid(row=5,column=3)
        Button(admin,text="Log Out",command=logout).grid(row=6,column=3)
        admin.mainloop()        




#for user,
def login_main():
        login=Tk()
        login.title("LOGIN PANEL")
        login.geometry("300x175")


        def search_book():
                conn=sqlite3.connect("DATABASE.db")
                cursor=conn.cursor()
                bid=str(bookid.get())
                print("\nThe deatils of the book with id = "+ bid) 
                showdata=cursor.execute("SELECT * FROM BOOKS WHERE ID='%s'"%bid)
                for row in showdata:
                        print("\nBOOK ID : ",row[0])
                        print("BOOK NAME : ",row[1])
                        print("AUTHOR : ",row[2])
                        print("GENRE : ",row[3])
                        print("LANGUAGE : ",row[4])
                        print("COST(INR) : ",row[5])
                        print("PUBLISHED DATE : ",row[6])
                bookid.delete(0,END)
                bookid.focus()


        def display_book():
                conn=sqlite3.connect("DATABASE.db")
                cursor=conn.cursor()
                print("\nDetails in the DATABASE")
                showdata=cursor.execute("SELECT * FROM BOOKS ORDER BY NAME ")
                for row in showdata:
                        print("\nBOOK ID : ",row[0])
                        print("BOOK NAME : ",row[1])
                        print("AUTHOR : ",row[2])
                        print("GENRE : ",row[3])
                        print("LANGUAGE : ",row[4])
                        print("COST(INR) : ",row[5])
                        print("PUBLISHED DATE : ",row[6])
                bookid.delete(0,END)
                bookid.focus()


        def cancel_book():
                bookid.delete(0,END)
                bookname.delete(0,END)
                author.delete(0,END)
                bookid.focus()


        def logout():
                login.quit()
                messagebox.showinfo("Login page","You successfully logged out")



        Label(login,text="WELCOME USER!",font=("TIMES",13),fg="red").grid(row=0,column=1)
        Label(login,text="BOOK ID").grid(row=1,column=0)
        Label(login,text="BOOK NAME").grid(row=2,column=0)
        Label(login,text="AUTHOR").grid(row=3,column=0)
        Label(login,text="*BOOK ID is sufficient for search operations",font=("TIMES",8),fg="blue").grid(row=6,column=1)
        bookid=Entry(login)
        bookid.grid(row=1,column=1)
        bookname=Entry(login)
        bookname.grid(row=2,column=1)
        author=Entry(login)
        author.grid(row=3,column=1)
        Button(login,text="Search",command=search_book).grid(row=4,column=0)
        Button(login,text="Display",command=display_book).grid(row=4,column=1)
        Button(login,text="Cancel",command=cancel_book).grid(row=5,column=0)
        Button(login,text="Log Out",command=logout).grid(row=5,column=1)
        login.mainloop()


#function calling,
##admin_main()
##login_main()
