"""List comprehensions - You have a list of integers from −10 to 10. Use it to create a new list that only
    contains the squares of the positive numbers that are divisible by 3."""
def list_comprehensions(i_list):
    r_integer_array = [e*e for e in i_list if (e%3==0)]
    return r_integer_array

"""Set Comprehensions - You have a text (string) with mixed upper and lower case letters and punctuation marks. 
    Extract all unique lowercase letters whose Unicode value is odd."""
def set_comprehensions(s_array):
    r_set_array = {e for e in s_array if((ord(e)%2==1) and (e.islower() and s_array.count(e)==1))}
    return r_set_array

"""Dictionary Comprehensions - Given is a list of words. Create a dictionary in which the keys are the 
    words and the values are the length of the word, but only if the word contains at least one vowel."""
def dictionary_comprehensions(w_list):
    r_dict_array = {e: len(e)  for e in w_list if (('a' in e)or('e' in e)or('i' in e)or('o' in e)or('u' in e))}
    #Ki-Verbesserte Methode
    #r_dict_array = {e: len(e) for e in w_list if any(vowel in e for vowel in 'aeiou')}
    return r_dict_array

if __name__ == "__main__":
    #List comprehension
    integer_list = list(range(-10, 11))
    print("Gegeben ist folgendes Int-Array:",integer_list,sep=" ")
    print("Herauskomt folgendes Array:", list_comprehensions(integer_list), sep=" ")
    print(" ")

    #Set Comprehensions
    string_input = 'a3"bB,7Z.z8x'
    print("Gegeben ist folgendes String-Array:",string_input,sep=" ")
    print("Herauskommt folgendes Array: ", set_comprehensions(string_input))
    print(" ")

    #Dictionary Comprehensions
    word_list = ['car', 'train', 'plane', 'boat', 'subway', 'xyz']
    print("Gegeben ist folgendes Dictionary: ", word_list, sep=" ")
    print("Herauskommt folgendes Array: ",dictionary_comprehensions(word_list),sep=" ")

