from racun.racunIO import ucitaj_racun, sacuvaj_racun
from knjige.knjigeIO import ucitaj_knjige
from akcije.akcijeIO import ucitaj_akcije
from datetime import datetime
from korisnici.korisniciIO import ucitaj_korisnike

racuni = ucitaj_racun()
knjige = ucitaj_knjige()
akcije = ucitaj_akcije()
korisnici=ucitaj_korisnike()

def prodaja_knjige():
    korpa = []
    now = datetime.now()
    novi_racun = {
        "sifra": 666,
        "prodavac": "Mirko Mirkovic",
        "datum_vreme": "2020-12-27T18:16:25.925653",
        "artikli": [], "akcije": [],
        "cena": 0.0
    }
    novi_racun['sifra'] = racuni[-1]['sifra'] + 1
    unos_artikala = True
    while(unos_artikala):
        sifra = input("\n Unesi sifru knjige ili akcije (unesi 'nazad' za povratak u meni, unesi 'x' za prekid unosa knjiga):")
        if sifra == 'nazad':
            return
        elif sifra == 'x':
            unos_artikala = False
        else:
            for knjiga in knjige:
                if knjiga['sifra'] == int(sifra):
                    kolicina = input("\n Unesi kolicinu:")
                    knjiga['kolicina'] = kolicina
                    novi_racun['artikli'].append(knjiga)
                    novi_racun['cena'] += knjiga['cena']*int(kolicina)
                    continue
            for akcija in akcije:
                if akcija['sifra'] == int(sifra):
                    kolicina = input("\n Unesi kolicinu:")
                    akcija['kolicina'] = kolicina
                    novi_racun['akcije'].append(akcija)
                    novi_racun['cena'] += akcija['nova cena']*int(kolicina)
    ispis_knjiga_racun(racuni)
    ispis_akcija_racun(racuni)
    # while True:
    #     print('\nZelite li da nastavite kupovinu?\n1. Da\n2. Odustani')
    #     stavka = int(input('Unesite odgovor:'))
    #         if stavka == 1:
    #             novi_racun['datum_vreme'] = now.strftime("%d.%m.%Y. %H:%M:%S")
    #             racuni.append(novi_racun)
    #             sacuvaj_racun(racuni)
    #         elif stavka == 2:
    #             return False
    #         else:
    #             print('Uneli ste pogresnu opciju. Pokusajte ponovo.')


def ispisi_racun(akcije):
    zaglavlje = f"{'sifra':<10}" \
                f"{'naslov':<20}" \
                f"{'stara cena':^20}" \
                f"{'nova cena':^20}" \
                f"{'datum vazenja':^20}"

    print(zaglavlje)
    print("-" * len(zaglavlje))
    for i in range(0, len(akcije)):
        for j in range(0, len(akcije[i]['artikli'])):
            za_ispis = f"{akcije[i]['sifra']:<10}" \
                       f"{akcije[i]['artikli'][j]['naslov']:<20}" \
                       f"{akcije[i]['artikli'][j]['cena']:<20}" \
                       f"{akcije[i]['nova cena']:<20}" \
                       f"{akcije[i]['datum_vazenja']:<20}"

            print(za_ispis)


#
# def prodaja_knjige():
#     global korpa
#     z = -1
#     i = 0
#     while True:
#         sifra = input("\nUnesite sifru (unesite 'nazad' za povratak):")
#         if (sifra == 'nazad'):
#             return False
#         elif (sifra != ''):
#             result = pretraga_knjiga_string("sifra", ' ')
#             if (result == None):
#                 break
#             else:
#                 print("Sifra ne sme da sadrzi razmake, pokusajte ponovo.")
#                 if (prodaja_knjige() == False):
#                     return False
#         else:
#             print("Unesite sifru.")
#             if (prodaja_knjige() == False):
#                 return False
#     for knjiga in knjige:
#         if (knjiga['sifra'] == sifra):
#             print('Knjiga je pronadjena.')
#             z = i
#             break
#         i += 1
#     if (z == -1):
#         print('Knjiga nije pronadjena, pokusajte ponovo.')
#         if (prodaja_knjige() == False):
#             return False
#     sadrzaj_korpe=[]
#     while True:
#         try:
#             q = int(input('Kolicina:'))
#             break
#         except ValueError: print('Unesite cele brojeve')
#     print('Sadrzaj se dodaje u korpu:')
#     for i in range(q):
#         sadrzaj_korpe+= [knjige[z]]
#     list(sadrzaj_korpe)
#     while True:
#         print('\nZelite li da nastavite kupovinu?\n1. Da\n2. Odustani')
#         stavka = input('Unesite odgovor:')
#         if stavka == '1':
#             korpa += sadrzaj_korpe
#             return True
#         elif stavka == '2':
#             return False
#         else:
#             print('Uneli ste pogresnu opciju. Pokusajte ponovo.')

def pravljenje_racuna():
    racun = {
        "sifra": 666,
        "prodavac": "Mirko Mirkovic",
        "datum_vreme": "2020-12-27T18:16:25.925653",
        "artikli": [],
        "ukupno": 0.0
    }
    stari_racun = ucitaj_racun()
    z=0
    for racun in stari_racun:
        z+=1
    racun['sifra'] = z
    racun['prodavac'] = korisnici.korisnicko_ime()
    racun['datum_vreme'] = datetime.now().isoformat()
    racun['artikli'] = artikli
    racun['ukupno'] = ukupno
    return racun

def ispis_zaglavlja(racuni):
    print('sifra racuna: '), print(int[racun['sifra']])
    print('prodavac: '), print(str[korisnici['korisnicko_ime']])
    print('datum i vreme: '), print(datetime.now().isoformat())
    print('__'*20)

def ispis_knjiga_racun(racuni):
    global za_ispis
    zaglavlje = f"{'artikli':<20}" \
                f"{'cena':<20}" \
                f"{'kolicina':<20}"

    print(zaglavlje)
    print("-" * len(zaglavlje))

    for racun in racuni:
        for i in range(0, len(racuni)):
            for j in range(0, len(racuni[i]['artikli'])):
                za_ispis = f"{racun[i]['artikli'][j]['naslov']:<20}" \
                           f"{racun[i]['artikli'][j]['cena']:^20}" \
                           f"{racun[i]['artikli'][j]['kolicina']:^20}"

        print(za_ispis)
    print("-" * len(zaglavlje))

def ispis_akcija_racun(racuni):
    zaglavlje = f"{'artikli':<20}" \
                f"{'cena':<20}" \
                f"{'kolicina':<20}"

    print(zaglavlje)
    print("-" * len(zaglavlje))

    for racun in racuni:
        za_ispis = f"{racun['akcije']['naslov']:<20}" \
                   f"{racun['cena']:<20}" \
                   f"{racun['akcije']['kolicina']:<20}"
        print(za_ispis)
    print("-" * len(zaglavlje))


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
    racun.save(racuni)
    print('Prodaja zavrsena. Izvolite racun:')
    print(racun)
    return False



# def  dodavanje_akcije():
#     nova_akcija = {
#       "sifra": 33,
#       "artikli": [{
#             "sifra": 350497,
#             "naslov": "Ana Karenjina",
#             "autor": "Tolstoj",
#             "isbn": "456372839",
#             "izdavac": "Laguna",
#             "broj strana": "213",
#             "godina": 2020,
#             "cena": 1899.1,
#             "kategorija": "Roman"
#         }],
#       "nova cena": 1800.0,
#       "datum_vazenja": "27.12.2020."
#     }
#     for akcija in akcije:
#         sifra = akcije['sifra']
#     sifra += 1
#     nova_akcija['sifra'] = sifra
#     akcija_knjige = []
#     while True:
#         prompt = 0
#         breaker = 0
#         sifra = input("Sacuvaj sifru (ukucaj 'nazad' za povratak):")
#         if (knjige.find(sifra) != None and sifra != ''):
#             knjiga1 = knjiga.find(sifra)
#             print('Knjiga je pronadjena.')
#             prompt = 1
#             print('Knjiga se dodaje u akcije:')
#             knjige = [knjiga1]
#             knjige.permissions('a')
#             knjige.list(knjige)
#             knjige.permissions('m')
#             while True:
#                 print('\nZelite li da nastavite\n1. Da\n2. Odustani')
#                 stavka = input('Unesi:')
#                 if stavka == '1':
#                     while True:
#                         try:
#                             price = float(input('New price for the book:'))
#                             knjiga1['cena'] = cena
#                             break
#                         except ValueError:
#                             print('Pogresan unos, pokusajte ponovo.')
#                     akcija_knjige.append(knjiga1)
#                     break
#                 elif stavka == '2':
#                     prompt = 0
#                     sifra = 'a'
#                     break
#                 else:
#                     print('Pogresan unos. Pokusajte ponovo.')
#         elif (sifra == 'nazad'):
#             return False
#         else:
#             print('Pogresan unos. Pokusajte ponovo.')
#         if (prompt == 1):
#             while True:
#                 print('\nZelite li da unesete jos neku knjigu u akciju\n1. Da\n2. Ne')
#                 stavka = input('Unesi:')
#                 if stavka == '1':
#                     break
#                 elif stavka == '2':
#                     breaker = 1
#                     break
#                 else:
#                     print('Pogresan unos. Pokusajte ponovo.')
#             if (breaker == 1 and akcija_knjige != []): break
#     nova_akcija['artikli'] = akcija_knjige
#
#     while True:
#         try:
#             godina = int(input('Godina izdanja:'))
#             izdanje = date(godina, 1, 1)
#             break
#         except ValueError:
#             print('Pogresan unos. Pokusajte ponovo.')
#     while True:
#         try:
#             mesec = int(input('Mesec:'))
#             expiry = date(godina, mesec, 1)
#             break
#         except ValueError:
#             print('Pogresan unos. Pokusajte ponovo.')
#     while True:
#         try:
#             dan = int(input('Dan:'))
#             expiry = date(godina, mesec, dan)
#             break
#         except ValueError:
#             print('Pogresan unos. Pokusajte ponovo.')
#     nova_akcija['izdanje'] = str(izdanje)
#     print('\nAkcija se dodaje.')
#     nova_akcija = [nova_akcija]
#     show_valid = False
#     ispisi_akcije(akcije)
#
#     while True:
#         print('\nZelite li da nastavite?\n1. Da\n2. Odustani')
#         stavka = input('Unesi:')
#         if stavka == '1':
#             akcije.append(nova_akcija)
#             break
#         elif stavka == '2':
#             return False
#         else:
#             print('Pogresan unos. Pokusajte ponovo.')
#     save(akcije)
#     print('%s je dodata u bazu podataka. Sifra akcije =[%s]' %(nova_akcija['naslov'], nova_akcija['sifra']))
#     return False
