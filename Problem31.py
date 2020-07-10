from sys import argv

def main():
    target = int(argv[1])
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0] * target

    for idx, coin in enumerate(coins):
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]

    print(ways[-1])
if __name__ == "__main__":
    main()