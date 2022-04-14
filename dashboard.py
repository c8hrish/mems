from tkinter import * 
from PIL import Image,ImageTk
from members import Membersin
from allmemlist import Membersvi

class MEMS:
    def __init__(self,root):
        self.root=root
        self.root.title("सदस्य व्यवस्थापन प्रणाली -- प्रागतिक सहजीवन संस्था, नागपूर ")
        self.root.geometry("1280x720+0+0")
        self.root.config(bg="white")

        #Icon
        self.logo_dash=ImageTk.PhotoImage(file="images/hope-logo.png")

        #Title
        title=Label(self.root,text="प्रागतिक सहजीवन संस्था, नागपूर",padx=10,compound=LEFT,image=self.logo_dash,font=("arial",25,"bold"),bg="#FFF6CD",fg="#E63E6D")
        title.place(x=0,y=0,relwidth=1,height=100)

        #Menu 1
        M_Frame1=LabelFrame(self.root,text="मुख्य सूची क्र. १",font=("goudy old style",18,"bold"),bg="white",fg="#3D087B")
        M_Frame1.place(x=20,y=115,width=500,height=300)

        #Button Modules 1
        btn_newmem=Button(M_Frame1,text="नवीन\nसदस्य जोडणी",font=('goudy old style',18,"bold"),bg="#FFF6CD",fg="#3B0000",cursor="hand2",command=self.add_member)
        btn_newmem.place(x=30,y=30,width=210,height=175)

        btn_updmem=Button(M_Frame1,text="सदस्य माहिती\nअद्ययावतीकरण",font=('goudy old style',18,"bold"),bg="#FFF6CD",fg="#3B0000",cursor="hand2")
        btn_updmem.place(x=250,y=30,width=210,height=175)

        #Menu 2
        M_Frame2=LabelFrame(self.root,text="मुख्य सूची क्र. २",font=("goudy old style",18,"bold"),bg="white",fg="#3D087B")
        M_Frame2.place(x=550,y=115,width=500,height=300)

        #Button Modules 2

        btn_allmem=Button(M_Frame2,text="संपूर्ण सदस्य यादी",font=('goudy old style',18,"bold"),bg="#FFF6CD",fg="#3B0000",cursor="hand2", command=self.view_info)
        btn_allmem.place(x=30,y=30,width=210,height=175)

        btn_archmem=Button(M_Frame2,text="सदस्य पत्ते",font=('goudy old style',18,"bold"),bg="#FFF6CD",fg="#3B0000",cursor="hand2")
        btn_archmem.place(x=250,y=30,width=210,height=175)

        # #Background Image
        # self.bg_img=Image.open("images/b-g.jpg")
        # self.bg_img=self.bg_img.resize((1170,315),Image.ANTIALIAS)
        # self.bg_img=ImageTk.PhotoImage(self.bg_img)

        # self.label_bg=Label(M_Frame,image=self.bg_img)
        # self.label_bg.place(x=10,y=135,width=1150,height=315)

        #Counter Button
        self.label_memb=Label(self.root,text="एकूण नोंदणीकृत\nसदस्य संख्या\n[0]",font=("arial",12,"bold"),bg="#FCF0C8",fg="#E63E6D",bd=10,relief=RIDGE)
        self.label_memb.place(x=1100,y=215,width=150,height=100)

        #Footer
        footer=Label(self.root,text="Made with ❤️by Sanjay Namdeorao Gulhane\n Contact us for any technical queries",font=("goudy old style",10),bg="#262626",fg="white")
        footer.pack(side=BOTTOM,fill=X)

    def add_member(self):
        self.new_win1=Toplevel(self.root)
        self.new_memobj=Membersin(self.new_win1)

    def view_info(self):
        self.new_win2=Toplevel(self.root)
        self.view_inobj=Membersvi(self.new_win2)

if __name__ == "__main__":
    root=Tk()
    obj=MEMS(root)
    root.mainloop()