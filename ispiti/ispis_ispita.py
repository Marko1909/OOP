def ispis_ispita(ispit):
    print(f'\tIspit iz kolegija {ispit["Kolegij"]["Ime"]}, koji nosi {ispit["Kolegij"]["ECTS"]} ECTS bodova održati će se {ispit["Datum"]}')


def get_ispit(redni_broj, ispit):
    return f'{redni_broj}. Ispit iz kolegija {ispit["Kolegij"]["Ime"]}'