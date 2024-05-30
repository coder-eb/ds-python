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

def two_sum(nums, target):
    seen = {}

    for index in range(len(nums)):
        num = nums[index]
        remainder = target - num
        if remainder in seen:        
            return [index, seen[remainder]]
        
        seen[num] = index

    return []

def remove_duplicates(nums):
    return list(set(nums))

def has_unique_chars(word):
    # Solution 1
    seen = set()
    for letter in word:
        if letter in seen:
            return False
        seen.add(letter)
    return True

    # Solution 2
    return len(string) == len(set([letter for letter in string]))

def find_pairs(arr1, arr2, target):
    pairs = list()

    arr2 = set(arr2)
    for num in arr1:
        remainder = target - num
        if remainder in arr2:
            pairs.append((num, remainder))
    return pairs

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_seq = 0

    for num in nums:
        if num - 1 in num_set:
            continue

        seq = 1
        temp = num
        while(temp+1 in num_set):
            seq += 1
            temp += 1
        
        if seq > longest_seq: 
            longest_seq = seq
    return longest_seq

def subarray_sum(nums, k):
    sums = {0: -1}
    total = 0
    for index, num in enumerate(nums):
        total+=num
        remainder = total - k
        if remainder in sums:
            return [sums[remainder]+1, index]
        sums[total] = index
    return []

        