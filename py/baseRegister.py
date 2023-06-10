import os
import tkinter as tk
import base64
from tkinter import messagebox
import uuid

"""
1. The necessary imports are done, including `os`, `tkinter`, `base64`, `messagebox`, and `uuid`.

This script provides a registration screen for a Health Care application. Users can sign up by providing a username,
password, and confirming the password. The provided information is then encoded and stored in a datasheet.txt file.
"""


# open another screen
def sign_in():
    root.destroy()  # close register screen
    os.system("python baseLogin.py")


class BaseRegister:
    def __init__(self, root):
        self.passwordCheckingField = None
        self.passwordField = None
        self.userField = None
        self.img = None
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.root.title('Register')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 925
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        tk.Label(self.root, text='Welcome in Health Care', fg="#643843", bg='white', font=(
            'Microsoft Yahei UI Light', 23, 'bold')).place(x=520, y=10)

        self.img = tk.PhotoImage(file='login.png')
        tk.Label(self.root, image=self.img, bg='white').place(x=600, y=100)

        frame = tk.Frame(self.root, width=350, height=600, bg="#fff")
        frame.place(x=50, y=110)

        heading = tk.Label(frame, text='Sign up', fg="#545B77",
                           bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=25, y=0)

        self.userField = tk.Entry(frame, width=25, fg='black', border=0, bg='white',
                                  font=('Microsoft Yahei UI Light', 11))
        self.userField.place(x=30, y=60)
        self.userField.insert(0, 'Username')
        self.userField.bind("<FocusIn>", self.on_enter_to_username)
        self.userField.bind("<FocusOut>", self.on_leave_to_username)
        tk.Frame(frame, width=295, height=2, bg='black').place(x=30, y=85)

        self.passwordField = tk.Entry(frame, width=25, fg='black', border=0,
                                      bg='white', font=('Microsoft Yahei UI Light', 11))
        self.passwordField.place(x=30, y=120)
        self.passwordField.insert(0, 'Password')
        self.passwordField.bind("<FocusIn>", self.on_enter_to_password)
        self.passwordField.bind("<FocusOut>", self.on_leave_to_password)
        self.passwordField.bind("<Key>", self.limit_character)
        self.passwordField.bind("<Key>", self.hide_characters)
        tk.Frame(frame, width=295, height=2, bg='black').place(x=30, y=145)

        self.passwordCheckingField = tk.Entry(frame, width=25, fg='black', border=0, bg='white',
                                              font=('Microsoft Yahei UI Light', 11))
        self.passwordCheckingField.place(x=30, y=180)
        self.passwordCheckingField.insert(0, 'Confirm password')
        self.passwordCheckingField.bind("<FocusIn>", self.on_enter_to_checking_password)
        self.passwordCheckingField.bind("<FocusOut>", self.on_leave_to_checking_password)
        self.passwordCheckingField.bind("<Key>", self.show_checking_password)
        self.passwordCheckingField.bind("<Key>", self.hide_checking_characters)
        tk.Frame(frame, width=295, height=2, bg='black').place(x=30, y=205)

        # Button to Register account
        tk.Button(frame, width=41, pady=7, text='Sign up', border=0, bg='#27374D', fg='white',
                  command=self.sign_up).place(x=30, y=240)

        # Button change to screen Login
        label = tk.Label(frame, text='I have an account', fg='black',
                         bg='white', font=('Microsoft Yahei UI Light', 9))
        label.place(x=150, y=290)
        tk.Button(frame, width=6, text='Sign in', border=0,
                  bg='white', cursor='hand2', fg='#27374D', command=sign_in).place(x=250, y=290)

    # Register section
    # When clicked sign_up button
    def sign_up(self):
        username = self.userField.get()

        # encode password
        password = self.passwordField.get()
        encode = base64.b64encode(password.encode('utf-8')).decode('utf-8')

        # encode checking_password
        checking_password = self.passwordCheckingField.get()
        encode_checking_password = base64.b64encode(checking_password.encode('utf-8')).decode('utf-8')

        if not username or username == 'Username' or password == 'Password':
            messagebox.showerror('Invalid', "Username and Password fields cannot be empty")
            return

        # Check if username already exists
        with open('datasheet.txt', 'r') as datasheet_file:
            for line in datasheet_file:
                if username in line:
                    messagebox.showerror('Invalid', "Username already exists in the database")
                    return

        if encode == encode_checking_password:
            try:
                # Generate UUID (ID)
                new_uuid = uuid.uuid4()

                # Convert to String
                uuid_str = str(new_uuid)
                file = open('datasheet.txt', 'a')
                file.write("{username-" + username + " : " + "password-" + encode + " : UUID." + uuid_str + "}" + "\n")
                file.close()

                self.userField.delete(0, 'end')
                self.passwordField.delete(0, 'end')
                self.passwordCheckingField.delete(0, 'end')
                self.userField.insert(0, 'Username')
                self.passwordField.insert(0, 'Password')
                self.passwordCheckingField.insert(0, 'Confirm password')

                messagebox.showinfo("Info", "Great, we saved your account")
            except:
                messagebox.showerror('Invalid', "Sorry something went wrong")
        else:
            messagebox.showerror('Invalid', "Both passwords should be the same")

    def on_enter_to_username(self, e):
        if self.userField.get() == 'Username':
            self.userField.delete(0, 'end')

    def on_leave_to_username(self, e):
        if self.userField.get() == '':
            self.userField.insert(0, 'Username')

    def on_enter_to_password(self, e):
        if self.passwordField.get() == 'Password':
            self.passwordField.delete(0, 'end')

    def on_leave_to_password(self, e):
        if self.passwordField.get() == '':
            self.passwordField.insert(0, 'Password')

    def limit_character(self, e):
        if len(self.passwordField.get()) > 10:
            self.passwordField.delete(10, 'end')

    def show_password(self):
        self.passwordField.config(show='')

    def hide_password(self):
        self.passwordField.config(show='*')

    def hide_characters(self, event):
        password = self.passwordField.get()
        if password != 'Password':
            self.passwordField.delete(0, 'end')
            self.passwordField.insert(0, password)

    def on_enter_to_checking_password(self, e):
        if self.passwordCheckingField.get() == 'Confirm password':
            self.passwordCheckingField.delete(0, 'end')

    def on_leave_to_checking_password(self, e):
        if self.passwordCheckingField.get() == '':
            self.passwordCheckingField.insert(0, 'Confirm password')

    def limit_character_checking_password(self, e):
        if len(self.passwordCheckingField.get()) > 10:
            self.passwordCheckingField.delete(10, 'end')

    def show_checking_password(self):
        self.passwordCheckingField.config(show='')

    def hide_checking_password(self):
        self.passwordCheckingField.config(show='*')

    def hide_checking_characters(self, event):
        passwordChecking = self.passwordCheckingField.get()
        if passwordChecking != 'Confirm password':
            self.passwordCheckingField.delete(0, 'end')
            self.passwordCheckingField.insert(0, passwordChecking)


# Create the root window and initialize the BaseRegister class
root = tk.Tk()
app = BaseRegister(root)
root.mainloop()
