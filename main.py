from korisnici.korisnici import prijava, registracija, ispis_korisnika, korisnici
from knjige.knjige import sortirane_knjige, pretrazi_knjige, dodavanje_knjiga, brisanje_knjige, izmena_knjige
from akcije.akcije import pretrazi_akcije, sortirane_akcije, dodavanje_akcije
from Prodaja import prodaja_knjige, izvestaj_ukupna_prodaja, izvestaj_prodaja_akcija, izvestaj_autor

def meni_administrator(ulogovani):
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
            sortirane_knjige(ulogovani)
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            sortirane_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            registracija()
        elif stavka == 6:
            ispis_korisnika()
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


def meni_menadzer(ulogovani):
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
            sortirane_knjige(ulogovani)
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
            izvestaj_autor()
        elif stavka == 0:
            return
        else:
            print("Pokusajte ponovo!")


def meni_prodavac(ulogovani_korisnik):

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
            sortirane_knjige(ulogovani_korisnik)
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            sortirane_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            prodaja_knjige(ulogovani_korisnik)
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
