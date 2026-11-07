from sqlite3 import connect

modifier = connect('PyGymDB.db')
try:
    # modifier.execute(Modifications)
    modifier.commit()
    print("Succès.\n"
          "N'oublie pas de supprimer les commandes et modifier les autres fichiers.")
finally:
    modifier.close()
