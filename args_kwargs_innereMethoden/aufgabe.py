def sum_square_numbers(*numbers):
    def pow2(zahl):
        return zahl* zahl
    result_list = [pow2(z) for z in numbers]
    return sum(result_list)

print(sum_square_numbers(1,2,3,4,5))

def addiere(*args):
    print("args ist vom Typ:", type(args))
    print("Inhalt:", args)
    return sum(args)

ergebnis = addiere(1, 2, 3, 4)
print("Summe:", ergebnis)

def person_info(**kwargs):
    print("kwargs ist vom Typ:", type(kwargs))
    print("Inhalt:", kwargs)

person_info(name="Olivia", alter=25, land="Österreich")
