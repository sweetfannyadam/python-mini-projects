from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([choice(letters) for _ in range(randint(8, 10))] +
                     [choice(numbers) for _ in range(randint(2, 4))] +
                     [choice(symbols) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    return password, password_entry.insert(0, password), pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()

    new_data = {
        website_input:
            {"email": email_input,
             "password": password_input
             }
    }

    if len(website_input) > 0 and len(email_input) > 0 and len(password_input) > 0:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered: \n{website_input}"
                                                                     f"\n{email_input}\n{password_input}"
                                                                     f"\nIs it ok to save?")
        if is_ok:
            try:
                with open(file="data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open(file="data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            messagebox.showinfo(title="Information", message="Successful!")
            return data_file, print('Data telah diinput')

    else:
        messagebox.showerror(message="Please don't leave any fields empty!")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_input = website_entry.get()
    if len(website_input) > 0:
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="There are no data stored, please save any password first.")
        else:
            if website_input in data:
               messagebox.showinfo(title=website_input, message=f"Email: {data[website_input]['email']}\n"
                                                                f"Password: {data[website_input]['password']}")
            else:
                messagebox.showinfo(title="Information", message="No details for the website exists.")
        finally:
            website_entry.delete(0, END)
    else:
        messagebox.showerror(title="Warning", message="Please don't leave website field empty!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightcolor="black")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="news")
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="news")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="news")
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="news")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="news")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="news")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="news")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="news")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="news")

window.mainloop()
