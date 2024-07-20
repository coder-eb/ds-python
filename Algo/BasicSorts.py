def bubble_sort(numbers):
    for items_to_compare in range(len(numbers)-1, 0, -1):
        for index in range(items_to_compare):
            if numbers[index] > numbers[index+1]:
                numbers[index], numbers[index+1] = numbers[index+1], numbers[index]
    return numbers

def selection_sort(numbers):
    for index_to_replace in range(len(numbers)-1):
        min_index = index_to_replace
        for curr_index in range(index_to_replace+1, len(numbers)):
            if numbers[curr_index] < numbers[min_index]:
                min_index = curr_index
        
        if min_index == index_to_replace:
            continue
        numbers[index_to_replace], numbers[min_index] = numbers[min_index], numbers[index_to_replace]
        
    return numbers

def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i-1
        while j > -1 and (nums[j] > temp):
            nums[j+1] = nums[j]
            nums[j] = temp
            j -= 1
    return nums

def main():
    sorted_list = insertion_sort([1, 3, 6, 4, 5, 2]) 
    print(sorted_list)
    
if __name__ == "__main__":
    main()