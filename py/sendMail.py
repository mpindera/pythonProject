import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import smtplib
from email.message import EmailMessage
import ssl
from tkinter import IntVar


def send_email(sender_email, password, selected_emails, subject, message):
    context = ssl.create_default_context()
    for email in selected_emails:
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(sender_email, password)
                msg = EmailMessage()
                msg['From'] = sender_email
                msg['To'] = email
                msg['Subject'] = subject
                msg.set_content(message)
                smtp.send_message(msg)
            messagebox.showinfo('Email', "Wiadomość została wysłana.")
        except Exception as e:
            messagebox.showerror('Błąd', f"Wystąpił błąd podczas wysyłania wiadomości: {str(e)}")

def read_emails(filename):
    with open(filename, 'r') as file:
        emails = file.read().split('|')
    return [email.strip() for email in emails if email.strip()]

def send_message():
    sender_email = 'mikolajpindera2@gmail.com'
    password = 'wwalnnbrcohqkgvk'
    subject = 'Subject of the email'
    message = 'Body of the email'

    selected_emails = [email for email, checkbox_var in checkbox_vars.items() if checkbox_var.get() == 1]

    if selected_emails:
        send_email(sender_email, password, selected_emails, subject, message)
    else:
        messagebox.showwarning('Brak zaznaczenia', 'Proszę zaznaczyć co najmniej jeden email.')


def create_checkbox_list(root, emails):
    checkbox_vars = {}
    for email in emails:
        checkbox_var = IntVar()
        checkbox = tk.Checkbutton(root, text=email, variable=checkbox_var)
        checkbox.pack(anchor="w")
        checkbox_vars[email] = checkbox_var

    return checkbox_vars

root = tk.Tk()

emails = read_emails('patient_emails.txt')
checkbox_vars = create_checkbox_list(root, emails)

send_button = tk.Button(root, text="Wyślij", command=send_message)
send_button.pack()

root.mainloop()
