def ispis_ispita(ispit):
    print(f'\tIspit iz kolegija {ispit["Kolegij"]["Ime"]}, koji nosi {ispit["Kolegij"]["ECTS"]} ECTS bodova održati će se {ispit["Datum"]}')


def get_ispit(redni_broj, ispit):
    return f'\t{redni_broj}. Ispit iz kolegija {ispit["Kolegij"]["Ime"]}'


def ispis_svih_ispita(ispiti):
    print("Popis svih ispita: ")
    for ispit in ispiti:
        ispis_ispita(ispit)