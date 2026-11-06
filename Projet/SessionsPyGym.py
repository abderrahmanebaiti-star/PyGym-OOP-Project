from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter.messagebox import showinfo, showerror
from DatabasePyGym import allowed_activities, add_session, get_sessions
import customtkinter as ctk
import ThemePyGym as theme

def sessions_page(window, username, back=None):
    window.title("PyGym - Sessions")
    background = window.cget("bg")
    frame = Frame(window, bg=background)
    frame.place(relx=.5, rely=.56, anchor=CENTER)
    ctk.CTkLabel(frame, text="MY SESSIONS", font=theme.TITLE, text_color=theme.yellow).pack(anchor="w")
    ctk.CTkLabel(frame, text="Member: " + username, font=theme.TEXT, text_color=theme.muted).pack(anchor="w")
    top = ctk.CTkFrame(frame, **theme.CARD)
    top.pack(pady=16, fill=X)
    ctk.CTkLabel(top, text="Activity", font=theme.BOLD, text_color=theme.text).pack(side=LEFT, padx=(20, 12), pady=16)
    allowed = allowed_activities(username)
    activity = Combobox(top, values=allowed, state="readonly", width=16, font=(theme.TEXT[0], 11))
    activity.pack(side=LEFT)
    if allowed:
        activity.current(0)

    table = Treeview(frame, columns=("date", "activity"), show="headings", height=7)
    table.heading("date", text="Date and time")
    table.heading("activity", text="Activity")
    table.column("date", width=250)

    def fill_table():
        table.delete(*table.get_children())
        for date_time, activity in get_sessions(username):
            table.insert("", END, values=(date_time, activity))

    def book():
        if add_session(username, activity.get()):
            showinfo("Session",
                     "Session booked!")
            fill_table()
        else:
            showerror("Refused",
                      "You need a higher subscription to book this session.")

    def go_back():
        frame.destroy()
        back(username)

    ctk.CTkButton(top, text="Book", command=book, font=theme.BOLD, width=100, height=40, **theme.PRIMARY).pack(side=RIGHT, padx=16)
    table.pack(fill=X)
    fill_table()

    if back is not None:
        ctk.CTkButton(frame, text="My subscription", command=go_back, font=theme.BOLD, height=46, **theme.OUTLINE).pack(fill=X, pady=(16, 0))
    theme.nav_bar(window, lambda: sessions_page(window, username, back))


if __name__ == '__main__':
    from MainPyGym import main_window
    # E.g.: Swimming
    sessions_page(main_window, "test")
    main_window.mainloop()
