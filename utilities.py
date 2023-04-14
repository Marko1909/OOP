def unos_intervala(min,max):

    while True:
        try:
            broj = int(input(f"Unesite cijeli broj: "))

            if broj < min or broj > max:
                raise Exception(f"Broj nije u intervalu od {min} do {max}")

        except ValueError:
            print('Morate upisati broj!')

        except Exception as e:
            print(e)

        else:
            return broj
