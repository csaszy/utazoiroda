import sys

def main():
    prices = []
    count = 0

    # az adatok beolvasása és tárolása
    with sys.stdin as file:
        next(file)
        for line in file:
            tokens = line.strip().split(' ')
            prices.append(int(tokens[1]))
    
    # létrehozunk egy dictionary-t, melyben a kulcsok a különféle 
    # árak lesznek (mivel minden kulcs csak egyszer fordulhat elő), ...
    d = dict().fromkeys(prices, 0) 

    # ... majd ezután a for ciklus után minden kulcsnak az értéke,
    # a aktuális ár előfordulásának száma lesz ...
    for price in prices:
        d[price] += 1
    
    # ... és ahol a kulcs értéke 1, az annyit jelenti, hogy az az aktuális ár csak egyszer 
    # fordult elő a listában -> tehát "egyértelműen meg lehet mondani, hogy melyik városba 
    # lehet utazni ennyiért" 
    for v in d.values():
        if v == 1: 
            count += 1

    print(count)

if __name__ == "__main__":
    main()