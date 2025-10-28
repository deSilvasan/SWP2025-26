
"""
Compares the color of the entered numbers (cards).
Returns true if they are all the same color, returns false if they are not all the same color.
It doesn't matter whether the numbers are in order or not.
"""
import random

def compare_colors(list_randomNumbers, color_number=4):
    for e in range(color_number):
        #Here, the numbers are compared to see if they fall within the interval.
        if all((1+(13*e)) <= n <= (13+(13*e)) for n in list_randomNumbers):
            return True
    return False

"""
It will compare whether the numbers are consecutive or not. Please note that the parameters must be passed in order. 
"""
def compare_order(list_randomNumbers):
    list_randomNumbers.sort()
    if (list_randomNumbers[len(list_randomNumbers)-1]-list_randomNumbers[0]) == 4:
        return True
    return False

"""
An ordered list must be submitted, and then random numbers are generated. You then receive a list with randomnumbers_count elements.
"""
def draw_random_numbers(numbers_list, randomnumbers_count):
    if randomnumbers_count > len(numbers_list):
        raise ValueError("randomnumbers_count cannot be greater than the list length")
    if randomnumbers_count == 0:
        return []
    random.seed(random.randint(1, len(numbers_list)))
    for e in range(randomnumbers_count):
        #random nummer is drawn
        random_number = random.randint(0,len(numbers_list)-1)
        random_number_list_element = numbers_list[random_number]
        #replace last list element with list element of random number and via versa
        numbers_list[random_number] = numbers_list[len(numbers_list)-e-1]
        numbers_list[len(numbers_list)-e-1] = random_number_list_element
    return numbers_list[-randomnumbers_count:]

"""Check whether the entire given numbers_list contains unique values (no duplicate values)."""
def is_unique(numbers_list):
    seen = set()
    for x in numbers_list:
        if x in seen:
            return False
        seen.add(x)
    return True

"""counts cards with the same value"""
def count_equal_cards(numbers_list):
    ergebnis_dict = {}
    for number in numbers_list:
        if(number<=13):
            if number not in ergebnis_dict:
                ergebnis_dict[number] = 0
            ergebnis_dict[number] += 1
        elif(number<=26):
            if number-13 not in ergebnis_dict:
                ergebnis_dict[number-13] = 0
            ergebnis_dict[number-13] += 1
        elif(number<=39):
            if number-26 not in ergebnis_dict:
                ergebnis_dict[number-26] = 0
            ergebnis_dict[number-26] += 1
        elif(number<=52):
            if number-39 not in ergebnis_dict:
                ergebnis_dict[number-39] = 0
            ergebnis_dict[number-39] += 1
    return [ergebnis_dict.values()]

"""Compares the combinations in a poker game and writes them to the given statistic_dict."""
def check_combinations_insert_statistic(randomnumbers_list, statistic_dict):
    if compare_colors(randomnumbers_list):
        if(compare_order(randomnumbers_list)):
            if(any(e%13 == 0for e in randomnumbers_list)):
                statistic_dict['RoyalFlush'] += 1
            elif(is_unique(randomnumbers_list)):
                statistic_dict['StraightFlush'] += 1
        else: statistic_dict['Flush'] += 1
    elif(any(e==4 for e in count_equal_cards(randomnumbers_list))):
        statistic_dict['FourOfAKind'] += 1
    elif(any(e==2 for e in count_equal_cards(randomnumbers_list)) and (any(e==3 for e in count_equal_cards(randomnumbers_list)))):
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