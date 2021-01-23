from racun.racunIO import ucitaj_racun, sacuvaj_racun
from knjige.knjigeIO import ucitaj_knjige
from akcije.akcijeIO import ucitaj_akcije
from datetime import datetime


racuni = ucitaj_racun()
knjige = ucitaj_knjige()
akcije = ucitaj_akcije()

def prodaja_knjige(ulogovani_korisnik):
    now = datetime.now()
    novi_racun = {
        "sifra": 666,
        "prodavac": ulogovani_korisnik['korisnicko_ime'],
        "datum_vreme": "2020-12-27T18:16:25.925653",
        "artikli": [], "akcije": [],
        "cena": 0.0
    }
    novi_racun['sifra'] = racuni[-1]['sifra'] + 1
    unos_artikala = True
    while(unos_artikala):
        sifra = input("\nUnesi sifru knjige ili akcije (unesi 'nazad' za povratak u meni, unesi 'x' za prekid unosa knjiga i prikaz sadrzaja korpe):")
        if sifra == 'nazad':
            return
        elif sifra == 'x':
            unos_artikala = False
        else:
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra) and knjiga['obrisano']=="False":
                    kolicina = input("\n Unesi kolicinu:")
                    knjiga['kolicina'] = kolicina
                    novi_racun['artikli'].append(knjiga)
                    novi_racun['cena'] += knjiga['cena']*int(kolicina)
                    continue
            for akcija in akcije:
                if akcija['sifra'] == int(sifra) and datetime.strptime(akcija['datum_vazenja'],'%Y-%m-%d') > datetime.now():
                    kolicina = input("\n Unesi kolicinu:")
                    akcija['kolicina'] = kolicina
                    novi_racun['akcije'].append(akcija)
                    for artikal in akcija['artikli']:
                        novi_racun['cena'] += float(artikal['nova cena'])*int(kolicina)
    print('\n')
    print('U korpi se nalaze sledeci artikli:')
    ispis_knjiga_racun(novi_racun)
    ispis_akcija_racun(novi_racun)
    ispis_racun_ukupno(novi_racun)
    a = True
    while a:
        print('\nZelite li da nastavite kupovinu?\n1. Da\n2. Odustani')
        stavka = int(input('Unesite odgovor:'))
        if stavka == 1:
            novi_racun['datum_vreme'] = now.strftime("%d.%m.%Y. %H:%M:%S")
            racuni.append(novi_racun)
            sacuvaj_racun(racuni)
            pravljenje_racuna(novi_racun)
            a = False
        elif stavka == 2:
            return False
        else:
            print('Uneli ste pogresnu opciju. Pokusajte ponovo.')

def pravljenje_racuna(racun):
    ispis_zaglavlja(racun)
    ispis_knjiga_racun(racun)
    ispis_akcija_racun(racun)
    ispis_racun_ukupno(racun)

def ispis_zaglavlja(racun):
    print('\n')
    print('__' * 35)
    print('Prodaja zavrsena. Izvolite racun:')
    print('--'*35)
    print('sifra racuna: ', racun['sifra'])
    print('prodavac: ',racun['prodavac'])
    print('datum i vreme: ',datetime.now().isoformat())
    print('__'*35)
    print('--'*35)

def ispis_knjiga_racun(racun):
    if racun['artikli']!=[]:
        zaglavlje = f"{'knjige':<30}" \
                    f"{'kolicina':^20}"\
                    f"{'cena':^20}"

        print(zaglavlje)
        print("-" * len(zaglavlje))

        for knjiga in racun['artikli']:
            za_ispis = f"{knjiga['naslov']:<30}" \
                       f"{knjiga['kolicina']:^20}" \
                       f"{knjiga['cena']:^20}"

            print(za_ispis)
        print("-" * len(zaglavlje))

def ispis_akcija_racun(racun):
    if racun['akcije'] != []:
        zaglavlje = f"{'akcije':<30}" \
                    f"{'kolicina':^20}"\
                    f"{'cena':^20}"


        print(zaglavlje)
        print("-" * len(zaglavlje))
        for akcija in racun['akcije']:
            for artikal in akcija['artikli']:
                za_ispis = f"{artikal['naslov']:<30}" \
                           f"{akcija['kolicina']:^20}"\
                           f"{artikal['nova cena']:^20}"

                print(za_ispis)
        print("_" * len(zaglavlje))
        print("-" * len(zaglavlje))

def ispis_racun_ukupno(racun):
    print("Ukupno: ", racun['cena'])



def kraj_kupovine():
    racuni = ucitaj_racun()
    racun = pravljenje_racuna()
    print('\nKnjige koje su odabrane su:')
    ispis_knjiga_racun(racuni)
    ispis_akcija_racun(racuni)
    while True:
        print('\nZelite li da nastavite?\n1. Da\n2. Odustani')
        stavka = input('Unesite:')
        if stavka == '1':
            racuni.append(racun)
            break
        elif stavka == '2':
            return False
        else:
            print('Pogresan unos.')
    sacuvaj_racun(racuni)
    print(racun)
    return False

def izvestaj():
    print('***' * 20)
    print("\n1. Prikazi izvestaj ukupne prodaje knjiga")
    print("2. Prikazi izvestaj ukupne prodaje akcija")
    print("3. Prikazi izvestaj ukupne prodaje po autoru")
    print("4. Prikazi izvestaj ukupne prodaje po izdavacu")
    print("5. Prikazi izvestaj ukupne prodaje po kategoriji")
    print("0. Napusti pretragu")
    print('***' * 20)
    stavka = input("Izaberite stavku: ")
    print('***' * 20)
    knjige = []
    if stavka == '1':
        print('\n')
        print('U nastavku se nalazi izvestaj ukupne prodaje svih knjiga: ')
        izvestaj_ukupna_prodaja()
    elif stavka == '2':
        print('\n')
        print('U nastavku se nalazi izvestaj ukupne prodaje akcija: ')
        izvestaj_akcije()
    elif stavka == '3':
        print('\n')
        print('Izvestaj ukupne prodaje knjiga sortiranih u odnosu na autora: ')
        izvestaj_autor()
    elif stavka == '4':
        print('\n')
        print('Izvestaj ukupne prodaje knjiga sortiranih u odnosu na izdavaca: ')
        izvestaj_izdavac()
    elif stavka == '5':
        print('\n')
        print('Izvestaj ukupne prodaje knjiga sortiranih u odnosu na kategoriju knjige: ')
        izvestaj_kategorija()
    elif stavka == '0':
        return
    else:
        print("Pogresan unos")
        return


def izvestaj_ukupna_prodaja():
    recnik ={}
    recnikCene = {}
    for knjiga in knjige:
        recnik[knjiga['naslov']] = 0
        recnikCene[knjiga['naslov']]=0
    for racun in racuni:
        for artikal in racun['artikli']:
            recnik[artikal['naslov']]+=int(artikal['kolicina'])
            recnikCene[artikal['naslov']] +=artikal['cena'] * int(artikal['kolicina'])
        for akcije in racun['akcije']:
            for artikal in akcije['artikli']:
                recnik[artikal['naslov']]+=int(akcije['kolicina'])
                recnikCene[artikal['naslov']] += float(artikal['nova cena']) * int(akcije['kolicina'])
    izvestaj_ukupne_knjige(recnik,recnikCene)

def izvestaj_prodaja_akcija():
    recnik ={}
    for akcija in akcije:
        recnik[akcija['sifra']] = 0
    for racun in racuni:
        for akcija in racun['akcije']:
            recnik[akcija['sifra']]+=int(akcija['kolicina'])
    print(recnik)

def izvestaj_akcije():
    sifra = input("Unesi sifru akcije: ")
    recnik = {}
    recnikCene = {}
    for akcija in akcije:
        if akcija['sifra']== sifra:
            recnik[akcija[artikli['naslov']]] = 0
            recnikCene[akcija[artikli['naslov']]] = 0
    for racun in racuni:
        for artikal in racun['artikli']:
            if artikal['naslov'] in recnik.keys():
                recnik[artikal['naslov']] +=int(artikal['kolicina'])
                recnikCene[artikal['naslov']] += artikal['cena'] * int(artikal['kolicina'])
        for akcija in racun['akcije']:
            for artikal in akcija['artikli']:
                if artikal['naslov'] in recnik.keys():
                    recnik[artikal['naslov']]+=int(akcija['kolicina'])
                    recnikCene[artikal['naslov']] += float(artikal['nova cena']) * int(akcija['kolicina'])
    izvestaj_ukupne_akcije(recnik,recnikCene)

def izvestaj_autor():
    autor = input("Unesi ime autora: ")
    recnik = {}
    recnikCene = {}
    for knjiga in knjige:
        if knjiga['autor'].lower() == autor.lower():
            recnik[knjiga['naslov']] = 0
            recnikCene[knjiga['naslov']] = 0
    for racun in racuni:
        for artikal in racun['artikli']:
            if artikal['naslov'] in recnik.keys():
                recnik[artikal['naslov']] +=int(artikal['kolicina'])
                recnikCene[artikal['naslov']] += artikal['cena'] * int(artikal['kolicina'])
        for akcija in racun['akcije']:
            for artikal in akcija['artikli']:
                if artikal['naslov'] in recnik.keys():
                    recnik[artikal['naslov']]+=int(akcija['kolicina'])
                    recnikCene[artikal['naslov']] += float(artikal['nova cena']) * int(akcija['kolicina'])
    izvestaj_ukupne_knjige(recnik,recnikCene)

def izvestaj_izdavac():
    izdavac = input("Unesi ime izdavaca: ")
    recnik = {}
    recnikCene = {}
    for knjiga in knjige:
        if knjiga['izdavac'].lower() == izdavac.lower():
            recnik[knjiga['naslov']] = 0
            recnikCene[knjiga['naslov']] = 0
    for racun in racuni:
        for artikal in racun['artikli']:
            if artikal['naslov'] in recnik.keys():
                recnik[artikal['naslov']] += int(artikal['kolicina'])
                recnikCene[artikal['naslov']] += artikal['cena'] * int(artikal['kolicina'])
        for akcija in racun['akcije']:
            for artikal in akcija['artikli']:
                if artikal['naslov'] in recnik.keys():
                    recnik[artikal['naslov']] += int(akcija['kolicina'])
                    recnikCene[artikal['naslov']] += float(artikal['nova cena']) * int(akcija['kolicina'])
    izvestaj_ukupne_knjige(recnik, recnikCene)

def izvestaj_kategorija():
    kategorija = input("Unesi ime kategorija: ")
    recnik = {}
    recnikCene = {}
    for knjiga in knjige:
        if knjiga['kategorija'].lower() == kategorija.lower():
            recnik[knjiga['naslov']] = 0
            recnikCene[knjiga['naslov']] = 0
    for racun in racuni:
        for artikal in racun['artikli']:
            if artikal['naslov'] in recnik.keys():
                recnik[artikal['naslov']] += int(artikal['kolicina'])
                recnikCene[artikal['naslov']] += artikal['cena'] * int(artikal['kolicina'])
        for akcija in racun['akcije']:
            for artikal in akcija['artikli']:
                if artikal['naslov'] in recnik.keys():
                    recnik[artikal['naslov']] += int(akcija['kolicina'])
                    recnikCene[artikal['naslov']] += float(artikal['nova cena']) * int(akcija['kolicina'])
    izvestaj_ukupne_knjige(recnik, recnikCene)

def izvestaj_ukupne_knjige(recnik, recnik2):
    zaglavlje = f"{'sifra':<8}" \
        f"{'naslov':<25}" \
        f"{'autor':<17}" \
        f"{'isbn':^12}" \
        f"{'izdavac':^15}" \
        f"{'godina izdanja':^15}" \
        f"{'broj strana':^15}" \
        f"{'cena':^20}" \
        f"{'kategorija':^15}" \
        f"{'kolicina':^10}" \
        f"{'zarada':^15}"
    print(zaglavlje)
    print("-" * len(zaglavlje))

    for knjiga in knjige:
        if knjiga['naslov'] in recnik.keys():
            za_ispis = f"{knjiga['sifra']:<8}" \
                        f"{knjiga['naslov']:<25}" \
                        f"{knjiga['autor']:<17}" \
                        f"{knjiga['isbn']:^12}" \
                        f"{knjiga['izdavac']:^15}" \
                        f"{knjiga['godina']:^15}" \
                        f"{knjiga['broj strana']:^15}" \
                        f"{knjiga['cena']:^20}" \
                        f"{knjiga['kategorija']:^15}" \
                        f"{recnik[knjiga['naslov']]:^10}" \
                        f"{recnik2[knjiga['naslov']]:^15}"

            print(za_ispis)

def izvestaj_ukupne_akcije(recnik, recnik2):
    akcije= ucitaj_akcije()
    zaglavlje = f"{'sifra             ':<10}" \
                 f"{'naslov':<30}" \
                 f"{'stara cena':<13}" \
                 f"{'nova cena':^15}" \
                 f"{'datum vazenja':>25}" \
                 f"{'kolicina':^10}" \
                 f"{'zarada':^15}"

    print(zaglavlje)
    print("-" * len(zaglavlje))

    for i in range(0, len(akcije)):
         date_time_obj = datetime.strptime(akcije[i]['datum_vazenja'], '%Y-%m-%d')
         if date_time_obj > datetime.now():
             print(akcije[i]['sifra'], " " * 85, akcije[i]['datum_vazenja'])
             for akcija in akcije:
                for j in range(0, len(akcije[i]['artikli'])):
                    if akcija[artikli['naslov']] in recnik.keys():
                        za_ispis = f"{akcije[i]['artikli'][j]['naslov']:^40}" \
                                   f"{akcije[i]['artikli'][j]['cena']:^20}" \
                                   f"{akcije[i]['artikli'][j]['nova cena']:^20}"
                        zarada = f"{recnik[akcije['naslov']]:^10}"\
                                  f"{recnik2[akcije['naslov']]:^15}"

                        print(za_ispis)
                        print(zarada)