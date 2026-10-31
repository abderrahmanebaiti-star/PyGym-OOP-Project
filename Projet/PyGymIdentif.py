from tkinter import *
from tkinter.messagebox import *

existing_members = ["ABC"]
PyGymWindow = Tk()

class Identification:
    def __init__(self):
        self.username = StringVar()
        self.password = StringVar()
        self.change_identification = None # Chof ila 7tajiti l hadi (fonction ktbdl lik mn login l signup ou viceversa)
        self.all_input = None
    def id_input(self, string, comm):
        PyGymWindow.title("PyGym - Identification")
        self.all_input = Frame(PyGymWindow)
        self.all_input.place(relx=.5, rely=.5, anchor=CENTER)

        username_label = Label(self.all_input, text="Username: ")
        username_label.focus_set()
        username_label.grid(row=0, column=0)

        username_entry = Entry(self.all_input, textvariable=self.username)
        username_entry.grid(row=0, column=1)


        password_label = Label(self.all_input, text="Password: ")
        password_label.grid(row=1, column=0)

        password_entry = Entry(self.all_input, textvariable=self.password, show="*")
        password_entry.grid(row=1, column=1)

        identification_button = Button(self.all_input, text=string, command=comm)
        identification_button.grid(row=2, column=1, padx=10)
        PyGymWindow.mainloop()
    def add_account(self):
        existing_members.append(self.username.get())
        showinfo(message="Account successfully created")
        PyGymWindow.quit()
class LogIn(Identification):
    def login(self):
        pass
    def __init__(self):
        Identification.__init__(self)
        self.id_input("Log In", self.login)

"""
Les cas:
Membre inscrit, mot de passe correcte (Success, entrer à l'interface du compte)
Membre inscrit, mot de passe incorrecte (Demander à réessayer ou cancel)
Membre non inscrit (Demander à sign up, réessayer le nom, ou cancel)
"""

class SignUp(Identification):
    def __init__(self):
        super().__init__()
        self.id_input("Sign Up", self.signup)
    def signup(self):
        if (self.username.get()) not in existing_members:
            self.add_account()
            print("# Success, interface suivante")
        else:
            login_instead = askyesnocancel(title="Warning", message="Account with this name already exists. Log in instead?")
            if login_instead is None:
                self.all_input.destroy()
            elif login_instead:
                print("# Je passerai à la fonction LogIn ici.")
                pass # Appel classe/fonction hna
            else:
                self.username.set('')
                self.password.set('')

u = SignUp()