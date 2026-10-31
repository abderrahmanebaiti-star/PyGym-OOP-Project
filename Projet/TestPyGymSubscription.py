from PyGymDatabase import *
from tkinter import *
from tkinter.messagebox import *

db_name = "BaseDeDonne.db"


offers = [
    ("Basic", 9.99, "$", "machines"),
    ("Standard", 14.99, "$", "machines + pool"),
    ("Premium", 19.99, "$", "toutes options"),
]


def subscription_status(ID_member):
    """Renvoie None (introuvable), True (abonné) ou False (non abonné)."""
    PyGymDatabase = connect(db_name)
    try:
        cursor = PyGymDatabase.cursor()
        cursor.execute(
            "SELECT actif FROM abonnement WHERE ID_member = ?",
            (ID_member,),
        )
        result = cursor.fetchone()
    finally:
        PyGymDatabase.close()

    if result is None:
        return None
    return bool(result[0])


class GymApp:
    def __init__(self, window):
        self.window = window
        window.title("Gym - Abonnement")

        Label(window, text="Entrez l'ID du membre :",
              font=("Arial", 12)).pack(pady=(20, 5))

        self.entry_id = Entry(window, font=("Arial", 12), justify="center")
        self.entry_id.pack()
        self.entry_id.focus()
        self.entry_id.bind("<Return>", lambda event: self.verify())

        Button(window, text="Vérifier", font=("Arial", 11),
               command=self.verify).pack(pady=10)

        self.label_resultat = Label(window, text="", font=("Arial", 12, "bold"))
        self.label_resultat.pack(pady=5)

        self.frame_offers = Frame(window)
        self.frame_offers.pack(pady=10, padx=20, anchor="w")

    def empty_offers(self):
        for widget in self.frame_offers.winfo_children():
            widget.destroy()

    def afficher_offres(self):
        self.empty_offers()
        Label(self.frame_offers, text="Nos offres d'abonnement :",
              font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 5))

        for nom, prix, devise, description in offers:
            Label(self.frame_offers,
                  text=f"• {nom} : {prix}{devise} /mois ({description})",
                  font=("Arial", 11)).pack(anchor="w")

    def verify(self):
        id_member = self.entry_id.get().strip()
        self.empty_offers()

        if not id_member:
            showwarning("Attention", "Veuillez entrer un ID.")
            return

        try:
            status = subscription_status(id_member)
        except Error:
            showerror("Erreur base de données", str(Error))
            return

        if status is None:
            self.label_resultat.config(text=" Membre introuvable.", fg="red")
        elif status:
            self.label_resultat.config(
                text="Membre trouvé : abonnement actif.", fg="green")
        else:
            self.label_resultat.config(
                text="Membre trouvé : abonnement inactif.", fg="orange")
            self.afficher_offres()


window = Tk()
GymApp(window)
window.mainloop()
