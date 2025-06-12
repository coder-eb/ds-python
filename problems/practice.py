from collections import defaultdict


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
    def isAnagram(s, t):
        l = len(s)
        if l != len(t): return False
        
        letters_s = {}
        letters_t = {}
        for index in range(l):
            letters_s[s[index]] = letters_s.get(s[index], 0) + 1
            letters_t[t[index]] = letters_t.get(t[index], 0) + 1
        return letters_s == letters_t

    def isAnagram_1(s, t):
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

    def longestConsecutive(self, nums):
        numSet = set(nums)

        longest = 0
        for num in nums:
            if (num-1) in numSet:
                continue
            
            length = 0
            while (num+length) in numSet:
                length += 1
                
            longest = max(longest, length)

        return longest

    def twoSumSorted(self, numbers, target):
        left_pointer = 0
        right_pointer = len(numbers)-1

        while left_pointer < right_pointer:
            sum = numbers[left_pointer] + numbers[right_pointer]
            if sum == target:
                return [numbers[left_pointer], numbers[right_pointer]]
            elif sum > target:
                right_pointer -= 1
            else:
                left_pointer += 1

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest = 0
        left = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            longest = max(longest, right-left+1)
        return longest

    def maxSumSubArray(self, arr, k):
        max_sum = 0
        current_running_sum = 0

        for index in range(0, len(arr)):
            current_running_sum += arr[index]
            if index >= k-1:
                max_sum = max(current_running_sum, max_sum)
                current_running_sum -= arr[index - (k-1)]
        return max_sum

    def smallestSubArray(self, arr, target):
        current_window_sum = 0
        min_window_size = float('infinity')
        window_start = 0
        
        for window_end in range(0, len(arr)):
            current_window_sum += arr[window_end]

            while current_window_sum >= target:
                min_window_size = min(min_window_size, window_end-window_start+1)
                current_window_sum -= arr[window_start]
                window_start+=1

        return 0 if min_window_size == float('infinity') else min_window_size

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int):
        counter = {}

        longest_window_size = 0
        window_start = 0
        for window_end in range(0, len(s)):
            letter = s[window_end]
            counter[letter] = counter.get(letter, 0) + 1

            while len(counter.keys()) > k:
                letter = s[window_start]
                if counter[letter] == 1:
                    del counter[letter]
                else:
                    counter[letter] = counter[letter]-1
                window_start+=1
            
            longest_window_size = max(longest_window_size, window_end-window_start+1)
        return longest_window_size

    def threeSum(self, nums):
        nums = sorted(nums)
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r-=1
                elif three_sum < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}

        window_start, max_window_size = 0, 0
        for window_end, letter in enumerate(s):
            counter[letter] = counter.get(letter, 0)+1

            while ((window_end-window_start+1) - max(counter.values())) > k:
                counter[s[window_start]] -= 1
                window_start+=1
            max_window_size = max(max_window_size, window_end-window_start+1)            

        return max_window_size

    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}
        for letter in t:
            countT[letter] = countT.get(letter,0)+1

        have, need = 0, len(countT.keys()) 
        res, res_len = [-1,-1], float('infinity')

        window_start = 0
        for window_end, letter in enumerate(s):
            window[letter] = window.get(letter,0) + 1
            if letter in countT and window[letter] == countT[letter]: 
                have += 1

            while have == need: 
                if (window_end-window_start+1) <= res_len:
                    res_len = window_end-window_start+1
                    res = [window_start, window_end+1]

                letter_to_remove = s[window_start]
                window[letter_to_remove]-=1
                window_start+=1

                if letter_to_remove in countT and window[letter_to_remove] < countT[letter_to_remove]:
                    have -= 1

        return "" if res_len == float('infinity') else s[res[0]:res[1]]
    
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l+r)//2
            prod = mid * mid
            if prod == x:
                return mid
            elif prod > x:
                r = mid - 1
            else:
                l = mid + 1
        return r

    def productExceptSelf(self, nums):
        res = [1]*len(nums)
        
        prefix = 1
        for i in range(0, len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

    def isValidSudoku(self, board) -> bool:
        row_checker = [None]*len(board)
        column_checker = [None]*len(board)
        square_checker = [None]*len(board)

        for row in range(len(board)):
            row_checker[row] = set()
            for column in range(len(board[row])):
                if row == 0:
                    column_checker[column] = set()

                cell = board[row][column]
                if cell == '.':
                    continue 
                
                square = (row // 3) * 3 + column // 3
                if square_checker[square] is None:
                    square_checker[square] = set()
                
                if (
                    cell in row_checker[row]
                    or cell in column_checker[column]
                    or cell in square_checker[square]
                ):
                    return False
                else: 
                    row_checker[row].add(cell)
                    column_checker[column].add(cell)
                    square_checker[square].add(cell)
        return True
 
if __name__ == "__main__":
    problems = Problems()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(problems.isValidSudoku(board))
