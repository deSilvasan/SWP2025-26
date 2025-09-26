
a = 2
b = 4

i = 1
while i <= 3:
    if a==b:
        print("a ist b")
    elif a<b:
        print("a ist kleiner als b")
    else:
        print("a ist größer als b")
    i = i + 1

essen = ["Schnitzelsemmel", "Jausenbrot", "Apfel", "Hamburger", "Lasagne"]
try:
    for element in essen:
        print("Silvana isst:", element, sep=" ")
        if(element=="Apfel"):
            continue
        if(element=="Hamburger"):
            break
        if(element=="Schnitzelsemmel"):
            pass
#Handling of exception
except Exception as e:
    print(e)
#execute if no exception
else:
    print("Silvana hat alles aufgegessen")
finally:
    print("Silvana hat keinen Hunger mehr")