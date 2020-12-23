from knjige.knjigeIO import ucitaj_knjige



knjige = ucitaj_knjige()
i = 0
z = len(knjige)

duzina = [1, 1, 1, 1, 1, 1, 1, 1, 1]
kljuc = ['sifra', 'naslov', 'isbn', 'autor', 'izdavac', 'broj strana', 'godina', 'cena', 'kategorija']


def duzina_liste2():
    max = '1'
    for i in range(9):
        max = len(str(knjige[0][kljuc[i]]))
        for j in range(z - 1):
            if (max < len(str(knjige[i + 1][kljuc[i]]))):
                max = len(str(knjige[j + 1][kljuc[i]]))
        duzina[i] = max


def pretraga_knjiga_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretraga_knjiga_jednakost(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost == knjiga[kljuc]:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige():
    print('***' * 20)
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po kategoriji")
    print("4. Pretraga po autoru")
    print("5. Pretraga po izdavacu")
    print("6. Pretraga po ceni")
    print("0. Napusti pretragu")
    print('***' * 20)
    stavka = int(input("Izaberite stavku: "))
    print('***' * 20)
    knjige = []
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        knjige = pretraga_knjiga_jednakost("sifra", sifra)
    elif stavka == 2:
        naslov = input("Unesite nalsov: ")
        knjige = pretraga_knjiga_string("naslov", naslov)
    elif stavka == 3:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretraga_knjiga_string("kategorija", kategorija)
    elif stavka == 4:
        autor = input("Unesite autora: ")
        knjige = pretraga_knjiga_string("autor", autor)
    elif stavka == 5:
        izdavac = input("Unesite izdavaca: ")
        knjige = pretraga_knjiga_string("izdavac", izdavac)
    elif stavka == 6:
        cena = input("Unesite cenu: ")
        knjige = pretraga_knjiga_jednakost("autor", cena)
    elif stavka == 0:
        return
    else:
        print("Pogresan unos")

    ispisi_knjige(knjige)



def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp

    return knjige


def sortirane_knjige():
    print('***' * 20)
    print("\n1. Sortiraj po sifri")
    print("2. Sortiraj po naslovi")
    print("3. Sortiraj po kategoriji")
    print("4. Sortiraj po autoru")
    print("5. Sortiraj po izdavacu")
    print("6. Sortiraj po ceni")
    print("0. Izlaz")
    print('***' * 20)
    stavka = int(input("Izaberite stavku: "))
    print('***' * 20)
    knjige = ucitaj_knjige()
    if stavka == 1:
        knjige = sortiraj_knjige("sifra")

    elif stavka == 2:
        knjige = sortiraj_knjige("naslov")

    elif stavka == 3:
        knjige = sortiraj_knjige("kategorija")

    elif stavka == 4:
        knjige = sortiraj_knjige("autor")

    elif stavka == 5:
        knjige = sortiraj_knjige("izdavac")

    elif stavka == 6:
        knjige = sortiraj_knjige("cena")

    elif stavka == 0:
        return
    else:
        print("Pogresan unos!")
    ispisi_knjige(knjige)

def ispisi_knjige(knjige):
        zaglavlje = f"{'sifra':<10}" \
                    f"{'naslov':<20}" \
                    f"{'autor':<20}" \
                    f"{'isbn':^15}" \
                    f"{'izdavac':^15}" \
                    f"{'godina izdanja':^15}" \
                    f"{'broj strana':^15}" \
                    f"{'cena':^20}" \
                    f"{'kategorija':^10}"

        print(zaglavlje)
        print("-" * len(zaglavlje))

        for knjiga in knjige:
            za_ispis = f"{knjiga['sifra']:<10}" \
                       f"{knjiga['naslov']:<20}" \
                       f"{knjiga['autor']:<20}" \
                       f"{knjiga['isbn']:^15}" \
                       f"{knjiga['izdavac']:^15}" \
                       f"{knjiga['godina']:^15}" \
                       f"{knjiga['broj strana']:^15}" \
                       f"{knjiga['cena']:^20}" \
                       f"{knjiga['kategorija']:^10}"
            print(za_ispis)
