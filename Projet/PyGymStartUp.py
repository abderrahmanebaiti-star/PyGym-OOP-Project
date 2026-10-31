from tkinter import *

dark_blue = "#306998"
white = "#FFFFFF"
blue = "#4B8BBE"
yellow = "#FFD43B"

title_font = "Georgia"
button_font = "Arial"


PyGymWindow = Tk()

PyGymWindow.title("PyGym")
PyGymWindow.geometry("360x320")
PyGymWindow.configure(bg=blue)

project_title = Label(PyGymWindow, text="PyGym", font=(title_font, 30),
                      bg=blue, fg=yellow)
project_title.pack(pady=(60, 30))
def call_log_in():
    print("Log in")
    PyGymWindow.destroy()
def call_sign_up():
    print("Sign up")
    PyGymWindow.destroy()
log_in_button = Button(PyGymWindow, text="Log in", command=call_log_in,
                      bg=dark_blue, fg=white, font=(button_font, 12), width=20, height=2)
log_in_button.pack(pady=(0, 15))

sign_up_button = Button(PyGymWindow, text="Sign up", command=call_sign_up,
                       bg=yellow, fg=dark_blue, font=(button_font, 12), width=20, height=2)
sign_up_button.pack(pady=(0, 15))

PyGymWindow.mainloop()