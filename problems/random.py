def profit_stock(prices):
    buy = 0
    max_profit = 0
    r_buy, r_sell = 0, 0
    for sell in range(len(prices)):
        profit = prices[sell] - prices[buy]
        if profit > max_profit:
            max_profit = profit
            r_buy, r_sell = buy, sell
        if prices[sell] < prices[buy]:
            buy = sell
    return r_buy, r_sell


def main(prices):
    profits = {}

    max_profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
            profits[profit] = f"{i}, {j}"
    print(profits[max_profit])

def lengthOfLongestSubstring(s):
    letters = {}
    longest = ''
    current = ''
    for letter in s:
        if letter in letters:
            letters = {}
            letters[letter] = 1
            current = ''
            continue
        else:
            current = f'{current}{letter}'
            if len(current) > len(longest):
                longest = current
            letters[letter] = letters.get(letter, 0) + 1
    return longest

def containsNearbyDuplicate(nums, k):
    seen = {}
    for index, num in enumerate(nums):
        if num in seen and index - seen[num] <= k: return True    
        seen[num] = index
    return False

def missingNumber(nums):
    seen = {}
    for num in nums:
        seen[num] = 1
    
    for num in range(len(nums)+1):
        if num not in seen: return num
        
def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j+=1
    return nums
   
def isPalindrome(x):
    if x < 0: return False
    
    temp = x
    reversed_num = 0
    while temp:
        reversed_num = (reversed_num * 10) + temp % 10
        temp = temp // 10
    return reversed_num == x

def romanToInt(s):
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    for index in range(len(s)):
        if index < len(s)-1 and map[s[index]] < map[s[index+1]]:
            total -= map[s[index]]
        else:
            total += map[s[index]]

    return total

def remove_element(nums, val):
    target_index = 0
    for index in range(len(nums)):
        if nums[index] != val:
            nums[target_index] = nums[index]
            target_index += 1

    for index in range(target_index, len(nums)):
        nums.pop()
    return target_index

def removeElement(nums, val):
    replace_index = 0
    for num in nums:
        if num != val:
            nums[replace_index] = num
            replace_index += 1
    return nums, replace_index

def removeElement_1(nums, target):
    l = len(nums)
    curr_index = 0
    iteration = 0
    while iteration < l:
        if nums[curr_index] == target:
            del nums[curr_index]
            nums.append(target)
        else:
            curr_index+=1
        iteration += 1
    return curr_index

def isAnagram(s, t):
    l = len(s)
    if l != len(t): return False
    
    letters_s = {}
    letters_t = {}
    for index in range(l):
        letters_s[s[index]] = letters_s.get(s[index], 0) + 1
        letters_t[t[index]] = letters_t.get(t[index], 0) + 1
    return letters_s == letters_t

def isAnagram(s, t):
    alphabets = [0] * 26

    for letter in s:
        alphabets[ord(letter) - ord('a')] += 1
    for letter in t:
        alphabets[ord(letter) - ord('a')] -= 1

    for alphabet in alphabets:
        if alphabet != 0:
            return False
    return True

def groupAnagrams(strs):
    combinations = {}
    for word in strs:
        canonical = "".join(sorted(word))
        combination = combinations.get(canonical, [])
        combination.append(word)
        combinations[canonical] = combination
    return list(combinations.values())

def isPalindrome_1(s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right: 
        left_char = s[left]
        right_char = s[right]

        if not left_char.isalnum() or not right_char.isalnum(): 
            if not left_char.isalnum():
                left += 1
            if not right_char.isalnum():
                right -= 1
            continue

        if left_char.lower() != right_char.lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    prices = [500000, 10, 800, 300, 1, 00000]
    print(profit_stock(prices))
    main(prices)