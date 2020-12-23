from korisnici.korisnici import prijava, registracija, ispis_korisnika
from knjige.knjige import sortirane_knjige, pretrazi_knjige, dodavanje_knjiga, brisanje_knjige
from akcije.akcije import pretrazi_akcije, ispisi_akcije, registracija_akcije


def meni_administrator():
    print()
    print('***'*20)
    while True:
        print("\n1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Lista korisnika")
        print("7. Dodaj knjigu")
        print("8. Izmeni knjigu")
        print("9. Obrisi knjigu")
        print("0. Kraj")
        print('***' * 20)
        stavka = int(input("Izaberite stavku: "))
        print('***' * 20)

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            ispisi_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            registracija()
        elif stavka == 6:
            ispis_korisnika(korisnici)
        elif stavka == 7:
            dodavanje_knjiga()
        elif stavka == 8:
            izmena_knjige()
        elif stavka == 9:
            brisanje_knjige()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def meni_menadzer():
    print('***' * 20)
    while True:
        print("\n 1. Sortiranje knjiga")
        print(" 2. Pretraga knjiga")
        print(" 3. Prikaz akcija")
        print(" 4. Registracija akcija")
        print(" 5. Registracija korisnika")
        print(" 6. Lista korisnika")
        print(" 7. Dodaj knjigu")
        print(" 8. Izmeni knjigu")
        print(" 9. Obrisi knjigu")
        print(" 0. Kraj")
        print('***' * 20)
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            ispisi_akcije()
        elif stavka == 4:
            registracija_akcije()
        elif stavka == 5:
            registracija()
        elif stavka == 6:
            ispis_korisnika(korisnici)
        elif stavka == 7:
            dodavanje_knjiga()
        elif stavka == 8:
            izmena_knjige()
        elif stavka == 9:
            print("Nemate dozvolu za ovu komandu")
            meni_menadzer()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def meni_prodavac():

    print('***' * 20)
    while True:
        print("\n1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Prodaj knjigu")
        print("6. Dodaj knjigu")
        print("7. Izmeni knjigu")
        print("8. Obrisi knjigu(logicko brisanje)")
        print("0. Kraj")
        print('***' * 20)
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            ispisi_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            prodaja()
        elif stavka == 6:
            dodavanje_knjiga()
        elif stavka == 7:
            izmena_knjige()
        elif stavka == 8:
            brisanje_knjige()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def main():
    for i in range(4):
        if i == 3:
            print("Previse neuspelih pokusaja za pprijavu!")
            exit()

        ulogovani_korisnik = prijava()
        if ulogovani_korisnik != False :
            print("Uspesna prijava!Tip korisnika:", ulogovani_korisnik['tip_korisnika'])
            if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
                meni_administrator()
            elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
                meni_menadzer()
            elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
                meni_prodavac()
            else:
                print("Greska! Nepostojeca uloga korisnika!")


main()
