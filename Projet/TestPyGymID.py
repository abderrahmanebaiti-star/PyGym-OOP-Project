from tkinter import *
from tkinter.messagebox import *
from PyGymDatabase import get_password, add_member, close

label_font = "Georgia"
yellow = "#FFD43B"
dark_blue = "#306998"

class Identification:
    def __init__(self, window, next_interface):
        self.window = window
        self.on_success = next_interface
        self.username = StringVar()
        self.password = StringVar()
        self.all_input = Frame(window)
    def id_input(self, string, comm, button_color, font_color="Black"):
        self.window.title("PyGym - Identification")
        self.all_input.configure(bg=self.window.cget("bg"))
        self.all_input.place(relx=.5, rely=.5, anchor=CENTER)

        username_label = Label(self.all_input, text="Username: ", bg=self.window.cget("bg"), fg="white", font=label_font)
        username_label.grid(row=0, column=0)

        username_entry = Entry(self.all_input, textvariable=self.username)
        username_entry.focus_set()
        username_entry.grid(row=0, column=1)

        password_label = Label(self.all_input, text="Password: ", bg=self.window.cget("bg"), fg="white", font=label_font)
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
    def __init__(self, window, after_ID):
        super().__init__(window, after_ID)
        self.id_input("Log In", self.login, button_color=yellow, font_color=dark_blue)

    def login(self):
        input_username = self.username.get()
        input_password = get_password(input_username)
        if input_password is not None:
            if input_password == self.password.get():
                showinfo(message="Logged in successfully")
                self.endID()
                self.on_success(self.username.get())
            else:
                try_again = askretrycancel(title="Error", message="Incorrect password. Try Again?")
                if try_again:
                    self.password.set('')
                else:
                    self.window.destroy()
                    close()
        else:
            try_signup = askyesnocancel(title="Warning", message="This account does not exist. Sign up instead?")
            if try_signup is None:
                self.window.destroy()
                close()
            elif try_signup:
                self.all_input.destroy()
                SignUp(self.window, self.on_success)
            else:
                self.username.set('')
                self.password.set('')


class SignUp(Identification):
    def __init__(self, window, after_ID):
        super().__init__(window, after_ID)
        self.id_input("Sign Up", self.signup, button_color=dark_blue, font_color=yellow)

    def signup(self):
        if not self.username.get().strip() or not self.password.get():
            showwarning("Empty field!", "Username and password are required.")
            return
        if get_password(self.username.get()) is None:
            self.add_account()
            self.on_success(self.username.get())
        else:
            login_instead = askyesnocancel(title="Existing account",
                                           message="Account with this name already exists. Log In instead?")
            if login_instead is None:
                self.window.destroy()
            elif login_instead:
                self.all_input.destroy()
                LogIn(self.window, self.on_success)
            else:
                self.username.set('')
                self.password.set('')