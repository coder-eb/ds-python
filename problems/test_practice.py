import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from problems.practice import Problems

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
