from sqlite3 import connect
from datetime import date
from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

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
# Partie Sessions:
# activité -> offre minimale requise
activities = {
    "Musculation": "Basic",     # machines
    "Cardio": "Basic",          # machines
    "Swimming": "Standard",     # machines + pool
    "Aquagym": "Standard",      # machines + pool
    "Yoga": "Premium",          # toutes options
    "CrossFit": "Premium",
    "Box": "Premium",
}

offer_level = {"Basic": 1, "Standard": 2, "Premium": 3}


def allowed_activities(username):
    offer = get_subscription(username)
    if offer is None:
        return []
    return [name for name, required in activities.items()
            if offer_level[offer] >= offer_level[required]]


def is_subscribed(username):
    return get_subscription(username) is not None


def add_session(username, activity):
    # enregistre la séance seulement si l'offre du membre couvre cette activité
    if activity in allowed_activities(username):
        PyGymDB.execute("INSERT INTO Sessions(ID_member, date_time, activity) "
                        "VALUES (?, datetime('now','localtime'), ?)",
                        (username, activity))
        PyGymDB.commit()
        return True
    return False

def get_sessions(username):
    return PyGymDB.execute("SELECT date_time,activity FROM Sessions WHERE ID_member = ? ORDER BY id DESC",
                           (username,)).fetchall()

# Close
def close():
    PyGymDB.close()


if __name__ == '__main__':
    print("Ce fichier n'est pas un programme.")
    close()