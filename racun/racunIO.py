import json

datoteka = './datoteke/racun.json'

def ucitaj_racun():
    with open(datoteka, 'r') as f:
        return json.load(f)

def sacuvaj_racun(novi_racun):
    with open(datoteka, "w") as f:
        json.dump(novi_racun, f, indent=4)