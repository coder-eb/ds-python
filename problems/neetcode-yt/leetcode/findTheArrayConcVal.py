def findTheArrayConcVal(nums):
    total = 0
    left, right = 0, len(nums)-1

    while left <= right:
        conc = f"{nums[left]}" if left == right else f"{nums[left]}{nums[right]}"
        num = int(conc)
        total += num 
        # Traverse
        left += 1
        right -= 1

    return total
