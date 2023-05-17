from datetime import date

kolegij = {
    "Ime kolegija": None,
    "ECTS bodovi": None,
}

predmet = input("Unesite ime kolegija ")

kolegij["Ime kolegija"] = predmet.upper()
kolegij["ECTS bodovi"] = input("Unesite ECTS bodove za kolegij: ")


dan = int(input("Unesite dan ispita: "))
mjesec = int(input("Unesite mjesec ispita: "))
godina = int(input("Unesite godinu ispita: "))

datum = date(godina, mjesec, dan)

ispit = {
    "Kolegij": kolegij["Ime kolegija"],
    "Datum": datum
}

student = {
    "Ispit": ispit,
    "Ime": None,
    "Prezime": None
}

ime = input("Unesite ime studenta: ")
prezime = input("Unesite prezime studenta: ")

student["Ime"] = ime.title()
student["Prezime"] = prezime.title()


print("Student", student["Ime"], student["Prezime"])
print("je prijavio ispit iz kolegija", student["Ispit"]["Kolegij"])
print("koji će se održati:", student["Ispit"]["Datum"])
