from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk         # pip install pillow
import mysql.connector
from tkinter import messagebox



class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

# Variables-------

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_mentor = StringVar()


# first image-----

        img1 = Image.open("images/image1.jpg")
        img1 = img1.resize((470,160),Image.ANTIALIAS)  # ANTIALIAS change the photo quality
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.btn1 = Button(self.root,image=self.photoimg1,cursor="hand2")
        self.btn1.place(x=0,y=0,width=470,height = 160)

# second image -----

        img2 = Image.open("images/image4.png")
        img2 = img2.resize((470,160),Image.ANTIALIAS)  # ANTIALIAS change the photo quality
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.btn2 = Button(self.root,image=self.photoimg2,cursor="hand2")
        self.btn2.place(x=470,y=0,width=470,height = 160)


# third image ------  

        img3 = Image.open("images/image3.jpg")
        img3 = img3.resize((470,160),Image.ANTIALIAS)  # ANTIALIAS change the photo quality
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.btn3 = Button(self.root,image=self.photoimg3,cursor="hand2")
        self.btn3.place(x=900,y=0,width=470,height = 160)

# background image----

        img_bg = Image.open("images/bbd.jpg")
        img_bg = img_bg.resize((1530,710),Image.ANTIALIAS)  # ANTIALIAS change the photo quality
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        bg_lbl = Label(self.root,image=self.photoimg_bg,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)
# lable title-----
        lbl_title = Label(bg_lbl,text="Student Managemant System", font=("times new roman",30,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)


# Manage frame---

        Manage_frame = Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=25,y=60,width=1300,height=480)

# left frame---

        DataLeftFrame = LabelFrame(Manage_frame,bd=2,text="Student Information",font=("times new roman",15,),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=5,width=630,height=470)

# left frame photo----

        img_frame = Image.open("images/images5.jpg")
        img_frame = img_frame.resize((625,120),Image.ANTIALIAS)  # ANTIALIAS change the photo quality
        self.photoimg_frame = ImageTk.PhotoImage(img_frame)

        bg_lbl1 = Label(DataLeftFrame,image=self.photoimg_frame,bd=2,relief=RIDGE)
        bg_lbl1.place(x=0,y=0,width=625,height=120)

# Current course labelframe information-----

        std_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",15,),fg="green",bg="white")
        std_info_frame.place(x=2,y=120,width=620,height=100)

# Labels-----

# Course----

        course = Label(std_info_frame,text="Course",font=("arial",12,"bold"),bg="white")
        course.grid(row=0,column=0,padx=2,sticky=W)

        combo_course = ttk.Combobox(std_info_frame,textvariable= self.var_course,font=("arial",10),width=17,state="readonly")
        combo_course["value"]=("Select Course","B.tech","M.Tech","B.Pharma","Diploma")
        combo_course.current(0)
        combo_course.grid(row=0,column=1,padx=20,pady=10,sticky=W)

#  Department---
        dept = Label(std_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
        dept.grid(row=0,column=2,padx=20,sticky=W)

        combo_dept = ttk.Combobox(std_info_frame,textvariable=self.var_dep,font=("arial",10),width=17,state="readonly")
        combo_dept["value"]=("Select Department","CSE","IT","CIVIL","MECHENICAL","ELECTRICAL","Pharmacy")
        combo_dept.current(0)
        combo_dept.grid(row=0,column=3,padx=0,pady=10,sticky=W)

# Year----

        year = Label(std_info_frame,text="Year",font=("arial",12,"bold"),bg="white")
        year.grid(row=1,column=0,padx=2,sticky=W)

        combo_year = ttk.Combobox(std_info_frame,textvariable= self.var_year,font=("arial",10),width=17,state="readonly")
        combo_year["value"]=("Select Year","First Year","Second Year","Third Year","Fourth Year")
        combo_year.current(0)
        combo_year.grid(row=1,column=1,padx=20,sticky=W)

# Semester---

        semester = Label(std_info_frame,text="Semester",font=("arial",12,"bold"),bg="white")
        semester.grid(row=1,column=2,padx=20,sticky=W)

        combo_semester = ttk.Combobox(std_info_frame,textvariable= self.var_semester,font=("arial",10),width=17,state="readonly")
        combo_semester["value"]=("Select Semester","First","Second","Third","Fourth","Five","Six","Seven","Eight")
        combo_semester.current(0)
        combo_semester.grid(row=1,column=3,padx=0,sticky=W)


# Class course labelframe information-----

        class_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Class Course Information",font=("times new roman",15,),fg="green",bg="white")
        class_info_frame.place(x=2,y=220,width=620,height=180)
# Student id level---
        student_id = Label(class_info_frame,text="Student_Id",font=("arial",12,"bold"),bg="white")
        student_id.grid(row=0,column=0,padx=2,pady=2,sticky=W)

        id_entry=ttk.Entry(class_info_frame,textvariable= self.var_std_id,font=("arial",10,),width=20)
        id_entry.grid(row=0,column=1,padx=10,pady=2)

# Student name level---
        student_name = Label(class_info_frame,text="Name",font=("arial",12,"bold"),bg="white")
        student_name.grid(row=0,column=2,padx=25,pady=2,sticky=W)

        name_entry=ttk.Entry(class_info_frame,textvariable= self.var_name,font=("arial",10,),width=20)
        name_entry.grid(row=0,column=3,padx=2,pady=2)

# Student Roll Number level---
        roll_number = Label(class_info_frame,text="Roll_Number",font=("arial",12,"bold"),bg="white")
        roll_number.grid(row=1,column=0,padx=2,pady=2,sticky=W)

        roll_number_entry=ttk.Entry(class_info_frame,textvariable= self.var_roll,font=("arial",10,),width=20)
        roll_number_entry.grid(row=1,column=1,padx=2,pady=2)
# Division---
        division = Label(class_info_frame,text="Division",font=("arial",12,"bold"),bg="white")
        division.grid(row=1,column=2,padx=20,pady=2,sticky=W)
        combo_division = ttk.Combobox(class_info_frame,textvariable= self.var_div,font=("arial",12),width=14,state="readonly")
        combo_division["value"]=("Select Division","Section A","Section B","Section C","Section D")
        combo_division.current(0)
        combo_division.grid(row=1,column=3,padx=0,pady=2,sticky=W)

# gender---
        gender = Label(class_info_frame,text="Gender",font=("arial",12,"bold"),bg="white")
        gender.grid(row=2,column=0,padx=2,pady=2,sticky=W)
        combo_gender = ttk.Combobox(class_info_frame,textvariable= self.var_gender,font=("arial",12),width=14,state="readonly")
        combo_gender["value"]=("Select Gender","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1,padx=7,pady=2,sticky=W)

# Student Date of Birth
        dob = Label(class_info_frame,text="Date of Birth",font=("arial",12,"bold"),bg="white")
        dob.grid(row=2,column=2,padx=2,pady=2,sticky=W)

        dob_entry=ttk.Entry(class_info_frame,textvariable= self.var_dob,font=("arial",10,),width=20)
        dob_entry.grid(row=2,column=3,padx=2,pady=2)

# Student contact number
        mob = Label(class_info_frame,text="Mobile No.",font=("arial",12,"bold"),bg="white")
        mob.grid(row=3,column=0,padx=2,pady=2,sticky=W)

        mob_entry=ttk.Entry(class_info_frame,textvariable= self.var_phone,font=("arial",10,),width=20)
        mob_entry.grid(row=3,column=1,padx=2,pady=2)

# Student Email_id
        email = Label(class_info_frame,text="Email_Id",font=("arial",12,"bold"),bg="white")
        email.grid(row=3,column=2,padx=2,pady=2,sticky=W)

        email_entry=ttk.Entry(class_info_frame,textvariable= self.var_email,font=("arial",10,),width=20)
        email_entry.grid(row=3,column=3,padx=2,pady=2)

# Student Address
        address = Label(class_info_frame,text="Address",font=("arial",12,"bold"),bg="white")
        address.grid(row=4,column=0,padx=2,pady=2,sticky=W)

        address_entry=ttk.Entry(class_info_frame,textvariable= self.var_address,font=("arial",10,),width=20)
        address_entry.grid(row=4,column=1,padx=2,pady=2)

# Student mentor
        mentor = Label(class_info_frame,text="Mentor",font=("arial",12,"bold"),bg="white")
        mentor.grid(row=4,column=2,padx=2,pady=2,sticky=W)

        dob_entry=ttk.Entry(class_info_frame,textvariable= self.var_mentor,font=("arial",10,),width=20)
        dob_entry.grid(row=4,column=3,padx=2,pady=2)

# button frame---

        btn_frame = Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=400,width=620,height=42)

        btn_add = Button(btn_frame,text="Save",command = self.add_data,font=("arial",11,"bold"),width=16,bg="blue",fg="white")
        btn_add.grid(row=0,column=0,padx=1)

        btn_update = Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=16,bg="blue",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete = Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=16,bg="blue",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset = Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=16,bg="blue",fg="white")
        btn_reset.grid(row=0,column=3,padx=1)

# right frame----

        DataRightFrame = LabelFrame(Manage_frame,bd=2,text="Student Information",font=("times new roman",15,),fg="red",bg="white")
        DataRightFrame.place(x=645,y=5,width=650,height=470)

# right frame photo---

        img_frame2 = Image.open("images/image2.jpg")
        img_frame2 = img_frame2.resize((645,120),Image.ANTIALIAS)  # ANTIALIAS change the photo quality
        self.photoimg_frame2 = ImageTk.PhotoImage(img_frame2)

        bg_lbl2 = Label(DataRightFrame,image=self.photoimg_frame2,bd=2,relief=RIDGE)
        bg_lbl2.place(x=0,y=0,width=645,height=120)

# search right  frame---

        DataSearchFrame = LabelFrame(DataRightFrame,bd=2,text="Search Student",font=("times new roman",15,),fg="red",bg="white")
        DataSearchFrame.place(x=0,y=120,width=645,height=60)
# Search lebel---
        search_by = Label(DataSearchFrame,font=("arial",11,"bold"),text="Search By :",fg="black",bg="brown")
        search_by.grid(row=0,column=0,padx=5)
# Combo search field

        self.var_combo_search=StringVar()
        combo_search = ttk.Combobox(DataSearchFrame,textvariable=self.var_combo_search,font=("arial",12),width=14,state="readonly")
        combo_search["value"]=("Search Option","Name","Roll No","Phone","DOB")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5,sticky=W)
# Search entry field---

        self.var_search=StringVar()
        search_entry=ttk.Entry(DataSearchFrame,textvariable=self.var_search,font=("arial",12,),width=20)
        search_entry.grid(row=0,column=2,padx=2)
#button for search and show all data---
        btn_search = Button(DataSearchFrame,command=self.search_data,text="Search",font=("arial",11,"bold"),width=9,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=2)

        btn_showall = Button(DataSearchFrame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),width=9,bg="blue",fg="white")
        btn_showall.grid(row=0,column=4,padx=2)

# Student table and Scrollbar---

        tableFrame = LabelFrame(DataRightFrame,bd=4,relief=RIDGE)
        tableFrame.place(x=0,y=180,width=645,height=263)

        scroll_x = ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableFrame,orient=VERTICAL)
        self.student_table = ttk.Treeview(tableFrame,column=("dep","Course","Year","Sem","Id","Name","Div","Roll No","Gender","DOB","Phone","Email","Address","Mentor"),xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="Student_Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Date of Birth")
        self.student_table.heading("Phone",text="Contact")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Mentor",text="Mentor")

        self.student_table["show"]= "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Mentor",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if (self.var_dep.get()=="" or self.var_name.get()=="" or self.var_std_id.get()=="" or self.var_roll.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="c@123",database="student")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_dep.get(),
                                                                self.var_course.get(),
                                                                self.var_year.get(),
                                                                self.var_semester.get(),
                                                                self.var_std_id.get(),
                                                                self.var_name.get(),
                                                                self.var_div.get(),
                                                                self.var_roll.get(),
                                                                self.var_gender.get(),
                                                                self.var_dob.get(),
                                                                self.var_phone.get(),
                                                                self.var_email.get(),
                                                                self.var_address.get(),
                                                                self.var_mentor.get(),
                                                                
                ))
                 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
# fetch data from database

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="c@123",database="student")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,value=i)
            conn.commit()
        conn.close()
                

    # Get cursor 

    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_phone.set(data[10])
        self.var_email.set(data[11])
        self.var_address.set(data[12])
        self.var_mentor.set(data[13])


# update data---

    def update_data(self):
        if (self.var_dep.get()=="" or self.var_name.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                update = messagebox.askyesno("Update","Are You Sure Want to Update Student Data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="c@123",database="student")
                    my_cursor=conn.cursor()
                    my_cursor.execute(" update Student set dep=%s , Course=%s , Year=%s , Sem=%s , Name=%s , Div=%s , Roll No=%s , Gender=%s , DOB=%s , Phone=%s , Email=%s , Address=%s , Mentor=%s where Student_Id=%s " ,(

                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_mentor.get(),
                                                                                        self.var_std_id.get()
                                                                                                                                     
                                                                           ) ) 
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Student Successfully Updated",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)} ",parent=self.root)
                

             
# delete data----

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure want to delete this data",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="c@123",database="student")
                    my_cursor=conn.cursor()
                    sql = "delete from Student where Student_Id=%s"
                    value = (self.var_std_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student data has been deleted",parent=self.root )
    
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

# reset data---

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Year")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_mentor.set("")

# Search data---

    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please Select Option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="c@123",database="student")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from Student where " +str(self.var_combo_search.get())+" LIKE '%" +str(self.var_search.get())+"%'")
                data = my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
 