import customtkinter as ctk
from tkinter import Canvas, PhotoImage, font
from tkinter.ttk import Style

bg, card, border, field = "#000000", "#181A1F", "#2A2D33", "#0E1013"   # noirs du design
yellow, yellow_hover, text, muted, red = "#F4C430", "#FFD95A", "#EDEDED", "#9AA0A6", "#E8735A"   # accents

# Styles reutilises par tous les ecrans (on les "deplie" avec ** dans les widgets)
CARD = dict(fg_color=card, border_color=border, border_width=1, corner_radius=16)
ACTIVE_CARD = dict(fg_color="#1D1A10", border_color=yellow, border_width=1, corner_radius=16)
PRIMARY = dict(fg_color=yellow, hover_color=yellow_hover, text_color=bg, corner_radius=12)
OUTLINE = dict(fg_color="transparent", hover_color=card, text_color=yellow, border_color=yellow, border_width=1, corner_radius=12)
DARK = dict(fg_color="#24272D", hover_color="#30343B", text_color=text, border_color=border, border_width=1, corner_radius=10)
DANGER = dict(fg_color="transparent", hover_color="#2A1A17", text_color=red, border_color=red, border_width=1, corner_radius=12)
ENTRY = dict(fg_color=field, border_color=border, text_color=text, corner_radius=10, width=290, height=44)

background = glow = logo = nav = None   # gardes dans des variables, sinon Tkinter les efface
history = []                            # les ecrans visites (fonctions qui les rouvrent)
TITLE_BIG = TITLE = PRICE = BOLD = TEXT = SMALL = None

def set_background(window):
    global background, glow, logo, TITLE_BIG, TITLE, PRICE, BOLD, TEXT, SMALL
    ctk.set_appearance_mode("dark")
    window.resizable(False, False)
    title_font = "Bebas Neue" if "Bebas Neue" in font.families() else "Impact"   # police du design, sinon Windows
    body_font = "Inter" if "Inter" in font.families() else "Segoe UI"
    TITLE_BIG, TITLE, PRICE = (title_font, 76, "bold"), (title_font, 46, "bold"), (title_font, 32, "bold")
    BOLD, TEXT, SMALL = (body_font, 16, "bold"), (body_font, 15), (body_font, 13)
    background = Canvas(window, bg=bg, highlightthickness=0)
    background.place(x=0, y=0, relwidth=1, relheight=1)     # toute la fenetre
    logo = PhotoImage(file="logo.png")                       # haltere de l'accueil
    style = Style()                                          # tableau + liste des activites
    style.theme_use("clam")
    style.configure("Treeview", background=field, fieldbackground=field, foreground=text, font=(body_font, 11), rowheight=32)
    style.configure("Treeview.Heading", background=card, foreground=yellow, font=(body_font, 11, "bold"), relief="flat")
    style.configure("TCombobox", arrowcolor=yellow, background=card, bordercolor=border, padding=6)
    style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])   # tableau sans bordure blanche
    style.map("TCombobox", fieldbackground=[("readonly", field)], foreground=[("readonly", text)])
    window.option_add("*TCombobox*Listbox.background", field)    # liste qui s'ouvre
    window.option_add("*TCombobox*Listbox.foreground", text)

def clear(window):  # detruit tous les widgets sauf le fond
    for widget in window.winfo_children():
        if widget != background:
            widget.destroy()

def home_screen(screen):  # appele par l'accueil : l'historique repart a zero
    history[:] = [screen]
    if nav is not None:
        nav.destroy()

def nav_bar(window, screen):  # memorise l'ecran actuel + boutons Back et Home
    global nav
    history.append(screen)
    if nav is not None:
        nav.destroy()
    nav = ctk.CTkFrame(window, fg_color=bg)
    nav.place(x=16, y=16)
    ctk.CTkButton(nav, text="← Back", command=lambda: go_back(window), width=84, height=40, font=BOLD, **DARK).pack(side="left")
    ctk.CTkButton(nav, text="Home", command=lambda: go_home(window), width=74, height=40, font=BOLD, **PRIMARY).pack(side="left", padx=10)

def go_back(window):
    if len(history) >= 2:
        history.pop()               # on retire l'ecran actuel
        previous = history.pop()    # on recupere l'ecran precedent
        clear(window)
        previous()                  # on le rouvre (il se re-memorise)

def go_home(window):
    clear(window)
    history[0]()                    # le premier ecran = l'accueil
