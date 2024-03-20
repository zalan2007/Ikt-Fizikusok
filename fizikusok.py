def beolvasas(file_path):
    adatok = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            adat = line.strip().split(',')
            adatok.append(adat)
    return adatok

def felfedezesi_evszamok(adatok):
    evszamok = [int(adat[2]) for adat in adatok]
    legkorabbi = min(evszamok)
    legkesobbi = max(evszamok)
    atlag = sum(evszamok) / len(evszamok)
    return legkorabbi, legkesobbi, atlag

def fizikus_kereses(adatok, nev):
    for adat in adatok:
        if nev.lower() in adat[0].lower():
            return adat[1], adat[2]
    return None, None

def main():
    file_path = "fizikusok.txt"
    adatok = beolvasas(file_path)

    while True:
        print("\n1. Listázás")
        print("2. Legkorábbi, legkésőbbi és átlagos évszám")
        print("3. Fizikus keresése név alapján")
        print("4. Kilépés")

        valasztas = input("\nVálassz egy menüpontot: ")

        if valasztas == "1":
            print("Fájl tartalma:")
            for adat in adatok:
                print(adat[0], "-", adat[1], "-", adat[2])

        elif valasztas == "2":
            legkorabbi, legkesobbi, atlag = felfedezesi_evszamok(adatok)
            print("Legkorábbi felfedezés éve:", legkorabbi)
            print("Legkésőbbi felfedezés éve:", legkesobbi)
            print("Átlagos felfedezési év:", atlag)

        elif valasztas == "3":
            nev = input("Add meg a fizikus nevét: ")
            fizikus_neve, felfedezes_eve = fizikus_kereses(adatok, nev)
            if fizikus_neve:
                print("Felfedezés:", fizikus_neve, "-", felfedezes_eve)
            else:
                print("Nincs találat.")

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Kérlek, válassz egy érvényes menüpontot.")

if __name__ == "__main__":
    main()