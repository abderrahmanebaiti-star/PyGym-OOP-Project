from         tkinter            import *
from         tkinter.messagebox import *
import customtkinter            as ctk
from   DatabasePyGym import hash_password, get_password, add_member, close
import    ThemePyGym as theme


class Identification:
    def __init__(self, window, for_next):
        self.window = window
        self.bg = self.window.cget("bg")
        self.for_next = for_next
        self.username = StringVar()
        self.password = StringVar()
        self.all_input = ctk.CTkFrame(window, **theme.CARD)
    def id_input(self, string, comm, button_color, font_color="Black"):
        self.window.title("PyGym - Identification")
        self.all_input.place(relx=.5, rely=.52, anchor=CENTER)
        title = ctk.CTkLabel(self.all_input, text=string.upper(), font=theme.TITLE, text_color=theme.yellow)
        title.grid(row=0, column=0, sticky=W, padx=32, pady=(28, 10))

        username_label = ctk.CTkLabel(self.all_input, text="Username", font=theme.SMALL, text_color=theme.muted)
        username_label.grid(row=1, column=0, sticky=W, padx=32)

        username_entry = ctk.CTkEntry(self.all_input, textvariable=self.username, font=theme.TEXT, **theme.ENTRY)
        username_entry.focus_set()
        username_entry.grid(row=2, column=0, padx=32, pady=(2, 14))

        password_label = ctk.CTkLabel(self.all_input, text="Password", font=theme.SMALL, text_color=theme.muted)
        password_label.grid(row=3, column=0, sticky=W, padx=32)

        password_entry = ctk.CTkEntry(self.all_input, textvariable=self.password, show="●", font=theme.TEXT, **theme.ENTRY)
        password_entry.grid(row=4, column=0, padx=32, pady=(2, 0) )

        identification_button = ctk.CTkButton(self.all_input, text=string, command=comm, font=theme.BOLD, fg_color=button_color,
                                              text_color=font_color, hover_color=theme.yellow_hover, corner_radius=12, width=290, height=46)
        identification_button.grid(row=5, column=0, padx=32, pady=(24, 32))
        username_entry.bind("<Return>", lambda event: password_entry.focus_set())  # Entree -> case suivante
        password_entry.bind("<Return>", lambda event: comm())
        theme.nav_bar(self.window, lambda: self.__class__(self.window, self.for_next))

    def add_account(self):
        add_member(self.username.get(), hash_password(self.password.get()))
        showinfo(message="Account successfully created.")
        self.endID()
    def endID(self):
        self.all_input.destroy()


class LogIn(Identification):
    def __init__(self, window, after_ID):
        super().__init__(window, after_ID)
        self.id_input("Log In", self.login, button_color=theme.yellow, font_color=theme.bg)

    def login(self):
        input_username = self.username.get().strip()
        correct_password = get_password(input_username)
        if correct_password is not None:
            if correct_password == hash_password(self.password.get()):
                showinfo(message="Logged in successfully.")
                self.endID()
                self.for_next(input_username)
            else:
                try_again = askretrycancel(title="Error",
                                           message="Incorrect password. Try Again?")
                if try_again:
                    self.password.set('')
                else:
                    self.window.destroy()
                    close()
        else:
            try_signup = askyesnocancel(title="Account not found",
                                        message="This account does not exist. Sign up instead?")
            if try_signup is None:
                self.window.destroy()
                close()
            elif try_signup:
                self.all_input.destroy()
                SignUp(self.window, self.for_next)
            else:
                self.username.set('')
                self.password.set('')


class SignUp(Identification):
    def __init__(self, window, after_ID):
        super().__init__(window, after_ID)
        self.id_input("Sign Up", self.signup, button_color=theme.yellow, font_color=theme.bg)

    def signup(self):
        if not self.username.get().strip() or not self.password.get():
            showwarning(title="Empty field!",
                        message="Username and password are required.")
            return
        if get_password(self.username.get()) is None:
            self.add_account()
            self.for_next(self.username.get())
        else:
            login_instead = askyesnocancel(title="Existing account",
                                           message="Account with this name already exists. Log In instead?")
            if login_instead is None:
                self.window.destroy()
                close()
            elif login_instead:
                self.all_input.destroy()
                LogIn(self.window, self.for_next)
            else:
                self.username.set('')
                self.password.set('')

if __name__ == '__main__':
    from MainPyGym import main_window
    # On teste Log In
    LogIn(main_window, after_ID=lambda u: Label(main_window,
                       text=f"Username: {u}", bg=main_window.cget("bg"),
                       font=("Georgia", 16)).pack())
    # E.g: Username: test
    #      Password: test
    main_window.mainloop()
