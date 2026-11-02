from   SubscriptionPyGym import Subscription
from       SessionsPyGym import sessions_page
from        StartUpPyGym import start
from IdentificationPyGym import *

dark_blue = "#3776AB"
blue = "#4B8BBE"
yellow = "#FFD43B"

main_window = Tk()
main_window.title("PyGym")
main_window.geometry("500x500")
main_window.configure(bg=dark_blue)

def go_sessions(username):
    sessions_page(main_window, username, go_subscription)

def go_subscription(username):
    Subscription(main_window, username, go_sessions)

if __name__ == "__main__":
    try:
        start(main_window,
              lambda w: LogIn(w, go_subscription),
              lambda w: SignUp(w, go_subscription))

        main_window.mainloop()
    finally:
        close()