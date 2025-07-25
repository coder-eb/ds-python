import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from problems.CustomDS import ListNode, find_node, linked_to_list, list_to_linked, list_to_tree
from problems.practice import Problems, airline, containsNearbyDuplicate, evalRPN, evalRPNr, fibonacci, isPalindrome, longest_consecutive_sequence_by_order, missingNumber, romanToInt

import pytest

@pytest.fixture
def problems():
    return Problems()

def test_lengthOfLongestSubstringKDistinct_basic(problems):
    assert problems.lengthOfLongestSubstringKDistinct("eceba", 2) == 3  # "ece"
    assert problems.lengthOfLongestSubstringKDistinct("aa", 1) == 2     # "aa"
    assert problems.lengthOfLongestSubstringKDistinct("abcadcacacaca", 3) == 11  # "cadcacacaca"

def test_lengthOfLongestSubstringKDistinct_empty(problems):
    assert problems.lengthOfLongestSubstringKDistinct("", 2) == 0

def test_lengthOfLongestSubstringKDistinct_k_zero(problems):
    assert problems.lengthOfLongestSubstringKDistinct("abc", 0) == 0

def test_lengthOfLongestSubstringKDistinct_k_greater_than_unique(problems):
    assert problems.lengthOfLongestSubstringKDistinct("aabbcc", 10) == 6

def test_lengthOfLongestSubstringKDistinct_all_same(problems):
    assert problems.lengthOfLongestSubstringKDistinct("aaaaaa", 1) == 6
    assert problems.lengthOfLongestSubstringKDistinct("aaaaaa", 2) == 6

def test_lengthOfLongestSubstringKDistinct_example(problems):
    assert problems.lengthOfLongestSubstringKDistinct("AAAHHIBC", 2) == 5  # "AAAHH"

def test_twoSumSorted_basic(problems):
    assert problems.twoSumSorted([1, 2, 3, 4], 3) == [1, 2]
    assert problems.twoSumSorted([2, 7, 11, 15], 9) == [2, 7]
    assert problems.twoSumSorted([-3, 0, 3, 4], 0) == [-3, 3]
    assert problems.twoSumSorted([1, 2], 3) == [1, 2]

def test_twoSumSorted_negative(problems):
    assert problems.twoSumSorted([-10, -3, 0, 5, 9], -13) == [-10, -3]

def test_twoSumSorted_large(problems):
    arr = list(range(1, 1001))
    assert problems.twoSumSorted(arr, 1999) == [999, 1000]

def test_threeSum_example1(problems):
    result = problems.threeSum([-1,0,1,2,-1,-4])
    expected = [[-1,-1,2], [-1,0,1]]
    assert sorted([sorted(triplet) for triplet in result]) == sorted([sorted(triplet) for triplet in expected])

def test_threeSum_example2(problems):
    result = problems.threeSum([0,1,1])
    expected = []
    assert result == expected

def test_threeSum_example3(problems):
    result = problems.threeSum([0,0,0])
    expected = [[0,0,0]]
    assert result == expected

def test_threeSum_no_triplets(problems):
    result = problems.threeSum([1,2,3,4,5])
    expected = []
    assert result == expected

def test_threeSum_duplicates(problems):
    result = problems.threeSum([-2,0,0,2,2])
    expected = [[-2,0,2]]
    assert sorted([sorted(triplet) for triplet in result]) == sorted([sorted(triplet) for triplet in expected])
    
def test_isAnagram_true():
    assert Problems.isAnagram("listen", "silent") is True
    assert Problems.isAnagram("anagram", "nagaram") is True
    assert Problems.isAnagram("", "") is True

def test_isAnagram_false():
    assert Problems.isAnagram("rat", "car") is False
    assert Problems.isAnagram("hello", "helloo") is False
    assert Problems.isAnagram("a", "A") is False  # case-sensitive

def test_isAnagram_1_true():
    assert Problems.isAnagram_1("listen", "silent") is True
    assert Problems.isAnagram_1("anagram", "nagaram") is True

def test_isAnagram_1_false():
    assert Problems.isAnagram_1("rat", "car") is False
    assert Problems.isAnagram_1("abc", "def") is False

def test_groupAnagrams_basic():
    result = Problems.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    # Compare as sets for unordered groups
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])

def test_groupAnagrams_empty():
    assert Problems.groupAnagrams([]) == []

def test_isPalindrome_1_true():
    assert Problems.isPalindrome_1("A man, a plan, a canal: Panama") is True
    assert Problems.isPalindrome_1("racecar") is True
    assert Problems.isPalindrome_1("") is True

def test_isPalindrome_1_false():
    assert Problems.isPalindrome_1("hello") is False
    assert Problems.isPalindrome_1("race a car") is False

def test_isValid_true():
    assert Problems.isValid("()") is True
    assert Problems.isValid("()[]{}") is True
    assert Problems.isValid("{[]}") is True

def test_isValid_false():
    assert Problems.isValid("(]") is False
    assert Problems.isValid("([)]") is False
    assert Problems.isValid("(((") is False

def test_topKFrequent_basic(problems):
    assert sorted(problems.topKFrequent([1,1,1,2,2,3], 2)) == [1,2]
    assert problems.topKFrequent([1], 1) == [1]

def test_topKFrequent_ties(problems):
    # All numbers appear once, k=2, should return any 2 numbers
    result = problems.topKFrequent([1,2,3,4], 2)
    assert len(result) == 2
    assert set(result).issubset({1,2,3,4})

def test_longestConsecutive_basic(problems):
    assert problems.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert problems.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert problems.longestConsecutive([]) == 0

def test_longestConsecutive_single(problems):
    assert problems.longestConsecutive([10]) == 1

def test_lengthOfLongestSubstring_basic(problems):
    assert problems.lengthOfLongestSubstring("abcabcbb") == 3
    assert problems.lengthOfLongestSubstring("bbbbb") == 1
    assert problems.lengthOfLongestSubstring("pwwkew") == 3
    assert problems.lengthOfLongestSubstring("") == 0

def test_maxSumSubArray_basic(problems):
    assert problems.maxSumSubArray([2,1,5,1,3,2], 3) == 9
    assert problems.maxSumSubArray([2,3,4,1,5], 2) == 7

def test_maxSumSubArray_k_equals_len(problems):
    arr = [1,2,3,4]
    assert problems.maxSumSubArray(arr, 4) == sum(arr)

def test_smallestSubArray_basic(problems):
    assert problems.smallestSubArray([2,1,5,2,3,2], 7) == 2
    assert problems.smallestSubArray([2,1,5,2,8], 7) == 1

def test_smallestSubArray_no_valid(problems):
    assert problems.smallestSubArray([1,1,1,1], 10) == 0

def test_characterReplacement_basic(problems):
    assert problems.characterReplacement("XYYX", 2) == 4  # Replace both X or both Y

def test_characterReplacement_example2(problems):
    assert problems.characterReplacement("AAABABB", 1) == 5  # Replace one B to get "AAAAA" or "BBBBB"

def test_characterReplacement_no_replacements_needed(problems):
    assert problems.characterReplacement("AAAA", 2) == 4  # Already all same

def test_characterReplacement_k_zero(problems):
    assert problems.characterReplacement("AABABBA", 0) == 2  # Longest block of same char is "AA" or "BB"

def test_characterReplacement_all_unique(problems):
    assert problems.characterReplacement("ABCDE", 2) == 3  # Replace any two to match a third

def test_characterReplacement_entire_string(problems):
    assert problems.characterReplacement("ABCD", 4) == 4  # Can make all same

def test_characterReplacement_single_char(problems):
    assert problems.characterReplacement("A", 0) == 1

def test_characterReplacement_long_run(problems):
    assert problems.characterReplacement("AABABBA", 1) == 4  # Replace one B to get "AABA" or "ABBA"

def test_minWindow_example1(problems):
    assert problems.minWindow("ADOBECODEBANC", "ABC") == "BANC"

def test_minWindow_example2(problems):
    assert problems.minWindow("a", "a") == "a"

def test_minWindow_example3(problems):
    assert problems.minWindow("a", "aa") == ""

def test_minWindow_no_window(problems):
    assert problems.minWindow("abcdef", "xyz") == ""

def test_minWindow_full_string(problems):
    assert problems.minWindow("abc", "abc") == "abc"

def test_minWindow_duplicates_in_t(problems):
    assert problems.minWindow("aaflslflsldkalskaaa", "aaa") == "aaa"

def test_minWindow_case_sensitive(problems):
    assert problems.minWindow("aAbBcC", "ABC") == "AbBcC"

def test_minWindow_multiple_possible(problems):
    assert problems.minWindow("abdabca", "abc") == "bca"

def test_minWindow_duplicate_letters(problems):
    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"
    # The minimal window containing a, b, c, d, d is "abbbbbcdd"
    assert problems.minWindow(s, t) == "abbbbbcdd"

def test_valid_sudoku_true(problems):
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
    assert problems.isValidSudoku(board) is True

def test_valid_sudoku_false(problems):
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert problems.isValidSudoku(board) is False

def test_valid_sudoku_empty(problems):
    board = [["."]*9 for _ in range(9)]
    assert problems.isValidSudoku(board) is True

def test_valid_sudoku_row_duplicate(problems):
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6","6",".","1","9","5",".",".","."],  # duplicate '6' in row
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert problems.isValidSudoku(board) is False

def test_valid_sudoku_col_duplicate(problems):
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        ["5",".",".",".","8",".",".","7","9"]  # duplicate '5' in column
    ]
    assert problems.isValidSudoku(board) is False

def test_valid_sudoku_box_duplicate(problems):
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","5"]  # duplicate '5' in bottom right box
    ]
    assert problems.isValidSudoku(board) is False

def test_container_with_most_water_example1(problems):
    height = [1,7,2,5,4,7,3,6]
    assert problems.maxArea(height) == 36

def test_container_with_most_water_example2(problems):
    height = [2,2,2]
    assert problems.maxArea(height) == 4

def test_container_with_most_water_minimum(problems):
    height = [1,1]
    assert problems.maxArea(height) == 1

def test_container_with_most_water_all_zeros(problems):
    height = [0,0,0,0]
    assert problems.maxArea(height) == 0

def test_container_with_most_water_increasing(problems):
    height = [1,2,3,4,5]
    assert problems.maxArea(height) == 6

def test_container_with_most_water_decreasing(problems):
    height = [5,4,3,2,1]
    assert problems.maxArea(height) == 6

def test_container_with_most_water_single_peak(problems):
    height = [1,1000,1]
    assert problems.maxArea(height) == 2

def test_container_with_most_water_large(problems):
    height = [1000] * 1000
    assert problems.maxArea(height) == 999000

def test_trapping_rain_water_example1(problems):
    height = [0,2,0,3,1,0,1,3,2,1]
    assert problems.trap(height) == 9

def test_trapping_rain_water_all_zeros(problems):
    height = [0,0,0,0]
    assert problems.trap(height) == 0

def test_trapping_rain_water_no_trap(problems):
    height = [1,2,3,4,5]
    assert problems.trap(height) == 0

def test_trapping_rain_water_single_peak(problems):
    height = [0,1,0]
    assert problems.trap(height) == 0

def test_trapping_rain_water_valley(problems):
    height = [3,0,2,0,4]
    assert problems.trap(height) == 7

def test_trapping_rain_water_flat(problems):
    height = [2,2,2,2]
    assert problems.trap(height) == 0

def test_trapping_rain_water_small(problems):
    height = [1]
    assert problems.trap(height) == 0

def test_trapping_rain_water_large(problems):
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert problems.trap(height) == 6

def test_trapping_rain_water_edge_case(problems):
    height = [4,2,3]
    assert problems.trap(height) == 1

def test_encode_decode_basic(problems):
    strs = ["neet", "code", "love", "you"]
    encoded = problems.encode(strs)
    decoded = problems.decode(encoded)
    assert decoded == strs

def test_encode_decode_with_symbols(problems):
    strs = ["we", "say", ":", "yes"]
    encoded = problems.encode(strs)
    decoded = problems.decode(encoded)
    assert decoded == strs

def test_encode_decode_empty_list(problems):
    strs = []
    encoded = problems.encode(strs)
    decoded = problems.decode(encoded)
    assert decoded == strs

def test_encode_decode_empty_strings(problems):
    strs = ["", "", ""]
    encoded = problems.encode(strs)
    decoded = problems.decode(encoded)
    assert decoded == strs

def test_encode_decode_mixed_empty_and_nonempty(problems):
    strs = ["a", "", "b", ""]
    encoded = problems.encode(strs)
    decoded = problems.decode(encoded)
    assert decoded == strs

def test_encode_decode_utf8(problems):
    strs = ["你好", "😊", "café", "💡"]
    encoded = problems.encode(strs)
    decoded = problems.decode(encoded)
    assert decoded == strs

def test_encode_decode_long_strings(problems):
    strs = ["a" * 199, "b" * 150, "c" * 50]
    encoded = problems.encode(strs)
    decoded = problems.decode(encoded)
    assert decoded == strs

def test_check_inclusion_true(problems):
    assert problems.checkInclusion("ab", "eidbaooo") is True

def test_check_inclusion_false(problems):
    assert problems.checkInclusion("ab", "eidboaoo") is False

def test_check_inclusion_exact_match(problems):
    assert problems.checkInclusion("abc", "abc") is True

def test_check_inclusion_substring_at_end(problems):
    assert problems.checkInclusion("adc", "dcda") is True

def test_check_inclusion_single_char_true(problems):
    assert problems.checkInclusion("a", "a") is True

def test_check_inclusion_single_char_false(problems):
    assert problems.checkInclusion("a", "b") is False

def test_check_inclusion_longer_s1(problems):
    assert problems.checkInclusion("abcd", "abc") is False

def test_check_inclusion_repeated_chars(problems):
    assert problems.checkInclusion("aabc", "caeabacb") is True

def test_check_inclusion_empty_s2(problems):
    assert problems.checkInclusion("a", "") is False

def test_check_inclusion_s1_equals_s2(problems):
    assert problems.checkInclusion("xyz", "xyz") is True

def test_check_inclusion_leetcode_96(problems):
    assert problems.checkInclusion('hello', 'ooolleoooleh') is False

def test_max_sliding_window_example1(problems):
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    assert problems.maxSlidingWindow(nums, k) == [3,3,5,5,6,7]

def test_max_sliding_window_example2(problems):
    nums = [1]
    k = 1
    assert problems.maxSlidingWindow(nums, k) == [1]

def test_max_sliding_window_example3(problems):
    nums = [1,2,1,0,4,2,6]
    k = 3
    assert problems.maxSlidingWindow(nums, k) == [2,2,4,4,6]

def test_max_sliding_window_all_negatives(problems):
    nums = [-7,-8,-6,-5,-9]
    k = 2
    assert problems.maxSlidingWindow(nums, k) == [-7,-6,-5,-5]

def test_max_sliding_window_k_equals_length(problems):
    nums = [4,2,12,3,8]
    k = 5
    assert problems.maxSlidingWindow(nums, k) == [12]

def test_max_sliding_window_k_is_two(problems):
    nums = [9, 11]
    k = 2
    assert problems.maxSlidingWindow(nums, k) == [11]

def test_max_sliding_window_leetcode_20(problems):
    nums = [1,-1]
    k = 1
    assert problems.maxSlidingWindow(nums, k) == [1,-1]

def test_max_sliding_window_leetcode_22(problems):
    nums = [1,3,1,2,0,5]
    k = 3
    assert problems.maxSlidingWindow(nums, k) == [3,3,2,5]

def test_evalRPN_example1(problems):
    tokens = ["1","2","+","3","*","4","-"]
    assert problems.evalRPN(tokens) == 5

def test_evalRPN_simple_add(problems):
    tokens = ["2", "3", "+"]
    assert problems.evalRPN(tokens) == 5

def test_evalRPN_simple_subtract(problems):
    tokens = ["5", "3", "-"]
    assert problems.evalRPN(tokens) == 2

def test_evalRPN_simple_multiply(problems):
    tokens = ["4", "2", "*"]
    assert problems.evalRPN(tokens) == 8

def test_evalRPN_simple_divide(problems):
    tokens = ["8", "2", "/"]
    assert problems.evalRPN(tokens) == 4

def test_evalRPN_negative_result(problems):
    tokens = ["2", "3", "-"]
    assert problems.evalRPN(tokens) == -1

def test_evalRPN_division_truncate_toward_zero(problems):
    tokens = ["7", "3", "/"]
    assert problems.evalRPN(tokens) == 2
    tokens = ["-7", "3", "/"]
    assert problems.evalRPN(tokens) == -2
    tokens = ["7", "-3", "/"]
    assert problems.evalRPN(tokens) == -2
    tokens = ["-7", "-3", "/"]
    assert problems.evalRPN(tokens) == 2

def test_evalRPN_complex(problems):
    tokens = ["4", "13", "5", "/", "+"]
    assert problems.evalRPN(tokens) == 6

def test_evalRPN_single_number(problems):
    tokens = ["42"]
    assert problems.evalRPN(tokens) == 42

def test_daily_temperatures_example1(problems):
    temperatures = [30,38,30,36,35,40,28]
    assert problems.dailyTemperatures(temperatures) == [1,4,1,2,1,0,0]

def test_daily_temperatures_example2(problems):
    temperatures = [22,21,20]
    assert problems.dailyTemperatures(temperatures) == [0,0,0]

def test_daily_temperatures_all_increasing(problems):
    temperatures = [10,20,30,40]
    assert problems.dailyTemperatures(temperatures) == [1,1,1,0]

def test_daily_temperatures_all_decreasing(problems):
    temperatures = [40,30,20,10]
    assert problems.dailyTemperatures(temperatures) == [0,0,0,0]

def test_daily_temperatures_single_element(problems):
    temperatures = [50]
    assert problems.dailyTemperatures(temperatures) == [0]

def test_daily_temperatures_plateau(problems):
    temperatures = [30,30,30,30]
    assert problems.dailyTemperatures(temperatures) == [0,0,0,0]

def test_daily_temperatures_mixed(problems):
    temperatures = [73,74,75,71,69,72,76,73]
    assert problems.dailyTemperatures(temperatures) == [1,1,4,2,1,1,0,0]

def test_car_fleet_example1(problems):
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    assert problems.carFleet(target, position, speed) == 3

def test_car_fleet_example2(problems):
    target = 10
    position = [3]
    speed = [3]
    assert problems.carFleet(target, position, speed) == 1

def test_car_fleet_example3(problems):
    target = 100
    position = [0,2,4]
    speed = [4,2,1]
    assert problems.carFleet(target, position, speed) == 1

def test_car_fleet_all_separate(problems):
    target = 10
    position = [0,2,4,6,8]
    speed = [1,1,1,1,1]
    assert problems.carFleet(target, position, speed) == 5

def test_car_fleet_all_one_fleet(problems):
    target = 10
    position = [0,1,2,3,4]
    speed = [5,4,3,2,1]
    assert problems.carFleet(target, position, speed) == 1

def test_car_fleet_reverse_order(problems):
    target = 20
    position = [19,18,17,16]
    speed = [1,2,3,4]
    assert problems.carFleet(target, position, speed) == 1 
def test_car_fleet_large_gap(problems):
    target = 100
    position = [0,50]
    speed = [1,1]
    assert problems.carFleet(target, position, speed) == 2

def test_car_fleet_edge_case(problems):
    target = 1
    position = [0]
    speed = [1]
    assert problems.carFleet(target, position, speed) == 1

def test_generate_parenthesis_n1(problems):
    n = 1
    expected = ["()"]
    result = problems.generateParenthesis(n)
    assert sorted(result) == sorted(expected)

def test_generate_parenthesis_n2(problems):
    n = 2
    expected = ["(())", "()()"]
    result = problems.generateParenthesis(n)
    assert sorted(result) == sorted(expected)

def test_generate_parenthesis_n3(problems):
    n = 3
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    result = problems.generateParenthesis(n)
    assert sorted(result) == sorted(expected)

def test_generate_parenthesis_n4_length(problems):
    n = 4
    # There are 14 valid combinations for n=4 (Catalan number)
    result = problems.generateParenthesis(n)
    assert len(result) == 14

def test_generate_parenthesis_unique(problems):
    n = 3
    result = problems.generateParenthesis(n)
    # All combinations should be unique
    assert len(result) == len(set(result))

def test_largest_rectangle_area_example1(problems):
    heights = [2,1,5,6,2,3]
    assert problems.largestRectangleArea(heights) == 10

def test_largest_rectangle_area_example2(problems):
    heights = [2,4]
    assert problems.largestRectangleArea(heights) == 4

def test_largest_rectangle_area_all_same(problems):
    heights = [3,3,3,3]
    assert problems.largestRectangleArea(heights) == 12

def test_largest_rectangle_area_single_bar(problems):
    heights = [7]
    assert problems.largestRectangleArea(heights) == 7

def test_largest_rectangle_area_increasing(problems):
    heights = [1,2,3,4,5]
    assert problems.largestRectangleArea(heights) == 9

def test_largest_rectangle_area_decreasing(problems):
    heights = [5,4,3,2,1]
    assert problems.largestRectangleArea(heights) == 9

def test_largest_rectangle_area_with_zero(problems):
    heights = [0,2,0,2]
    assert problems.largestRectangleArea(heights) == 2

def test_largest_rectangle_area_large_gap(problems):
    heights = [2,1,2]
    assert problems.largestRectangleArea(heights) == 3

def test_next_greater_elements_example1(problems):
    nums = [1,2,1]
    assert problems.nextGreaterElements(nums) == [2,-1,2]

def test_next_greater_elements_example2(problems):
    nums = [1,2,3,4,3]
    assert problems.nextGreaterElements(nums) == [2,3,4,-1,4]

def test_next_greater_elements_all_same(problems):
    nums = [5,5,5,5]
    assert problems.nextGreaterElements(nums) == [-1,-1,-1,-1]

def test_next_greater_elements_strictly_decreasing(problems):
    nums = [4,3,2,1]
    assert problems.nextGreaterElements(nums) == [-1,4,4,4]

def test_next_greater_elements_strictly_increasing(problems):
    nums = [1,2,3,4]
    assert problems.nextGreaterElements(nums) == [2,3,4,-1]

def test_next_greater_elements_single_element(problems):
    nums = [10]
    assert problems.nextGreaterElements(nums) == [-1]

def test_next_greater_elements_with_negatives(problems):
    nums = [-1,0,1]
    assert problems.nextGreaterElements(nums) == [0,1,-1]

def test_asteroid_collision_example1(problems):
    asteroids = [5,10,-5]
    assert problems.asteroidCollision(asteroids) == [5,10]

def test_asteroid_collision_example2(problems):
    asteroids = [8,-8]
    assert problems.asteroidCollision(asteroids) == []

def test_asteroid_collision_example3(problems):
    asteroids = [10,2,-5]
    assert problems.asteroidCollision(asteroids) == [10]

def test_asteroid_collision_no_collision(problems):
    asteroids = [1,2,3]
    assert problems.asteroidCollision(asteroids) == [1,2,3]

def test_asteroid_collision_all_left(problems):
    asteroids = [-2,-1,-3]
    assert problems.asteroidCollision(asteroids) == [-2,-1,-3]

def test_asteroid_collision_chain_reaction(problems):
    asteroids = [1,-2,-2,-2]
    assert problems.asteroidCollision(asteroids) == [-2,-2,-2]

def test_asteroid_collision_large_right_hits_left(problems):
    asteroids = [3,5,-7]
    assert problems.asteroidCollision(asteroids) == [-7]

def test_asteroid_collision_equal_size(problems):
    asteroids = [4,-4]
    assert problems.asteroidCollision(asteroids) == []

def test_asteroid_collision_multiple_collisions(problems):
    asteroids = [10, 2, -5, -15, 20]
    assert problems.asteroidCollision(asteroids) == [-15, 20]

def test_sum_subarray_mins_example1(problems):
    arr = [3,1,2,4]
    assert problems.sumSubarrayMins(arr) == 17

def test_sum_subarray_mins_example2(problems):
    arr = [11,81,94,43,3]
    assert problems.sumSubarrayMins(arr) == 444

def test_sum_subarray_mins_single_element(problems):
    arr = [5]
    assert problems.sumSubarrayMins(arr) == 5

def test_sum_subarray_mins_all_same(problems):
    arr = [2,2,2]
    # All subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2] -> mins: 2,2,2,2,2,2 = 12
    assert problems.sumSubarrayMins(arr) == 12

def test_sum_subarray_mins_strictly_increasing(problems):
    arr = [1,2,3]
    # [1],[2],[3],[1,2],[2,3],[1,2,3] -> mins: 1,2,3,1,2,1 = 10
    assert problems.sumSubarrayMins(arr) == 10

def test_sum_subarray_mins_strictly_decreasing(problems):
    arr = [3,2,1]
    # [3],[2],[1],[3,2],[2,1],[3,2,1] -> mins: 3,2,1,2,1,1 = 10
    assert problems.sumSubarrayMins(arr) == 10

def test_sum_subarray_mins_large_values(problems):
    arr = [30000, 30000, 30000]
    # All subarrays: [30000],[30000],[30000],[30000,30000],[30000,30000],[30000,30000,30000]
    # mins: 30000,30000,30000,30000,30000,30000 = 180000
    assert problems.sumSubarrayMins(arr) == 180000
    
def test_maximumSubarraySum_example1(problems):
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    # Valid subarrays: [1,5,4]=10, [5,4,2]=11, [4,2,9]=15
    # [2,9,9] and [9,9,9] are invalid (duplicates)
    assert problems.maximumSubarraySum(nums, k) == 15

def test_maximumSubarraySum_example2(problems):
    nums = [4, 4, 4]
    k = 3
    # Only subarray is [4,4,4] which has duplicates
    assert problems.maximumSubarraySum(nums, k) == 0

def test_maximumSubarraySum_all_unique(problems):
    nums = [1, 2, 3, 4, 5]
    k = 2
    # All subarrays of length 2 are unique: [1,2]=3, [2,3]=5, [3,4]=7, [4,5]=9
    assert problems.maximumSubarraySum(nums, k) == 9

def test_maximumSubarraySum_k_equals_1(problems):
    nums = [7, 8, 9]
    k = 1
    # Each element is a subarray, all unique
    assert problems.maximumSubarraySum(nums, k) == 9

def test_maximumSubarraySum_no_valid_subarray(problems):
    nums = [2, 2, 2, 2]
    k = 2
    # All subarrays have duplicates
    assert problems.maximumSubarraySum(nums, k) == 0

def test_maximumSubarraySum_entire_array(problems):
    nums = [1, 2, 3, 4]
    k = 4
    # Only subarray is [1,2,3,4], all unique
    assert problems.maximumSubarraySum(nums, k) == 10

def test_maximumSubarraySum_large_k_with_duplicates(problems):
    nums = [1, 2, 3, 2, 1, 4, 5]
    k = 5
    # [1,2,3,2,1] (duplicates), [2,3,2,1,4] (duplicates), [3,2,1,4,5] (all unique, sum=15)
    assert problems.maximumSubarraySum(nums, k) == 15

def test_maximumSubarraySum_single_element(problems):
    nums = [42]
    k = 1
    assert problems.maximumSubarraySum(nums, k) == 42

def test_maximumSubarraySum_k_greater_than_unique_elements(problems):
    nums = [1, 2, 2, 3, 4]
    k = 3
    # [1,2,2] (duplicates), [2,2,3] (duplicates), [2,3,4] (all unique, sum=9)
    assert problems.maximumSubarraySum(nums, k) == 9

def test_maximumSubarraySum_multiple_max_subarrays(problems):
    nums = [1, 2, 3, 1, 2, 3]
    k = 3
    # [1,2,3]=6, [2,3,1]=6, [3,1,2]=6, [1,2,3]=6
    assert problems.maximumSubarraySum(nums, k) == 6

def test_maximumSubarraySum_all_elements_same(problems):
    nums = [5, 5, 5, 5, 5]
    k = 2
    # All subarrays have duplicates
    assert problems.maximumSubarraySum(nums, k) == 0

def test_maximumSubarraySum_k_equals_len(problems):
    nums = [10, 20, 30]
    k = 3
    # Only subarray is [10,20,30], all unique
    assert problems.maximumSubarraySum(nums, k) == 60

def test_maximumSubarraySum_large_input_unique(problems):
    nums = list(range(1, 1001))
    k = 1000
    # Only subarray is all unique, sum = sum 1..1000
    assert problems.maximumSubarraySum(nums, k) == sum(range(1, 1001))

def test_maximumSubarraySum_large_input_duplicates(problems):
    nums = [1]*1000
    k = 2
    # All subarrays have duplicates
    assert problems.maximumSubarraySum(nums, k) == 0

def test_maximumSubarraysum_self_example1(problems):
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    # Valid subarrays: [1,5,4]=10, [5,4,2]=11, [4,2,9]=15
    # [2,9,9] and [9,9,9] are invalid (duplicates)
    assert problems.maximumSubarraySum_self(nums, k) == 15

def test_maximumSubarraysum_self_example2(problems):
    nums = [4, 4, 4]
    k = 3
    # Only subarray is [4,4,4] which has duplicates
    assert problems.maximumSubarraySum_self(nums, k) == 0

def test_maximumSubarraysum_self_all_unique(problems):
    nums = [1, 2, 3, 4, 5]
    k = 2
    # All subarrays of length 2 are unique: [1,2]=3, [2,3]=5, [3,4]=7, [4,5]=9
    assert problems.maximumSubarraySum_self(nums, k) == 9

def test_maximumSubarraysum_self_k_equals_1(problems):
    nums = [7, 8, 9]
    k = 1
    # Each element is a subarray, all unique
    assert problems.maximumSubarraySum_self(nums, k) == 9

def test_maximumSubarraysum_self_no_valid_subarray(problems):
    nums = [2, 2, 2, 2]
    k = 2
    # All subarrays have duplicates
    assert problems.maximumSubarraySum_self(nums, k) == 0

def test_maximumSubarraysum_self_entire_array(problems):
    nums = [1, 2, 3, 4]
    k = 4
    # Only subarray is [1,2,3,4], all unique
    assert problems.maximumSubarraySum_self(nums, k) == 10

def test_maximumSubarraysum_self_large_k_with_duplicates(problems):
    nums = [1, 2, 3, 2, 1, 4, 5]
    k = 5
    # [1,2,3,2,1] (duplicates), [2,3,2,1,4] (duplicates), [3,2,1,4,5] (all unique, sum=15)
    assert problems.maximumSubarraySum_self(nums, k) == 15

def test_maximumSubarraysum_self_single_element(problems):
    nums = [42]
    k = 1
    assert problems.maximumSubarraySum_self(nums, k) == 42

def test_maximumSubarraysum_self_k_greater_than_unique_elements(problems):
    nums = [1, 2, 2, 3, 4]
    k = 3
    # [1,2,2] (duplicates), [2,2,3] (duplicates), [2,3,4] (all unique, sum=9)
    assert problems.maximumSubarraySum_self(nums, k) == 9

def test_maximumSubarraysum_self_multiple_max_subarrays(problems):
    nums = [1, 2, 3, 1, 2, 3]
    k = 3
    # [1,2,3]=6, [2,3,1]=6, [3,1,2]=6, [1,2,3]=6
    assert problems.maximumSubarraySum_self(nums, k) == 6

def test_maximumSubarraysum_self_all_elements_same(problems):
    nums = [5, 5, 5, 5, 5]
    k = 2
    # All subarrays have duplicates
    assert problems.maximumSubarraySum_self(nums, k) == 0

def test_maximumSubarraysum_self_k_equals_len(problems):
    nums = [10, 20, 30]
    k = 3
    # Only subarray is [10,20,30], all unique
    assert problems.maximumSubarraySum_self(nums, k) == 60

def test_maximumSubarraysum_self_large_input_unique(problems):
    nums = list(range(1, 1001))
    k = 1000
    # Only subarray is all unique, sum = sum 1..1000
    assert problems.maximumSubarraySum_self(nums, k) == sum(range(1, 1001))

def test_maximumSubarraysum_self_large_input_duplicates(problems):
    nums = [1]*1000
    k = 2
    # All subarrays have duplicates
    assert problems.maximumSubarraySum_self(nums, k) == 0

def test_fibonacci_basic():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_containsNearbyDuplicate_basic():
    assert containsNearbyDuplicate([1,2,3,1], 3) is True
    assert containsNearbyDuplicate([1,0,1,1], 1) is True
    assert containsNearbyDuplicate([1,2,3,1,2,3], 2) is False

def test_missingNumber_basic():
    assert missingNumber([3,0,1]) == 2
    assert missingNumber([0,1]) == 2
    assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8

def test_isPalindrome_basic():
    assert isPalindrome(121) is True
    assert isPalindrome(-121) is False
    assert isPalindrome(10) is False

def test_romanToInt_basic():
    assert romanToInt("III") == 3
    assert romanToInt("LVIII") == 58
    assert romanToInt("MCMXCIV") == 1994

def test_longest_consecutive_sequence_by_order_basic():
    assert longest_consecutive_sequence_by_order([100, 4, 200, 1, 3, 2]) == 1
    assert longest_consecutive_sequence_by_order([0,3,7,2,5,8,4,6,0,1]) == 2

def test_evalRPN_practice_basic(problems):
    assert evalRPN(["2","1","+","3","*"]) == 9
    assert evalRPN(["4","13","5","/","+"]) == 6

def test_evalRPNr_basic():
    assert evalRPNr(["2","1","+","3","*"]) == 9
    assert evalRPNr(["4","13","5","/","+"]) == 6

def test_airline_basic():
    assert airline() == ['Seattle', 'Memphis', 'Hawaii', 'New York', 'Washington']

def test_mySqrt_basic(problems):
    assert problems.mySqrt(4) == 2
    assert problems.mySqrt(8) == 2
    assert problems.mySqrt(0) == 0
    assert problems.mySqrt(1) == 1

def test_productExceptSelf_basic(problems):
    assert problems.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert problems.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

def test_carFleet_1_basic(problems):
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    assert problems.carFleet_1(target, position, speed) == 3

def test_largestRectangleArea_brute_basic(problems):
    heights = [2,1,5,6,2,3]
    assert problems.largestRectangleArea_brute(heights) == 10

def test_sumSubarrayMins_self_basic(problems):
    arr = [3,1,2,4]
    assert problems.sumSubarrayMins_self(arr) == 17


def test_can_jump_example1(problems):
    nums = [2,3,1,1,4]
    assert problems.canJump(nums) is True

def test_can_jump_example2(problems):
    nums = [3,2,1,0,4]
    assert problems.canJump(nums) is False

def test_can_jump_single_element(problems):
    nums = [0]
    assert problems.canJump(nums) is True

def test_can_jump_all_zeros_except_first(problems):
    nums = [1,0,0,0]
    assert problems.canJump(nums) is False

def test_can_jump_large_jump_at_start(problems):
    nums = [5,0,0,0,0,0]
    assert problems.canJump(nums) is True

def test_can_jump_last_zero_but_reachable(problems):
    nums = [2,0,0]
    assert problems.canJump(nums) is True

def test_can_jump_not_reachable_due_to_zeros(problems):
    nums = [1,1,0,1]
    assert problems.canJump(nums) is False

def test_can_jump_all_ones(problems):
    nums = [1,1,1,1,1]
    assert problems.canJump(nums) is True

def test_sorted_squares_example1(problems):
    nums = [-4,-1,0,3,10]
    assert problems.sortedSquares(nums) == [0,1,9,16,100]

def test_sorted_squares_example2(problems):
    nums = [-7,-3,2,3,11]
    assert problems.sortedSquares(nums) == [4,9,9,49,121]

def test_sorted_squares_all_positive(problems):
    nums = [1,2,3,4,5]
    assert problems.sortedSquares(nums) == [1,4,9,16,25]

def test_sorted_squares_all_negative(problems):
    nums = [-5,-4,-3,-2,-1]
    assert problems.sortedSquares(nums) == [1,4,9,16,25]

def test_sorted_squares_single_zero(problems):
    nums = [0]
    assert problems.sortedSquares(nums) == [0]

def test_sorted_squares_single_negative(problems):
    nums = [-3]
    assert problems.sortedSquares(nums) == [9]

def test_sorted_squares_single_positive(problems):
    nums = [7]
    assert problems.sortedSquares(nums) == [49]

def test_sorted_squares_mixed_with_duplicates(problems):
    nums = [-2,-2,0,2,2]
    assert problems.sortedSquares(nums) == [0,4,4,4,4]


def test_move_zeroes_example1(problems):
    nums = [0,1,0,3,12]
    problems.moveZeroes(nums)
    assert nums == [1,3,12,0,0]

def test_move_zeroes_example2(problems):
    nums = [0]
    problems.moveZeroes(nums)
    assert nums == [0]

def test_move_zeroes_no_zeroes(problems):
    nums = [1,2,3]
    problems.moveZeroes(nums)
    assert nums == [1,2,3]

def test_move_zeroes_all_zeroes(problems):
    nums = [0,0,0]
    problems.moveZeroes(nums)
    assert nums == [0,0,0]

def test_move_zeroes_zeros_at_end(problems):
    nums = [1,2,3,0,0]
    problems.moveZeroes(nums)
    assert nums == [1,2,3,0,0]

def test_move_zeroes_zeros_at_start(problems):
    nums = [0,0,1,2,3]
    problems.moveZeroes(nums)
    assert nums == [1,2,3,0,0]

def test_move_zeroes_alternating(problems):
    nums = [0,1,0,2,0,3]
    problems.moveZeroes(nums)
    assert nums == [1,2,3,0,0,0]

def test_move_zeroes_single_element_nonzero(problems):
    nums = [5]
    problems.moveZeroes(nums)
    assert nums == [5]

def test_move_zeroes_negatives_and_zeros(problems):
    nums = [-1,0,0,1,0]
    problems.moveZeroes(nums)
    assert nums == [-1,1,0,0,0]

def test_merge_two_lists_both_nonempty(problems):
    l1 = list_to_linked([1,2,4])
    l2 = list_to_linked([1,3,4])
    merged = problems.mergeTwoLists(l1, l2)
    assert linked_to_list(merged) == [1,1,2,3,4,4]

def test_merge_two_lists_one_empty(problems):
    l1 = list_to_linked([])
    l2 = list_to_linked([0])
    merged = problems.mergeTwoLists(l1, l2)
    assert linked_to_list(merged) == [0]

def test_merge_two_lists_both_empty(problems):
    l1 = list_to_linked([])
    l2 = list_to_linked([])
    merged = problems.mergeTwoLists(l1, l2)
    assert linked_to_list(merged) == []

def test_merge_two_lists_disjoint(problems):
    l1 = list_to_linked([1,2,3])
    l2 = list_to_linked([4,5,6])
    merged = problems.mergeTwoLists(l1, l2)
    assert linked_to_list(merged) == [1,2,3,4,5,6]

def test_merge_two_lists_interleaved(problems):
    l1 = list_to_linked([1,3,5])
    l2 = list_to_linked([2,4,6])
    merged = problems.mergeTwoLists(l1, l2)
    assert linked_to_list(merged) == [1,2,3,4,5,6]

def test_merge_two_lists_duplicates(problems):
    l1 = list_to_linked([1,1,2])
    l2 = list_to_linked([1,1,2])
    merged = problems.mergeTwoLists(l1, l2)
    assert linked_to_list(merged) == [1,1,1,1,2,2]

def test_remove_element_example1(problems):
    nums = [3,2,2,3]
    val = 3
    length = problems.removeElement(nums, val)
    assert length == 2
    assert sorted(nums[:length]) == [2,2]

def test_remove_element_example2(problems):
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    length = problems.removeElement(nums, val)
    assert length == 5
    assert sorted(nums[:length]) == [0,0,1,3,4]

def test_remove_element_no_removal(problems):
    nums = [1,2,3,4]
    val = 5
    length = problems.removeElement(nums, val)
    assert length == 4
    assert sorted(nums[:length]) == [1,2,3,4]

def test_remove_element_all_removed(problems):
    nums = [2,2,2]
    val = 2
    length = problems.removeElement(nums, val)
    assert length == 0

def test_remove_element_empty(problems):
    nums = []
    val = 1
    length = problems.removeElement(nums, val)
    assert length == 0

def test_remove_element_single_element(problems):
    nums = [1]
    val = 1
    length = problems.removeElement(nums, val)
    assert length == 0

def test_remove_element_single_element_not_removed(problems):
    nums = [1]
    val = 2
    length = problems.removeElement(nums, val)
    assert length == 1
    assert nums[0] == 1


def test_merge_sorted_array_example1(problems):
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    problems.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]

def test_merge_sorted_array_example2(problems):
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    problems.merge(nums1, m, nums2, n)
    assert nums1 == [1]

def test_merge_sorted_array_example3(problems):
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    problems.merge(nums1, m, nums2, n)
    assert nums1 == [1]

def test_merge_sorted_array_all_nums2_smaller(problems):
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    problems.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,4,5,6]

def test_merge_sorted_array_all_nums2_larger(problems):
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [4,5,6]
    n = 3
    problems.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,4,5,6]

def test_merge_sorted_array_interleaved(problems):
    nums1 = [2,4,6,0,0,0]
    m = 3
    nums2 = [1,3,5]
    n = 3
    problems.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,4,5,6]

def test_merge_sorted_array_duplicates(problems):
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,2,2]
    n = 3
    problems.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,2,2,3]


def test_remove_duplicates_example1(problems):
    nums = [1,1,2]
    length = problems.removeDuplicates(nums)
    assert length == 2
    assert nums[:length] == [1,2]

def test_remove_duplicates_example2(problems):
    nums = [0,0,1,1,1,2,2,3,3,4]
    length = problems.removeDuplicates(nums)
    assert length == 5
    assert nums[:length] == [0,1,2,3,4]

def test_remove_duplicates_no_duplicates(problems):
    nums = [1,2,3,4,5]
    length = problems.removeDuplicates(nums)
    assert length == 5
    assert nums[:length] == [1,2,3,4,5]

def test_remove_duplicates_all_same(problems):
    nums = [2,2,2,2]
    length = problems.removeDuplicates(nums)
    assert length == 1
    assert nums[:length] == [2]

def test_remove_duplicates_single_element(problems):
    nums = [7]
    length = problems.removeDuplicates(nums)
    assert length == 1
    assert nums[:length] == [7]

def test_max_profit_example1(problems):
    prices = [7,1,5,3,6,4]
    assert problems.maxProfit(prices) == 5  # Buy at 1, sell at 6

def test_max_profit_example2(problems):
    prices = [7,6,4,3,1]
    assert problems.maxProfit(prices) == 0  # No profit possible

def test_max_profit_single_day(problems):
    prices = [5]
    assert problems.maxProfit(prices) == 0

def test_max_profit_two_days_profit(problems):
    prices = [1,2]
    assert problems.maxProfit(prices) == 1

def test_max_profit_two_days_loss(problems):
    prices = [2,1]
    assert problems.maxProfit(prices) == 0

def test_max_profit_all_same(problems):
    prices = [3,3,3,3]
    assert problems.maxProfit(prices) == 0

def test_max_profit_profit_at_end(problems):
    prices = [5,4,3,2,10]
    assert problems.maxProfit(prices) == 8

def test_max_profit_profit_at_start(problems):
    prices = [1,10,2,1,0]
    assert problems.maxProfit(prices) == 9


def test_binary_search_found_middle(problems):
    nums = [-1,0,3,5,9,12]
    target = 9
    assert problems.search(nums, target) == 4

def test_binary_search_found_left(problems):
    nums = [-1,0,3,5,9,12]
    target = -1
    assert problems.search(nums, target) == 0

def test_binary_search_found_right(problems):
    nums = [-1,0,3,5,9,12]
    target = 12
    assert problems.search(nums, target) == 5

def test_binary_search_not_found(problems):
    nums = [-1,0,3,5,9,12]
    target = 2
    assert problems.search(nums, target) == -1

def test_binary_search_single_element_found(problems):
    nums = [1]
    target = 1
    assert problems.search(nums, target) == 0

def test_binary_search_single_element_not_found(problems):
    nums = [1]
    target = 2
    assert problems.search(nums, target) == -1

def test_binary_search_empty(problems):
    nums = []
    target = 1
    assert problems.search(nums, target) == -1


def test_find_min_rotated_example1(problems):
    nums = [3,4,5,1,2]
    assert problems.findMin(nums) == 1

def test_find_min_rotated_example2(problems):
    nums = [4,5,6,7,0,1,2]
    assert problems.findMin(nums) == 0

def test_find_min_rotated_not_rotated(problems):
    nums = [1,2,3,4,5]
    assert problems.findMin(nums) == 1

def test_find_min_rotated_single_element(problems):
    nums = [10]
    assert problems.findMin(nums) == 10

def test_find_min_rotated_two_elements(problems):
    nums = [2,1]
    assert problems.findMin(nums) == 1

def test_find_min_rotated_at_end(problems):
    nums = [2,3,4,5,1]
    assert problems.findMin(nums) == 1

def test_find_min_rotated_at_start(problems):
    nums = [1,2,3,4,5]
    assert problems.findMin(nums) == 1

def test_find_min_rotated_large(problems):
    nums = list(range(101, 200)) + list(range(1, 101))
    assert problems.findMin(nums) == 1

def test_find_min_rotated_leetcode_88(problems):
    nums = [5,1,2,3,4]
    assert problems.findMin(nums) == 1


def test_candies_example1(problems):
    n = 3
    arr = [1, 2, 2]
    assert problems.candies(arr) == 4  # [1,2,1]

def test_candies_example2(problems):
    n = 10
    arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
    assert problems.candies(arr) == 19

def test_candies_all_same(problems):
    n = 5
    arr = [1, 1, 1, 1, 1]
    assert problems.candies(arr) == 5  # [1,1,1,1,1]

def test_candies_strictly_increasing(problems):
    n = 4
    arr = [1, 2, 3, 4]
    assert problems.candies(arr) == 10  # [1,2,3,4]

def test_candies_strictly_decreasing(problems):
    n = 4
    arr = [4, 3, 2, 1]
    assert problems.candies(arr) == 10  # [4,3,2,1]

def test_candies_valley(problems):
    n = 5
    arr = [2, 1, 2, 1, 2]
    assert problems.candies(arr) == 8  # [2,1,2,1,2]

def test_candies_single_child(problems):
    n = 1
    arr = [5]
    assert problems.candies(arr) == 1

def test_candies_two_children_same(problems):
    n = 2
    arr = [2, 2]
    assert problems.candies(arr) == 2  # [1,1]

def test_candies_two_children_different(problems):
    n = 2
    arr = [1, 2]
    assert problems.candies(arr) == 3  # [1,2]

def test_search_rotated_found_middle(problems):
    nums = [4,5,6,7,0,1,2]
    target = 0
    assert problems.searchRotated(nums, target) == 4

def test_search_rotated_found_left(problems):
    nums = [4,5,6,7,0,1,2]
    target = 4
    assert problems.searchRotated(nums, target) == 0

def test_search_rotated_found_right(problems):
    nums = [4,5,6,7,0,1,2]
    target = 2
    assert problems.searchRotated(nums, target) == 6

def test_search_rotated_not_found(problems):
    nums = [4,5,6,7,0,1,2]
    target = 3
    assert problems.searchRotated(nums, target) == -1

def test_search_rotated_single_element_found(problems):
    nums = [1]
    target = 1
    assert problems.searchRotated(nums, target) == 0

def test_search_rotated_single_element_not_found(problems):
    nums = [1]
    target = 2
    assert problems.searchRotated(nums, target) == -1

def test_search_rotated_not_rotated(problems):
    nums = [1,2,3,4,5,6,7]
    target = 5
    assert problems.searchRotated(nums, target) == 4

def test_search_rotated_two_elements(problems):
    nums = [5,1]
    target = 1
    assert problems.searchRotated(nums, target) == 1

def test_search_rotated_leetcode_159(problems):
    nums = [1,3,5]
    target = 3
    assert problems.searchRotated(nums, target) == 1


def test_search_rotated_ii_found_middle(problems):
    nums = [2,5,6,0,0,1,2]
    target = 0
    assert problems.searchRotatedII(nums, target) is True

def test_search_rotated_ii_not_found(problems):
    nums = [2,5,6,0,0,1,2]
    target = 3
    assert problems.searchRotatedII(nums, target) is False

def test_search_rotated_ii_duplicates(problems):
    nums = [1,1,1,1,1,2,1,1]
    target = 2
    assert problems.searchRotatedII(nums, target) is True

def test_search_rotated_ii_all_duplicates(problems):
    nums = [1,1,1,1,1,1,1]
    target = 2
    assert problems.searchRotatedII(nums, target) is False

def test_search_rotated_ii_single_element_found(problems):
    nums = [1]
    target = 1
    assert problems.searchRotatedII(nums, target) is True

def test_search_rotated_ii_single_element_not_found(problems):
    nums = [1]
    target = 2
    assert problems.searchRotatedII(nums, target) is False

def test_search_rotated_ii_not_rotated(problems):
    nums = [1,2,3,4,5,6,7]
    target = 5
    assert problems.searchRotatedII(nums, target) is True

def test_search_rotated_ii_empty(problems):
    nums = []
    target = 1
    assert problems.searchRotatedII(nums, target) is False

def test_search_rotated_ii_target_at_end(problems):
    nums = [2,2,2,3,4,2]
    target = 4
    assert problems.searchRotatedII(nums, target) is True

def test_search_rotated_ii_target_at_start(problems):
    nums = [4,5,6,7,0,1,2,4,4]
    target = 4
    assert problems.searchRotatedII(nums, target) is True

def test_remove_nth_from_end_middle(problems):
    head = list_to_linked([1,2,3,4,5])
    n = 2
    result = problems.removeNthFromEnd(head, n)
    assert linked_to_list(result) == [1,2,3,5]

def test_remove_nth_from_end_head(problems):
    head = list_to_linked([1,2,3,4,5])
    n = 5
    result = problems.removeNthFromEnd(head, n)
    assert linked_to_list(result) == [2,3,4,5]

def test_remove_nth_from_end_tail(problems):
    head = list_to_linked([1,2,3,4,5])
    n = 1
    result = problems.removeNthFromEnd(head, n)
    assert linked_to_list(result) == [1,2,3,4]

def test_remove_nth_from_end_single_element(problems):
    head = list_to_linked([1])
    n = 1
    result = problems.removeNthFromEnd(head, n)
    assert linked_to_list(result) == []

def test_remove_nth_from_end_two_elements_remove_first(problems):
    head = list_to_linked([1,2])
    n = 2
    result = problems.removeNthFromEnd(head, n)
    assert linked_to_list(result) == [2]

def test_remove_nth_from_end_two_elements_remove_last(problems):
    head = list_to_linked([1,2])
    n = 1
    result = problems.removeNthFromEnd(head, n)
    assert linked_to_list(result) == [1]

def test_reorder_list_even_length(problems):
    head = list_to_linked([1,2,3,4])
    problems.reorderList(head)
    assert linked_to_list(head) == [1,4,2,3]

def test_reorder_list_odd_length(problems):
    head = list_to_linked([1,2,3,4,5])
    problems.reorderList(head)
    assert linked_to_list(head) == [1,5,2,4,3]

def test_reorder_list_two_elements(problems):
    head = list_to_linked([1,2])
    problems.reorderList(head)
    assert linked_to_list(head) == [1,2]

def test_reorder_list_single_element(problems):
    head = list_to_linked([1])
    problems.reorderList(head)
    assert linked_to_list(head) == [1]

def test_reorder_list_longer(problems):
    head = list_to_linked([1,2,3,4,5,6])
    problems.reorderList(head)
    assert linked_to_list(head) == [1,6,2,5,3,4]

def test_merge_k_lists_all_empty(problems):
    lists = [list_to_linked([]), list_to_linked([]), list_to_linked([])]
    merged = problems.mergeKLists(lists)
    assert linked_to_list(merged) == []

def test_merge_k_lists_single_list(problems):
    lists = [list_to_linked([1,2,3])]
    merged = problems.mergeKLists(lists)
    assert linked_to_list(merged) == [1,2,3]

def test_merge_k_lists_two_lists(problems):
    lists = [list_to_linked([1,4,5]), list_to_linked([1,3,4])]
    merged = problems.mergeKLists(lists)
    assert linked_to_list(merged) == [1,1,3,4,4,5]

def test_merge_k_lists_three_lists(problems):
    lists = [
        list_to_linked([1,4,5]),
        list_to_linked([1,3,4]),
        list_to_linked([2,6])
    ]
    merged = problems.mergeKLists(lists)
    assert linked_to_list(merged) == [1,1,2,3,4,4,5,6]

def test_merge_k_lists_some_empty(problems):
    lists = [
        list_to_linked([]),
        list_to_linked([1]),
        list_to_linked([0,2])
    ]
    merged = problems.mergeKLists(lists)
    assert linked_to_list(merged) == [0,1,2]

def test_merge_k_lists_all_single_element(problems):
    lists = [
        list_to_linked([1]),
        list_to_linked([0]),
        list_to_linked([2])
    ]
    merged = problems.mergeKLists(lists)
    assert linked_to_list(merged) == [0,1,2]

def test_merge_k_lists_duplicates(problems):
    lists = [
        list_to_linked([1,4,5]),
        list_to_linked([1,3,4]),
        list_to_linked([2,6,6])
    ]
    merged = problems.mergeKLists(lists)
    assert linked_to_list(merged) == [1,1,2,3,4,4,5,6,6]

def test_merge_k_lists_empty_input(problems):
    lists = []
    merged = problems.mergeKLists(lists)
    assert linked_to_list(merged) == []

def test_max_depth_empty(problems):
    assert problems.maxDepth(None) == 0

def test_max_depth_single_node(problems):
    root = list_to_tree([1])
    assert problems.maxDepth(root) == 1

def test_max_depth_balanced(problems):
    root = list_to_tree([3,9,20,None,None,15,7])
    assert problems.maxDepth(root) == 3

def test_max_depth_left_skewed(problems):
    root = list_to_tree([1,2,None,3,None,4,None])
    assert problems.maxDepth(root) == 4

def test_max_depth_right_skewed(problems):
    root = list_to_tree([1,None,2,None,3,None,4])
    assert problems.maxDepth(root) == 4

def test_max_depth_full_tree(problems):
    root = list_to_tree([1,2,3,4,5,6,7])
    assert problems.maxDepth(root) == 3

def test_diameter_of_binary_tree_example1(problems):
    root = list_to_tree([1,2,3,4,5])
    assert problems.diameterOfBinaryTree(root) == 3  # Path: 4-2-1-3 or 5-2-1-3

def test_diameter_of_binary_tree_single_node(problems):
    root = list_to_tree([1])
    assert problems.diameterOfBinaryTree(root) == 0

def test_diameter_of_binary_tree_two_nodes(problems):
    root = list_to_tree([1,2])
    assert problems.diameterOfBinaryTree(root) == 1

def test_diameter_of_binary_tree_left_skewed(problems):
    root = list_to_tree([1,2,None,3,None,4,None])
    assert problems.diameterOfBinaryTree(root) == 3

def test_diameter_of_binary_tree_right_skewed(problems):
    root = list_to_tree([1,None,2,None,3,None,4])
    assert problems.diameterOfBinaryTree(root) == 3

def test_diameter_of_binary_tree_balanced(problems):
    root = list_to_tree([1,2,3,4,5,6,7])
    assert problems.diameterOfBinaryTree(root) == 4  # Path: 4-2-1-3-7

def test_diameter_of_binary_tree_empty(problems):
    root = list_to_tree([])
    assert problems.diameterOfBinaryTree(root) == 0

def test_lca_bst_example1(problems):
    root = list_to_tree([6,2,8,0,4,7,9,None,None,3,5])
    p = find_node(root, 2)
    q = find_node(root, 8)
    lca = problems.lowestCommonAncestor(root, p, q)
    assert lca.val == 6

def test_lca_bst_example2(problems):
    root = list_to_tree([6,2,8,0,4,7,9,None,None,3,5])
    p = find_node(root, 2)
    q = find_node(root, 4)
    lca = problems.lowestCommonAncestor(root, p, q)
    assert lca.val == 2

def test_lca_bst_root_and_leaf(problems):
    root = list_to_tree([2,1])
    p = find_node(root, 2)
    q = find_node(root, 1)
    lca = problems.lowestCommonAncestor(root, p, q)
    assert lca.val == 2

def test_lca_bst_left_skewed(problems):
    root = list_to_tree([3,2,None,1])
    p = find_node(root, 1)
    q = find_node(root, 2)
    lca = problems.lowestCommonAncestor(root, p, q)
    assert lca.val == 2

def test_lca_bst_right_skewed(problems):
    root = list_to_tree([1,None,2,None,3])
    p = find_node(root, 2)
    q = find_node(root, 3)
    lca = problems.lowestCommonAncestor(root, p, q)
    assert lca.val == 2

def test_lca_bst_same_node(problems):
    root = list_to_tree([2,1,3])
    p = find_node(root, 1)
    q = find_node(root, 1)
    lca = problems.lowestCommonAncestor(root, p, q)
    assert lca.val == 1