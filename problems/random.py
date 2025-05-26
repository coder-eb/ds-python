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

def fibonacci(n):
    items = [0, 1]
    for i in range(2, n+1):
        new_item = items[-1] + items[-2]
        items.append(new_item)
    return items[n]

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

def isValid(s):
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = []
    for bracket in s:
        if bracket in pairs.keys():
            expected_bracket = pairs[bracket]
            if not stack or stack.pop() != expected_bracket:
                return False
        else:
            stack.append(bracket)
    return len(stack) == 0

def longest_consecutive_sequence(nums):
    nums = set(nums)
    longest_sequence = current_sequence = 0
    for num in nums:
        current_sequence = 1
        if num - 1 not in nums:
            while num + 1 in nums:
                current_sequence += 1
                num = num + 1
        longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence    

def longest_consecutive_sequence_by_order(nums):
    if not len(nums): return 0

    prev_num = nums[0]
    longest_seq = current_seq = 1
    for index in range(1, len(nums)):
        current_num = nums[index]

        if ((current_num - 1 == prev_num) or (current_num == prev_num)):
            current_seq += 1
        else:
            current_seq = 1
        longest_seq = max(current_seq, longest_seq)
        prev_num = current_num
    return longest_seq     

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            number = stack.pop(-2) + stack.pop(-1)
        elif token == '-':
            number = stack.pop(-2) - stack.pop(-1)
        elif token == '*':
            number = stack.pop(-2) * stack.pop(-1)
        elif token == '/':
            number = stack.pop(-2) / stack.pop(-1)
        else:
            number = token
        stack.append(int(number))

    return stack.pop()

def __evalRPNr(orig, new):
    if new[-1] in ['+', '-', '*', '/']:
        token = new.pop()
        number2 = new.pop()
        number1 = new.pop()
        if token == '+':
            number = number1 + number2
        elif token == '-':
            number = number1 - number2
        elif token == '*':
            number = number1 * number2
        else:
            number = number1 / number2

        number = int(number)
        if len(orig) == 0:
            return number
        
        new = new + [number]
    else:
        pass

    if orig[0] in ['+', '-', '*', '/']:
        new_1 = orig[0]
    else:
        new_1 = int(orig[0])

    return __evalRPNr(orig[1:], new+[new_1])

def evalRPNr(orig):
    return __evalRPNr(orig[1:], [int(orig[0])])

def airline():
    tickets = [
        ["New York", "Washington"],
        ["Seattle", "Memphis"],
        ["Hawaii", "New York"],
        ["Memphis", "Hawaii"],
    ]

    map = {}
    for source, destination in tickets:
        map[source] = destination

    start = set(map.keys()).difference(set(map.values())).pop()
    route = []
    while start:
        route.append(start)
        start = map.get(start)
    return route

class Problems:
    def topKFrequent(self, nums: list, k: int):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1
        
        freq = [[] for i in range(len(nums)+1)]
        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for number in freq[i]:
                res.append(number)
                if len(res) == k:
                    return res

if __name__ == "__main__":
    problems = Problems()
    print(problems.topKFrequent([5,7,7], 2))
