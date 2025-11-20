import sys, random

"""fills a list up to an upper limit"""
def fill_array_numbers(upper_limit):
    # Return a list containing numbers from 1 up to upper_limit (inclusive)
    return list(range(0, upper_limit))

"""
Compares the color of the entered numbers (cards).
Returns true if they are all the same color, returns false if they are not all the same color.
It doesn't matter whether the numbers are in order or not.
"""
def compare_colors(list_randomNumbers):
    # Calculate the color bucket of the first card by integer division by 13
    ganzzahl = list_randomNumbers[0]//13
    for e in list_randomNumbers:
        # Check if all cards belong to the same color bucket
        if((e//13) != ganzzahl):
            return False
    return True

"""
It will compare whether the numbers are consecutive or not. Please note that the parameters must be passed in order. 
"""
def compare_order(list_randomNumbers):
    sortiert = sorted(list_randomNumbers)
    for i in range(len(sortiert) - 1):
        # Check if difference between consecutive items is exactly 1
        if sortiert[i + 1] - sortiert[i] != 1:
            return False
    return True

"""
An ordered list must be submitted, and then random numbers are generated. You then receive a list with randomnumbers_count elements.
"""
def draw_random_numbers(numbers_list, randomnumbers_count):
    for e in range(randomnumbers_count):
        #random nummer is drawn
        random_number = random.randint(0,len(numbers_list)-1)
        random_number_list_element = numbers_list[random_number]
        #replace last list element with list element of random number and via versa
        numbers_list[random_number] = numbers_list[len(numbers_list)-e-1]
        numbers_list[len(numbers_list)-e-1] = random_number_list_element
    # return last randomnumbers_count elements as randomly drawn cards
    return numbers_list[-randomnumbers_count:]

"""Check whether the entire given numbers_list contains unique values (no duplicate values)."""
def is_unique(numbers_list):
    seen = set()
    for x in numbers_list:
        # If already seen, list is not unique
        if x in seen:
            return False
        seen.add(x)
    return True

"""counts cards with the same value, but not the same color. gives back a list with numbers and their frequency in the array"""
def count_equal_cards(numbers_list):
    ergebnis_dict = {}
    for number in numbers_list:
        # Maps card IDs to ranks within a suit (0 to 12) by subtracting multiples of 13
        if(number<=12):
            if number not in ergebnis_dict:
                ergebnis_dict[number] = 0
            ergebnis_dict[number] += 1
        elif(number<=25):
            if number-13 not in ergebnis_dict:
                ergebnis_dict[number-13] = 0
            ergebnis_dict[number-13] += 1
        elif(number<=38):
            if number-26 not in ergebnis_dict:
                ergebnis_dict[number-26] = 0
            ergebnis_dict[number-26] += 1
        elif(number<=51):
            if number-39 not in ergebnis_dict:
                ergebnis_dict[number-39] = 0
            ergebnis_dict[number-39] += 1
    # Return the counts of each card rank across different suits
    return list(ergebnis_dict.values())

"""Compares the combinations in a poker game and writes them to the given statistic_dict."""
def check_combinations_insert_statistic(randomnumbers_list, statistic_dict):
    if compare_colors(randomnumbers_list):
        if(compare_order(randomnumbers_list)):
            if(any((e-1)%13 == 0 for e in randomnumbers_list)):
                statistic_dict['RoyalFlush'] += 1
            elif(is_unique(randomnumbers_list)):
                statistic_dict['StraightFlush'] += 1
        else: statistic_dict['Flush'] += 1
    elif(any(e==4 for e in count_equal_cards(randomnumbers_list))):
        statistic_dict['FourOfAKind'] += 1
    elif(any(e==2 for e in count_equal_cards(randomnumbers_list))
         and (any(e==3 for e in count_equal_cards(randomnumbers_list)))):
        statistic_dict['FullHouse'] += 1
    elif(compare_order(randomnumbers_list)):
        statistic_dict['Straight'] += 1
    elif(any(e==3 for e in count_equal_cards(randomnumbers_list))):
        statistic_dict['ThreeOfAKind-Set'] += 1
    elif(count_equal_cards(randomnumbers_list).count(2)==2):
        statistic_dict['TwoPair'] += 1
    elif(count_equal_cards(randomnumbers_list).count(2)==1):
        statistic_dict['OnePair'] += 1
    else: statistic_dict['HighCard'] += 1

if __name__ == "__main__":
    poker_cards_count = 52
    cards_drawn = 5
    moves_total = 0
    statistic_dict = {'HighCard':0, 'OnePair':0, 'TwoPair':0, 'ThreeOfAKind-Set':0, 'Straight':0, 'Flush':0,
                      'FullHouse':0, 'FourOfAKind':0, 'StraightFlush':0, 'RoyalFlush':0}
    wahrscheinlichkeit_dict = {'HighCard': 50.1, 'OnePair': 42.3, 'TwoPair': 4.75, 'ThreeOfAKind-Set': 2.11, 'Straight': 0.392, 'Flush': 0.197,
                      'FullHouse': 0.144, 'FourOfAKind': 0.0240, 'StraightFlush': 0.00139, 'RoyalFlush': 0.000154}
    #if there are any arguments given
    if len(sys.argv) > 1:
        moves_total = int(sys.argv[1])
    #if there aren't any arguments given
    else:
        try:
            print("Moves total: ")
            moves_total = int(input())
        except:
            sys.exit(0)

    print("Total Poker cards:", poker_cards_count, sep=" ")
    print("cards drawn in each round", cards_drawn, sep=" ")
    print("total played rounds", moves_total, sep=" ")

    for e in range(moves_total):
        filled_list = fill_array_numbers(poker_cards_count)
        randomnumber_list = draw_random_numbers(filled_list, cards_drawn)
        check_combinations_insert_statistic(randomnumber_list, statistic_dict)

    #prozentuelle Anteile
    procentual_result = {}
    for e in statistic_dict:
        if(statistic_dict[e] != 0):
            procentual_result[e] = (statistic_dict[e]/moves_total)*100
        else: procentual_result[e] = 0
    print("prozentuale Ergebnisse" , procentual_result, sep=" ")
    print("wahrscheinlichkeiten bei 1000 Zügen", wahrscheinlichkeit_dict, sep=" ")