from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike
import re

korisnici=ucitaj_korisnike()
n =len(korisnici)

def prijava():
    korisncko_ime = input("korisnicko ime: ")
    lozinka = input("loznika: ")
    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisncko_ime and korisnik['lozinka'] == lozinka:
            return korisnik
    return False

def unos_sa_proverom(poruka, naziv_unosa="Unos"):
    while True:
        unos = input(poruka)
        if unos != '':
            greska = re.search(' ', unos)
            if greska == None:
                return unos
            else:
                print(f"{naziv_unosa} ne sme da sadrzi razmake!")
        else:
            print(f"{naziv_unosa} ne sme biti prazan!")

def registracija(): #ispis tek registrovanog korisnika
    korisnici = ucitaj_korisnike()
    while True:
        korisnicko_ime = unos_sa_proverom("\nKorisnicko ime(upisite 'nazad' kako bi ste napustili registraciju): ",
                                          "Korisnicko ime")
        if korisnicko_ime == 'nazad':
            return
        postojece_korisnicko_ime = False
        for korisnik in korisnici:
            if korisnik['korisnicko_ime'] == korisnicko_ime:
                postojece_korisnicko_ime = True
                print("Korisnicko ime je vec zauzeto. Pokusajte drugo!")
                break

        if postojece_korisnicko_ime == False:
            break

    lozinka = unos_sa_proverom("Lozinka: ", "Lozinka")
    ime = input("Ime:")
    prezime = input("Prezime:")

    while True:
        tip_korisnika = input("Pristup menadzera ili prodavca(m/p):")
        if tip_korisnika == 'm' or tip_korisnika == 'p':
            break
        else:
            print("Pogresan tip korisnika! Pokusajte ponovo!")

    novi_korsinik = {}
    novi_korsinik['korisnicko_ime'] = korisnicko_ime
    novi_korsinik['lozinka'] = lozinka
    novi_korsinik['ime'] = ime
    novi_korsinik['prezime'] = prezime

    if tip_korisnika == 'm':
        novi_korsinik['tip_korisnika'] = 'Menadzer'
    else:
        novi_korsinik['tip_korisnika'] = 'Prodavac'
    print("\n Korisnik se dodaje:")
    korisnici.append(novi_korsinik)
    sacuvaj_korisnike(korisnici)
    print("%s je REGISTROVAN dodat u korisnike bazu podatka.Tip korisnika=[%s]" % (novi_korsinik['korisnicko_ime'], novi_korsinik['tip_korisnika']))

duzina=[1,1,1,1,1]
kljuc=['korisnicko_ime','lozinka','ime','prezime','tip_korisnika']

def duzina_liste():
        max = '1'
        for i in range(5):
            max = len(str(korisnici[0][kljuc[i]]))
            for j in range(1):
                if max < len(str(korisnici[j + 1][kljuc[i]])):
                    max < len(str(korisnici[j + 1][kljuc[i]]))
                duzina[i] = max


def sortiraj_korisnika (kljuc):
        korisnik = ucitaj_korisnike()

        for i in range(len(korisnik)):
            for j in range(len(korisnik)):
                if korisnik[i][kljuc] < korisnik[j][kljuc]:
                    temp = korisnik[i]
                    korisnik[i] = korisnik[j]
                    korisnik[j] = temp

        return korisnik

def sortiranje_korisnika():
    print('***' * 20)
    print("1. Prikazi korisnike po imenu")
    print("2. Prikazi korisnike po prezimenu")
    print("3. Prikazi korisnike po tipu korisnika")
    print("0. Izlaz")
    print('***' * 20)
    stavka = input("Izaberite stavku: ")
    print('***' * 20)
    korisnici = ucitaj_korisnike()
    if stavka == '1':
        korisnici = sortiraj_korisnika("ime")

    elif stavka == '2':
        korisnici = sortiraj_korisnika("prezime")

    elif stavka == '3':
        korisnici = sortiraj_korisnika("tip_korisnika")

    elif stavka == '0':
        return
    else:
        print("Pogresan unos!")
        return
    ispis_korisnika(korisnici)

def ispis_korisnika(korisnici):
    zaglavlje = f"{'ime':<20}" \
                f"{'prezime':<20}" \
                f"{'korisnicko ime':<20}" \
                f"{'tip korisnika':<20}"

    print(zaglavlje)
    print("-" * len(zaglavlje))

    for korisnik in korisnici:
        za_ispis = f"{korisnik['ime']:<20}" \
                   f"{korisnik['prezime']:<20}" \
                   f"{korisnik['korisnicko_ime']:<20}" \
                   f"{korisnik['tip_korisnika']:<20}"
        print(za_ispis)