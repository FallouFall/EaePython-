from collections import Counter

def search_max_char(text):
    characters = Counter(text.replace(' ', ''))
    return characters.most_common(1)


def separate_odd_even(nums):
    # Using Pyton Compression lIST .NO loop with lamda expression
    # Possible to use Numpay with condition where,if ?
    listSeparated = []
    listOdd = [this for this in nums if this % 2 == 0]
    listEven = [this for this in nums if this % 2 != 0]
    listSeparated.append(listOdd)
    listSeparated.append(listEven)
    return listSeparated
