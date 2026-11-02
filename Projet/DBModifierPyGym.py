from sqlite3 import connect

modifier = connect('PyGymDB.db')
try:
    # modifier.execute(Tes modifications)
    modifier.execute("ALTER TABLE GymSubs RENAME COLUMN type_offre TO offer_type")
    modifier.commit()
    print("Succès.\n"
          "N'oublie pas de supprimer les commandes et modifier les autres fichiers.")
finally:
    modifier.close()