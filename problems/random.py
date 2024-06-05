from os import remove


def main():
    prices = [10, 100, 200, 300, 50, 500]
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
        
if __name__ == "__main__":
    print(removeElement([0,1,2,2,3,0,4,2], 2))