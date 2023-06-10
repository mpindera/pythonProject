import os
import tkinter as tk

"""
Menu to select options 
"""

# open another screen
def sign_in():
    root.destroy()  # close register screen
    os.system("python baseLogin.py")


def main_screen():
    root.destroy()
    os.system("python mainPageAdmin.py")


def send_email():
    root.destroy()
    os.system("python sendMail.py")


def add_admin():
    root.destroy()
    os.system("python addAdmin.py")


class BaseRegister:
    def __init__(self, root):
        self.passwordCheckingField = None
        self.passwordField = None
        self.userField = None
        self.img = None
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.root.title('Chooser')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 600
        window_height = 300
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        tk.Label(self.root, text='Welcome in Health Care', fg="#643843", bg='white', font=(
            'Microsoft Yahei UI Light', 23, 'bold')).place(x=120, y=10)

        self.img = tk.PhotoImage(file='login.png')
        tk.Label(self.root, image=self.img, bg='white').place(x=600, y=100)

        tk.Button(root, width=41, pady=7, text='Send mail', command=send_email, border=0,
                  bg='#27374D',
                  fg='white').place(x=150, y=110)
        tk.Button(root, width=41, pady=7, text='Register person', command=main_screen,
                  border=0, bg='#27374D',
                  fg='white').place(x=150, y=160)
        tk.Button(root, width=41, pady=7, text='Add admin', command=add_admin,
                  border=0, bg='#27374D',
                  fg='white').place(x=150, y=210)


root = tk.Tk()
app = BaseRegister(root)
root.mainloop()
