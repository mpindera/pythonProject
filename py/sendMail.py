from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("patient_emails", "*.txt")])
    if filepath:
        with open(filepath, "r") as file:
            content = file.read()
            text.delete("1.0", "end")
            text.insert("1.0", content)

def select_text():
    selected_text = text.get("sel.first", "sel.last")
    print("Selected Text:", selected_text)

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=text.yview)

open_button = Button(root, text="Open File", command=open_file)
open_button.pack()

select_button = Button(root, text="Select Text", command=select_text)
select_button.pack()

root.mainloop()
