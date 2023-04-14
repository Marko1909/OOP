def ispis_kolegija(kolegij):
    print(f'\tKolegij {kolegij["Ime"]} nosi {kolegij["ECTS"]} ECTS bodova')


def get_kolegij(redni_broj, kolegij):
    return f'\t{redni_broj}. {kolegij["Ime"]}'


def ispis_svih_kolegija(kolegiji):
    print("Popis svih kolegija: ")
    for kolegij in kolegiji:
        ispis_kolegija(kolegij)