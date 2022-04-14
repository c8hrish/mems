from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog

from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime, date

import sqlite3

class Membersin:
    def __init__(self,root):
        self.root=root
        self.root.title("सदस्य व्यवस्थापन प्रणाली -- प्रागतिक सहजीवन संस्था, नागपूर ")
        self.root.geometry("1280x720+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        #Title
        title=Label(self.root,text="नवीन सदस्य जोडणी",relief=RIDGE,anchor="w",padx=10,font=("arial",20,"bold"),bg="#FFF6CD",fg="#3B0000")
        title.place(x=0,y=0,relwidth=1,height=80)

        #Variables
        self.var_fname=StringVar()
        self.var_mname=StringVar()
        self.var_lname=StringVar()
        self.var_mothname=StringVar()
    
        self.var_address1=StringVar()
        self.var_address2=StringVar()
        self.var_loca=StringVar()
        self.var_teh=StringVar()
        self.var_distr=StringVar()
        self.var_pinco=StringVar()
        self.var_state=StringVar()
        self.var_country=StringVar()

        self.var_dob=StringVar()
        self.var_contno=StringVar()
        self.var_altno=StringVar()
        self.var_whatno=StringVar()       
        self.var_aadhar=StringVar()
        self.var_emailid=StringVar()

        self.var_memid=StringVar()
        self.var_applid=StringVar()
        self.var_appldt=StringVar()

        self.Checkbutton1=IntVar()  
        self.Checkbutton2=IntVar()  

        #Menu 3
        M_Frame3=LabelFrame(self.root,text="वैयक्तिक माहिती",font=("goudy old style",18,"bold"),bg="white",fg="#3D087B")
        M_Frame3.place(x=20,y=115,width=900,height=330)

        #Labels
        lbl_fname=Label(M_Frame3,text="पहिले नाव:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_fname.place(x=10,y=10)
        
        lbl_mname=Label(M_Frame3,text="मधले नाव:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_mname.place(x=300,y=10)
        
        lbl_lname=Label(M_Frame3,text="आडनाव:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_lname.place(x=600,y=10)        

        lbl_address1=Label(M_Frame3,text="पत्ता  १:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_address1.place(x=10,y=50)
        lbl_address2=Label(M_Frame3,text="पत्ता  २:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_address2.place(x=300,y=50)

        lbl_address2=Label(M_Frame3,text="गांव:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_address2.place(x=600,y=50)

        lbl_teh=Label(M_Frame3,text="तालुका:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_teh.place(x=10,y=90)
        lbl_distr=Label(M_Frame3,text="ज़िल्हा:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_distr.place(x=300,y=90)
        lbl_state=Label(M_Frame3,text="राज्य:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_state.place(x=600,y=90)
        lbl_country=Label(M_Frame3,text="देश:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_country.place(x=10,y=130)
        lbl_pinco=Label(M_Frame3,text="पिन कोड:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_pinco.place(x=300,y=130)
        
        lbl_contno1=Label(M_Frame3,text="संपर्क क्र. १",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_contno1.place(x=10,y=170)

        lbl_altno=Label(M_Frame3,text="संपर्क क्र. २",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_altno.place(x=300,y=170)
        
        lbl_whatno=Label(M_Frame3,text="व्हॉट्सऍप क्र.",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_whatno.place(x=600,y=170)

        lbl_dob=Label(M_Frame3,text="जन्मतारीख:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_dob.place(x=10,y=210)
        
        lbl_aadhar=Label(M_Frame3,text="आधार क्र.",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_aadhar.place(x=300,y=210)
        
        lbl_emailid=Label(M_Frame3,text="ई-मेल:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_emailid.place(x=600,y=210)
        
        lbl_mothname=Label(M_Frame3,text="आईचे माहेरचे नाव-आडनाव:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_mothname.place(x=10,y=250)

        lbl_addnote=Label(M_Frame3,text="अतिरिक्त माहिती:",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_addnote.place(x=410,y=250)

        #Menu 4
        M_Frame4=LabelFrame(self.root,text="कार्यालयीन नोंदी",font=("goudy old style",18,"bold"),bg="white",fg="#3D087B")
        M_Frame4.place(x=20,y=455,width=900,height=150)
        
        lbl_memid=Label(M_Frame4,text="सदस्य क्र.",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_memid.place(x=10,y=10)
        lbl_applid=Label(M_Frame4,text="ठराव क्र.",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_applid.place(x=300,y=10)
        lbl_applidate=Label(M_Frame4,text="ठराव दि.",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        lbl_applidate.place(x=600,y=10)

        # lbl_appr1=Label(M_Frame4,text="अध्यक्षांची स्वीकृती",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        # lbl_appr1.place(x=10,y=50)
        # lbl_appr2=Label(M_Frame4,text="सचिवांची मान्यता",font=('goudy old style',12,"bold"),bg="white",fg="#171717")
        # lbl_appr2.place(x=300,y=50)

        #Menu 5
        self.M_Frame5=LabelFrame(self.root,text="पासपोर्ट साईज फोटो",font=("goudy old style",18,"bold"),bg="white",fg="#3D087B")
        self.M_Frame5.place(x=935,y=115,width=300,height=330)
        self.button = Button(self.M_Frame5, text = "फोटो शोधा",command = self.fileDialog)
        self.button.place(x=120,y=20)

        #TextFields
        self.txt_fname=Entry(M_Frame3,textvariable=self.var_fname,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_fname.place(x=100,y=10,width=175)
        
        self.txt_mname=Entry(M_Frame3,textvariable=self.var_mname,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_mname.place(x=390,y=10,width=175)
        
        self.txt_lname=Entry(M_Frame3,textvariable=self.var_lname,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_lname.place(x=690,y=10,width=175)

        self.txt_address1=Entry(M_Frame3,textvariable=self.var_address1,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_address1.place(x=100,y=50,width=175)
        self.txt_address2=Entry(M_Frame3,textvariable=self.var_address2,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_address2.place(x=390,y=50,width=175)
        self.txt_location=Entry(M_Frame3,textvariable=self.var_loca,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_location.place(x=690,y=50,width=175)
        self.txt_teh=Entry(M_Frame3,textvariable=self.var_teh,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_teh.place(x=100,y=90,width=175)
        self.txt_distr=Entry(M_Frame3,textvariable=self.var_distr,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_distr.place(x=390,y=90,width=175)
        self.statechoosen = ttk.Combobox(M_Frame3, textvariable = self.var_state)
        self.statechoosen.place(x=690,y=90,width=175)
        self.statechoosen['values']=(
            'अंदमान व निकोबार द्वीपसमुह','आंध्र प्रदेश','अरुणाचल प्रदेश','आसाम','बिहार','छत्तीसगढ','गोवा','गुजरात','हरियाणा',
            'हिमाचल प्रदेश','झारखंड','कर्नाटक','केरळ','मध्य प्रदेश','महाराष्ट्र','मणीपुर','मेघालय','मिजोरम',
            'नागालँड','ओडिशा','पंजाब','राजस्थान','सिक्कीम','तामिळनाडू','तेलंगण','त्रिपुरा','उत्तर प्रदेश',
            'उत्तराखंड','पश्चिम बंगाल','Other'
        )
        self.countrychoosen = ttk.Combobox(M_Frame3, textvariable = self.var_country)
        self.countrychoosen.place(x=100,y=130,width=175)
        self.countrychoosen['values']=(
            'भारत','Other'
        )
        self.txt_pinco=Entry(M_Frame3,textvariable=self.var_pinco,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_pinco.place(x=390,y=130,width=175)

        self.txt_contno=Entry(M_Frame3,textvariable=self.var_contno,font=('goudy old style',12,"bold"),bg="lightyellow",fg="#171717")
        self.txt_contno.place(x=100,y=170,width=175)
        self.txt_altno=Entry(M_Frame3,textvariable=self.var_altno,font=('goudy old style',12,"bold"),bg="lightyellow",fg="#171717")
        self.txt_altno.place(x=390,y=170,width=175)
        self.txt_whatno=Entry(M_Frame3,textvariable=self.var_whatno,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_whatno.place(x=690,y=170,width=175)

        self.cal=DateEntry(M_Frame3, selectmode='day',textvariable=self.var_dob, cursor="hand2", background='lightyellow',foreground='#171717', year=2000, month=1, day=1)
        self.cal.place(x=100,y=210,width=175)

        self.txt_aadhar=Entry(M_Frame3,textvariable=self.var_aadhar,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_aadhar.place(x=390,y=210,width=175)
        
        self.txt_emailid=Entry(M_Frame3,textvariable=self.var_emailid,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_emailid.place(x=690,y=210,width=175)

        self.txt_mothname=Entry(M_Frame3,textvariable=self.var_mothname,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_mothname.place(x=210,y=250,width=175,height=25)

        self.txt_addnote=Text(M_Frame3,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_addnote.place(x=550,y=250,width=300,height=35)
        
        self.txt_memid=Entry(M_Frame4,textvariable=self.var_memid,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_memid.place(x=100,y=10,width=175)

        self.txt_applid=Entry(M_Frame4,textvariable=self.var_applid,font=('goudy old style',12),bg="lightyellow",fg="#171717")
        self.txt_applid.place(x=390,y=10,width=175)

        today = date.today()
        self.cal2=DateEntry(M_Frame4, selectmode='day',textvariable=self.var_appldt, cursor="hand2", background='lightyellow',foreground='#171717', year=today.year, month=today.month, day=today.day)
        self.cal2.place(x=690,y=10,width=175)

        self.check1 = Checkbutton(M_Frame4, text = "सचिव मान्यता", font=('goudy old style',12,"bold"),
                      variable = self.Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

        self.check1.place(x=250,y=50)
  
        self.check2 = Checkbutton(M_Frame4, text = "अध्यक्ष स्वीकृती", font=('goudy old style',12,"bold"),
                      variable = self.Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)
        self.check2.place(x=450,y=50)


        #Buttons
        canc_memb=Button(self.root,text="रद्द करा",font=("arial",15,"bold"),bg="#FF5C58",fg="white",bd=5,relief=RIDGE,cursor="hand2")
        canc_memb.place(x=955,y=500,width=120,height=60)

        save_memb=Button(self.root,text="जतन करा",font=("arial",15,"bold"),bg="#3DB2FF",fg="white",bd=5,relief=RIDGE,cursor="hand2",command=self.add)
        save_memb.place(x=1100,y=500,width=120,height=60)

    #Functions
        
    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.M_Frame5, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)

        img = Image.open(self.filename)
        img = img.resize((144,192),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

        self.label2 = Label(self.M_Frame5, image=photo)
        self.label2.image = photo 
        self.label2.place(x=75, y=60)
    
    def add(self):
        con=sqlite3.connect(database="mems.db")
        cur=con.cursor()
        try:
            if self.var_fname.get()=="" or self.var_mname.get()=="" or self.var_lname.get()=="" or self.var_address1.get()=="" or self.var_loca.get()=="" or self.var_teh.get()=="" or self.var_distr.get()=="" or self.var_contno.get()=="" or self.var_aadhar.get()=="" or self.var_dob.get()=="" or self.Checkbutton1=="0" or self.Checkbutton2=="0":
                messagebox.showerror("त्रुटी","अपूर्ण माहिती अस्वीकार्य. कृपया संपूर्ण तपशील पुरवा.",parent=self.root)
            else:
                cur.execute("select * from members where uid=?", (self.var_aadhar.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("त्रुटी","आधार क्रमांक आधीच नोंदणीकृत आहे. कृपया तपासून पहा.",parent=self.root)
                else:
                    cur.execute("insert into members (fname, mname, lname, addr1, addr2, place, tehs, distr, state, country, pinco, contaNum, altNum, whatNum, dob, uid, eid, mothermname descr, applid, appldt, check1, check2) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_fname.get(),
                        self.var_mname.get(),
                        self.var_lname.get(),
                    
                        self.var_address1.get(),
                        self.var_address2.get(),
                        self.var_loca.get(),
                        self.var_teh.get(),
                        self.var_distr.get(),
                        self.var_state.get(),
                        self.var_country.get(),
                        self.var_pinco.get(),
                        
                        self.var_contno.get(),
                        self.var_altno.get(),
                        self.var_whatno.get(),
                        self.var_dob.get(),  
                        self.var_aadhar.get(),
                        self.var_emailid.get(),
                        self.var_mothname.get(),
                        self.txt_addnote.get("1.0",END),

                        self.var_applid.get(),
                        self.var_appldt.get(),

                        self.Checkbutton1.get(),
                        self.Checkbutton2.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("यशस्वी","नवीन सभासदाची नोंदणी संपूर्णपणे यशस्वी..!",parent=self.root)
        except Exception as exc:
            messagebox.showerror("Error",f"Error due to {str(exc)}")

if __name__ == "__main__":
    root=Tk()
    obj=Membersin(root)
    root.mainloop()