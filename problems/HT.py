def item_in_common(list1, list2):
    my_dict = {}
    for item in list1:
        my_dict[item] = True
    for item in list2:
        if item in my_dict:
            return True
        
    return False

def first_non_repeating_char(word):
    letters = {}
    for letter in word:
        letters[letter] = letters.get(letter, 0) + 1

    for letter in word:
        if letters[letter] == 1:
            return letter

def find_duplicates(numbers):
    seen = {}
    duplicates = []
    for number in numbers:
        if number in seen:
            duplicates.append(number)
            continue
        seen[number] = None
    return duplicates

def group_anagrams(strings):
    groups = {}

    for string in strings:
        sorted_str = "".join(sorted(string))

        group = groups.get(sorted_str, [])
        group.append(string)
        groups[sorted_str] = group

    return list(groups.values())