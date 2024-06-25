from tkinter import *
import tkinter.messagebox
import sqlite3
from patient_form import Patient
from room_form import Room
from employee_form import Employee
from appointment_form import Appointment
from billing_form import Billing

# Establish connection to SQLite database
conn = sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

# Class For Menu    
class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x600+350+70")
        self.master.config(bg="light green")
        self.frame = Frame(self.master, bg="light green")
        self.frame.pack()
       
        self.lblTitle = Label(self.frame, text="MAIN MENU", font="Helvetica 20 bold", bg="light green")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        # Buttons for different functionalities
        self.button1 = Button(self.LoginFrame, text=" PATIENT REGISTRATION", width=30, font="Helvetica 14 bold", bg="gray", command=self.Patient_Reg)       
        self.button1.grid(row=1, column=0, pady=10)
        
        self.button2 = Button(self.LoginFrame, text=" ROOM ALLOCATION", width=30, font="Helvetica 14 bold", bg="purple", command=self.Room_Allocation)
        self.button2.grid(row=3, column=0, pady=10)
        
        self.button3 = Button(self.LoginFrame, text=" EMPLOYEE REGISTRATION", width=30, font="Helvetica 14 bold", bg="royalblue", command=self.Employee_Reg)
        self.button3.grid(row=5, column=0, pady=10)
        
        self.button4 = Button(self.LoginFrame, text=" BOOK APPOINTMENT", width=30, font="Helvetica 14 bold", bg="hotpink", command=self.Appointment_Form)
        self.button4.grid(row=7, column=0, pady=10)
        
        self.button5 = Button(self.LoginFrame, text=" PATIENT BILL", width=30, font="Helvetica 14 bold", bg="green", command=self.Billing_Form)
        self.button5.grid(row=9, column=0, pady=10)
        
        self.button6 = Button(self.LoginFrame, text=" EXIT", width=30, font="Helvetica 14 bold", bg="red", command=self.Exit)
        self.button6.grid(row=11, column=0, pady=10)
        
    # Function to Exit Menu Window
    def Exit(self):
        self.master.destroy()

    # Function to open Patient Registration Window   
    def Patient_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow)
        
    # Function to open Room Allocation Window   
    def Room_Allocation(self):
        self.newWindow = Toplevel(self.master)
        self.app = Room(self.newWindow)
        
    # Function to open Employee Registration Window 
    def Employee_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Employee(self.newWindow)
        
    # Function to open Appointment Window
    def Appointment_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Appointment(self.newWindow)
        
    # Function to open Billing Window
    def Billing_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Billing(self.newWindow)

# Function to start the application
def main():
    root = Tk()
    app = Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
