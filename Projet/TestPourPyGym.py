from TestPyGymStart import *
from TestPyGymID import *

dark_blue = "#306998"
blue = "#4B8BBE"
yellow = "#FFD43B"

window = Tk()
window.title("PyGym")
window.geometry("360x320")
window.configure(bg="black")

u = start(window, LogIn, SignUp)

window.mainloop()