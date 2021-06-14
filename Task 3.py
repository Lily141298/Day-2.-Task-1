#Day3 - Python programming - Simple registration Form

#importing library
from tkinter import *
from tkinter import ttk

#Create object
root = Tk()

#Declaring Window Title
root.title("Registration Screen")

#Declaring Window size
root.geometry('300x300')

#Declaring Window Color
root.configure(background = "yellow")

#below four fields are declared
Firstname = Label(root ,text = "First Name",width=15,font=("bold",18)).grid(row = 0,column = 0)
LastName = Label(root ,text = "Last Name",width=15,font=("bold",18)).grid(row = 1,column = 0)
Email = Label(root,text = "Email Id",width=15,font=("bold",18)).grid(row = 2,column = 0)
Mobile = Label(root,text = "Contact Number",width=15,font=("bold",18)).grid(row = 3,column = 0)
Address = Label(root,text = "Address",width=15,font=("bold",18)).grid(row = 4,column = 0)
Country = Label(root,text = "Country",width=15,font=("bold",18)).grid(row = 5,column = 0)
Pincode= Label(root,text = "Pincode",width=15,font=("bold",18)).grid(row = 6,column = 0)

#List of country
list_of_country=['India','UK','US','China','Japan']

#Dropdown menu
a=StringVar()
dropdown = OptionMenu(root,a,*list_of_country)
dropdown.config(width=18)
a.set('Select Country')
dropdown.grid(row = 5,column = 1)

Gender =Label(root ,text = "Gender",width=15,font=("bold", 18)).grid(row = 9,column = 0)
Emp_id = Label(root ,text = "Emp id",width=15,font=("bold", 18)).grid(row = 8,column = 0)
var=IntVar()
Radiobutton(root, text="Male",padx = 20, variable=var, value=1).grid(row = 9,column = 1)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).grid(row = 9,column = 2)
Choose =Label(root ,text = "Date of Birth",width=15,font=("bold", 18)).grid(row = 11,column = 0)
var=IntVar()
L2 = Label(root, text="Language known",width=15,font=("bold", 18))
L2.grid(row = 10,column = 0)
var = IntVar()
Checkbutton(root, text="java", variable=var).grid(row = 10,column = 1)
var = IntVar()
Checkbutton(root, text="python", variable=var).grid(row = 10,column = 2)

Firstname1 = Entry(root).grid(row = 0,column = 1)
Lastname1 = Entry(root).grid(row = 1,column = 1)
Email1 = Entry(root).grid(row = 2,column = 1)
Mobile = Entry(root).grid(row = 3,column = 1)
Country = Entry(root).grid(row = 4,column = 1)
Pincode = Entry(root).grid(row = 6,column = 1)
Employee_id = Entry(root).grid(row = 8,column = 1)
DateofBirth = Entry(root).grid(row = 11,column = 1)


#fubction declaration
def clicked():
    root= "Welcome" + txt.get()
L2.configure(text= root)
Button(root, text="Submit", command=clicked,width=15).grid(row = 14,column = 3)
root.mainloop()

