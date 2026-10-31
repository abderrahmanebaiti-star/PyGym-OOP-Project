import os
from PyGymDatabase import *

# os.rename('BaseDeDonne.db', 'PyGymDB.db')

db = connect('BaseDeDonne.db')

'''
db.execute("ALTER TABLE Abonnement RENAME TO PyGymSubscribers")
db.commit()
'''


db.execute("ALTER TABLE Abonnement DROP COLUMN actif")
db.commit()
db.close()