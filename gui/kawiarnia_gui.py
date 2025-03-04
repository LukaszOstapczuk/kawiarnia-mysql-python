import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttkb  # Ulepszony wygląd GUI

# 📌 Połączenie z bazą MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="BazaTest123", 
    database="kawiarnia_db"
)
cursor = conn.cursor()

# 📌 Walidacje danych
def get_valid_number(prompt, entry):
    """ Sprawdza, czy wpisana wartość jest liczbą większą od 0. """
    value = entry.get().strip()
    if value.isdigit() and int(value) > 0:
        return int(value)
    messagebox.showwarning("Błąd", f"❌ {prompt} musi być liczbą większą od 0!")
    return None

def get_non_empty_string(prompt, entry):
    """ Sprawdza, czy wpisana wartość nie jest pusta. """
    value = entry.get().strip()
    if value:
        return value
    messagebox.showwarning("Błąd", f"❌ {prompt} nie może być puste!")
    return None

# 📌 Główne okno aplikacji
root = ttkb.Window(themename="superhero")
root.title("Zarządzanie Kawiarnią")
root.geometry("600x700")

# 📌 Funkcje obsługi klientów
def pokaz_klientow():
    """ Wyświetla listę klientów """
    cursor.execute("SELECT id, imie, email FROM klienci")
    wyniki = cursor.fetchall()

    top = tk.Toplevel(root)
    top.title("Lista klientów")
    top.geometry("400x300")

    tree = ttk.Treeview(top, columns=("ID", "Imię", "Email"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Imię", text="Imię")
    tree.heading("Email", text="Email")

    for row in wyniki:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both")

def dodaj_klienta():
    """ Dodaje nowego klienta """
    def zapis_klienta():
        imie = get_non_empty_string("Imię", entry_imie)
        email = get_non_empty_string("Email", entry_email)
        if imie and email:
            cursor.execute("INSERT INTO klienci (imie, email) VALUES (%s, %s)", (imie, email))
            conn.commit()
            messagebox.showinfo("Sukces", "✅ Dodano nowego klienta!")
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Dodaj Klienta")
    top.geometry("300x200")

    ttk.Label(top, text="Imię:").pack()
    entry_imie = ttk.Entry(top)
    entry_imie.pack()

    ttk.Label(top, text="Email:").pack()
    entry_email = ttk.Entry(top)
    entry_email.pack()

    ttk.Button(top, text="Zapisz", command=zapis_klienta).pack()

def edytuj_klienta():
    """ Edycja danych klienta """
    def aktualizuj_klienta():
        klient_id = get_valid_number("ID Klienta", entry_id)
        nowe_imie = get_non_empty_string("Nowe imię", entry_imie)
        nowy_email = get_non_empty_string("Nowy email", entry_email)

        if klient_id and nowe_imie and nowy_email:
            cursor.execute("UPDATE klienci SET imie = %s, email = %s WHERE id = %s", (nowe_imie, nowy_email, klient_id))
            conn.commit()
            messagebox.showinfo("Sukces", f"✅ Zmieniono dane klienta {klient_id}!")
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Edytuj Klienta")
    top.geometry("300x200")

    ttk.Label(top, text="ID klienta:").pack()
    entry_id = ttk.Entry(top)
    entry_id.pack()

    ttk.Label(top, text="Nowe imię:").pack()
    entry_imie = ttk.Entry(top)
    entry_imie.pack()

    ttk.Label(top, text="Nowy email:").pack()
    entry_email = ttk.Entry(top)
    entry_email.pack()

    ttk.Button(top, text="Zapisz", command=aktualizuj_klienta).pack()

def usun_klienta():
    """ Usuwa klienta """
    def kasuj_klienta():
        klient_id = get_valid_number("ID Klienta", entry_id)
        if klient_id:
            cursor.execute("DELETE FROM klienci WHERE id = %s", (klient_id,))
            conn.commit()
            messagebox.showinfo("Sukces", f"✅ Usunięto klienta {klient_id}!")
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Usuń Klienta")
    top.geometry("250x150")

    ttk.Label(top, text="ID klienta:").pack()
    entry_id = ttk.Entry(top)
    entry_id.pack()

    ttk.Button(top, text="Usuń", command=kasuj_klienta).pack()

# 📌 Funkcje obsługi zamówień
def pokaz_zamowienia():
    """ Wyświetla listę zamówień """
    cursor.execute("SELECT zamowienia.id, klienci.imie, zamowienia.status, zamowienia.laczna_kwota FROM zamowienia JOIN klienci ON zamowienia.klient_id = klienci.id")
    wyniki = cursor.fetchall()

    top = tk.Toplevel(root)
    top.title("Lista zamówień")
    top.geometry("850x300")

    tree = ttk.Treeview(top, columns=("ID", "Klient", "Status", "Kwota"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Klient", text="Klient")
    tree.heading("Status", text="Status")
    tree.heading("Kwota", text="Kwota")

    for row in wyniki:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both")

def dodaj_zamowienie():
    """ Dodaje nowe zamówienie """
    def zapis_zamowienia():
        klient_id = get_valid_number("ID Klienta", entry_klient_id)
        kwota = get_valid_number("Kwota", entry_kwota)
        if klient_id and kwota:
            cursor.execute("INSERT INTO zamowienia (klient_id, laczna_kwota, status) VALUES (%s, %s, 'Nowe')", (klient_id, kwota))
            conn.commit()
            messagebox.showinfo("Sukces", "✅ Dodano nowe zamówienie!")
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Dodaj Zamówienie")
    top.geometry("300x200")

    ttk.Label(top, text="ID Klienta:").pack()
    entry_klient_id = ttk.Entry(top)
    entry_klient_id.pack()

    ttk.Label(top, text="Kwota:").pack()
    entry_kwota = ttk.Entry(top)
    entry_kwota.pack()

    ttk.Button(top, text="Zapisz", command=zapis_zamowienia).pack()


def edytuj_zamowienie():
    """ Edycja kwoty zamówienia """
    def aktualizuj_zamowienie():
        zamowienie_id = get_valid_number("ID Zamówienia", entry_id)
        nowa_kwota = get_valid_number("Nowa kwota", entry_kwota)
        if zamowienie_id and nowa_kwota:
            cursor.execute("UPDATE zamowienia SET laczna_kwota = %s WHERE id = %s", (nowa_kwota, zamowienie_id))
            conn.commit()
            messagebox.showinfo("Sukces", "✅ Zmieniono kwotę zamówienia!")
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Edytuj Zamówienie")
    top.geometry("300x200")

    ttk.Label(top, text="ID Zamówienia:").pack()
    entry_id = ttk.Entry(top)
    entry_id.pack()

    ttk.Label(top, text="Nowa kwota:").pack()
    entry_kwota = ttk.Entry(top)
    entry_kwota.pack()

    ttk.Button(top, text="Zapisz", command=aktualizuj_zamowienie).pack()

def usun_zamowienie():
    """ Usuwa zamówienie """
    def kasuj_zamowienie():
        zamowienie_id = get_valid_number("ID Zamówienia", entry_id)
        if zamowienie_id:
            cursor.execute("DELETE FROM zamowienia WHERE id = %s", (zamowienie_id,))
            conn.commit()
            messagebox.showinfo("Sukces", f"✅ Usunięto zamówienie {zamowienie_id}!")
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Usuń Zamówienie")
    top.geometry("250x150")

    ttk.Label(top, text="ID Zamówienia:").pack()
    entry_id = ttk.Entry(top)
    entry_id.pack()

    ttk.Button(top, text="Usuń", command=kasuj_zamowienie).pack()

    # 📌 Funkcje obsługi zamówień
def zmien_status_zamowienia():
    def aktualizuj_status():
        zamowienie_id = get_valid_number("ID Zamówienia", entry_id)
        nowy_status = get_non_empty_string("Nowy status", entry_status)
        if zamowienie_id and nowy_status:
            cursor.execute("UPDATE zamowienia SET status = %s WHERE id = %s", (nowy_status, zamowienie_id))
            conn.commit()
            messagebox.showinfo("Sukces", "✅ Zmieniono status zamówienia!")
            top.destroy()

    top = tk.Toplevel(root)
    top.title("Zmień Status Zamówienia")
    top.geometry("300x200")

    ttk.Label(top, text="ID Zamówienia:").pack()
    entry_id = ttk.Entry(top)
    entry_id.pack()

    ttk.Label(top, text="Nowy status:").pack()
    entry_status = ttk.Entry(top)
    entry_status.pack()

    ttk.Button(top, text="Zapisz", command=aktualizuj_status).pack()

# 📌 PRZYCISKI MENU GŁÓWNEGO
buttons = [
    ("📋 Lista Klientów", pokaz_klientow),
    ("🛒 Lista Zamówień", pokaz_zamowienia),
    ("➕ Dodaj Klienta", dodaj_klienta),
    ("✏️ Edytuj Klienta", edytuj_klienta),
    ("❌ Usuń Klienta", usun_klienta),
    ("➕ Dodaj Zamówienie", dodaj_zamowienie),
     ("✏️ Edytuj Zamówienie", edytuj_zamowienie),
     ("🔄 Zmień Status Zamówienia", zmien_status_zamowienia),
    ("❌ Usuń Zamówienie", usun_zamowienie),
]

for text, command in buttons:
    ttkb.Button(root, text=text, command=command).pack(pady=5)

ttkb.Button(root, text="❌ Zamknij", command=root.quit).pack(pady=10)

root.mainloop()

cursor.close()
conn.close()
