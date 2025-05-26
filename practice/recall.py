from curses.ascii import isalnum


def twoSum(nums: list, target: int):
    seen = {}

    for index, num in enumerate(nums):
        remainder = target - num
        if remainder in seen:
            return [seen[remainder], index]
        else:
            seen[num] = index 
    return []

def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    
    counter1, counter2 = {}, {}
    for i in range(len(s)):
        letter1 = s[i]
        letter2 = t[i]

        counter1[letter1] = counter1.get(letter1, 0) + 1
        counter2[letter2] = counter2.get(letter2, 0) + 1
         
    return counter1 == counter2

def hasDuplicate(nums: list):
    return len(nums) != len(set(nums))

def groupAnagrams(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
            
        existing_group = groups.get(key, [])
        existing_group.append(word)
        groups[key] = existing_group
    return list(groups.values())

def isPalindrome(s: str):
    left, right = 0, len(s)-1

    while left < right:
        left_char = s[left]
        right_char = s[right]

        if not (left_char.isalnum() and right_char.isalnum()): 
            if not left_char.isalnum():
                left += 1
            else:
                right -= 1

            continue

        if left_char.lower() != right_char.lower():
            return False
        
        left += 1
        right -= 1
        
    return True

def maxProfit(prices: list):
    buyIndex, sellIndex = 0, 0
    idealBuyIndex, idealSellIndex, maxProfit = 0, 0, 0
    
    for index, price in enumerate(prices, 0):
        profit = price - prices[buyIndex]
        if price > prices[sellIndex]:
            sellIndex = index

        if profit > maxProfit:
            idealBuyIndex, idealSellIndex, maxProfit = buyIndex, sellIndex, profit
        
        if price < prices[buyIndex]: 
            buyIndex = index
    
    return [maxProfit, idealBuyIndex, idealSellIndex]

def isValid(s: str):
    stack = []
    bracketGroups = {
        "}": "{",
        "]": "[",
        ")": "(",
    }

    for bracket in s:
        # Open bracket
        if bracket not in bracketGroups:
            stack.append(bracket)
        # Closing bracket
        else:
            if len(stack) == 0: #check if closing bracket exists
                return False
            
            prevBracket = stack.pop()
            if prevBracket != bracketGroups[bracket]:
                return False

    return len(stack) == 0

def keepPlussin(digits, position, add):
    if position < 0:
        digits.insert(0, add)
        return digits

    current_digit = digits[position] + add

    if current_digit < 10:
        digits[position] = current_digit
        return digits
    else:
        remainder = current_digit % 10
        quotient = current_digit // 10

        digits[position] = remainder
        return keepPlussin(digits, position-1, quotient)

def plusOne(digits: list):
    return keepPlussin(digits, len(digits)-1, 1)

class Problems:
    def plusOne(self, digits):
        if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]

def main():
    problems = Problems()
    print(problems.plusOne([9, 9, 9]))

if __name__ == '__main__':
    main()
