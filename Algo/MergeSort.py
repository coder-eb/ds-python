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

def main():
    left = [2, 8, 10]
    right = [1, 1, 3, 5, 7, 11]
    merged = merge(left, right)
    print(merged)

if __name__ == '__main__':
    main()