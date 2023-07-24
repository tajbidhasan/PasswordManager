from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import json

FONT_NAME = "Times New Roman"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    new_password = "".join(password_list)

    input_password.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()

    json_data = {website: {
        "Email": username,
        "Password": password
    }

    }

    if len(password) < 0 and len(website) < 0 and len(username) < 0:
        messagebox.showerror(title="Error", message="Please do not leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving the data
                json.dump(json_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(json_data)
            with open("data.json", "w") as data_file:
                # saving the data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_username.delete(0, END)
            input_password.delete(0, END)


def find_password():
    website = input_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="NO data file found")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassowrd: {password}")
        else:
            messagebox.showinfo(title=website, message="No record")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website", font=(FONT_NAME, 14))
label_website.grid(column=0, row=1)

label_username = Label(text="Email/Username", font=(FONT_NAME, 14))
label_username.grid(column=0, row=2)

label_password = Label(text="Password", font=(FONT_NAME, 14))
label_password.grid(column=0, row=3)

input_website = Entry(width=21)
input_website.grid(column=1, row=1)
input_website.focus()

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)

input_username = Entry(width=38)
input_username.grid(columnspan=2, column=1, row=2)

input_password = Entry(width=21)
input_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, columnspan=2, row=4)

window.mainloop()
