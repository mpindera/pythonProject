import os
import tkinter as tk
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
import ssl

window = tk.Tk()
window.title("Sending e-mails")
window.geometry("600x600")


def go_back(root):
    root.destroy()
    os.system('python ChooserMain.py')
def send_email():
    sender_email = 'mikolajpindera2@gmail.com'
    password = 'wwalnnbrcohqkgvk'

    go_back_button = tk.Button(window, text="Go Back", command=lambda: go_back(window))
    go_back_button.pack()

    try:
        recipient_emails = listbox.curselection()
        title = title_entry.get()
        subject = subject_entry.get('1.0', tk.END)

        context = ssl.create_default_context()

        for index in recipient_emails:
            recipient_email = listbox.get(index)

            message = EmailMessage()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = title
            message.set_content(subject)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                server.login(sender_email, password)
                server.send_message(message)

        messagebox.showinfo("Success", "Message e-mail has send!")
        go_back(window)
    except Exception as e:
        messagebox.showerror("ERROR!", str(e))

with open("patient_emails.txt", "r") as file:
    emails = file.read().split("|")

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
listbox.pack(fill=tk.BOTH, expand=True)

for email in emails:
    listbox.insert(tk.END, email.strip())

scrollbar.config(command=listbox.yview)

title_label = tk.Label(window, text="Title:")
title_label.pack()

title_entry = tk.Entry(window,width=40)
title_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()

subject_entry = tk.Text(window, height=10)
subject_entry.pack()

send_button = tk.Button(window, text="Send", command=send_email)
send_button.pack()

window.mainloop()
