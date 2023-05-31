import tkinter as tk

root = tk.Tk()

# Dane
data = {
    'Zapotrzebowanie': '123',
    'Białko': '123',
    'Tłuszcz': '123',
    'Węglowodany': '123'
}

def display_table():
    table_frame = tk.Frame(root)
    table_frame.grid(row=0, column=1, padx=10, pady=10)

    # Wyświetlanie danych w tabeli
    for i, (key, value) in enumerate(data.items()):
        label_key = tk.Label(table_frame, text=key, padx=10, pady=5)
        label_key.grid(row=i, column=0, sticky='w')
        label_value = tk.Label(table_frame, text=value, padx=10, pady=5)
        label_value.grid(row=i, column=1, sticky='w')

# Tworzenie przycisku
button = tk.Button(root, text="Wyświetl dane", command=display_table)
button.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
