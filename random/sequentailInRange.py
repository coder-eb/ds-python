def main(low, high):
    sequential_nums = []
    low_digit, high_digit = len(str(low)), len(str(high))

    for num_length in range(low_digit, high_digit+1):
        range_start = range_end = range_step = 0
        multiplier = 1
        
        for i in range(0, num_length):
            range_start_digit = 1 + i
            range_end_digit = 9 - i

            range_start = range_start * 10 + range_start_digit
            range_end = range_end_digit * multiplier + range_end
            range_step = range_step * 10 + 1

            multiplier *= 10

        for sequential_num in range(range_start, range_end+1, range_step):
            if sequential_num < low: continue
            if sequential_num > high: return sequential_nums

            sequential_nums.append(sequential_num)
    return sequential_nums

if __name__ == '__main__':
    print(main(100, 300))
    # num = 123/10
    # print(round(num))
