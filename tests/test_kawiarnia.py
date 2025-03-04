import mysql.connector
import pandas as pd

# 📌 Połączenie z bazą MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="BazaTest123", 
        database="kawiarnia_db"
    )
    cursor = conn.cursor()
    print("✅ Połączono z bazą danych")
except mysql.connector.Error as err:
    print(f"❌ Błąd połączenia z bazą: {err}")
    exit()

# 📌 Test 1: Dodawanie nowego klienta
try:
    test_klient = ("Testowy Klient", "testowy@example.com")
    cursor.execute("INSERT INTO klienci (imie, email) VALUES (%s, %s)", test_klient)
    conn.commit()
    print("✅ Dodano nowego klienta")
except Exception as e:
    print(f"❌ Błąd podczas dodawania klienta: {e}")

# 📌 Test 2: Pobranie listy klientów
cursor.execute("SELECT * FROM klienci;")
klienci_wyniki = cursor.fetchall()
kolumny_klienci = [i[0] for i in cursor.description]
df_klienci = pd.DataFrame(klienci_wyniki, columns=kolumny_klienci)

# 📌 Test 3: Dodawanie zamówienia dla nowego klienta
cursor.execute("SELECT id FROM klienci WHERE email = %s", (test_klient[1],))
klient_id = cursor.fetchone()[0]

test_zamowienie = (klient_id, 50.00, "Nowe")
cursor.execute("INSERT INTO zamowienia (klient_id, laczna_kwota, status) VALUES (%s, %s, %s)", test_zamowienie)
conn.commit()

# 📌 Test 4: Pobranie listy zamówień
cursor.execute("SELECT * FROM zamowienia;")
zamowienia_wyniki = cursor.fetchall()
kolumny_zamowienia = [i[0] for i in cursor.description]
df_zamowienia = pd.DataFrame(zamowienia_wyniki, columns=kolumny_zamowienia)

# 📌 Test 5: Edycja kwoty zamówienia
cursor.execute("SELECT id FROM zamowienia WHERE klient_id = %s", (klient_id,))
zamowienie_id = cursor.fetchone()[0]

cursor.execute("UPDATE zamowienia SET laczna_kwota = %s WHERE id = %s", (75.00, zamowienie_id))
conn.commit()

# 📌 Test 6: Zmiana statusu zamówienia
cursor.execute("UPDATE zamowienia SET status = %s WHERE id = %s", ("Gotowe", zamowienie_id))
conn.commit()

# 📌 Test 7: Pobranie zamówienia po edycji
cursor.execute("SELECT * FROM zamowienia WHERE id = %s", (zamowienie_id,))
zamowienie_po_edycji = cursor.fetchall()
kolumny_zamowienie_edycja = [i[0] for i in cursor.description]
df_zamowienie_po_edycji = pd.DataFrame(zamowienie_po_edycji, columns=kolumny_zamowienie_edycja)

# 📌 Test 8: Usunięcie zamówienia
cursor.execute("DELETE FROM zamowienia WHERE id = %s", (zamowienie_id,))
conn.commit()

# 📌 Test 9: Usunięcie testowego klienta
cursor.execute("DELETE FROM klienci WHERE id = %s", (klient_id,))
conn.commit()

# Zamknięcie połączenia
cursor.close()
conn.close()
print("✅ Testy zakończone pomyślnie")

# 📌 Wyświetlenie wyników w terminalu
print("\n📋 Lista klientów (przed usunięciem):")
print(df_klienci)

print("\n🛒 Lista zamówień (przed edycją):")
print(df_zamowienia)

print("\n🛒 Lista zamówień (po edycji):")
print(df_zamowienie_po_edycji)
