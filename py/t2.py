import tkinter as tk
import smtplib
from tkinter import messagebox


def send_email():
    selected_emails = [listbox.get(index) for index in listbox.curselection()]
    subject = subject_entry.get()
    text = text_entry.get("1.0", tk.END)

    if not selected_emails:
        messagebox.showwarning("No Emails Selected", "Please select at least one email.")
        return

    if not subject or not text.strip():
        messagebox.showwarning("Missing Fields", "Please enter a subject and email text.")
        return

    try:
        with smtplib.SMTP("smtp.gmail.com", 465) as smtp:
            smtp.starttls()
            smtp.login("mikolajpindera2@gmail.com", "wwalnnbrcohqkgvk")
            for email in selected_emails:
                message = f"Subject: {subject}\n\n{text}"
                smtp.sendmail("your_email", email, message)

        messagebox.showinfo("Email Sent", "Email(s) sent successfully.")
    except smtplib.SMTPException:
        messagebox.showerror("Email Error", "An error occurred while sending the email.")


# Create the main window
root = tk.Tk()
root.title("Email Sender")

# Create the widgets
subject_label = tk.Label(root, text="Subject:")
subject_label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

text_label = tk.Label(root, text="Text:")
text_label.pack()

text_entry = tk.Text(root, height=10)
text_entry.pack()

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

with open("patient_emails.txt", "r") as file:
    data = file.readlines()
    for line in data:
        items = line.strip().split("|")
        listbox.insert(tk.END, *items)

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

# Run the main event loop
root.mainloop()
