import tkinter as tk
import subprocess

"""
You can change the UUID text here
You can, for example, give admin rights to other people
"""

# Function to update the UUID based on user selection
def update_uuid():
    selected_indices = listbox.curselection()
    if selected_indices:
        for selected_index in selected_indices:
            selected_person = persons[selected_index]
            new_uuid = uuid_entry.get()
            persons[selected_index] = selected_person.replace("UUID." + selected_person.split("UUID.")[1],
                                                              "UUID." + new_uuid)
        update_listbox()
        save_data()


# Function to update the listbox with the list of persons
def update_listbox():
    listbox.delete(0, tk.END)
    for person in persons:
        listbox.insert(tk.END, person)


# Function to save the updated data to the datasheet.txt file
def save_data():
    with open("datasheet.txt", "w") as file:
        for person in persons:
            file.write(person + "\n")


# Function to open the chooserMain.py script
def open_chooser_main():
    window.destroy()
    subprocess.Popen(["python", "chooserMain.py"])


# Read data from the datasheet.txt file
with open("datasheet.txt", "r") as file:
    data = file.read().strip()

# Parse the data into a list of persons
lines = data.split("\n")
persons = []
for line in lines:
    username = line.split(":")[0].split("-")[1].strip()
    password = line.split(":")[1].split("-")[1].strip()
    uuid_value = line.split("UUID.")[1].strip()
    persons.append(f"{{username-{username} : password-{password} : UUID.{uuid_value}}}")

# Create the main application window
window = tk.Tk()
window.title("UUID Changer")

# Center the window on the screen
window_width = 550
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.resizable(False, False)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox to display the list of persons
listbox = tk.Listbox(window, width=80, height=10, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
listbox.pack()

# Connect the scrollbar to the listbox
scrollbar.config(command=listbox.yview)

# Display the initial list of persons
update_listbox()

# Create an entry field for the user to enter a new UUID
uuid_label = tk.Label(window, text="New UUID:")
uuid_label.pack()

uuid_entry = tk.Entry(window, width=40)
uuid_entry.pack()

# Create a button to update the UUIDs
button = tk.Button(window, text="Change UUID", command=update_uuid)
button.pack()

# Create a "Back" button to go back to the chooserMain.py script
back_button = tk.Button(window, text="Back", command=open_chooser_main)
back_button.pack()

# Start the main application loop
window.mainloop()
