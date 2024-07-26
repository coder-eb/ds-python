def merge(left, right):
    merged = []

    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def merge_sort(items):
    if len(items) == 1:
        return items
    
    mid_index = len(items) // 2
    left = merge_sort(items[:mid_index])
    right = merge_sort(items[mid_index:])
    
    return merge(left, right)

def main():
    items = [1, 10, 5, 8, 3, 2]
    sorted = merge_sort(items)
    print(sorted)

if __name__ == '__main__':
    main()