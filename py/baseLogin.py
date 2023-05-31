import base64
import os
import tkinter as tk
import uuid
from tkinter import messagebox
import re


# When clicked sign_in button
def check_credentials(username, password, uuid):
    return check_credentials_in_file(username, password, uuid)


def check_credentials_in_file(username, password, uuid):
    with open('datasheet.txt', 'r') as datasheet_file:
        for line in datasheet_file:
            line = line.strip()
            if line.startswith("{") and line.endswith("}"):
                line = line[1:-1]
                credentials = line.split(":")
                if len(credentials) == 3:
                    user = credentials[0].strip().split("-")[-1].strip()
                    passwd = credentials[1].strip().split("-")[-1].strip()
                    file_uuid = credentials[2].strip().split(".")[-1].strip()
                    if user == username and passwd == password:
                        with open('uuid.txt', 'r') as uuid_file:
                            for uuid_line in uuid_file:
                                if uuid_line.strip() == file_uuid:
                                    return True

    return False



# open another screen
def sign_up():
    root.destroy()  # close login screen
    os.system("python baseRegister.py")


def main_screen():
    root.destroy()  # close login screen
    os.system("python MainPageAdmin.py")


class BaseLogin:
    def __init__(self, root):
        self.passwordField = None
        self.img = None
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.root.title('Login')
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

        heading = tk.Label(frame, text='Login to account', fg="#545B77",
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

        # Button to Login account
        tk.Button(frame, width=41, pady=7, text='Enter to account', border=0, bg='#27374D', fg='white',
                  command=self.sign_in).place(x=30, y=170)

        # Button change to screen Register
        label = tk.Label(frame, text='I don\'t have an account', fg='black',
                         bg='white', font=('Microsoft Yahei UI Light', 9))
        label.place(x=110, y=260)
        tk.Button(frame, width=6, text='Sign up', border=0,
                  bg='white', cursor='hand2', fg='#27374D', command=sign_up).place(x=250, y=260)

    def sign_in(self):
        username = self.userField.get()
        password = self.passwordField.get()

        # decode the password
        decode = base64.b64encode(password.encode('utf-8')).decode('utf-8')

        if not username or not password or username == 'Username' or password == 'Password':
            messagebox.showerror('Error', "Username and Password fields cannot be empty")
            return

        if check_credentials(username, decode, uuid):
            messagebox.showwarning('Success', "Welcome!")
            main_screen()
        else:
            messagebox.showerror('Error', "Invalid credentials")

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


root = tk.Tk()
base_login = BaseLogin(root)
root.mainloop()
