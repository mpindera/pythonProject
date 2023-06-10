import os
import tkinter as tk
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
import ssl

"""
Allows email to be sent to recipients from a list of email addresses stored on file.
"""

window = tk.Tk()
window.title("Sending e-mails")
window.geometry("600x600")
window.resizable(False, False)  # Disable window resizing


def go_back():
    window.destroy()
    os.system('python ChooserMain.py')


def send_email():
    sender_email = 'mikolajpindera2@gmail.com'
    password = 'wwalnnbrcohqkgvk'

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

        messagebox.showinfo("Success", "Message e-mail has been sent!")

    except Exception as e:
        messagebox.showerror("ERROR!", str(e))

    go_back()


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

title_entry = tk.Entry(window, width=40)
title_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()

subject_entry = tk.Text(window, height=10)
subject_entry.pack()

send_button = tk.Button(window, text="Send", command=send_email)
send_button.pack()

go_back_button = tk.Button(window, text="Go Back", command=go_back)
go_back_button.pack()

window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()
pos_x = (screen_width - window_width) // 2
pos_y = (screen_height - window_height) // 2
window.geometry(f"+{pos_x}+{pos_y}")

window.mainloop()
