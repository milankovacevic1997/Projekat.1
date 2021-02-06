from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from knjige.knjigeIO import ucitaj_knjige
from datetime import datetime

akcije=ucitaj_akcije()
knjige=ucitaj_knjige()

def pretraga_akcija_string(kljuc, vrednost):
    filtrirane_akcije = []
    if kljuc == 'sifra':
        for akcija in akcije:
            if int(vrednost) == akcija[kljuc]:
                filtrirane_akcije.append(akcija)
    else:
        for akcija in akcije:
            for artikal in akcija['artikli']:
                if artikal[kljuc].lower() == vrednost.lower():
                    filtrirane_akcije.append(akcija)
    return filtrirane_akcije

def pretrazi_akcije():
    print('***' * 20)
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po artiklu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    print("0. Napusti pretragu")
    print('***' * 20)
    stavka = input("Izaberite stavku: ")
    print('***' * 20)
    akcije = []
    if stavka == '1':
        sifra = int(input("Unesite sifru: "))
        akcije = pretraga_akcija_string("sifra", sifra)
    elif stavka == '2':
        naslov = input("Unesite nalsov: ")
        akcije =pretraga_akcija_string("naslov", naslov)
    elif stavka == '3':
        autor = input("Unesite autora: ")
        akcije = pretraga_akcija_string("autor", autor)
    elif stavka == '4':
        kategorija = input("Unesite kategoriju:")
        akcije = pretraga_akcija_string('kategorija', kategorija)
    elif stavka== '0':
        return
    else:
        print("Pogresan unos")
        return

    ispisi_akcije(akcije)


def sortiraj_akcije_sifra(kljuc):
    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

def sortiraj_akcije_datum():
    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if datetime.strptime(akcije[i]['datum_vazenja'],'%Y-%m-%d') < datetime.strptime(akcije[j]['datum_vazenja'],'%Y-%m-%d'):
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp



def sortirane_akcije():
    print('***' * 20)
    print("\n1. Sortiraj po sifri")
    print("2. Sortiraj po datumu")
    print("0. Izlaz")
    print('***' * 20)

    stavka = input("Izaberite stavku: ")
    print('***' * 20)
    if stavka == '1':
        sortiraj_akcije_sifra("sifra")

    elif stavka == '2':
        sortiraj_akcije_datum()

    elif stavka == '0':
        return
    else:
        print("Pogresan unos!")
        return
    ispisi_akcije(akcije)

def ispisi_akcije(akcije):
        zaglavlje = f"{'sifra             ':<10}" \
                    f"{'naslov':<30}" \
                    f"{'stara cena':<13}" \
                    f"{'nova cena':^15}" \
                    f"{'datum vazenja':>20}"

        print(zaglavlje)
        print("-" * len(zaglavlje))

        for i in range (0,len(akcije)):
            date_time_obj = datetime.strptime(akcije[i]['datum_vazenja'], '%Y-%m-%d')
            if date_time_obj >= datetime.now():
                print(akcije[i]['sifra'], " "*80, akcije[i]['datum_vazenja'])
                for j in range (0,len(akcije[i]['artikli'])):
                    za_ispis = f"{akcije[i]['artikli'][j]['naslov']:^40}" \
                               f"{akcije[i]['artikli'][j]['cena']:^20}" \
                               f"{akcije[i]['artikli'][j]['nova cena']:^20}"

                    print(za_ispis)


def  dodavanje_akcije():
    nova_akcija = {
      "sifra": 33,
      "artikli": [],
      "datum_vazenja": "27.12.2020."
    }
    nova_akcija['sifra'] = akcije[-1]['sifra'] + 1
    unos_knjiga = True
    while(unos_knjiga):
        sifra = input("\nUnesi sifru knjige (unesi 'nazad' za povratak u meni, unesi 'x' za prekid unosa knjiga): ")
        if sifra == 'nazad':
            return
        elif sifra == 'x':
            unos_knjiga = False
        else:
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra) and knjiga['obrisano']== "False":
                    nova_cena = input("\nUnesi novu cenu knjige: ")
                    knjiga['nova cena'] = nova_cena
                    nova_akcija['artikli'].append(knjiga)
    datum_vazenja = input("\nUnesi datum vazenja akcije (godina-mesec-dan): ")
    nova_akcija['datum_vazenja'] = datum_vazenja
    akcije.append(nova_akcija)
    sacuvaj_akcije(akcije)
    print('Nova akcija je dodata u bazu podataka. Sifra akcije=[%s]' % (nova_akcija['sifra']))


