from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

# Class for BOOKING APPOINTMENT
class Appointment:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="light green")
        self.frame = Frame(self.master, bg="light green")
        self.frame.pack()

        # ============= ATTRIBUTES ============

        self.pat_ID = IntVar()
        self.emp_ID = StringVar()
        self.ap_no = StringVar()
        self.ap_time = StringVar()
        self.ap_date = StringVar()
        self.des = StringVar()

        # =============== TITLE ===========
        self.lblTitle = Label(self.frame, text="APPOINTMENT FORM", font="Helvetica 20 bold", bg="light green")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        # ============== FRAME ===========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # =========== LABELS ==============
        self.lblpid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblpid.grid(row=0, column=0)
        self.lblpid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_ID)
        self.lblpid_entry.grid(row=0, column=1)

        self.lbldid = Label(self.LoginFrame, text="DOCTOR ID", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lbldid.grid(row=1, column=0)
        self.lbldid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_ID)
        self.lbldid_entry.grid(row=1, column=1)

        self.lblap = Label(self.LoginFrame, text="APPOINTMENT NO", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblap.grid(row=2, column=0)
        self.lblap_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_no)
        self.lblap_entry.grid(row=2, column=1)

        self.lblapt = Label(self.LoginFrame, text="APPOINTMENT TIME(HH:MM:SS)", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblapt.grid(row=0, column=2)
        self.lblapt_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_time)
        self.lblapt_entry.grid(row=0, column=3)

        self.lblapd = Label(self.LoginFrame, text="APPOINTMENT DATE(YYYY-MM-DD)", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblapd.grid(row=1, column=2)
        self.lblapd_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_date)
        self.lblapd_entry.grid(row=1, column=3)

        self.lbldes = Label(self.LoginFrame, text="DESCRIPTION", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lbldes.grid(row=2, column=2)
        self.lbldes_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.des)
        self.lbldes_entry.grid(row=2, column=3)

        # =========== BUTTONS ==============
        self.button2 = Button(self.LoginFrame2, text="SAVE", width=10, font="Helvetica 14 bold", bg="light blue", command=self.INSERT_AP)
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="light coral", command=self.DE_AP_DISPLAY)
        self.button3.grid(row=3, column=2)

        self.button4 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS", width=20, font="Helvetica 14 bold", bg="white", command=self.S_AP_DISPLAY)
        self.button4.grid(row=3, column=3)

        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="red", command=self.Exit)
        self.button6.grid(row=3, column=4)

    # FUNCTION TO EXIT APPOINTMENT WINDOW
    def Exit(self):
        self.master.destroy()

    # FUNCTION TO INSERT DATA IN APPOINTMENT FORM
    def INSERT_AP(self):
        e1 = self.pat_ID.get()
        e2 = self.emp_ID.get()
        e3 = self.ap_no.get()
        e4 = self.ap_time.get()
        e5 = self.ap_date.get()
        e6 = self.des.get()

        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("SELECT * FROM appointment WHERE AP_NO =?", (e3,)))
        x = len(p)
        if x != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "APPOINTMENT ALREADY EXISTS")
        else:
            conn.execute("INSERT INTO appointment VALUES(?,?,?,?,?,?)", (e1, e2, e3, e4, e5, e6))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "APPOINTMENT SET SUCCESSFULLY")
        conn.commit()

    # FUNCTION TO OPEN DELETE APPOINTMENT DISPLAY WINDOW
    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_AP(self.newWindow)

    # FUNCTION TO OPEN SEARCH APPOINTMENT DISPLAY WINDOW
    def S_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = SEA_AP(self.newWindow)


# CLASS FOR DISPLAY MENU FOR DELETE APPOINTMENT
class DEL_AP:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="light green")
        self.frame = Frame(self.master, bg="light green")
        self.frame.pack()
        self.de1_ap = StringVar()
        self.lblTitle = Label(self.frame, text="DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold", bg="light green")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        # ============== FRAME ===========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # =========== LABELS ==============
        self.lblpatid = Label(self.LoginFrame, text="ENTER APPOINTMENT NO TO DELETE", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.de1_ap)
        self.lblpatid_entry.grid(row=0, column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="light green", command=self.DELETE_AP)
        self.DeleteB.grid(row=3, column=1)

    # FUNCTION TO DELETE DATA IN APPOINTMENT FORM
    def DELETE_AP(self):
        inp_d = self.de1_ap.get()
        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("SELECT * FROM appointment WHERE AP_NO =?", (inp_d,)))
        if len(p) == 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "APPOINTMENT NOT FOUND")
        else:
            conn.execute("DELETE FROM appointment WHERE AP_NO =?", (inp_d,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "APPOINTMENT DELETED SUCCESSFULLY")
        conn.commit()


# CLASS FOR DISPLAY MENU FOR SEARCH APPOINTMENT
class SEA_AP:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="light green")
        self.frame = Frame(self.master, bg="light green")
        self.frame.pack()
        self.entry = StringVar()
        self.lblTitle = Label(self.frame, text="SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold", bg="light green")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=25)
        # ============== FRAME ===========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # =========== LABELS ==============
        self.lblpatid = Label(self.LoginFrame, text="ENTER DATE TO VIEW APPOINTMENTS(YYYY-MM-DD)", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.entry)
        self.lblpatid_entry.grid(row=0, column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="light green", command=self.SEARCH_AP)
        self.SearchB.grid(row=0, column=1)

    # FUNCTION TO SEARCH DATA IN APPOINTMENT FORM
    def SEARCH_AP(self):
        ap = self.entry.get()
        c = conn.cursor()
        p = list(c.execute("SELECT * FROM appointment WHERE AP_DATE =?", (ap,)))
        if len(p) == 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "NO APPOINTMENTS FOUND")
        else:
            for row in p:
                tkinter.messagebox.showinfo("APPOINTMENT DETAILS", f"Appointment Number: {row[2]}\nPatient ID: {row[0]}\nDoctor ID: {row[1]}\nAppointment Date: {row[4]}\nAppointment Time: {row[3]}\nDescription: {row[5]}")

# Main function to start the application
def main():
    root = Tk()
    app = Appointment(root)
    root.mainloop()

if __name__ == '__main__':
    main()
