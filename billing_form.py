from tkinter import *
import tkinter.messagebox
import sqlite3

conn = sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

class Billing:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="light green")
        self.frame = Frame(self.master, bg="light green")
        self.frame.pack()

        # Attributes
        self.P_id = IntVar()
        self.dd = StringVar()
        self.treat_1 = StringVar()
        self.treat_2 = StringVar()
        self.cost_t = IntVar()
        self.med = StringVar()
        self.med_q = IntVar()
        self.price = IntVar()

        # Title
        self.lblTitle = Label(self.frame, text="BILLING WINDOW", font="Helvetica 20 bold", bg="light green")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=25)

        # Frames
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light green", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels and Entries
        self.lblpid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblpid.grid(row=0, column=0)
        self.entpid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.P_id)
        self.entpid.grid(row=0, column=1)

        self.lbldid = Label(self.LoginFrame, text="DATE DISCHARGED (DD-MM-YYYY)", font="Helvetica 14 bold",
                            bg="light green", bd=22)
        self.lbldid.grid(row=1, column=0)
        self.entdid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dd)
        self.entdid.grid(row=1, column=1)
        self.btnUpdateDate = Button(self.LoginFrame, text="UPDATE DISCHARGE DATE", width=25, font="Helvetica 14 bold",
                                    bg="yellow", command=self.UPDATE_DATE)
        self.btnUpdateDate.grid(row=1, column=3)

        self.lbltreat = Label(self.LoginFrame, text="TREATMENT", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lbltreat.grid(row=2, column=0)
        self.enttreat = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.treat_1)
        self.enttreat.grid(row=2, column=1)

        self.lblcode_t1 = Label(self.LoginFrame, text="TREATMENT CODE", font="Helvetica 14 bold", bg="light green",
                                bd=22)
        self.lblcode_t1.grid(row=3, column=0)
        self.entcode_t1 = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.treat_2)
        self.entcode_t1.grid(row=3, column=1)

        self.lblap = Label(self.LoginFrame, text="TREATMENT COST ₹", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblap.grid(row=4, column=0)
        self.entap = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.cost_t)
        self.entap.grid(row=4, column=1)

        self.lblmed = Label(self.LoginFrame, text="MEDICINE", font="Helvetica 14 bold", bg="light green", bd=22)
        self.lblmed.grid(row=2, column=2)
        self.entmed = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.med)
        self.entmed.grid(row=2, column=3)

        self.lblmedqty = Label(self.LoginFrame, text="MEDICINE QUANTITY", font="Helvetica 14 bold", bg="light green",
                               bd=22)
        self.lblmedqty.grid(row=3, column=2)
        self.entmedqty = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.med_q)
        self.entmedqty.grid(row=3, column=3)

        self.lblmedprice = Label(self.LoginFrame, text="MEDICINE PRICE ₹", font="Helvetica 14 bold", bg="light green",
                                 bd=22)
        self.lblmedprice.grid(row=4, column=2)
        self.entmedprice = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.price)
        self.entmedprice.grid(row=4, column=3)

        # Buttons
        self.btnUpdateData = Button(self.LoginFrame2, text="UPDATE DATA", width=15, font="Helvetica 14 bold",
                                    bg="yellow", command=self.UPDATE_DATA)
        self.btnUpdateData.grid(row=3, column=2)

        self.btnGenerateBill = Button(self.LoginFrame2, text="GENERATE BILL", width=15, font="Helvetica 14 bold",
                                      bg="green", command=self.GEN_BILL)
        self.btnGenerateBill.grid(row=3, column=3)

        self.btnExit = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="red",
                              command=self.Exit)
        self.btnExit.grid(row=3, column=4)

    def UPDATE_DATE(self):
        global b1, b2
        b1 = self.P_id.get()
        b2 = self.dd.get()
        conn.execute("UPDATE ROOM SET DATE_DISCHARGED=? WHERE PATIENT_ID=?", (b2, b1))
        conn.commit()
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")

    def UPDATE_DATA(self):
        global b1, b3, b4, b5, b6, b7, b8
        b1 = self.P_id.get()
        b3 = self.treat_1.get()
        b4 = self.treat_2.get()
        b5 = self.cost_t.get()
        b6 = self.med.get()
        b7 = self.med_q.get()
        b8 = self.price.get()
        
        try:
            conn.execute("INSERT INTO TREATMENT (PATIENT_ID, TREATMENT, TREATMENT_CODE, T_COST) VALUES (?, ?, ?, ?)",
                         (b1, b3, b4, b5))
            conn.execute("INSERT INTO MEDICINE (PATIENT_ID, MEDICINE_NAME, M_QTY, M_COST) VALUES (?, ?, ?, ?)",
                         (b1, b6, b7, b8))
            conn.commit()
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "BILLING DATA SAVED")
        except sqlite3.IntegrityError:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "Patient ID already registered for billing.")

    def GEN_BILL(self):
        global b1
        b1 = self.P_id.get()
        try:
            cursor = conn.execute("SELECT sum(T_COST + (M_COST * M_QTY) + (julianday(DATE_DISCHARGED) - julianday(DATE_ADMITTED)) * RATE) FROM ROOM NATURAL JOIN TREATMENT NATURAL JOIN MEDICINE WHERE PATIENT_ID=?", (b1,))
            for row in cursor:
                total_amount = row[0]
                self.lblTotalAmount = Label(self.LoginFrame, text="TOTAL AMOUNT OUTSTANDING", font="Helvetica 14 bold", bg="light green", bd=22)
                self.lblTotalAmount.grid(row=5, column=0)
                self.lblTotalAmountValue = Label(self.LoginFrame, text=f"₹ {total_amount:.2f}", font="Helvetica 14 bold", bg="light green", bd=22)
                self.lblTotalAmountValue.grid(row=5, column=1)
        except Exception as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", f"Error: {e}")

    def Exit(self):
        self.master.destroy()


def main():
    root = Tk()
    application = Billing(root)
    root.mainloop()


if __name__ == "__main__":
    main()
