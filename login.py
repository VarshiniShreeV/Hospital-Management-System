from tkinter import *
import tkinter.messagebox
from menu import Menu  # Assuming Menu is a class defined in menu.py

# Function to start the application
def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()

# Main Window for Login
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x600+350+70")
        self.master.config(bg="teal")
        self.frame = Frame(self.master, bg="teal")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text="HOSPITAL MANAGEMENT SYSTEM", font="Helvetica 20 bold", bg="teal", fg="black")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=400, height=80, relief="ridge", bg="teal", bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="teal", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblUsername = Label(self.LoginFrame1, text="Username", font="Helvetica 14 bold", bg="teal", bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.entUsername = Entry(self.LoginFrame1, font="Helvetica 14 bold", textvariable=self.Username, bd=2)
        self.entUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.LoginFrame1, text="Password", font="Helvetica 14 bold", bg="teal", bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.entPassword = Entry(self.LoginFrame1, font="Helvetica 14 bold", show="*", textvariable=self.Password, bd=2)
        self.entPassword.grid(row=1, column=1)

        self.btnLogin = Button(self.LoginFrame2, text="Login", font="Helvetica 10 bold", width=10, bg="teal", command=self.Login_system)
        self.btnLogin.grid(row=3, column=0)

        self.btnExit = Button(self.LoginFrame2, text="Exit", font="Helvetica 10 bold", width=10, bg="teal", command=self.Exit)
        self.btnExit.grid(row=3, column=1)

    def Login_system(self):
        username = self.Username.get()
        password = self.Password.get()

        if username == 'admin' and password == '2024':
            self.open_menu_window()
        elif username == 'user' and password == '2420':
            self.open_menu_window()
        else:
            tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM", "Please enter a valid username and password")

    def open_menu_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Menu(self.newWindow)

    def Exit(self):
        self.master.destroy()

if __name__ == "__main__":
    main()
