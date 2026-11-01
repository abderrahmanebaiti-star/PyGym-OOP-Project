from _sqlite3 import connect
from datetime import date

DB_NAME = 'BaseDeDonne.db'

# Open
def get_connection():
    conn = connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


PyGymDB = get_connection()
PyGymDB.execute("CREATE TABLE IF NOT EXISTS GymMembers ("
                "ID_member VARCHAR PRIMARY KEY,"
                "password VARCHAR,"
                "date TIMESTAMP)")
PyGymDB.execute("CREATE TABLE IF NOT EXISTS GymSubs ("
                "ID_member VARCHAR PRIMARY KEY,"
                "type_offre VARCHAR,"
                "FOREIGN KEY (ID_member) REFERENCES GymMembers(ID_member))")
PyGymDB.commit()

# Partie Identification:
def get_password(username):
    row=PyGymDB.execute("SELECT password FROM GymMembers WHERE ID_member = ?",(username,)).fetchone()
    return row[0] if row else None

def add_member(username, password):
    PyGymDB.execute('INSERT INTO GymMembers(ID_member,password,date) Values (?,?,?)',(username,password,date.today().isoformat()))
    PyGymDB.commit()

# Partie Subscription:
def get_subscription(username):
    row = PyGymDB.execute("SELECT type_offre FROM GymSubs WHERE ID_member = ?",
                          (username,)).fetchone()
    return row[0] if row else None

def set_subscription(username, offer):
    if get_subscription(username) is None:
        PyGymDB.execute("INSERT INTO GymSubs (ID_member, type_offre) VALUES (?, ?)",
                        (username, offer))
    else:
        PyGymDB.execute("UPDATE GymSubs SET type_offre = ? WHERE ID_member = ?",
                        (offer, username))
    PyGymDB.commit()

# Close
def close():
    PyGymDB.close()

if __name__ == '__main__':
    close()