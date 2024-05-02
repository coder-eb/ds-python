def main(low, high):
    seq_template = "123456789"
    seq_nums = []
    low_digit, high_digit = len(str(low)), len(str(high))

    for num_length in range(low_digit, high_digit+1):
        slice_start = 0
        slice_end = num_length
        while slice_end <= 9:
            seq_num = int(seq_template[slice_start:slice_end])
            slice_start += 1
            slice_end += 1

            if seq_num < low: continue
            if seq_num > high: return seq_nums
            seq_nums.append(seq_num)

    return seq_nums

if __name__ == '__main__':
    print(main(100, 10000))
    # num = 123/10
    # print(round(num))
