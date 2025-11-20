def compare_numbers(eingabe_liste, val):
    ergebnis_list = []
    for e in eingabe_liste:
        for x in eingabe_liste:
            index_e = eingabe_liste.index(e)
            index_x = eingabe_liste.index(x)
            if((e+x)==val) and not any(a for a in ergebnis_list if (e == a[0]) or (x == a[0])) and not (index_x == index_e):
                ergebnis_tuple = (e,x)
                ergebnis_list.append(ergebnis_tuple)
    return set(ergebnis_list)

def print_result(eingabe_liste):
    if(len(eingabe_liste)>0):
        print(eingabe_liste)
    else:
        print("Keine Ergebnisse in liste")

def main():
    nummern_liste = [2,4,5,8,10,2,2,2,5,6,4,7]
    print_result(compare_numbers(nummern_liste,12))

if __name__ == "__main__":
    main()