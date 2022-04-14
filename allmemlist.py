from tkinter import * 
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import pyglet, os
import sqlite3

class Membersvi:
    def __init__(self,root):
        self.root=root
        self.root.title("सदस्य व्यवस्थापन प्रणाली -- प्रागतिक सहजीवन संस्था, नागपूर ")
        self.root.geometry("1280x720+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        #Title
        title=Label(self.root,text="संपूर्ण सदस्य यादी",relief=RIDGE,anchor="w",padx=10,font=("arial",20,"bold"),bg="#FFF6CD",fg="#3B0000")
        title.place(x=0,y=0,relwidth=1,height=80)

        #Menu 6 
        M_Frame6=LabelFrame(self.root,text="क्रमवार",font=("goudy old style",18,"bold"),bg="white",fg="#3D087B")
        M_Frame6.place(x=20,y=115,width=300,height=500)

        lbl_search=Label(M_Frame6,text="शोध",bg="white",fg="#111111")
        lbl_search.place(x=10,y=20)
        
        self.search_list=StringVar()
        
        self.search_li=Entry(M_Frame6,textvariable=self.search_list,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.search_li.place(x=60,y=20,width=175)

        #Content

        #Menu 7
        self.M_Frame7=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        self.M_Frame7.place(x=335,y=115,width=900,height=555)

        scrolly=Scrollbar(self.M_Frame7,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx=Scrollbar(self.M_Frame7,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)

        self.MembersTable=ttk.Treeview(self.M_Frame7, columns=("memid","fullname","age","contaNum","uid","addr2"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.config(command=self.MembersTable.xview)
        scrolly.config(command=self.MembersTable.yview)

        style = ttk.Style()
        style.configure("Treeview.Heading")

        self.MembersTable.heading("memid",text="सदस्य क्र.", anchor="w")
        self.MembersTable.heading("fullname",text="संपूर्ण नाव", anchor="w")
        self.MembersTable.heading("age",text="वय", anchor="w")
        self.MembersTable.heading("contaNum",text="संपर्क क्र.", anchor="w")
        self.MembersTable.heading("uid",text="आधार क्र.", anchor="w")
        self.MembersTable.heading("addr2",text="गांव", anchor="w")
        self.MembersTable["show"]="headings"

        self.MembersTable.column("memid",width=50)
        self.MembersTable.column("fullname",width=100)
        self.MembersTable.column("age",width=50)
        self.MembersTable.column("contaNum",width=150)
        self.MembersTable.column("uid",width=150)
        self.MembersTable.column("addr2",width=100)
        self.MembersTable.pack(fill=BOTH,expand=1)
        
        self.show()

    #Functions
    def show(self):
        con=sqlite3.connect(database="mems.db")
        cur=con.cursor()
        try:
            cur.execute("select * from members")
            rows=cur.fetchall()
            self.MembersTable.delete(*self.MembersTable.get_children())
            for row in rows:
                self.MembersTable.insert('',END,values=row)
        except Exception as exc:
            messagebox.showerror("Error",f"Error due to {str(exc)}")


    #Buttons
        print_list=Button(self.root,text="छपाई करा",font=("arial",12,"bold"),bg="#FF5C58",fg="white",bd=5,relief=RIDGE,cursor="hand2")
        print_list.place(x=100,y=625,width=120,height=45)

if __name__ == "__main__":
    root=Tk()
    obj=Membersvi(root)
    root.mainloop()