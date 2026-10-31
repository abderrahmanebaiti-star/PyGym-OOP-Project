from PyGymDatabase import *
from tkinter import *
from tkinter.messagebox import *

DB_NAME = "BaseDeDonne.db"


OFFRES = [
    ("Basic", 9.99, "$", "machines"),
    ("Standard", 14.99, "$", "machines + pool"),
    ("Premium", 19.99, "$", "toutes options"),
]


def membre_subscription(ID_member):
    """Renvoie None (introuvable), True (abonné) ou False (non abonné)."""
    PyGymDatabase = connect(DB_NAME)
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
        window.title("Gym - Vérification d'abonnement")
        window.geometry("420x320")

        Label(window, text="Entrez l'ID du membre :",
              font=("Arial", 12)).pack(pady=(20, 5))

        self.entry_id = Entry(window, font=("Arial", 12), justify="center")
        self.entry_id.pack()
        self.entry_id.focus()
        self.entry_id.bind("<Return>", lambda event: self.verifier())

        Button(window, text="Vérifier", font=("Arial", 11),
               command=self.verifier).pack(pady=10)

        self.label_resultat = Label(window, text="", font=("Arial", 12, "bold"))
        self.label_resultat.pack(pady=5)

        self.frame_offres = Frame(window)
        self.frame_offres.pack(pady=10, padx=20, anchor="w")

    def vider_offres(self):
        for widget in self.frame_offres.winfo_children():
            widget.destroy()

    def afficher_offres(self):
        self.vider_offres()
        Label(self.frame_offres, text="Nos offres d'abonnement :",
                 font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 5))

        for nom, prix, devise, description in OFFRES:
            Label(self.frame_offres,
                     text=f"• {nom} : {prix}{devise} /mois ({description})",
                     font=("Arial", 11)).pack(anchor="w")

    def verifier(self):
        id_member = self.entry_id.get().strip()
        self.vider_offres()

        if not id_member:
            showwarning("Attention", "Veuillez entrer un ID.")
            return

        try:
            status = membre_subscription(id_member)
        except Error as e:
            showerror("Erreur base de données", str(e))
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


fenetre = Tk()
GymApp(fenetre)
fenetre.mainloop()
