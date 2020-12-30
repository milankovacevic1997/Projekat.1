from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from knjige.knjigeIO import ucitaj_knjige

akcije=ucitaj_akcije()
n=len(akcije)
knjige=ucitaj_knjige()

kljuc = ['sifra', 'autor', 'kategorija', 'cena']

def pretraga_akcija_string(kljuc, vrednost):
    filtrirane_akcije = []
    if kljuc == 'sifra' or kljuc=="nova cena" or kljuc=="datum_vazenja":
        for akcija in akcije:
            if vrednost.lower() in akcija[kljuc].lower():
                filtrirane_akcije.append(akcija)
    else:
        for akcija in akcije:
            for artikal in akcija['artikli']:
                if artikal[kljuc].lower() == vrednost.lower():
                    filtrirane_akcije.append(akcija)
    return filtrirane_akcije



def pretraga_akcija_jednakost(kljuc,vrednost):
    akcije=ucitaj_akcije()
    filtritane_akcije=[]

    for akcija in akcije:
        if vrednost==akcija[kljuc]:
            filtritane_akcije.append(akcija)
    return filtritane_akcije


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
        naslov = input("Unesite nalsov: ")
        akcije =pretraga_akcija_string("naslov", naslov)
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

    ispisi_akcije(akcije)


def sortiraj_akcije(kljuc):
    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp
    ispisi_akcije(akcije)


def sortirane_akcije():
    print('***' * 20)
    print("\n1. Sortiraj po sifri")
    print("2. Sortiraj po datumu")
    print("0. Izlaz")
    print('***' * 20)

    stavka = int(input("Izaberite stavku: "))
    print('***' * 20)
    if stavka == 1:
        sortiraj_akcije("sifra")

    elif stavka == 2:
        sortiraj_akcije("datum_vazenja")

    elif stavka == 0:
        return
    else:
        print("Pogresan unos!")
    ispisi_akcije(akcije)

def ispisi_akcije(akcije):
        zaglavlje = f"{'sifra':<10}" \
                    f"{'naslov':<20}" \
                    f"{'stara cena':^20}" \
                    f"{'nova cena':^20}" \
                    f"{'datum vazenja':^20}"

        print(zaglavlje)
        print("-" * len(zaglavlje))
        for i in range (0,len(akcije)):
            for j in range (0,len(akcije[i]['artikli'])):
                za_ispis = f"{akcije[i]['sifra']:<10}" \
                           f"{akcije[i]['artikli'][j]['naslov']:<20}" \
                           f"{akcije[i]['artikli'][j]['cena']:<20}" \
                           f"{akcije[i]['nova cena']:<20}" \
                           f"{akcije[i]['datum_vazenja']:<20}"

                print(za_ispis)


def  dodavanje_akcije():
    nova_akcija = {
      "sifra": 33,
      "artikli": [],
      "nova cena": 1800.0,
      "datum_vazenja": "27.12.2020."
    }
    sifra = akcije[-1]['sifra']
    nova_akcija['sifra'] = sifra + 1
    unos_knjiga = True
    while(unos_knjiga):
        sifra = input("\n Unesi sifru knjige (unesi 'nazad' za povratak u meni, unesi 'x' za prekid unosa knjiga):")
        if sifra == 'nazad':
            return
        elif sifra == 'x':
            unos_knjiga = False
        else:
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra):
                    nova_akcija['artikli'].append(knjiga)
    nova_cena = input("\n Unesi cenu akcije")
    nova_akcija['nova cena'] = nova_cena
    datum_vazenja = input("\n Unesi datum vazenja akije")
    nova_akcija['datum_vazenja'] = datum_vazenja
    akcije.append(nova_akcija)
    sacuvaj_akcije(akcije)
    print('Nova akcija je dodata u bazu podataka. Sifra akcije=[%s]' % (nova_akcija['sifra']))


