from korisnici.korisnici import prijava, registracija, ispis_korisnika, korisnici
from knjige.knjige import sortirane_knjige, pretrazi_knjige, dodavanje_knjiga, brisanje_knjige, izmena_knjige
from akcije.akcije import pretrazi_akcije, sortirane_akcije, dodavanje_akcije
from Prodaja import prodaja_knjige


def meni_administrator():
    print()
    print('***'*20)
    while True:
        print("\n1. Sortiranje knjiga") #radi
        print("2. Pretraga knjiga") #radi
        print("3. Prikaz akcija")#radi
        print("4. Pretraga akcija")#radi
        print("5. Registracija korisnika") #radi
        print("6. Lista korisnika")#radi
        print("7. Dodaj knjigu")#radi
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
            sortirane_akcije()
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
    print('\n')
    print('***' * 20)
    while True:
        print(" 1. Sortiranje knjiga")#radi
        print(" 2. Pretraga knjiga")#radi
        print(" 3. Prikaz akcija")#radi
        print(" 4. Pretraga akcija")#radi
        print(" 5. Registracija akcija")#radi
        print(" 6. Registracija korisnika")#radi
        print(" 7. Lista korisnika")#radi
        print(" 8. Kreiraj izvestaj")
        print(" 0. Kraj")
        print('***' * 20)
        stavka = int(input("Izaberite stavku: "))
        print('***' * 20)

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            sortirane_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            dodavanje_akcije()
        elif stavka == 6:
            registracija()
        elif stavka == 7:
            ispis_korisnika(korisnici)
        elif stavka == 8:
            print("Nemate dozvolu za ovu komandu")
            meni_menadzer()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def meni_prodavac():

    print('***' * 20)
    while True:
        print("\n1. Sortiranje knjiga")#radi
        print("2. Pretraga knjiga")#radi
        print("3. Prikaz akcija")#radi
        print("4. Pretraga akcija")#radi
        print("5. Prodaj knjigu")
        print("6. Dodaj knjigu")#radi
        print("7. Izmeni knjigu")
        print("8. Obrisi knjigu(logicko brisanje)")
        print("0. Kraj")
        print('***' * 20)
        stavka = int(input("Izaberite stavku: "))
        print('***' * 20)

        if stavka == 1:
            sortirane_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            sortirane_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            prodaja_knjige()
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
    mogucnost_prijave = True
    i = 0
    while(mogucnost_prijave):
        if i == 3:
            print("Previse neuspelih pokusaja za pprijavu!")
            mogucnost_prijave = False
            exit()
        ulogovani_korisnik = prijava()
        if ulogovani_korisnik != False :
            print("Uspesna prijava!Tip korisnika:", ulogovani_korisnik['tip_korisnika'])
            if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
                meni_administrator()
            elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
                meni_menadzer()
            else:
                meni_prodavac()
        else:
            print("Greska! Nepostojeca uloga korisnika!")
            i = i + 1


main()
