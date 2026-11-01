from tkinter import *
from DatabasePyGym import get_subscription, set_subscription, close
from tkinter.messagebox import askyesno

dark_blue = "#306998"
blue = "#4B8BBE"
yellow = "#FFD43B"

all_offers = {
    "Basic": (9.99, "$", "machines"),
    "Standard": (14.99, "$", "machines + pool"),
    "Premium": (19.99, "$", "all options"),
}


class Subscription:
    def __init__(self, window, ID_member, on_done):
        self.window = window
        self.on_done = on_done
        window.title("Gym - Subscription")
        self.bg = window.cget("bg")
        self.ID = ID_member

        self.frame_sub = Frame(window, bg=self.bg)
        self.frame_sub.place(anchor=CENTER, relx=.5, rely=.5)
        self.label_result = Label(self.frame_sub, text="", font=("Georgia", 12, "bold"), bg=self.bg)
        self.label_result.pack(pady=5)

        self.frame_offers = Frame(self.frame_sub, bg=self.bg)
        self.frame_offers.pack(pady=10, padx=20, anchor="w")

        self.verify(ID_member)

    def finish(self):
        self.frame_sub.destroy()
        if self.on_done:
            self.on_done(self.ID)

    def buy_offer(self, offer):
        if not askyesno("Confirmation", f"Are you sure you want to buy {offer}?"):
            return
        set_subscription(self.ID, offer)
        self.finish()

    def show_offers(self, sub_level=None):
        current_price = all_offers[sub_level][0] if sub_level in all_offers else 0
        Label(self.frame_offers, text="Our subscription offers :",
              font=("Georgia", 12, "bold"), fg="red", bg=self.bg).grid(row=0, column=0)

        offer_row = 1
        for name, (price, currency, description) in all_offers.items():
            offer_row +=1
            offer_label = Label(self.frame_offers,text=f"• {name} ({description}): ",
                                font=("Georgia", 11), bg=self.bg, fg="white")
            offer_label.grid(row=offer_row, column=0, sticky=W)
            if current_price < price:
                choice = Button(self.frame_offers, text=f"{price} {currency}",
                                command=lambda offer=name: self.buy_offer(offer),
                                font=("Georgia", 12), bg=dark_blue, fg=yellow)
            elif current_price == price:
                choice = Label(self.frame_offers, text="Active",
                               font=("Georgia", 12), bg=self.bg, fg="green")
            else:
                choice = Label(self.frame_offers, text="", bg=self.bg)
            choice.grid(row=offer_row, column=1, sticky=EW)
        Button(self.frame_offers, text="Cancel",
               font=("Georgia", 9), command=self.finish,
               bg=blue, fg="black").grid(row=offer_row+1, column=2, sticky=W)

    def verify(self, ID_member):
        status = get_subscription(ID_member)

        if status is None:
            self.label_result.config(text="No subscription.", fg="red")
            self.show_offers()
        else:
            self.label_result.config(text=f"Subscription: {status}.", fg="green")
            self.show_offers(status)

if __name__ == '__main__':
    try:
        window = Tk()
        window.title("PyGym")
        window.geometry("360x320")
        window.configure(bg="black")

        Subscription(window, "admin", None)
        window.mainloop()
    finally:
        close()
