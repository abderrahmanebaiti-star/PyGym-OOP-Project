from         tkinter import *
import customtkinter as ctk
import ThemePyGym    as theme

def start(window, log_in, sign_up):
    theme.home_screen(lambda: start(window, log_in, sign_up))
    StartUpFrame = Frame(window)
    StartUpFrame.place(relx=.5, rely=.55, anchor=CENTER)
    StartUpFrame.configure(bg=window.cget("bg"))

    Label(StartUpFrame, image=theme.logo, bg=window.cget("bg")).pack()
    project_title = ctk.CTkLabel(StartUpFrame, text="PYGYM", font=theme.TITLE_BIG, text_color=theme.yellow)
    project_title.pack(pady=(4, 6))
    ctk.CTkLabel(StartUpFrame, text="Your gym: machines, pool and online session\nbooking.",
                 font=theme.TEXT, text_color=theme.muted).pack(pady=(0, 30))
    def call_log_in():
        StartUpFrame.destroy()
        log_in(window)
    def call_sign_up():
        StartUpFrame.destroy()
        sign_up(window)

    log_in_button = ctk.CTkButton(StartUpFrame, text="Log in", command=call_log_in,
                                  width=360, height=48, font=theme.BOLD,  **theme.PRIMARY)
    log_in_button.pack(pady=(0, 14))

    sign_up_button = ctk.CTkButton(StartUpFrame, text="Sign up", command=call_sign_up,
                                   width=360, height=48, font=theme.BOLD, **theme.OUTLINE)
    sign_up_button.pack()

    links = Frame(StartUpFrame, bg=window.cget("bg"))
    links.pack(pady=(28, 24))
    for name in ("Plans", "Sessions"):   # liens : il faut un compte, ils ouvrent donc Log in
        link = ctk.CTkLabel(links, text=name, font=(theme.SMALL[0], 13, "bold", "underline"), text_color=theme.text, cursor="hand2")
        link.pack(side=LEFT, padx=12)
        link.bind("<Button-1>", lambda event: call_log_in())
    ctk.CTkLabel(StartUpFrame, text="ouvert : chaque jour de 10:00 -> 23:00", font=theme.SMALL, text_color=theme.muted).pack()

if __name__ == '__main__':
    from MainPyGym import main_window
    start(main_window,
          lambda w : Label(w, text="Logging in", bg=main_window.cget("bg"), font=theme.TEXT).pack(),
          lambda w : Label(w, text="Signing up", bg=main_window.cget("bg"), font=theme.TEXT).pack())

    main_window.mainloop()
