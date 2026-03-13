import random

class ChainLink():
    value = None
    nextLink = None

    def __init__(self, v):
        self.value = v

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        #self.current Zeiger auf aktuelle Element der verketteten Liste
        if self.current is None:
            raise StopIteration

        value = self.current
        self.current = self.current.nextLink
        return value

#Chain zwischen zwei Chains einfügen
def addChainInBetweenLinks(firstElement, indexToInsert, value):
    index = 0
    for elem in firstElement:
        if index == indexToInsert:
            insertedLink = ChainLink(value)
            insertedLink.nextLink = elem.nextLink
            elem.nextLink = insertedLink
            break
        index += 1

#Chain zwischen zwei Chains löschen
def removeChainInBetweenLinks(firstElement, indexToRemove):
    index = 0
    for elem in firstElement:
        if index+1 == indexToRemove:
            nextElem = elem.nextLink
            elem.nextLink = nextElem.nextLink
            break
        index += 1

#Methode um die Länge von der verketteten Liste bekommen
def getLinkLength(firstElement):
    count = 0
    for _ in firstElement:
        count += 1
    return count

#ein Chain link wird am Ende der Liste hinzugefügt
def addLinkEnd(firstElement, elem):
    for element in firstElement:
        if(type(element.nextLink) != ChainLink):
            element.nextLink = elem
            break

#alle Elemente ausgeben
def printAllElements():
    for elem in firstElem:
        print(elem.value)

if __name__ == "__main__":
    random.Random(15)
    firstElem = ChainLink(random.randrange(1, 10))
    link_element_count = 10
    currentElem = firstElem
    for i in range(link_element_count):
        newLink = ChainLink(random.randrange(1, 10))
        currentElem.nextLink = newLink
        currentElem = newLink
        random.Random(15)
    print("List of Elements: ")
    printAllElements()
    length =  getLinkLength(firstElem)
    print(f"Lenght of ChainLink: {length}")
    addLinkEnd(firstElem, ChainLink(random.randrange(1, 10)))
    print("current list with new element at end")
    printAllElements()
    length = getLinkLength(firstElem)
    print(f"Lenght of ChainLink: {length}")
    addChainInBetweenLinks(firstElem, 3, random.randrange(1, 10))
    print("add element in chain")
    printAllElements()
    removeChainInBetweenLinks(firstElem, 5)
    print("remove element in chain")
    printAllElements()