from korisnici.korisnici import prijava, registracija, sortiranje_korisnika
from knjige.knjige import sortirane_knjige, pretrazi_knjige, dodavanje_knjiga, brisanje_knjige, izmena_knjige
from akcije.akcije import pretrazi_akcije, sortirane_akcije, dodavanje_akcije
from racun.Prodaja import prodaja_knjige, izvestaj


def meni_administrator(ulogovani):
    print()
    print('***'*20)
    while True:
        print("\n1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Registracija korisnika")
        print("6. Lista korisnika")
        print("7. Dodaj knjigu")
        print("8. Izmeni knjigu")
        print("9. Obrisi knjigu")
        print("0. Kraj")
        print('***' * 20)
        stavka = input("Izaberite stavku: ")
        print('***' * 20)

        if stavka == "1":
            sortirane_knjige(ulogovani)
        elif stavka == "2":
            pretrazi_knjige(ulogovani)
        elif stavka == "3":
            sortirane_akcije()
        elif stavka == "4":
            pretrazi_akcije()
        elif stavka == "5":
            registracija()
        elif stavka == "6":
            sortiranje_korisnika()
        elif stavka == "7":
            dodavanje_knjiga()
        elif stavka == "8":
            izmena_knjige()
        elif stavka == "9":
            brisanje_knjige()
        elif stavka == "0":
            return
        else:
            print("Pokusajte ponovo!")
            meni_administrator(ulogovani)


def meni_menadzer(ulogovani):
    print('\n')
    print('***' * 20)
    while True:
        print(" 1. Sortiranje knjiga")
        print(" 2. Pretraga knjiga")
        print(" 3. Prikaz akcija")
        print(" 4. Pretraga akcija")
        print(" 5. Registracija akcija")
        print(" 6. Registracija korisnika")
        print(" 7. Lista korisnika")
        print(" 8. Kreiraj izvestaj")
        print(" 0. Kraj")
        print('***' * 20)
        stavka = input("Izaberite stavku: ")
        print('***' * 20)

        if stavka == '1':
            sortirane_knjige(ulogovani)
        elif stavka == '2':
            pretrazi_knjige(ulogovani)
        elif stavka == '3':
            sortirane_akcije()
        elif stavka == '4':
            pretrazi_akcije()
        elif stavka == '5':
            dodavanje_akcije()
        elif stavka == '6':
            registracija()
        elif stavka == '7':
            sortiranje_korisnika()
        elif stavka == '8':
            izvestaj()
        elif stavka == '0':
            return
        else:
            print("Pokusajte ponovo!")
            meni_menadzer(ulogovani)


def meni_prodavac(ulogovani_korisnik):

    print('***' * 20)
    while True:
        print("\n1. Sortiranje knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Prodaj knjigu")
        print("6. Dodaj knjigu")
        print("7. Izmeni knjigu")
        print("8. Obrisi knjigu")
        print("0. Kraj")
        print('***' * 20)
        stavka = input("Izaberite stavku: ")
        print('***' * 20)

        if stavka == '1':
            sortirane_knjige(ulogovani_korisnik)
        elif stavka == '2':
            pretrazi_knjige(ulogovani_korisnik)
        elif stavka == '3':
            sortirane_akcije()
        elif stavka == '4':
            pretrazi_akcije()
        elif stavka == '5':
            prodaja_knjige(ulogovani_korisnik)
        elif stavka == '6':
            dodavanje_knjiga()
        elif stavka == '7':
            izmena_knjige()
        elif stavka == '8':
            brisanje_knjige()
        elif stavka == '0':
            return
        else:
            print("Pokusajte ponovo!")
            meni_prodavac(ulogovani_korisnik)


def main():
    mogucnost_prijave = True
    i = 0
    while(mogucnost_prijave):
        if i == 3:
            print("Previse neuspelih pokusaja za prijavu!")
            mogucnost_prijave = False
            exit()
        ulogovani_korisnik = prijava()
        if ulogovani_korisnik != False :
            print("Uspesna prijava!Tip korisnika:", ulogovani_korisnik['tip_korisnika'])
            if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
                meni_administrator(ulogovani_korisnik)
            elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
                meni_menadzer(ulogovani_korisnik)
            else:
                meni_prodavac(ulogovani_korisnik)
        else:
            print("Greska! Nepostojeca uloga korisnika!")
            i = i + 1


main()
