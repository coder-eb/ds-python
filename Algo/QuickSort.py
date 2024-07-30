def swap(numbers, left_index, right_index):
    numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index] 

def pivot(numbers, pivot_index, end_index):
    swap_index = pivot_index
    for current_index in range(pivot_index+1, end_index+1):
        if numbers[current_index] < numbers[pivot_index]:
            swap_index += 1
            swap(numbers, swap_index, current_index)
    
    swap(numbers, pivot_index, swap_index)

    return swap_index

def quick_sort(numbers, left, right):
    if left >= right:
        return
    
    pivot_index = pivot(numbers, left, right)
    quick_sort(numbers, left, pivot_index-1)
    quick_sort(numbers, pivot_index+1, right)

    return numbers


def main():
    numbers = [4, 6, 1, 7, 3, 2, 5]
    print(quick_sort(numbers, 0, len(numbers)-1))
    print(numbers)

if __name__ == '__main__':
    main()