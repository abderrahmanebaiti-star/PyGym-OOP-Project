from tkinter import *
from MainPyGym import yellow, blue


title_font = "Georgia"
button_font = "Georgia"

def start(window, log_in, sign_up):
    StartUpFrame = Frame(window)
    StartUpFrame.place(relx=.5, rely=.5, anchor=CENTER)
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
                          bg=blue, fg=yellow, font=(button_font, 12), width=20, height=2)
    log_in_button.pack(pady=(0, 15))

    sign_up_button = Button(StartUpFrame, text="Sign up", command=call_sign_up,
                           bg=yellow, fg=blue, font=(button_font, 12), width=20, height=2)
    sign_up_button.pack(pady=(0, 15))

if __name__ == "__main__":
    from MainPyGym import main_window
    start(main_window,
          lambda w : Label(w, text="Logging in",
                              bg=main_window.cget("bg"),
                                        font=(button_font, 16)).pack(),
          lambda w : Label(w, text="Signing up",
                              bg=main_window.cget("bg"),
                              font=(button_font, 16)).pack())

    main_window.mainloop()