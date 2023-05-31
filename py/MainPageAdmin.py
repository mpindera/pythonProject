import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Spinbox, Label
import re
from email.message import EmailMessage
import ssl
import smtplib
from tkinter import messagebox


def on_key_press(event):
    # Check if the pressed key is a number or a special key like backspace or delete
    if event.char.isdigit() or event.keysym in ['BackSpace', 'Delete']:
        return True
    else:
        return False


class mainPageAdmin:

    def check_all(self, username_dietitian):
        if self.patient_field_email.get() \
                and username_dietitian \
                and self.patient_field_name.get() \
                and self.selected_option_gender.get() \
                and self.selected_option_activity.get() \
                and self.entry_weight.get() \
                and self.entry_height.get() \
                and self.patient_field_age.get():
            return True
        else:
            return False

    def send_mail(self):
        email_sender = 'mikolajpindera2@gmail.com'
        email_password = 'wwalnnbrcohqkgvk'
        email_receiver = self.patient_field_email.get()
        name_receiver = self.patient_field_name.get()

        email_to_save = email_receiver
        filename = 'patient_emails.txt'

        subject = 'Diet'

        username_dietitian = self.dietitian_field_name.get()

        caloric_requirements = round(
            float((10 * float(self.entry_weight.get())) + (6.25 * float(self.entry_height.get())) - (
                    5 * float(self.patient_field_age.get()) + 5)) * float(self.selected_option_activity.get()))

        protein = round(((caloric_requirements * 0.2) / 4), 1)
        fat = round(((caloric_requirements * 0.3) / 9), 1)
        carbohydrates = round(((caloric_requirements * 0.5) / 4), 1)

        self.data = {
            'Caloric requirements': caloric_requirements,
            'Protein': protein,
            'Fat': fat,
            'Carbohydrates': carbohydrates
        }

        self.table_frame = tk.Frame(root)
        self.table_frame.grid(row=0, column=1, padx=10, pady=10)
        self.table_frame.place(x=320, y=300)

        for i, (key, value) in enumerate(self.data.items()):
            label_key = tk.Label(self.table_frame, text=key, padx=10, pady=5, bg='#F9F5F6')
            label_key.grid(row=i, column=0, sticky='w')
            label_value = tk.Label(self.table_frame, text=value, padx=10, pady=5, bg='#F9F5F6')
            label_value.grid(row=i, column=1, sticky='w')

        body = f"""
        <html>
        <body>
        <p>Hello, <strong>{name_receiver}</strong> It's email
        from your dietitian:<strong> {username_dietitian}</strong></p>
        <p>Here are your nutritional requirements:</p>
        <p>Caloric requirements: <strong>{caloric_requirements}kcal</strong></p>
        <ul>
          <li>Protein: {protein}g</li>
          <li>Fat: {fat}g</li>
          <li>Carbohydrates: {carbohydrates}g</li>
        </ul>
        </body>
        </html>
        """

        with open(filename, 'w') as file:
            file.write(email_to_save + '|')

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.add_alternative(body, subtype='html')

        context = ssl.create_default_context()
        if self.check_all(username_dietitian):
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())
                messagebox.showinfo('Diet', "Email was send.")
            except:
                messagebox.showerror('Error', "Email wasn't send.")
        else:
            messagebox.showerror('Error', "Please fill everything.")

    def __init__(self, root):
        self.table_frame = None
        self.data = None
        self.patient_field_age = None
        self.entry_height = None
        self.entry_weight = None
        self.selected_option_activity = None
        self.selected_option_gender = None
        self.dietitian_field_name = None
        self.nameField = None
        self.root = root
        self.create_widgets()

    def on_enter_to_patient_field_name(self, e):
        if self.patient_field_name.get() == 'Patient name':
            self.patient_field_name.delete(0, 'end')

    def on_leave_to_patient_field_name(self, e):
        if self.patient_field_name.get() == '':
            self.patient_field_name.insert(0, 'Patient name')

    def on_enter_to_patient_field_email(self, e):
        if self.patient_field_email.get() == 'Patient email':
            self.patient_field_email.delete(0, 'end')

    def on_leave_to_patient_field_email(self, e):
        if self.patient_field_email.get() == '':
            self.patient_field_email.insert(0, 'Patient email')

    def on_enter_to_dietitian_field_name(self, e):
        if self.dietitian_field_name.get() == 'Dietitian name':
            self.dietitian_field_name.delete(0, 'end')

    def on_leave_to_dietitian_field_name(self, e):
        if self.dietitian_field_name.get() == '':
            self.dietitian_field_name.insert(0, 'Dietitian name')

    def create_widgets(self):
        self.root.title('Admin Page')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 925
        window_height = 500
        self.root['bg'] = 'green'
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

        self.root.resizable(False, False)
        self.root.configure(bg="#F9F5F6")
        tk.Label(self.root, text='Welcome in Health Care', fg="#643843", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 23, 'bold')).place(x=295, y=10)

        def validate_spinbox(value):
            if value == "" or re.match("^[0-9]+$", value) and len(value) < 3:
                error_label.config(text="")
                return True
            else:
                error_label.config(text="Enter only numbers")
                return False

        # adding Patient email
        tk.Label(self.root, text='Patient email', fg="black", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 15, 'bold')).place(x=100, y=110)

        self.patient_field_email = tk.Entry(self.root, width=25, fg='black', border=1, bg='#F9F5F6',
                                            font=('Microsoft Yahei UI Light', 11))
        self.patient_field_email.place(x=100, y=150)
        self.patient_field_email.insert(0, 'Patient email')
        self.patient_field_email.bind("<FocusIn>", self.on_enter_to_patient_field_email)
        self.patient_field_email.bind("<FocusOut>", self.on_leave_to_patient_field_email)

        # adding Patient name
        tk.Label(self.root, text='Patient name', fg="black", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 15, 'bold')).place(x=100, y=190)

        self.patient_field_name = tk.Entry(self.root, width=25, fg='black', border=1, bg='#F9F5F6',
                                           font=('Microsoft Yahei UI Light', 11))
        self.patient_field_name.place(x=100, y=230)
        self.patient_field_name.insert(0, 'Patient name')
        self.patient_field_name.bind("<FocusIn>", self.on_enter_to_patient_field_name)
        self.patient_field_name.bind("<FocusOut>", self.on_leave_to_patient_field_name)

        # adding Dietitian name
        tk.Label(self.root, text='Dietitian full name', fg="black", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 15, 'bold')).place(x=100, y=270)

        self.dietitian_field_name = tk.Entry(self.root, width=25, fg='black', border=1, bg='#F9F5F6',
                                             font=('Microsoft Yahei UI Light', 11))
        self.dietitian_field_name.place(x=100, y=310)
        self.dietitian_field_name.insert(0, 'Dietitian name')
        self.dietitian_field_name.bind("<FocusIn>", self.on_enter_to_dietitian_field_name)
        self.dietitian_field_name.bind("<FocusOut>", self.on_leave_to_dietitian_field_name)

        # gender, tack option, menu
        tk.Label(self.root, text='Gender', fg="black", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 15, 'bold'))
        options = ["Woman", "Man", "Woman"]

        self.selected_option_gender = tk.StringVar(root)
        self.selected_option_gender.set(options[0])

        ttk.OptionMenu(root, self.selected_option_gender, *options).place(x=340, y=150)

        # activity, tack option, menu
        tk.Label(self.root, text='Activity', fg="black", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 15, 'bold')).place(x=340, y=190)
        options = ["1.2", "1.2", "1.3", "1.5", "1.7", "1.9"]

        self.selected_option_activity = tk.StringVar(root)
        self.selected_option_activity.set(options[0])

        ttk.OptionMenu(root, self.selected_option_activity, *options).place(x=340, y=230)

        # weight
        def validate_entry_weight(value):
            if value == "" or (re.match(r"^\d*\.?\d*$", value) and len(value) < 6):
                error_label_weight.config(text="")
                return True
            else:
                error_label_weight.config(text="Enter correct eg. 64.1")
                return False

        vcmd_weight = (root.register(validate_entry_weight), '%P')

        tk.Label(root, text='Weight', fg="black", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 15, 'bold')).place(x=450, y=110)

        self.entry_weight = tk.Entry(root, validate='key', validatecommand=vcmd_weight)
        self.entry_weight.place(x=450, y=150)

        error_label_weight = tk.Label(root, foreground='red', background='#F9F5F6')
        error_label_weight.place(x=450, y=171)

        # height
        def validate_entry_height(value):
            if value == "" or (re.match(r"^\d*\.?\d*$", value) and len(value) < 6):
                error_label_height.config(text="")
                return True
            else:
                error_label_height.config(text="Enter correct eg. 172.1")
                return False

        vcmd_height = (root.register(validate_entry_height), '%P')

        tk.Label(root, text='Height', fg="black", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 15, 'bold')).place(x=450, y=190)

        self.entry_height = tk.Entry(root, validate='key', validatecommand=vcmd_height)
        self.entry_height.place(x=450, y=230)

        error_label_height = tk.Label(root, foreground='red', background='#F9F5F6')
        error_label_height.place(x=450, y=250)

        # add spinbox with age
        vcmd = (self.root.register(validate_spinbox), '%P')

        tk.Label(self.root, text='Age', fg="black", bg='#F9F5F6', font=(
            'Microsoft Yahei UI Light', 15, 'bold')).place(x=605, y=110)

        self.patient_field_age = Spinbox(self.root, from_=0, to=99, validate='key', validatecommand=vcmd)
        self.patient_field_age.place(x=605, y=150)

        error_label = Label(self.root, foreground='red', background='#F9F5F6')
        error_label.place(x=605, y=171)

        # Button accept
        style = ttk.Style()
        style.configure('calculate.TButton', foreground='blue', font=('Arial', 12, 'bold'))

        button = ttk.Button(root, text="Calculate", style='calculate.TButton', command=self.send_mail)
        button.place(x=605, y=220)


root = tk.Tk()
mainPage = mainPageAdmin(root)
root.mainloop()
