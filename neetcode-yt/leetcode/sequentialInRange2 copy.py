from collections import deque


def main(low, high):
    seq_nums = []
    
    queue = deque(range(1, 9))
    while queue:
        n = queue.popleft()
        if n > high: continue
        if n >= low: 
            seq_nums.append(n)

        ones = n % 10
        if ones == 9: continue
        n = (n * 10) + (ones + 1)
        queue.append(n)

    return seq_nums

if __name__ == '__main__':
    print(main(100, 100000))
    # num = 123/10
    # print(round(num))
