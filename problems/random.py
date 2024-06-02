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

if __name__ == "__main__":
    print(missingNumber([0,1]))