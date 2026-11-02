from SubscriptionPyGym import Subscription
from SessionsPyGym import sessions_page
from StartUpPyGym import start
from IdentificationPyGym import *

dark_blue = "#306998"
blue = "#4B8BBE"
yellow = "#FFD43B"

main_window = Tk()
main_window.title("PyGym")
main_window.geometry("360x320")
main_window.configure(bg=blue)

def go_sessions(username):
    sessions_page(main_window, username, back=go_subscription)

def go_subscription(username):
    Subscription(main_window, username, go_sessions)


start(main_window,
      lambda w: LogIn(w, go_subscription),
      lambda w: SignUp(w, go_subscription))

main_window.mainloop()