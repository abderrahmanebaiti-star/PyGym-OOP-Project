from   SubscriptionPyGym import Subscription
from       SessionsPyGym import sessions_page
from        StartUpPyGym import start
from IdentificationPyGym import *
import customtkinter as ctk
import ThemePyGym as theme

main_window = ctk.CTk()
main_window.title("PyGym")
main_window.geometry("600x720")
main_window.configure(fg_color=theme.bg)
theme.set_background(main_window)

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
