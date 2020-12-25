from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from knjige.knjigeIO import ucitaj_knjige

akcije=ucitaj_akcije()
n=len(akcije)
knjige=ucitaj_knjige()

kljuc = ['sifra', 'autor', 'kategorija', 'cena']

def pretraga_akcija_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []

    for akcija in akcije:
        if vrednost.lower() in akcija[kljuc].lower():
            filtrirane_akcije.append(akcija)
    return filtrirane_akcije


def pretraga_akcija_jednakost(kljuc,vrednost):
    akcije=ucitaj_akcije()
    filtritane_akcije=[]

    for akcija in akcije:
        if vrednost==akcija[kljuc]:
            filtritane_akcije.append(akcija)
    return filtritane_akcije

def sort():
    while True:
        print("\nSortiraj po"
              "\n1. sifri"
              "\n2. datum vazenja"
              "\n0. nazad")
        stavka = input("Opcija:")
        if stavka == 1:
            sorter = 'sifra'
            break
        elif stavka == 2:
            sorter = 'datum_vazenja'
            break
        elif stavka == 0:
            return False
        else:
            print("pogresan unos!")

    if sorter == 'sifra':
        akcije.sort(key=lambda akcije: akcije.get('sifra'))
    if sorter == 'datum_vazenja':
        akcije.sort(key=lambda akcije: akcije.get('datum_vazenja'))
    ispis_akcija(akcije)


def pretrazi_akcije():
    print('***' * 20)
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po artiklu")
    print("3. Pretraga po datumu vazenja")
    print("0. Napusti pretragu")
    print('***' * 20)
    stavka = int(input("Izaberite stavku: "))
    print('***' * 20)
    akcije = []
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        akcije = pretraga_akcija_jednakost("sifra", sifra)
    elif stavka == 2:
        artikli = input("Unesite nalsov: ")
        akcije =pretraga_akcija_string("artikli", artikli)
    elif stavka == 3:
        datum_vazenja = input("Unesite datum vazenja: ")
        akcije = pretraga_akcija_jednakost("datum_vazenja", datum_vazenja)
    elif stavka == 4:
        kategorija = input("Unesite kategoriju:")
        akcije = pretraga_akcija_string('kategorija', kategorija)
    elif stavka==0:
        return
    else:
        print("Pogresan unos")

    ispisi_akcije()


def sortiraj_akcije(kljuc):
    akcije = ucitaj_akcije()

    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije


def sortirane_akcije():
    print('***' * 20)
    print("\n1. Sortiraj po sifri")
    print("2. Sortiraj po datumu")
    print("0. Izlaz")
    print('***' * 20)

    stavka = int(input("Izaberite stavku: "))
    print('***' * 20)
    knjige = ucitaj_akcije()
    if stavka == 1:
        knjige = sortiraj_akcije("sifra")

    elif stavka == 2:
        knjige = sortiraj_akcije("datum_vazenja")

    elif stavka == 0:
        return
    else:
        print("Pogresan unos!")
    ispisi_akcije()

def ispisi_akcije():

    zaglavlje = f"{'sifra':<15}" \
                f"{'artikli':<45}" \
                f"{'cena':<15}" \
                f"{'datum vazenja':<20}"

    print(zaglavlje)
    print("-" * len(zaglavlje))

    for akcija in akcije:
        za_ispis = f"{akcija['sifra']:<15}" \
                   f"{akcija['artikli']:<45}" \
                   f"{akcija['cena']:<15}" \
                   f"{akcija['datum_vazenja']:<20}"
        print(za_ispis)

def  registracija_akcije():
    global sifra
    for akcija in akcije:
        sifra=akcija['sifra']
    sifra+=1
    artikli=input('artikli:')
    cena=float(input('cena:'))
    datum_vazenja=int(input('datum_vazenja:'))
    nova_akcija={
        "sifra": 3,
        "artikli": "Knjiga 1",
        "cena": 650.0,
        "datum_vazenja": "20.12.2020."
    }
    nova_akcija['sifra'] = sifra
    nova_akcija['artikli']= artikli
    nova_akcija['cena']=cena
    nova_akcija['datum_vazenja']=datum_vazenja

    akcije.append(nova_akcija)
    sacuvaj_akcije(akcije)
    print('%s je dodata u bazu podataka. Sifra akcije =[%s]' %(nova_akcija['naslov'], nova_akcija['sifra']))
    return False
