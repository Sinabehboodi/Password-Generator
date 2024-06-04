import tkinter as tk
from tkinter import E,W
import random
import string

root = tk.Tk()

root.title('Password Generator')
root.configure(background='#c3c1e5')


name_lbl = tk.Label(
    root,
    text='PASSWORD GENERATOR',
    font=('Quanty Special DEMO', 20),
    bg='#c3c1e5',
    fg='#0a0a0a'
)
name_lbl.grid(padx=20,pady=10,columnspan=2)


# lenght label
lenght_lbl = tk.Label(
    root,
    text='Enter your length:',
    font=('Microsoft JhengHei UI',11,'bold'),
    bg='#c3c1e5',
    fg='#0a0a0a',
)
lenght_lbl.grid(sticky='w',row=1,padx=20)#


# user lenght
user_lengh = tk.Spinbox(
    root,
    from_=5,
    to_=20,
    width=10,
    font = ('Microsoft JhengHei UI', 11)
)
user_lengh.grid(row=1,column=1,padx=20,pady=10,sticky='w')


# label frame
label_frame = tk.LabelFrame(
    root,
    text='Settings',
    bg='#c3c1e5',
    fg='#0a0a0a',
    font=('Microsoft JhengHei UI', 10 , 'bold')
)
label_frame.grid(sticky='w',padx=20,pady=10)


# check button
lower_option = tk.IntVar()
upper_option = tk.IntVar()
symbole_option = tk.IntVar()
number_option = tk.IntVar()


# lowercase
font = ('Microsoft JhengHei UI', 11)
lower_check_btn = tk.Checkbutton(
    label_frame,
    text="lowercase (a-z)",
    variable=lower_option,
    bg='#c3c1e5',
    fg='#0a0a0a',
    font=font
)
lower_check_btn.grid(sticky='w',padx=5,pady=5)


# uppercase
upper_check_btn = tk.Checkbutton(
    label_frame,
    text="uppercase (A-Z)",
    variable=upper_option,
    bg='#c3c1e5',
    fg='#0a0a0a',
    font=font
)
upper_check_btn.grid(sticky='w',padx=5,pady=5)


# symbole
symbole_check_btn = tk.Checkbutton(
    label_frame,
    text="symbole (@#$%...)",
    variable=symbole_option,
    bg='#c3c1e5',
    fg='#0a0a0a',
    font=font
)
symbole_check_btn.grid(sticky='w',padx=5,pady=5)


# number
number_check_btn = tk.Checkbutton(
    label_frame,
    text="numbers (123...)",
    variable=number_option,
    bg='#c3c1e5',
    fg='#0a0a0a',
    font=font
)
number_check_btn.grid(sticky='w',padx=5,pady=5)

def generat_random_chr():
    choices = ''
    if lower_option.get():
        choices += string.ascii_lowercase
    if upper_option.get():
        choices += string.ascii_uppercase
    if symbole_option.get():
        choices += string.punctuation
    if number_option.get():
        choices += string.digits
        
    return random.choice(choices)

def generate_password():
    entry_show.delete(0, tk.END) 
    length = int(user_lengh.get())
    final_password = ""
    for i in range(length):
        final_password += generat_random_chr()
    entry_show.insert(0, final_password)


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_show.get())

# generate buttn
generate_btn = tk.Button(
    root,
    text="GENERATE",
    font=('Quanty Special DEMO', 13),
    width=20,
    bg='#6356db',
    fg='white',
    command=generate_password
)
generate_btn.grid(padx=20,pady=10,columnspan=2)


# An entry to display the generated password
entry_show = tk.Entry(
    root,
    text="GENERATE",
    font=(13),
    width=26,
    bd=0,
    bg='#c3c1e5',
    fg='black',
)
entry_show.grid(padx=20,pady=10,columnspan=2)


# copy buttn
copy_btn = tk.Button(
    root,
    text="copy clipboard",
    font=('Quanty Special DEMO', 13),
    width=20,
    bg='#6356db',
    fg='white',
    command=copy_to_clipboard
)
copy_btn.grid(padx=20,pady=10,columnspan=2)



root.mainloop()