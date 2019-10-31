"""
https://www.codechef.com/OCT19B/problems/S10E

PASSED
-------
"""

def good_prices(prices):
    # Base case = if there is only 5 of less numbers:
    ans = 0
    X = len(prices)

    for i in range(0, X):
        if i < 5:
            if all(prices[i] < c for c in prices[:i]):
                ans += 1
        else:
            if all(prices[i] < c for c in prices[i-5:i]):
                ans += 1
    
    print(ans)


if __name__ == "__main__":
    for i in range(int(input())):
        N = int(input())
        prices = map(int, raw_input().split(' ')) # prices become a array that you can iterate through
        good_prices(prices)