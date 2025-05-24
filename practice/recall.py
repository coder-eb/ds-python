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

def main():
    print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))

if __name__ == '__main__':
    main()
