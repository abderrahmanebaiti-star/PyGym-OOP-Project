# import os
from sqlite3 import connect

# os.rename('BaseDeDonne.db', 'PyGymDB.db')

db = connect('BaseDeDonne.db')
try:
    '''
    db.execute("ALTER TABLE Abonnement RENAME TO PyGymSubscribers")
    db.execute("ALTER TABLE GymMembers RENAME COLUMN mot_de_pass TO password")
    db.commit()
    ''' # J'exécute plus tard
    # db.execute(Tes modifications)
    db.commit()
    print("Succès.\n"
          "N'oublie pas de supprimer les commandes et modifier les autres fichiers.")
finally:
    db.close()
# deleted column id_abo, actif from abonnement