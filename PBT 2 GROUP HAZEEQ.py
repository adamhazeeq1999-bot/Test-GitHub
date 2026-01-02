'''
ADAM HAZEEQ BIN ABDUL HALIM (F1122)
MOHAMAD FAHRIN BIN MOHD AZHAR (F1126)
MUHAMMAD AZIM BIN AZHAR (F1062)
ADAM DANIAL BIN MOHD ALI HANAFIAH (F1110)
'''


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

registration = []

t = tk.Tk()
t.title("Registration Form")
t.geometry("500x450")


full_name = tk.StringVar()
email = tk.StringVar()
gender = tk.StringVar()
country = tk.StringVar()
java = tk.IntVar()
python = tk.IntVar()


def form():
    full_name_value = full_name.get()  
    email_value = email.get()
    gender_value = gender.get()
    country_value = country.get()

    if java.get() == 1 and python.get() == 1:
        program = "Java, Python"
    elif java.get() == 1:
        program = "Java"
    elif python.get() == 1:
        program = "Python"
    else:
        program = "No Program"

    if country_value == "Please select your country":
        messagebox.showwarning("Warning", "Please select a country.")
        return


    registration.append({
        "Full Name": full_name_value,
        "Email": email_value,
        "Gender": gender_value,
        "Country": country_value,
        "Program": program
    })

    messagebox.showinfo("Information", "Data saved successfully!")

 
    print("\n--- New Registration Check In ---")
    print(f"Full Name  : {full_name_value}")
    print(f"Email      : {email_value}")
    print(f"Gender     : {gender_value}")
    print(f"Country    : {country_value}")
    print(f"Programming: {program}")


tk.Label(t, text="Registration Form", font=('Arial', 14)).grid(row=0, column=1, pady=10)

tk.Label(t, text="Full name").grid(row=1, column=0, sticky='w', padx=10)
tk.Entry(t, textvariable=full_name).grid(row=1, column=1)

tk.Label(t, text="Email").grid(row=2, column=0, sticky='w', padx=10)
tk.Entry(t, textvariable=email).grid(row=2, column=1)

tk.Label(t, text="Gender").grid(row=3, column=0, sticky='w', padx=10)
tk.Radiobutton(t, text="Male", variable=gender, value="Male").grid(row=3, column=1, sticky='w')
tk.Radiobutton(t, text="Female", variable=gender, value="Female").grid(row=3, column=1)

tk.Label(t, text="Select your country").grid(row=4, column=0, sticky='w', padx=10)
country_combo = ttk.Combobox(t, textvariable=country, state='readonly', width=25)
country_combo['values'] = ("Please select your country", "Malaysia", "Indonesia", "Singapore", "Thailand")
country_combo.grid(row=4, column=1)
country_combo.current(0)

tk.Label(t, text="Programming").grid(row=5, column=0, sticky='w', padx=10)
tk.Checkbutton(t, text="Java", variable=java).grid(row=5, column=1, sticky='w')
tk.Checkbutton(t, text="Python", variable=python).grid(row=5, column=1)

tk.Button(t, text="Submit", command=form, bg="red", fg="white").grid(row=6, column=1, pady=10)


t.mainloop()
