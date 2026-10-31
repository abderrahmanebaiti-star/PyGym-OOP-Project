from tkinter import *
from tkinter.messagebox import *
from PyGymDatabase import *

label_font = "Georgia"
yellow = "#FFD43B"
dark_blue = "#306998"

class Identification:
    def __init__(self, window):
        self.window = window
        self.username = StringVar()
        self.password = StringVar()
        self.all_input = Frame(window)
    def id_input(self, string, comm, button_color, font_color="Black"):
        self.window.title("PyGym - Identification")
        self.all_input.configure(bg=self.window.cget("bg"))
        self.all_input.place(relx=.5, rely=.5, anchor=CENTER)

        username_label = Label(self.all_input, text="Username: ", bg=self.window.cget("bg"), font=label_font)
        username_label.grid(row=0, column=0)

        username_entry = Entry(self.all_input, textvariable=self.username)
        username_entry.focus_set()
        username_entry.grid(row=0, column=1)

        password_label = Label(self.all_input, text="Password: ", bg=self.window.cget("bg"), font=label_font)
        password_label.grid(row=1, column=0)

        password_entry = Entry(self.all_input, textvariable=self.password, show="\u25cf")
        password_entry.grid(row=1, column=1)

        identification_button = Button(self.all_input, text=string, command=comm, font=label_font, bg=button_color, fg=font_color)
        identification_button.grid(row=2, column=1, padx=10)

    def add_account(self):
        add_member(self.username.get(), self.password.get())
        showinfo(message="Account successfully created")
        self.endID()
    def endID(self):
        self.all_input.destroy()


class LogIn(Identification):
    def __init__(self, window):
        self.window = window
        super().__init__(window)
        self.id_input("Log In", self.login, button_color=yellow, font_color=dark_blue)
        window.configure(bg=dark_blue)

    def login(self):
        nom = self.username.get()
        motdepasse = get_password(nom)
        if motdepasse is not None:
            if motdepasse == self.password.get():
                showinfo(message="Logged in successfully")
                self.endID()
                Label(self.window, text="INTERFACE LI MORAHA", font=("TkDefaultFont", 20)).pack()
            else:
                try_again = askretrycancel(title="Error", message="Incorrect password. Try Again?")
                if try_again:
                    self.password.set('')
                else:
                    self.window.destroy()
        else:
            try_signup = askyesnocancel(title="Warning", message="This account does not exist. Sign up instead?")
            if try_signup is None:
                self.window.destroy()
            elif try_signup:
                self.all_input.destroy()
                SignUp(self.window)
            else:
                self.username.set('')
                self.password.set('')


class SignUp(Identification):
    def __init__(self, window):
        self.window = window
        super().__init__(window)
        self.id_input("Sign Up", self.signup, button_color=dark_blue, font_color=yellow)
        window.configure(bg=yellow)

    def signup(self):
        if get_password(self.username.get()) is None:
            self.add_account()
            Label(self.window, text="INTERFACE LI MORAHA", font=("TkDefaultFont", 20)).pack()
        else:
            login_instead = askyesnocancel(title="Warning",
                                           message="Account with this name already exists. Log In instead?")
            if login_instead is None:
                self.endID()
            elif login_instead:
                self.all_input.destroy()
                LogIn(self.window)
            else:
                self.username.set('')