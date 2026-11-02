from tkinter import *
def start(window, log_in, sign_up):
    dark_blue = "#306998"
    yellow = "#FFD43B"

    title_font  = "Georgia"
    button_font = "Georgia"
    StartUpFrame = Frame(window)
    StartUpFrame.pack(pady=(0, 15))
    StartUpFrame.configure(bg=window.cget("bg"))

    project_title = Label(StartUpFrame, text="PyGym", font=(title_font, 30),
                          bg=window.cget("bg"), fg=yellow)
    project_title.pack(pady=(60, 30))
    def call_log_in():
        StartUpFrame.destroy()
        log_in(window)
    def call_sign_up():
        StartUpFrame.destroy()
        sign_up(window)


    log_in_button = Button(StartUpFrame, text="Log in", command=call_log_in,
                          bg=dark_blue, fg=yellow, font=(button_font, 12), width=20, height=2)
    log_in_button.pack(pady=(0, 15))

    sign_up_button = Button(StartUpFrame, text="Sign up", command=call_sign_up,
                           bg=yellow, fg=dark_blue, font=(button_font, 12), width=20, height=2)
    sign_up_button.pack(pady=(0, 15))