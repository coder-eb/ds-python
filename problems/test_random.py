import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from problems.random import Problems

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