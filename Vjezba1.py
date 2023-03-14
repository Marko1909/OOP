#Ova linija mora biti komentar!
print('Dobrodošli', '!'*3)

# Napisati sljedeće izraze u jednoj liniji koda
ime = input("Unesite vaše ime: ")

print('Unesite vaše prezime: ', end="")
prezime = input()

print('Unesite vaš JMBAG: ', end="")
def jmbag():
   JMBAG = input()
   return JMBAG

JMBAG = jmbag()

# TODO zatražite od korisnika broj godina
godine = input("Unesite vaš broj godina: ")

# TODO ime i prezime ispišite u navodnim znakovima
print(f'Korisnik : ', '"',ime,'"', '"',prezime,'"', godine, end='!')