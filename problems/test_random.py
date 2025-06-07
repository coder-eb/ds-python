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