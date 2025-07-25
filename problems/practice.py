from collections import deque
from typing import List, Optional
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from problems.CustomDS import ListNode, TreeNode, list_to_tree, find_node

def fibonacci(n):
    items = [0, 1]
    for i in range(2, n+1):
        new_item = items[-1] + items[-2]
        items.append(new_item)
    return items[n]

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
    
    def maxArea(self, heights):
        max_area = 0
        
        l, r = 0, len(heights)-1

        while l < r:
            area = min(heights[r], heights[l]) * (r-l)
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_area

    def trap(self, height) -> int:
        if not height:
            return 0
        trapped_water = 0

        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l+=1
                left_max = max(left_max, height[l])
                trapped_water += left_max - height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])
                trapped_water+= right_max - height[r]

        return trapped_water

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            encoded_w = str(len(word)) + "#" + word
            res += encoded_w
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            
            word_len = int(s[i:j]) 
            res.append(s[j+1:j+1+word_len])
            i = j+1+word_len
        return res

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches=0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            add_index = ord(s2[r]) - ord('a')
            s2_count[add_index] += 1
            if s1_count[add_index] == s2_count[add_index]:
                matches+=1
            elif s1_count[add_index] == s2_count[add_index]-1:
                matches-=1

            remove_index = ord(s2[l]) - ord('a')
            s2_count[remove_index] -= 1
            if s1_count[remove_index] == s2_count[remove_index]:
                matches += 1
            elif s1_count[remove_index] == s2_count[remove_index]+1:
                matches-=1

            l+=1

        return matches == 26
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = []

        l=0
        for r in range(0, len(nums)):
            while len(deq) > 0 and deq[-1] < nums[r]:
                deq.pop()
            deq.append(nums[r])

            if (r-l+1) > k:
                if deq[0] == nums[l]:
                    deq.popleft()
                l+=1

            if r >= k-1:
                res.append(deq[0])
            
        return res

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operation:
                number = token
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+':
                    number = num1 + num2
                elif token == '-':
                    number = num1 - num2
                elif token == '*':
                    number = num1 * num2
                elif token == '/':
                    number = num1 / num2
            stack.append(int(number))
        return stack.pop()

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)   
        for cur_i, cur_t in enumerate(temperatures):
            while len(stack) and cur_t > stack[-1][1]:
                prev_i, prev_t = stack.pop()
                answer[prev_i] = cur_i - prev_i
            stack.append([cur_i, cur_t])
        return answer

    # neetcode - stack approach
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position,speed) for position, speed in zip(position, speed)], reverse=True)
        stack = []

        for position, speed in cars:
            time = (target - position)/speed
            stack.append(time)
            if len(stack)>1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
    # algomonster - no stack approach
    def carFleet_1(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position,speed) for position, speed in zip(position, speed)], reverse=True)

        count = 0
        prev_time = 0
        for position, speed in cars:
            time = (target - position)/speed
            if time > prev_time:
                count+=1
                prev_time = time
        return count

    def generateParenthesis(self, n: int) -> List[str]:
        brackets = []
        def bracketBuilder(string, open, close):
            if (open == n) and (close == n):
                brackets.append(string)
                return
            
            if open == close:
                bracketBuilder(string+"(", open+1, close)
            elif open > close:
                if open < n:
                    bracketBuilder(string+"(",open+1,close)
                bracketBuilder(string+")",open,close+1)

        bracketBuilder("", 0, 0)
        return brackets
    
    def largestRectangleArea_brute(self, heights: List[int]) -> int:
        largest_rectangle = 0
        for cur_index, cur_height in enumerate(heights):
            prev_small, next_small = None, None
            for i in range(cur_index-1, -1, -1):
                if heights[i] < cur_height:
                    prev_small = i
                    break
            for i in range(cur_index+1, len(heights)):
                if heights[i] < cur_height:
                    next_small = i
                    break
            
            if prev_small is None:
                prev_small = -1
            if next_small is None:
                next_small = len(heights)

            cur_rectangle = (next_small-prev_small-1)*cur_height
            largest_rectangle = max(cur_rectangle, largest_rectangle)

        return largest_rectangle
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for cur_index, cur_height in enumerate(heights):
            start = cur_index
            while stack and stack[-1][1] > cur_height:
                prev_index, prev_height = stack.pop()
                area = prev_height * (cur_index - prev_index)
                max_area = max(max_area, area)
                start = prev_index
            stack.append([start, cur_height])

        for start, cur_height in stack:
            max_area = max(max_area, cur_height * (len(heights) - start))

        return max_area

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1]*len(nums)

        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                res[stack.pop()] = nums[i%n]
            if i < n:
                stack.append(i)
        return res

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if -a > stack[-1]:
                    stack.pop()
                    continue

                if -a == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack

    def sumSubarrayMins_self(self, arr: List[int]) -> int:
        MOD = 10**9+7
        stack = []
        totalSum = 0
        currentSum = 0
        for num in arr:
            popped = 0
            while stack and stack[-1] > num:
                currentSum-=stack.pop()
                popped+=1

            for i in range(0,popped+1):
                stack.append(num)
                currentSum+=num

            totalSum += currentSum
        return totalSum % MOD

    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = [0]*len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1] if stack else -1
            res[i] = res[j] + (i-j)*arr[i]

            stack.append(i)
            
        return sum(res) % (10**9+7)
    
    def maximumSubarraySum_self(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        
        counter = {}
        have_letters = 0
        maxSum, currentSum = 0, 0
        
        l=0
        for r in range(0, len(nums)):
            num = nums[r]
            if counter.get(num,0) == 0:
                have_letters+=1
                currentSum+=num
            elif counter.get(num,0) == 1:
                have_letters-=1
                currentSum-=num

            counter[num] = counter.get(num, 0)+1
            
            
            if r+1 >= k:
                if have_letters == k:
                    maxSum = max(maxSum, currentSum)

                num = nums[l]
                counter[num]-=1
                if counter[num] == 0:
                    have_letters-=1
                    currentSum-=num
                elif counter[num] == 1:
                    have_letters+=1
                    currentSum+=num
                l+=1
            
        return maxSum

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        max_sum, current_sum = 0, 0
        l = 0
        for r in range(len(nums)):
            while nums[r] in seen:
                current_sum -= nums[l]
                seen.remove(nums[l])
                l+=1
            
            seen.add(nums[r])
            current_sum += nums[r]
            if (r - l + 1) == k:
                max_sum = max(max_sum, current_sum)
                current_sum -= nums[l]
                seen.remove(nums[l])
                l+=1
        return max_sum

    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for gas_found in nums:
            if gas < 0:
                return False
            
            gas = max(gas, gas_found)
            gas -= 1
        return True

    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        l, r, i = 0, len(nums)-1, len(nums)-1
        while l <= r:
            if (nums[l] * nums[l]) > (nums[r] * nums[r]):
                res[i] = nums[l] * nums[l]
                l+=1
            else:
                res[i] = nums[r] * nums[r]
                r-=1
            i-=1
        return res

    def moveZeroes(self, nums: List[int]) -> None:
        l = r = 0
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l+=1
            r+=1
        return nums

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 else list2

        return dummy.next
    
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] != val:
                l+=1
        return l
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l, r, i = m-1, n-1, m+n-1
        while l >= 0 and r >= 0:
            if nums1[l] > nums2[r]:
                nums1[i] = nums1[l]
                l-=1
            else:
                nums1[i] = nums2[r]
                r-=1
            i-=1
        
        while r >= 0:
            nums1[i] = nums2[r]
            i-=1
            r-=1
        
        return nums1

    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_index = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[min_buy_index]
            max_profit = max(max_profit, profit)

            if prices[i] < prices[min_buy_index]:
                min_buy_index = i

        return max_profit

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            
            if target > nums[m]:
                l=m+1
            else:
                r=m-1
        return -1

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            temp = nums[left:right+1]
            mid = left + (right-left)//2
            if right - left == 1:
                return min(nums[left], nums[right])

            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid
        return nums[left]

    def candies(self, ratings):
        candies = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)

    def searchRotated(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = left + (right - left)//2
            if target == nums[middle]:
                return middle
            
            visualize = nums[left],nums[middle],nums[right]
            if nums[middle] >= nums[left]:
                if (target <= nums[middle]) and (target >= nums[left]):
                    right = middle-1
                else:
                    left = middle+1
            else:
                if (target >= nums[middle]) and (target <= nums[right]):
                    left = middle+1
                else:
                    right = middle-1
        return -1

    def searchRotatedII(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = left + (right - left)//2
            if target == nums[middle]:
                return True

            if nums[middle] >= nums[left]:
                if nums[middle] == nums[left]:
                    left+=1
                elif (target <= nums[middle]) and (target >= nums[left]):
                    right = middle-1
                else:
                    left = middle+1
            else:
                if nums[middle] == nums[right]:
                    right-=1
                elif (target >= nums[middle]) and (target <= nums[right]):
                    left = middle+1
                else:
                    right = middle-1
        return False

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        slow, fast = start, head
        
        for _ in range(n):
            fast = fast.next
        
        while fast:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return start.next

    def reorderList_leetcode(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2
        return head

    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        node = head
        while node:
            stack.append(node)
            node=node.next

        length = len(stack)
        dummy = ListNode(0,head)
        current = dummy.next
        for _ in range(0, length//2):
            next = current.next
            current.next = stack.pop()
            current.next.next = next
            current = next
        current.next = None
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists
            
        return lists[0]

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        a_val = root.val 
        left_length = self.maxDepth(root.left)
        right_length = self.maxDepth(root.right)
        max_length = max(left_length, right_length)
        return 1+max_length
    
        res = 0
        stack = [[root,1]]
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])
        return res

        level = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
        return level
        
    def __bfs(self, node: Optional[ListNode], current_sum):
        if node is None:
            print(current_sum)
            return None

        self.__bfs(node.left, current_sum+1)
        self.__bfs(node.right, current_sum+1)
        return
    
    def bfs(self, root: Optional[TreeNode]) -> int:
        self.__bfs(root, 0)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def dfs(node, height):
            if node is None:
                return 0

            left_height = dfs(node.left, height)
            right_height = dfs(node.right, height)
            self.max_diameter = max(self.max_diameter, left_height+right_height)

            return 1+max(left_height,right_height)

        dfs(root,0)
        return self.max_diameter

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
                    
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if root == p or root == q:
            return root
        
        if left is None and right is None:
            return None
        if left is not None and right is not None:
            return root
        # if left is not None and right is None: 
        if left is not None:
            return left
        # if left is None and right is not None:
        else:
            return right
    
if __name__ == "__main__":
    problems = Problems()
    root = list_to_tree([6,2,8,0,4,7,4])
    p = find_node(root, 2)
    q = find_node(root, 4)
    print(problems.lowestCommonAncestor(root, p, q))
