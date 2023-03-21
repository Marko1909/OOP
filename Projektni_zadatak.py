from datetime import date

korisnik = {}

korisnik["Ime"] = input("Unesite ime korisnika: ").capitalize()
korisnik["Prezime"] = input("Unesite prezime korisnika: ").capitalize()
korisnik["Telefon"] = int(input("Unesite telefon korisnika: "))
korisnik["Email"] = input("Unesite email korisnika: ").strip()

artikl = {}

artikl["Naslov"] = input("Unesite naslov artikla: ")
artikl["Opis"] = input("Unesite opis artikla: ")
artikl["Cijena"] = float(input("Unesite cijenu artikla: "))

prodaja = {}

dan = int(input("Unesite dan isteka prodaje: "))
mjesec = int(input("Unesite mjesec isteka prodaje: "))
godina = int(input("Unesite godinu isteka prodaje: "))

prodaja["Datum"] = date(godina, mjesec, dan)
prodaja["Artikl"] = artikl
prodaja["Korisnik"] = korisnik

print('Informacije o artiklu: ')
print(f'\t\t Naslov: {prodaja["Artikl"]["Naslov"]}')
print(f'\t\t Opis: {prodaja["Artikl"]["Opis"]}')
print(f'\t\t Cijena: {prodaja["Artikl"]["Cijena"]}')

print('Datum isteka prodaje: ')
print(f'\t\t Dan: {prodaja["Datum"].day}')
print(f'\t\t Mjesec: {prodaja["Datum"].month}')
print(f'\t\t Godina: {prodaja["Datum"].year}')

print('Informacije o korisniku: ')
print(f'\t\t Puno ime: {prodaja["Korisnik"]["Ime"]} {prodaja["Korisnik"]["Prezime"]}')
print(f'\t\t Telefon: {prodaja["Korisnik"]["Telefon"]}')
print(f'\t\t Email: {prodaja["Korisnik"]["Email"]}')
