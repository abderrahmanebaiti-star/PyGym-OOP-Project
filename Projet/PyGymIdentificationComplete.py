from tkinter import *
from tkinter.messagebox import *
from PyGymDatabase import *

PyGymWindow = Tk()

class Identification:
    def __init__(self):
        self.username = StringVar()
        self.password = StringVar()
        self.all_input = None

    def id_input(self, string, comm):
        PyGymWindow.title("PyGym - Identification")
        self.all_input = Frame(PyGymWindow)
        self.all_input.place(relx=.5, rely=.5, anchor=CENTER)

        username_label = Label(self.all_input, text="Username: ")
        username_label.grid(row=0, column=0)

        username_entry = Entry(self.all_input, textvariable=self.username)
        username_entry.focus_set()
        username_entry.grid(row=0, column=1)


        password_label = Label(self.all_input, text="Password: ")
        password_label.grid(row=1, column=0)

        password_entry = Entry(self.all_input, textvariable=self.password, show="\u25cf")
        password_entry.grid(row=1, column=1)

        identification_button = Button(self.all_input, text=string, command=comm)
        identification_button.grid(row=2, column=1, padx=10)

    def add_account(self):
        add_member(self.username.get(), self.password.get())
        showinfo(message="Account successfully created")
        self.all_input.destroy()
class LogIn(Identification):
    def login(self):
        nom=self.username.get()
        motdepasse = get_password(nom)
        if motdepasse is not None:
            if motdepasse == self.password.get():
                showinfo(message="Logged in successfully")
                self.all_input.destroy()
                Label(PyGymWindow, text="INTERFACE LI MORAHA", font=("TkDefaultFont",20)).pack()
            else:
                try_again = askretrycancel(title="Error", message="Incorrect password. Try Again?")
                if try_again:
                    self.password.set('')
                else:
                    PyGymWindow.destroy()
        else :
            try_signup = askyesnocancel(title="Warning", message="This account does not exist. Sign up instead?")
            if try_signup is None:
                PyGymWindow.destroy()
            elif try_signup:
                self.all_input.destroy()
                SignUp()
            else:
                self.username.set('')
                self.password.set('')

    def __init__(self):
        Identification.__init__(self)
        self.id_input("Log In", self.login)


class SignUp(Identification):
    def __init__(self):
        super().__init__()
        self.id_input("Sign Up", self.signup)
    def signup(self):
        if get_password(self.username.get()) is None:
            self.add_account()
            Label(PyGymWindow, text="INTERFACE LI MORAHA", font=("TkDefaultFont", 20)).pack()
        else:
            login_instead = askyesnocancel(title="Warning", message="Account with this name already exists. Log In instead?")
            if login_instead is None:
                PyGymWindow.destroy()
            elif login_instead:
                LogIn()
            else:
                self.username.set('')
# Class Client:
#     def __init__(self,username):

if '__main__' == __name__:
    v = LogIn()
    '''
    Pour le moment ghi bdl l'action manuellement v = LogIn() ola SignUp() bach tester
    Mn b3d anzido les boutons m3a Titre kbir etc
    '''

    PyGymWindow.mainloop()
    close()