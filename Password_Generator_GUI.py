
############################################# PASSWORD GENERATOR TOOL #################################################

#importing necessary modules
import string
import random
from tkinter import *
import pyperclip

#Creating a window
root = Tk()
root.title("Password Generator Tool")
root.geometry("500x350")

#Creating a label
label_title = Label(root, text="Choose the strength of your password", fg='white', bg='blue', font=("Arial", 15, "bold"))
label_title.pack()


choice = IntVar()
#selection method get the choice
def selection():
    selection = choice.get()

#poor only contain uppercase and lowercase letter
poor = string.ascii_uppercase + string.ascii_lowercase
#average contain uppercase and lowercase letter as well as digits
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
#strong password contain all the letters as well as special symbols
strong = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation


#Creating a radio button to ask the user for strength of password
rb1 = Radiobutton(root, text="poor password", variable=choice, value=1, command=selection)
rb1.pack()

rb2 = Radiobutton(root, text="average password", variable=choice, value=2, command=selection)
rb2.pack()

rb3 = Radiobutton(root, text="strong password", variable=choice, value=3, command=selection)
rb3.pack()

#label for length of password
label_password = Label(root, text="Choose length of your password",fg='white',bg='red',font=("Arial", 10, "bold"))
label_password.pack()

val = IntVar()

#Creating a spin box to adust the length of password
spintlength = Spinbox(root, from_=8, to=100, textvariable=val, width=15)
spintlength.pack()

#Creating a passgen function to get the choice
def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))

    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))

    elif choice.get() == 3:
        return "".join(random.sample(strong, val.get()))

# declaring a variable of string type and this variable will be
# used to store the password generated
passstr = StringVar()
#callback function generate a password
def callback():
    # setting the password to the entry widget
    passstr.set(passgen())

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

#Creating a submit button for generate a password
submit_button = Button(root, text="Generate Password", command=callback)
submit_button.pack(pady=10)

# entry widget to show the generated password
Entry(root, textvariable=passstr,font =25).pack(pady=3)

# button to call the copytoclipboard function
copy_button = Button(root, text="Copy to clipboard", command=copytoclipboard)
copy_button.pack()

# mainloop() is an infinite loop used to run the application when
# it's in ready state
root.mainloop()
