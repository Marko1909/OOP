from ispiti import ispis_ispita
def ispis_studenta(student):
    print(f'Student {student["Ime"]} {student["Prezime"]} je prijavio: ')
    ispis_ispita(student["Ispit"])