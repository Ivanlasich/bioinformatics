import numpy as np

def DPChange(money, Coins):
    MinNumCoins = np.zeros(money+1)
    for m in range(1, money+1):
        MinNumCoins[m] = np.Inf
        for i in Coins:
            if m >= i:
                if MinNumCoins[m - i] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - i] + 1
    return MinNumCoins[money]


money = int(input())
Coins = list(map(int, input().split(',')))
print(int(DPChange(money, Coins)))