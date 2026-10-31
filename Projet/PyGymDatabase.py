from _sqlite3 import *
from datetime import date

PyGymDB = connect('BaseDeDonne.db')
PyGymDB.execute("Create TABLE IF NOT EXISTS GymMembers(ID_member VARCHAR,mot_de_pass VARCHAR,date TIMESTAMP)")
PyGymDB.execute("CREATE TABLE if not exists Abonnement(id_abo VARCHAR,ID_member VARCHAR,type_offre VARCHAR, actif BOOLEAN DEFAULT 0)")
def get_password(username):
    row=PyGymDB.execute("SELECT mot_de_pass FROM GymMembers WHERE ID_member = ?",(username,)).fetchone()
    return row[0] if row else None
def add_member(username, password):
    PyGymDB.execute('INSERT INTO GymMembers(ID_member,mot_de_pass,date) Values (?,?,?)',(username,password,date.today().isoformat()))
    PyGymDB.commit()
def add_subscriber(username):
    PyGymDB.execute('INSERT INTO Abonnement(ID_member, type_offre, actif) VALUES (?, ?, ?)',
                    (username, "Aucun", 0))

    PyGymDB.commit()
def close():
    PyGymDB.close()

if __name__ == '__main__':
    print("Attention, n'exécute pas ce fichier!")
    close()