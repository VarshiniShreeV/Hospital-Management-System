from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Connect to SQLite database
conn = sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")


# Class for PATIENT REGISTRATION
class Patient:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="light green")
        self.frame = Frame(self.master, bg="light green")
        self.frame.pack()

        # Attributes
        self.pat_ID = IntVar()
        self.pat_name = StringVar()
        self.pat_dob = StringVar()
        self.pat_address = StringVar()
        self.pat_sex = StringVar()
        self.pat_BG = StringVar()
        self.pat_email = StringVar()
        self.pat_contact = IntVar()
        self.pat_contactalt = IntVar()
        self.pat_CT = StringVar()

        # Title
        self.lblTitle = Label(self.frame, text="PATIENT REGISTRATION FORM", font="Helvetica 20 bold", bg="light green")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # Frame
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels
        labels = [
            ("PATIENT ID", self.pat_ID, 0, 0),
            ("PATIENT NAME", self.pat_name, 1, 0),
            ("SEX", self.pat_sex, 2, 0),
            ("DOB (DD-MM-YYYY)", self.pat_dob, 3, 0),
            ("BLOOD GROUP", self.pat_BG, 4, 0),
            ("CONTACT NUMBER", self.pat_contact, 0, 2),
            ("ALTERNATE CONTACT", self.pat_contactalt, 1, 2),
            ("EMAIL", self.pat_email, 2, 2),
            ("CONSULTING TEAM / DOCTOR", self.pat_CT, 3, 2),
            ("ADDRESS", self.pat_address, 4, 2)
        ]

        for label_text, var, row, col in labels:
            lbl = Label(self.LoginFrame, text=label_text, font="Helvetica 14 bold", bg="light green", bd=22)
            lbl.grid(row=row, column=col)
            entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=var)
            entry.grid(row=row, column=col + 1)

         # =========== BUTTONS ==============
        self.button2 = Button(self.LoginFrame2, text="SUBMIT", width=10, font="Helvetica 14 bold", bg="green", command=self.INSERT_PAT)
        self.button2.grid(row=3, column=1)

        self.btnUpdateData = Button(self.LoginFrame2, text="UPDATE", width=10, font="Helvetica 14 bold", bg="light blue", command=self.UPDATE_PAT)
        self.btnUpdateData.grid(row=3, column=2)

        self.button3 = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="light coral", command=self.D_DISPLAY)
        self.button3.grid(row=3, column=3)

        self.button4 = Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="white", command=self.S_DISPLAY)
        self.button4.grid(row=3, column=4)

        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="red", command=self.Exit)
        self.button6.grid(row=3, column=5)

        


    # Function to insert data in patient form
    def INSERT_PAT(self):
        p1 = self.pat_ID.get()
        p2 = self.pat_name.get()
        p3 = self.pat_sex.get()
        p4 = self.pat_BG.get()
        p5 = self.pat_dob.get()
        p6 = self.pat_contact.get()
        p7 = self.pat_contactalt.get()
        p8 = self.pat_address.get()
        p9 = self.pat_CT.get()
        p10 = self.pat_email.get()

        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM PATIENT  WHERE PATIENT_ID =?", (p1,))
                if cursor.fetchone():
                    messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT_ID ALREADY EXISTS")
                else:
                    cursor.execute('INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?)', (p1, p2, p3, p4, p5, p8, p9, p10,))
                    cursor.execute('INSERT INTO CONTACT_NO VALUES (?,?,?)', (p1, p6, p7,))
                    messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS INSERTED INTO DATABASE")
        except sqlite3.Error as e:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", f"Error inserting data: {e}")

    # Function to update data in patient form
    def UPDATE_PAT(self):
        u1 = self.pat_ID.get()
        u2 = self.pat_name.get()
        u3 = self.pat_sex.get()
        u4 = self.pat_dob.get()
        u5 = self.pat_BG.get()
        u6 = self.pat_contact.get()
        u7 = self.pat_contactalt.get()
        u8 = self.pat_email.get()
        u9 = self.pat_CT.get()
        u10 = self.pat_address.get()

        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM PATIENT WHERE PATIENT_ID=?", (u1,))
                if cursor.fetchone():
                    cursor.execute('UPDATE PATIENT SET NAME=?,SEX=?,DOB=?,BLOOD_GROUP=?,ADDRESS=?,CONSULT_TEAM=?,EMAIL=? where PATIENT_ID=?',
                                   (u2, u3, u4, u5, u10, u9, u8, u1,))
                    cursor.execute('UPDATE CONTACT_NO set CONTACTNO=?,ALT_CONTACT=? WHERE PATIENT_ID=?', (u6, u7, u1,))
                    messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS UPDATED INTO DATABASE")
                else:
                    messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT IS NOT REGISTERED")
        except sqlite3.Error as e:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", f"Error updating data: {e}")

    # Function to exit patient registration window
    def Exit(self):
        self.master.destroy()

    # Function to open delete patient display window
    def D_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DMenu(self.newWindow)

    # Function to open search patient display window
    def S_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = SMenu(self.newWindow)


# Class for DELETE MENU FOR DELETE PATIENT
class DMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="light green")
        self.frame = Frame(self.master, bg="light green")
        self.frame.pack()

        self.del_pid = IntVar()
        self.lblTitle = Label(self.frame, text="DELETE WINDOW", font="Helvetica 20 bold", bg="light green")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # Frame
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels
        self.lblpatid = Label(self.LoginFrame, text="ENTER PATIENT ID TO DELETE", font="Helvetica 14 bold",
                              bg="light green", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.del_pid)
        self.lblpatid.grid(row=0, column=1)

        # Delete Button
        self.DeleteB = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="light coral",
                              command=self.DELETE_PAT)
        self.DeleteB.grid(row=3, column=1)

    # Function to delete data in patient form
    def DELETE_PAT(self):
        inp_d = self.del_pid.get()

        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM PATIENT WHERE PATIENT_ID = ?', (inp_d,))
                cursor.execute('DELETE FROM CONTACT_NO WHERE PATIENT_ID = ?', (inp_d,))
                messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "PATIENT RECORD DELETED")
        except sqlite3.Error as e:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", f"Error deleting data: {e}")

        self.master.destroy()


# Class for SEARCH MENU FOR SEARCHING PATIENT
class SMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="light green")
        self.frame = Frame(self.master, bg="light green")
        self.frame.pack()

        self.s_pid = IntVar()
        self.lblTitle = Label(self.frame, text="SEARCH WINDOW", font="Helvetica 20 bold", bg="light green")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # Frame
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels
        self.lblpatid = Label(self.LoginFrame, text="ENTER PATIENT ID TO SEARCH", font="Helvetica 14 bold",
                              bg="light green", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.s_pid)
        self.lblpatid.grid(row=0, column=1)

        # Search Button
        self.SearchB = Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="white",
                              command=self.SEARCH_PAT)
        self.SearchB.grid(row=3, column=1)

    # Function to search data in patient form
    def SEARCH_PAT(self):
        search_p = self.s_pid.get()

        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM PATIENT WHERE PATIENT_ID = ?', (search_p,))
                row = cursor.fetchone()
                if row:
                    self.pat_ID.set(row[0])
                    self.pat_name.set(row[1])
                    self.pat_sex.set(row[2])
                    self.pat_BG.set(row[3])
                    self.pat_dob.set(row[4])
                    self.pat_address.set(row[5])
                    self.pat_CT.set(row[6])
                    self.pat_email.set(row[7])
                    cursor.execute('SELECT * FROM CONTACT_NO WHERE PATIENT_ID = ?', (search_p,))
                    row = cursor.fetchone()
                    if row:
                        self.pat_contact.set(row[1])
                        self.pat_contactalt.set(row[2])
                    else:
                        messagebox.showerror("HOSPITAL DATABASE SYSTEM", "CONTACT DETAILS NOT FOUND")
                else:
                    messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT DETAILS NOT FOUND")
        except sqlite3.Error as e:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", f"Error searching data: {e}")

        self.master.destroy()


# Main function to run the application
def main():
    root = Tk()
    app = Patient(root)
    root.mainloop()


if __name__ == "__main__":
    main()
