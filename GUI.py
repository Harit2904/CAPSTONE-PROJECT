import tkinter as tk
from tkinter import ttk
import pandas as pd
data = pd.read_csv("room_dataset.csv")
def show_date_info():
    date_selected = dropdown.get()
    selected_data = data[data['Date'] == date_selected]
    table.delete(*table.get_children())
    for index, row in selected_data.iterrows():
        room_temperatures = [row[f"S{i}_Temp"] for i in range(1, 5)]
        room_sounds = [row[f"S{i}_Sound"] for i in range(1, 5)]
        room_lights = [row[f"S{i}_Light"] for i in range(1, 5)]
        row_data = [date_selected, row['Time']] + room_temperatures + room_sounds + room_lights + [row['Room_Occupancy_Count']]
        table.insert("", tk.END, values=row_data)
wn = tk.Tk()
wn.title("Occupancy Information")
dropdown = tk.Label(wn, text="Select Date")
dropdown.pack()
dates = data['Date'].unique().tolist()
dropdown = ttk.Combobox(wn, values=dates)
dropdown.pack()
show_button = tk.Button(wn, text="Show", command=show_date_info)
show_button.pack()
table_frame = tk.Frame(wn)
table_frame.pack(pady=10)
table = ttk.Treeview(table_frame, columns=('Date', 'Time', 'Room 1 Temp', 'Room 2 Temp', 'Room 3 Temp', 'Room 4 Temp',
                                           'Room 1 Sound', 'Room 2 Sound', 'Room 3 Sound', 'Room 4 Sound',
                                           'Room 1 Light', 'Room 2 Light', 'Room 3 Light', 'Room 4 Light',
                                           'Occupancy Count'), show='headings')
table.heading('Date', text='Date')
table.heading('Time', text='Time')
table.heading('Room 1 Temp', text='Room 1 Temp')
table.heading('Room 2 Temp', text='Room 2 Temp')
table.heading('Room 3 Temp', text='Room 3 Temp')
table.heading('Room 4 Temp', text='Room 4 Temp')
table.heading('Room 1 Sound', text='Room 1 Sound')
table.heading('Room 2 Sound', text='Room 2 Sound')
table.heading('Room 3 Sound', text='Room 3 Sound')
table.heading('Room 4 Sound', text='Room 4 Sound')
table.heading('Room 1 Light', text='Room 1 Light')
table.heading('Room 2 Light', text='Room 2 Light')
table.heading('Room 3 Light', text='Room 3 Light')
table.heading('Room 4 Light', text='Room 4 Light')
table.heading('Occupancy Count', text='Occupancy Count')
table.column('Date', width=80)
table.column('Time', width=80)
table.column('Room 1 Temp', width=100)
table.column('Room 2 Temp', width=100)
table.column('Room 3 Temp', width=100)
table.column('Room 4 Temp', width=100)
table.column('Room 1 Sound', width=100)
table.column('Room 2 Sound', width=100)
table.column('Room 3 Sound', width=100)
table.column('Room 4 Sound', width=100)
table.column('Room 1 Light', width=100)
table.column('Room 2 Light', width=100)
table.column('Room 3 Light', width=100)
table.column('Room 4 Light', width=100)
table.column('Occupancy Count', width=120)
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", rowheight=25)
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
table.pack()
wn.mainloop()

