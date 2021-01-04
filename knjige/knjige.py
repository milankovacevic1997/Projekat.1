from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige
import re


knjige = ucitaj_knjige()
i = 0
z = len(knjige)

duzina = [1, 1, 1, 1, 1, 1, 1, 1, 1]

kljuc = ['sifra', 'naslov', 'isbn', 'autor', 'izdavac', 'broj strana', 'godina', 'cena', 'kategorija']


def duzina_liste2():
    max = '1'
    for i in range(9):
        max = len(str(knjige[0][kljuc[i]]))
        for j in range(z - 1):
            if (max < len(str(knjige[i + 1][kljuc[i]]))):
                max = len(str(knjige[j + 1][kljuc[i]]))
        duzina[i] = max


def pretraga_knjiga_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretraga_knjiga_jednakost(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost == knjiga[kljuc]:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige():
    print('***' * 20)
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po kategoriji")
    print("4. Pretraga po autoru")
    print("5. Pretraga po izdavacu")
    print("6. Pretraga po ceni")
    print("0. Napusti pretragu")
    print('***' * 20)
    stavka = int(input("Izaberite stavku: "))
    print('***' * 20)
    knjige = []
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        knjige = pretraga_knjiga_jednakost("sifra", sifra)
    elif stavka == 2:
        naslov = input("Unesite nalsov: ")
        knjige = pretraga_knjiga_string("naslov", naslov)
    elif stavka == 3:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretraga_knjiga_string("kategorija", kategorija)
    elif stavka == 4:
        autor = input("Unesite autora: ")
        knjige = pretraga_knjiga_string("autor", autor)
    elif stavka == 5:
        izdavac = input("Unesite izdavaca: ")
        knjige = pretraga_knjiga_string("izdavac", izdavac)
    elif stavka == 6:
        cena = input("Unesite cenu: ")
        knjige = pretraga_knjiga_jednakost("autor", cena)
    elif stavka == 0:
        return
    else:
        print("Pogresan unos")

    ispisi_knjige(knjige)



def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp

    return knjige


def sortirane_knjige():
    print('***' * 20)
    print("\n1. Sortiraj po sifri")
    print("2. Sortiraj po naslovi")
    print("3. Sortiraj po kategoriji")
    print("4. Sortiraj po autoru")
    print("5. Sortiraj po izdavacu")
    print("6. Sortiraj po ceni")
    print("0. Izlaz")
    print('***' * 20)
    stavka = int(input("Izaberite stavku: "))
    print('***' * 20)
    knjige = ucitaj_knjige()
    if stavka == 1:
        knjige = sortiraj_knjige("sifra")

    elif stavka == 2:
        knjige = sortiraj_knjige("naslov")

    elif stavka == 3:
        knjige = sortiraj_knjige("kategorija")

    elif stavka == 4:
        knjige = sortiraj_knjige("autor")

    elif stavka == 5:
        knjige = sortiraj_knjige("izdavac")

    elif stavka == 6:
        knjige = sortiraj_knjige("cena")

    elif stavka == 0:
        return
    else:
        print("Pogresan unos!")
    ispisi_knjige(knjige)

def ispisi_knjige(knjige):
        zaglavlje = f"{'sifra':<8}" \
                    f"{'naslov':<25}" \
                    f"{'autor':<25}" \
                    f"{'isbn':^15}" \
                    f"{'izdavac':^15}" \
                    f"{'godina izdanja':^15}" \
                    f"{'broj strana':^15}" \
                    f"{'cena':^20}" \
                    f"{'kategorija':^10}"

        print(zaglavlje)
        print("-" * len(zaglavlje))

        for knjiga in knjige:
            za_ispis = f"{knjiga['sifra']:<8}" \
                       f"{knjiga['naslov']:<25}" \
                       f"{knjiga['autor']:<25}" \
                       f"{knjiga['isbn']:^15}" \
                       f"{knjiga['izdavac']:^15}" \
                       f"{knjiga['godina']:^15}" \
                       f"{knjiga['broj strana']:^15}" \
                       f"{knjiga['cena']:^20}" \
                       f"{knjiga['kategorija']:^10}"
            print(za_ispis)

def  dodavanje_knjiga():
    global sifra
    for knjiga in knjige:
        sifra=knjiga['sifra']
    sifra+=1
    naslov=input('naslov:')
    autor=input('autor:')
    isbn=input('isbn:')
    izdavac=input('izdavac:')
    godina=int(input('godina:'))
    cena=float(input('cena:'))
    broj_strana=int(input('broj strana:'))
    kategorija=input('kategorija:')
    nova_knjiga={
        "sifra": 3,
        "naslov": "Knjiga 1",
        "autor": "Pera Peric",
        "isbn": "1312312312312",
        "izdavac": "Vulkan",
        "broj strana": "231",
        "godina": 2020,
        "cena": 650.0,
        "kategorija": "Roman"
    }
    nova_knjiga['sifra'] = sifra
    nova_knjiga['naslov']= naslov
    nova_knjiga['autor']=autor
    nova_knjiga['isbn']=isbn
    nova_knjiga['izdavac']=izdavac
    nova_knjiga['broj strana']=broj_strana
    nova_knjiga['godina']=godina
    nova_knjiga['cena']=cena
    nova_knjiga['kategorija']=kategorija

    knjige.append(nova_knjiga)
    sacuvaj_knjige(knjige)
    print('%s je dodata u bazu podataka. Knjiga sifra=[%s]' %(nova_knjiga['naslov'], nova_knjiga['sifra']))
    return False

def izmena_knjige():
    unos = 0
    sifra = input("\n Unesi sifru knjige (unesi 'nazad' za povratak):")
    i=0
    for knjiga in knjige:
        if knjige['sifra']==sifra:
            unos=1
            print("Knjiga pronadjena!")
            break
        elif sifra=='nazad':
            return False
        i+=1
    if unos==0:
        print("Knjiga nije pronadjena, pokusaj opet!")
        if izmena_knjige()==False:
            return False

    stara_knjiga={
    "sifra": 3,
    "naslov": "Knjiga 1",
    "autor": "Pera Peric",
    "isbn": "1312312312312",
    "izdavac": "Vulkan",
    "broj strana": "231",
    "godina": 2020,
    "cena": 650.0,
    "kategorija": "Roman"}
    stara_knjiga=knjige[i]
    z=1
    stara_knjiga=[stara_knjiga]
    ispisi_knjige(stara_knjiga)

    naslov=input("\n Izmena naslova!")
    if naslov=='':
        naslov=knjige[i]['naslov']
    autor=input("\n Izmena autora!")
    if autor=='':
        autor=knjige[i]['autor']
    isbn=input("\n Izmena isbn!")
    if isbn=='':
        isbn=knjige[i]['isbn']
    izdavac=input("\n Izmena izdavaca!")
    if izdavac=='':
        izdavac=knjige[i]['izdavac']
    try:
        broj_strana=int(input("\nIzmena broja strana:"))
    except ValueError:
        broj_strana=knjige[i]['broj strana']
    try:
        godina=int(input("\nizmena godine:"))
    except ValueError:
        godina=knjige[i]['godina']
    try:
        cena=float(input("\n Izmena cene!"))
    except ValueError:
        cena=knjige[i]['cena']

    kategorija=input("\n Izmena kategorije!")
    if kategorija=='':
        kategorija=knjige[i]['kategorija']
    brisanje=knjige[i]['brisanje']
    nova_knjiga={
    "sifra": 3,
    "naslov": "Knjiga 1",
    "autor": "Pera Peric",
    "isbn": "1312312312312",
    "izdavac": "Vulkan",
    "broj strana": "231",
    "godina": 2020,
    "cena": 650.0,
    "kategorija": "Roman",
    "brisanje": False
    }
    nova_knjiga['sifra'] = sifra
    nova_knjiga['naslov']= naslov
    nova_knjiga['autor']=autor
    nova_knjiga['isbn']=isbn
    nova_knjiga['izdavac']=izdavac
    nova_knjiga['broj strana']=broj_strana
    nova_knjiga['godina']=godina
    nova_knjiga['cena']=cena
    nova_knjiga['kategorija']=kategorija
    nova_knjiga['brisanje']=brisanje

    stara_knjiga=[knjige[z],nova_knjiga]
    print("\nIzmena ")
    ispisi_knjige(stara_knjiga)

    sacuvaj_knjige(knjige)
    print('%s je dodata u bazu podataka. Knjiga sifra=[%s]' %(nova_knjiga['naslov'], nova_knjiga['sifra']))
    return False

def brisanje_knjige():
    z = -1
    i = 0
    while True:
        sifra=input("\nUnesite sifru knjige koju zelite da obrisete (ukucajte 'nazad' za povratak):")
        if sifra=='nazad':
            return False
        elif sifra != '':
            greska=re.search(' ',sifra)
            if greska== None:
                break
            else:
                print("sifra ne sme da sadrzi razmak,pokusaj ponovo")
                return

    for knjiga in knjige:
        if knjiga['sifra']==sifra:
            print("Knjiga je pronadjenja")
            z=i
            break
            i+=1
        if z==-1:
            print("knjiga nije pronadjena, pokusaj ponovo!")
            if brisanje_knjige()==False:
                return False
    obrisane_knjige=[knjige[z]]
    print('\nKnjiga se brise!')
    ispisi_knjige(obrisane_knjige)
    sacuvaj_knjige(knjige)
    print('%s je dodata u bazu podataka. Knjiga sifra=[%s]' % (obrisane_knjige['naslov'], obrisane_knjige['sifra']))
    return False

