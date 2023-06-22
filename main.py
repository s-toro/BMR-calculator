import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

def calculate():
    bmr = 0
    gender = selected_gender.get()
    height = height_var.get()
    weight = weight_var.get()
    age = age_var.get()
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "Female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    tk.messagebox.showinfo('BMR', f'Your BMR is {bmr}')

# root 
root = tk.Tk()
root.geometry('640x480')
root.title('Basal Metabolic Rate (BMR) calculator')

age_var = tk.IntVar()
age_label = ttk.Label(root, text='Age').grid(row=0, column=0)
age_field = ttk.Entry(root, textvariable=age_var).grid(row=0, column=1, sticky='W')
selected_gender = tk.StringVar(root)
gender_label = ttk.Label(root, text='Gender').grid(row=1, column=0)
radio_buttons = {"Male" : "Male", "Female" : "Female"}
radio_button_row = 1
for (text, value) in radio_buttons.items():
    ttk.Radiobutton(root, variable=selected_gender,
                    text = text,
                    value = value).grid(row=radio_button_row, column=1, sticky='W')
    radio_button_row += 1
height_var = tk.IntVar()
height_label = ttk.Label(root, text='Height').grid(row=3, column=0)
height_field = ttk.Entry(root, textvariable = height_var).grid(row=3,column=1, sticky='W')
height_units_label = tk.Label(root, text='cm').grid(row=3, column=2, sticky='W')
weight_var = tk.IntVar()
weight_label = ttk.Label(root, text='Weight').grid(row=4, column=0)
weight_field = ttk.Entry(root, textvariable = weight_var).grid(row=4, column=1, sticky='W')
weight_unit_label = ttk.Label(root, text='kg').grid(row=4, column=2, sticky='W')
empty_label = ttk.Label(root).grid(row=5)
settings_label = ttk.Label(root, text='Settings').grid(row=6)
bmr_formula = tk.StringVar()
bmr_formula_label = ttk.Label(root, text='BMR esitmation formula:').grid(row=7)
bmr_formula_list = [
    'Mifflin-St Jeor',
    'Revised Harris-Benedict',
    'Katch-McArdle'
]
bmr_formula_drop = ttk.OptionMenu(root, bmr_formula, bmr_formula_list[0], *bmr_formula_list).grid(row=7, column=1)

calculate_button = ttk.Button(root, text='Calculate',
                            command=calculate).grid(row=9)
root.mainloop()
