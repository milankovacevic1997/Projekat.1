from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige

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


def pretrazi_knjige(ulogovani):
    print('***' * 20)
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po kategoriji")
    print("4. Pretraga po autoru")
    print("5. Pretraga po izdavacu")
    print("6. Pretraga po opsegu cene") #ne radi
    print("0. Napusti pretragu")
    print('***' * 20)
    stavka = input("Izaberite stavku: ")
    print('***' * 20)
    knjige = []
    if stavka == '1':
        sifra = int(input("Unesite sifru: "))
        knjige = pretraga_knjiga_jednakost("sifra", sifra)
    elif stavka == '2':
        naslov = input("Unesite nalsov: ")
        knjige = pretraga_knjiga_string("naslov", naslov)
    elif stavka == '3':
        kategorija = input("Unesite kategoriju: ")
        knjige = pretraga_knjiga_string("kategorija", kategorija)
    elif stavka == '4':
        autor = input("Unesite autora: ")
        knjige = pretraga_knjiga_string("autor", autor)
    elif stavka == '5':
        izdavac = input("Unesite izdavaca: ")
        knjige = pretraga_knjiga_string("izdavac", izdavac)
    elif stavka == '6':
        cenaMin = input("Unesite minimalnu cenu: ")
        cenaMax = input("Unesite maksimalnu cenu: ")
        knjige = pretraga_knjige_opseg_cene(cenaMin,cenaMax) #NE RADIII
    elif stavka == '0':
        return
    else:
        print("Pogresan unos")
        return

    ispisi_knjige(knjige, ulogovani)

def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp

    return knjige

def pretraga_knjige_opseg_cene(cenaMin,cenaMax):
    pronadjene = []
    for knjiga in knjige:
        if knjiga['cena']<=float(cenaMax) and knjiga['cena']>=float(cenaMin):
            pronadjene.append(knjiga)
    return pronadjene

def sortirane_knjige(ulogovani):
    print('***' * 20)
    print("\n1. Sortiraj po sifri")
    print("2. Sortiraj po naslovi")
    print("3. Sortiraj po kategoriji")
    print("4. Sortiraj po autoru")
    print("5. Sortiraj po izdavacu")
    print("6. Sortiraj po ceni")
    print("0. Izlaz")
    print('***' * 20)
    stavka =input("Izaberite stavku: ")
    print('***' * 20)
    knjige = ucitaj_knjige()
    if stavka == '1':
        knjige = sortiraj_knjige("sifra")

    elif stavka == '2':
        knjige = sortiraj_knjige("naslov")

    elif stavka == '3':
        knjige = sortiraj_knjige("kategorija")

    elif stavka == '4':
        knjige = sortiraj_knjige("autor")

    elif stavka == '5':
        knjige = sortiraj_knjige("izdavac")

    elif stavka == '6':
        knjige = sortiraj_knjige("cena")

    elif stavka == '0':
        return
    else:
        print("Pogresan unos!")
        return
    ispisi_knjige(knjige,ulogovani)

def ispisi_knjige(knjige,ulogovani):
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
            if knjiga['obrisano']=="True":
                if ulogovani['tip_korisnika']=="Administrator":
                    print(za_ispis)
                else:
                    pass
            else:
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
        "kategorija": "Roman",
        "obrisano": "False"
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
    nova_knjiga['obrisano']='False'

    knjige.append(nova_knjiga)
    sacuvaj_knjige(knjige)
    print('%s je dodata u bazu podataka. Knjiga sifra=[%s]' %(nova_knjiga['naslov'], nova_knjiga['sifra']))
    return False

def izmena_knjige():
    unos = 0
    sifra = input("\nUnesi sifru knjige (unesi 'nazad' za povratak):")
    i=0

    for knjiga in knjige:
        if knjiga['sifra']==int(sifra):
            unos=1
            print("Knjiga pronadjena!")
            break
        elif sifra=='nazad':
            return False
        i+=1
    if unos==0:
        print("Knjiga nije pronadjena, pokusaj opet!")

    naslov=input("\nIzmena naslova: ")
    if naslov!='':
        knjige[i]['naslov']=naslov
    autor=input("\nIzmena autora: ")
    if autor!='':
        knjige[i]['autor']=autor
    isbn=input("\nIzmena isbn: ")
    if isbn!='':
        knjige[i]['isbn']=isbn
    izdavac=input("\nIzmena izdavaca: ")
    if izdavac!='':
        knjige[i]['izdavac']=izdavac
    try:
        broj_strana=int(input("\nIzmena broja strana:"))
        knjige[i]['broj strana']=broj_strana
    except ValueError:
        pass
    try:
        godina=int(input("\nIzmena godine: "))
        knjige[i]['godina'] = godina
    except ValueError:
        pass
    try:
        cena=float(input("\nIzmena cene: "))
        knjige[i]['cena'] = cena
    except ValueError:
        pass

    kategorija=input("\nIzmena kategorije: ")
    if kategorija!='':
        knjige[i]['kategorija'] = kategorija
    sacuvaj_knjige(knjige)
    print('%s je izmenjena u bazi podataka. Knjiga sifra=[%s]' %(knjige[i]['naslov'], knjige[i]['sifra']))
    return False

def brisanje_knjige():
    sifra=input("\nUnesite sifru knjige koju zelite da obrisete (ukucajte 'nazad' za povratak):")
    if sifra=='nazad':
        return
    else:
        for knjiga in knjige:
            if knjiga['sifra']==int(sifra):
                knjiga['obrisano']="True"
                print('%s je obrisana u bazi podataka. Knjiga sifra=[%s]' % (knjiga['naslov'], knjiga['sifra']))
        sacuvaj_knjige(knjige)





