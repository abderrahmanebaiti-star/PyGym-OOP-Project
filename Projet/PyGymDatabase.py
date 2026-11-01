from sqlite3 import connect
from datetime import date

DB_NAME = 'PyGymDB.db'


def get_connection():
    conn = connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


PyGymDB = get_connection()
# Initialisation Identification
PyGymDB.execute("CREATE TABLE IF NOT EXISTS GymMembers ("
                "ID_member VARCHAR PRIMARY KEY,"
                "password VARCHAR,"
                "date TIMESTAMP)")
# Initialisation Subscription
PyGymDB.execute("CREATE TABLE IF NOT EXISTS GymSubs ("
                "ID_member VARCHAR PRIMARY KEY,"
                "type_offre VARCHAR,"
                "FOREIGN KEY (ID_member) REFERENCES GymMembers(ID_member))")
# Initialisation Session
PyGymDB.execute("CREATE TABLE IF NOT EXISTS Sessions ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "ID_member VARCHAR,"
                "date_time TEXT,"
                "activity VARCHAR,"
                "FOREIGN KEY (ID_member) REFERENCES GymMembers(ID_member))")
PyGymDB.commit()


# Partie Identification:
def get_password(username):
    row = PyGymDB.execute("SELECT password FROM GymMembers WHERE ID_member = ?", (username,)).fetchone()
    return row[0] if row else None


def add_member(username, password):
    PyGymDB.execute('INSERT INTO GymMembers(ID_member,password,date) Values (?,?,?)',
                    (username, password, date.today().isoformat()))
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


# Partie Sessions:
activities = ["Musculation", "Cardio", "Yoga"]


def is_subscribed(username):
    # abonné = il a une ligne dans GymSubs
    return get_subscription(username) is not None


def add_session(username, activity):
    # enregistre la séance seulement si le membre est abonné
    if is_subscribed(username):
        PyGymDB.execute("INSERT INTO Sessions(ID_member, date_time, activity) VALUES (?, datetime('now','localtime'), ?)",
                        (username, activity))
        PyGymDB.commit()
        return True
    return False


def get_sessions(username):
    return PyGymDB.execute("SELECT date_time,activity FROM Sessions WHERE ID_member = ? ORDER BY id DESC",
                           (username,)).fetchall()


# --- Seulement pour TESTER (donne une offre à un membre) ---
def set_offer(username, offer):
    set_subscription(username, offer)


# Close
def close():
    PyGymDB.close()


if __name__ == '__main__':
    close()