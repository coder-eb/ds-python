def main():
    prices = [10, 100, 200, 300, 50, 500]
    profits = {}

    max_profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
            profits[profit] = f"{i}, {j}"
    print(profits[max_profit])


if __name__ == "__main__":
    main()