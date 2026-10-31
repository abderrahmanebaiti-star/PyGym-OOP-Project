from sqlite3 import *
from PyGymIdentif import *

""" 
Plan TKINTER:
1. Interface Label (PyGym)
             Boutons (Log In, Sign Up, Cancel)
2. Interface Entrées pour ID_Member et Mot de passe (pour Log In et Sign Up)
3. Si Success, interface Label (ID_Member, Date expiration abonnement (si abonné))
                         Boutons (Add subscription, Upgrade subscription, Cancel Subscription, Log Out)
Plan DB:
Table Members (ID member, Mot de passe (encrypted), Subscription Status (True/False))
Table Abonnements (ID member, Date Début, Date Expiration, Type Abonnement)
Table Séances (ID member, Schedule, Types Séances, Dernière Visite) 
"""

PyGymWindow = Tk()

PyGymDB = connect('PyGym.db')
PyGymDB.execute('CREATE TABLE IF NOT EXISTS GymMembers(ID_member VARCHAR PRIMARY KEY, mot_de_passe VARCHAR, date_inscription DATETIME)')
PyGymDB.commit()

GymMembers = PyGymDB.execute('SELECT ID_member FROM GymMembers')
cursor = PyGymDB.execute('SELECT ID_member FROM GymMembers')
existing_members = cursor.fetchall()

class Subscription(Identification):
    def __init__(self):
        Identification.__init__(self)
    def subscription(self):
        pass
choice = input("1. Log in\n"
              "2. Sign up\n"
              "3. Cancel\n"
              "Enter a valid choice: ")
""" 
On va changer les choix (1, 2, 3) aux boutons (Log In, Sign up, Cancel) en 1.
"""
PyGymWindow.mainloop()