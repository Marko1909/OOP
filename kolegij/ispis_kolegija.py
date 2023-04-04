def ispis_kolegija(kolegij):
    print(f'\tKolegij {kolegij["Ime"]} nosi {kolegij["ECTS"]} ECTS bodova')


def get_kolegij(redni_broj, kolegij):
    return f'\t{redni_broj}. {kolegij["Ime"]}'
