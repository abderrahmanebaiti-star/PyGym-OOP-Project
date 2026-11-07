from         tkinter            import *
from         tkinter.messagebox import askyesno
import customtkinter            as ctk
from   DatabasePyGym import get_subscription, add_subscription, close
import    ThemePyGym as theme

all_offers = {
    "Basic"   : (9.99, "$", "machines"),
    "Standard": (14.99, "$", "machines + pool"),
    "Premium" : (19.99, "$", "all options"),
}


class Subscription:
    def __init__(self, window, ID_member, for_next):
        self.window = window
        self.for_next = for_next
        window.title("Gym - Subscription")
        self.bg = window.cget("bg")
        self.ID = ID_member

        self.frame_sub = Frame(window, bg=self.bg)
        self.frame_sub.place(anchor=CENTER, relx=.5, rely=.55)
        ctk.CTkLabel(self.frame_sub,                     text="SUBSCRIPTION", font=theme.TITLE, text_color=theme.yellow).pack(anchor="w")
        self.label_result = ctk.CTkLabel(self.frame_sub, text=""            , font=theme.TEXT , text_color=theme.muted)
        self.label_result.pack(anchor="w", pady=(0, 10))

        self.frame_offers = Frame(self.frame_sub, bg=self.bg)
        self.frame_offers.pack()

        self.verify(ID_member)
        theme.nav_bar(window, lambda: Subscription(window, ID_member, for_next))

    def finish(self):
        self.frame_sub.destroy()
        self.for_next(self.ID)

    def buy_offer(self, offer):
        confirmed = askyesno("Confirmation", f"Are you sure you want to buy {offer}?")
        if confirmed:
            add_subscription(self.ID, offer)
        self.finish()

    def show_offers(self, sub_level=None):
        current_price = all_offers[sub_level][0] if sub_level in all_offers else 0
        for name, (price, currency, description) in all_offers.items():
            active = current_price == price
            row = ctk.CTkFrame(self.frame_offers, width=460, height=78, **(theme.ACTIVE_CARD if active else theme.CARD))
            row.pack(pady=7)
            head = ctk.CTkFrame(row, fg_color="transparent")       # nom + badge ACTIVE
            head.place(x=22, y=12)
            ctk.CTkLabel(head, text=name                    , font=theme.BOLD , text_color=theme.text).pack(side=LEFT)
            ctk.CTkLabel(row , text=description.capitalize(), font=theme.SMALL, text_color=theme.muted).place(x=22, y=42)
            if current_price < price:
                choice = ctk.CTkButton(row, text=f"Switch · {price} {currency}",
                                       command=lambda offer=name: self.buy_offer(offer), font=theme.BOLD,
                                       width=150, height=44, **theme.DARK)
            elif active:
                ctk.CTkLabel(head, text="ACTIVE", font=(theme.SMALL[0], 11, "bold"), fg_color=theme.yellow,
                             text_color=theme.bg, corner_radius=8, height=22, width=60).pack(side=LEFT, padx=10)
                choice = ctk.CTkLabel(row, text=f"{price} {currency}", font=theme.PRICE, text_color=theme.yellow)
            else:
                choice = ctk.CTkLabel(row, text="")
            choice.place(relx=1, x=-18, rely=.5, anchor=E)
        ctk.CTkButton(self.frame_offers, text="Cancel subscription", command=self.finish, font=theme.BOLD,
                      width=460, height=46, **theme.DANGER).pack(pady=(10, 0))

    def verify(self, ID_member):
        status = get_subscription(ID_member)

        if status is None:
            self.label_result.configure(text="You have no subscription yet.")
            self.show_offers()
        else:
            self.label_result.configure(text=f"Your current plan: {status}")
            self.show_offers(status)

if __name__ == '__main__':
    try:
        from MainPyGym import main_window
        # E.g: Standard
        Subscription(main_window, "test",
                     lambda u: Label(main_window, text=f"Sessions de {u}",
                                     bg=main_window.cget("bg"),
                                     font=theme.TEXT).pack())
        main_window.mainloop()
    finally:
        close()
