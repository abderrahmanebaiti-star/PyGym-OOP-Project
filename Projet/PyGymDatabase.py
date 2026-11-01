from _sqlite3 import *
from datetime import date

PyGymDB = connect('BaseDeDonne.db')
PyGymDB.execute("CREATE TABLE IF NOT EXISTS GymMembers(ID_member VARCHAR,mot_de_pass VARCHAR,date TIMESTAMP)")
PyGymDB.execute("CREATE TABLE if NOT EXISTS Abonnement(ID_member VARCHAR,type_offre VARCHAR)")
def get_password(username):
    row=PyGymDB.execute("SELECT mot_de_pass FROM GymMembers WHERE ID_member = ?",(username,)).fetchone()
    return row[0] if row else None
def add_member(username, password):
    PyGymDB.execute('INSERT INTO GymMembers(ID_member,mot_de_pass,date) Values (?,?,?)',(username,password,date.today().isoformat()))
    PyGymDB.commit()
def add_subscriber(username, offer):
    PyGymDB.execute('INSERT INTO Abonnement(ID_member, type_offre) VALUES (?, ?, ?)',
                    (username, offer, 0))
    PyGymDB.commit()
def close():
    PyGymDB.close()

if __name__ == '__main__':
    print("Attention, n'exécute pas ce code!")
    close()