from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
CREAMY = "#FCFAEE"
RED = "#B8001F"
BLACK = "#181C14"
# ---------------------------- PASSWORD SEARCH ---------------------------------- #
def search():
    if len(website_entry.get()) == 0:
        messagebox.showinfo(message="you left some fields empty")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                file_found = True
        except FileNotFoundError:
            messagebox.showinfo(message= "Error", detail="Data file was not found")
            file_found = False
        if file_found:
            try:
                user_email = data[website_entry.get()]["email"]
                user_password = data[website_entry.get()]["password"]
                messagebox.showinfo(message= f"{website_entry.get()}", detail=f"Email: {user_email}\nPassword:  {user_password}")
            except KeyError:
                messagebox.showinfo(message= "Error", detail="No details for the website exist")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_list1 = [random.choice(letters) for i in range(random.randint(8, 10))]
    pass_list2 = [random.choice(symbols) for j in range(random.randint(2, 4))]
    pass_list3 = [random.choice(numbers) for k in range(random.randint(2, 4))]
    password_list = pass_list1 + pass_list2 + pass_list3

    random.shuffle(password_list)

    password = "".join(password_list)
    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if (len(website) == 0) or (len(password) == 0) or (len(email) == 0):
        messagebox.showinfo(message="you left some fields empty")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg= CREAMY)
window.title("Password Manager")

#canvas
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=CREAMY)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", bg=CREAMY, fg=RED, font=("Courier", 15, "bold"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=CREAMY, fg=RED, font=("Courier", 15, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=CREAMY, fg= RED, font=("Courier", 15, "bold"))
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=26, highlightthickness=0, fg=BLACK, bg=CREAMY, font=("Courier", 12, "bold"))
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=49, highlightthickness=0, bg=CREAMY, fg=BLACK, font=("Courier", 12, "bold"))
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "Kemodragon2005@gmail.com")

password_entry = Entry(width=26, highlightthickness=0, bg=CREAMY, fg=BLACK, font=("Courier", 12, "bold"))
password_entry.grid(column=1, row=3)

#Buttons
generate_button = Button(width=14, highlightbackground=CREAMY, text="Generate", font=("Courier", 15, "bold"), command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(width=36, highlightbackground=CREAMY, text="Add", font=("Courier", 15, "bold"), command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(width=14, highlightbackground=CREAMY, text="Search", font=("Courier", 15, "bold"), command=search)
search_button.grid(column=2, row=1)





window.mainloop()