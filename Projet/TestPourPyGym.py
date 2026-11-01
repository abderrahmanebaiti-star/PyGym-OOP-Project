from TestPyGymSubscription import Subscription
from TestPyGymStart import *
from TestPyGymID import *

dark_blue = "#306998"
blue = "#4B8BBE"
yellow = "#FFD43B"

main_window = Tk()
main_window.title("PyGym")
main_window.geometry("360x320")
main_window.configure(bg="black")

def go_subscription(username):
    Subscription(main_window, username)

u = start(main_window,
          lambda w: LogIn(w, go_subscription),
          lambda w: SignUp(w, go_subscription))

main_window.mainloop()