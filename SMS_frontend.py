from tkinter import *
import tkinter.messagebox
import SMS_backend as pb

class Student:
    
    def __init__(self, root):
        self.root = root 
        self.root.title("Student Database Management System")
        self.root.geometry(newGeometry="1225x585+0+0")
        self.root.config(bg="white")
        self.root.resizable(width=True, height=True)

        
        # Assign some variables to store our entry field values
        studentId = StringVar()
        firstName = StringVar()
        lastname = StringVar()
        dob = StringVar()
        age = StringVar()
        gender = StringVar()
        address = StringVar()
        mobile = StringVar()
        
        # FUNCTIONS 
        pb.studentData()
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("E-JUST Student DBMS", "Confirm if you want to exit")
            if iExit > 0:
                self.root.destroy()
                return
        
        def clearData():
            self.txtStudentId.delete(0, END)
            self.txtFirstName.delete(0, END)
            self.txtlastname.delete(0, END)
            self.txtDob.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtMobile.delete(0, END) 
        
        pb.studentData()
        
        def addData():
            if len(studentId.get()) != 0:
                pb.addStudentRecord(studentId.get(), firstName.get(), lastname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (studentId.get(), firstName.get(), lastname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()))

        def displayData():
            studentList.delete(0, END)
            for row in pb.viewStudentData():
                studentList.insert(END, row)

        def studentRec(event):
            global sd
            searchStd = studentList.curselection()[0]
            sd = studentList.get(searchStd)
            self.txtStudentId.delete(0, END)
            self.txtStudentId.insert(END, sd[0])
            self.txtFirstName.delete(0, END)
            self.txtFirstName.insert(END, sd[1])
            self.txtlastname.delete(0, END)
            self.txtlastname.insert(END, sd[2])
            self.txtDob.delete(0, END)
            self.txtDob.insert(END, sd[3])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[4])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[5])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, sd[6])
            self.txtMobile.delete(0, END)  
            self.txtMobile.insert(END, sd[7])                         
        
        def deleteData():
            if len(studentId.get()) != 0:
                pb.deleteStudentRecord(sd[0])
                clearData()
                displayData()
        
        def searchDatabase():
            studentList.delete(0, END)
            for row in pb.searchStudentData(studentId.get(), firstName.get(), lastname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()):
                studentList.insert(END, row, str(""))       
        
        def update():
            if len(studentId.get()) != 0:
                pb.deleteStudentRecord(sd[0])
            if len(studentId.get()) != 0:
                pb.addStudentRecord(studentId.get(), firstName.get(), lastname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get())
                studentList.delete(0, END)
                studentList.insert(END, (studentId.get(), firstName.get(), lastname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()))   

        #FRAMES 
        MainFrame = Frame(self.root, bg="white")
        MainFrame.grid()  # THIS IS MAIN FRAME OUR WINDOW
        TitFrame = Frame(MainFrame, bd=1, padx=54, pady=8, bg="gray", relief=RIDGE)
        TitFrame.pack(side=TOP)  # THIS IS STITLE FRAME
    
        self.lblTit = Label(TitFrame, font=('Times', 47, 'bold'), text="Students Database Management System", bg="gray", fg="black")
        self.lblTit.grid()

        self.lblTit = Label(TitFrame, font=('Times', 25, 'bold'), text="E-JUST UNIVERSITY", bg="gray", fg="black")
        self.lblTit.grid()


        ButtonFrame = Frame(MainFrame, bd=1, width=1350, height=70, padx=18, pady=10, bg="gray", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)#

        DataFrame = Frame(MainFrame, bd=9, width=1300, height=400, padx=20, pady=20, bg="#555", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)  # THIS IS STI
         
        DataFrameLeft = LabelFrame(DataFrame, font=('Times', 12, 'bold'), bd=1, width=450, height=300, bg="Ghost White", relief=RIDGE, text="STUDENT INFO\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, font=('Times', 12, 'bold'), bd=1, width=450, height=300, bg="Ghost White", relief=RIDGE, text="STUDENT DETAILS\n")
        DataFrameRight.pack(side=RIGHT)
        #Lables and entry widget 
       
        self.lblStudentId = Label(DataFrameLeft, font=('Times', 12, 'bold'), padx=2, pady=3, text="Student Id:", bg="ghost white")
        self.lblStudentId.grid(row=0, column=0, sticky=W)
       
        self.txtStudentId = Entry(DataFrameLeft, font=('Times', 12, 'bold'), textvariable=studentId, bg="ghost white", width=39)
        self.txtStudentId.grid(row=0, column=1)  # student id

        self.lblFirstName = Label(DataFrameLeft, font=('Times', 12, 'bold'), padx=2, pady=3, text="First Name:", bg="ghost white")
        self.lblFirstName.grid(row=1, column=0, sticky=W)
       
        self.txtFirstName = Entry(DataFrameLeft, font=('Times', 12, 'bold'), textvariable=firstName, bg="ghost white", width=39)
        self.txtFirstName.grid(row=1, column=1)  # firstname

        self.lbllastname = Label(DataFrameLeft, font=('Times', 12, 'bold'), padx=2, pady=3, text="Last Name:", bg="ghost white")
        self.lbllastname.grid(row=2, column=0, sticky=W)
       
        self.txtlastname = Entry(DataFrameLeft, font=('Times', 12, 'bold'), textvariable=lastname, bg="ghost white", width=39)
        self.txtlastname.grid(row=2, column=1)  # surname

        self.lblDob = Label(DataFrameLeft, font=('Times', 12, 'bold'), padx=2, pady=3, text="Date of Birth", bg="ghost white")
        self.lblDob.grid(row=3, column=0, sticky=W)
       
        self.txtDob = Entry(DataFrameLeft, font=('Times', 12, 'bold'), textvariable=dob, bg="ghost white", width=39)
        self.txtDob.grid(row=3, column=1)  # dateof birth

        self.lblAge = Label(DataFrameLeft, font=('Times', 12, 'bold'), padx=2, pady=3, text="Age:", bg="ghost white")
        self.lblAge.grid(row=4, column=0, sticky=W)
       
        self.txtAge = Entry(DataFrameLeft, font=('Times', 12, 'bold'), textvariable=age, bg="ghost white", width=39)
        self.txtAge.grid(row=4, column=1)  # age

        self.lblGender = Label(DataFrameLeft, font=('Times', 12, 'bold'), padx=2, pady=3, text="Gender:", bg="ghost white")
        self.lblGender.grid(row=5, column=0, sticky=W)
       
        self.txtGender = Entry(DataFrameLeft, font=('Times', 12, 'bold'), textvariable=gender, bg="ghost white", width=39)
        self.txtGender.grid(row=5, column=1)  # gender

        self.lblAddress = Label(DataFrameLeft, font=('Times', 12, 'bold'), padx=2, pady=3, text="Address:", bg="ghost white")
        self.lblAddress.grid(row=6, column=0, sticky=W)
       
        self.txtAddress = Entry(DataFrameLeft, font=('Times', 12, 'bold'), textvariable=address, bg="ghost white", width=39)
        self.txtAddress.grid(row=6, column=1)  # address

        self.lblMobile = Label(DataFrameLeft, font=('Times', 12, 'bold'), padx=2, pady=3, text="Mobile:", bg="ghost white")
        self.lblMobile.grid(row=7, column=0, sticky=W)
       
        self.txtMobile = Entry(DataFrameLeft, font=('Times', 12, 'bold'), textvariable=mobile, bg="ghost white", width=39)
        self.txtMobile.grid(row=7, column=1)  # mobile

        # List Box and ScrollBar Widget 
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0 ,column=1, sticky='ns')  # scroll bar

        studentList = Listbox(DataFrameRight, width=68, height=12, font=('Times', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentList.bind('<<ListboxSelect>>', studentRec)
        studentList.grid(row=0, column=0, padx=10)
        scrollbar.config(command=studentList.yview)

        # Button Widget
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('Times', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=addData)
        self.btnAddData.grid(row=0, column=0)  # ADD NEW

        self.btnDisplay = Button(ButtonFrame, text="Display", font=('Times', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=displayData)
        self.btnDisplay.grid(row=0, column=1)  # DISPLAY

        self.btnClear = Button(ButtonFrame, text="Clear", font=('Times', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=clearData)
        self.btnClear.grid(row=0, column=2)  # CLEAR

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('Times', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=deleteData)
        self.btnDelete.grid(row=0, column=3)  # DELETE

        self.btnSearch = Button(ButtonFrame, text="Search", font=('Times', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=searchDatabase)
        self.btnSearch.grid(row=0, column=4)  # SEARCH

        self.btnUpdate = Button(ButtonFrame, text="Update", font=('Times', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=update)
        self.btnUpdate.grid(row=0, column=5)  # UPDATE

        self.btnExit = Button(ButtonFrame, text="Exit", font=('Times', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=iExit)
        self.btnExit.grid(row=0, column=6)  # EXIT

if __name__ == '__main__':
    root = Tk()  # CREATE AN OBJECT
    application = Student(root)  # PASS IT TO OUR CLASS WITH ITS PROPERTIES IN CLASS
    root.mainloop()  # RUN UNTIL CLOSING THE WINDOW MANUALLY
