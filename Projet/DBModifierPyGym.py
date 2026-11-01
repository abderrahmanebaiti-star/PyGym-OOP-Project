from sqlite3 import connect

db = connect('PyGymDB.db')
try:
    # db.execute(Tes modifications)
    db.commit()
    print("Succès.\n"
          "N'oublie pas de supprimer les commandes et modifier les autres fichiers.")
finally:
    db.close()