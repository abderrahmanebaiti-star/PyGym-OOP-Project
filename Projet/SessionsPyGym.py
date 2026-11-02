from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter.messagebox import showinfo, showerror
from DatabasePyGym import allowed_activities, add_session, get_sessions

dark_blue = "#3776AB"
blue = "#4B8BBE"
yellow = "#FFD43B"
label_font = "Georgia"

def sessions_page(window, username, back=None):
    window.title("PyGym - Sessions")
    background = window.cget("bg")
    frame = Frame(window, bg=background)
    frame.pack(fill=BOTH, expand=True)


    Label(frame, text="My sessions", font=(label_font, 22), bg=background, fg=yellow).pack(pady=(20, 5))
    Label(frame, text="Member : " + username, bg=background, fg="white").pack()


    top = Frame(frame, bg=background)
    top.pack(pady=15)
    Label(top, text="Activity :", bg=background, fg=yellow).pack(side=LEFT, padx=5)
    allowed = allowed_activities(username)
    activity = Combobox(top, values=allowed, state="readonly", width=15)
    activity.pack(side=LEFT, padx=5)
    if allowed:
        activity.current(0)


    table = Treeview(frame, columns=("date", "activity"), show="headings", height=8)
    table.heading("date", text="Date and time")
    table.heading("activity", text="Activity")

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

    Button(top, text="Book a session", command=book, bg=dark_blue, fg=yellow).pack(side=LEFT, padx=10)
    table.pack(pady=10)
    fill_table()

    if back is not None:
        Button(frame, text="Back", command=go_back, bg=yellow, fg=dark_blue, width=12).pack(pady=10)


if __name__ == '__main__':
    from MainPyGym import main_window
    # E.g.: Swimming
    sessions_page(main_window, "test")
    main_window.mainloop()