from sqlite3 import connect

db = connect('BaseDeDonne.db')
try:
    # db.execute(Tes modifications)
    db.commit()
    print("Succès.\n"
          "N'oublie pas de supprimer les commandes et modifier les autres fichiers.")
finally:
    db.close()
# deleted column id_abo, actif from abonnement
# added constraints to tables (primary-foreign to ID_member)
# changed "Abonnement" to "GymSubs"
# changed database name to "PyGymDB"