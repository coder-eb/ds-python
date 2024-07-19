def bubble_sort(numbers):
    for items_to_compare in range(len(numbers)-1, 0, -1):
        for index in range(items_to_compare):
            if numbers[index] > numbers[index+1]:
                numbers[index], numbers[index+1] = numbers[index+1], numbers[index]
    return numbers

def main():
    sorted_list = bubble_sort([4, 3, 2, 1, 6, 5, 12, 9, 8, 7])
    print(sorted_list)
    
if __name__ == "__main__":
    main()