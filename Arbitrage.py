liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

import itertools


pools = [[[17, 10], [11, 7], [15, 9], [21, 5]], [[36, 4], [13, 6], [25, 3]], [[30, 12], [10, 8]], [[60, 25]]]

tokens = [0, 1, 2, 3, 4]

# Arbitrager's initial holdings
arbitrager_holdings = {
    0: 0,
    1: 5,
    2: 0,
    3: 0,
    4: 0
}

def find_profitable_path(pools_, arbitrager_holdings, target_profit):
    paths = list(itertools.permutations([0, 2, 3, 4]))
    # print(paths)
    for i in range(len(paths)):
        holdings = arbitrager_holdings
        pools = pools_  
        paths[i] = list(paths[i])
        paths[i].append(1)
        paths[i].insert(0, 1)
        # print(paths[i])
        for j in range(len(paths[i])-1):
            calculate_pool(paths[i][j], paths[i][j+1], holdings, pools)
        if holdings[1] > target_profit:
            return paths[i], holdings[1]
    return None, 0

def calculate_pool(token_changed, token_received, holdings, pools):
    if token_changed > token_received:
        idx = token_changed - token_received - 1
        k = pools[token_received][idx][0]*pools[token_received][idx][1]
        holdings[token_received] = pools[token_received][idx][0] - k/(pools[token_received][idx][1]+holdings[token_changed])
        pools[token_received][idx][1] += holdings[token_changed]
        pools[token_received][idx][0] = k/pools[token_received][idx][1]
        holdings[token_changed] = 0
    else:
        idx = token_received - token_changed - 1
        k = pools[token_changed][idx][0]*pools[token_changed][idx][1]
        holdings[token_received] = pools[token_changed][idx][0] - k/(pools[token_changed][idx][1]+holdings[token_changed])
        pools[token_changed][idx][1] += holdings[token_changed]
        pools[token_changed][idx][0] = k/pools[token_changed][idx][1]
        holdings[token_changed] = 0
    # print(holdings[token_received])

def print_result(path, profit):
    for i in range(len(path)-1):
        if path[i] == 0:
            print("tokenA->", end="")
        elif path[i] == 1:
            print("tokenB->", end="")
        elif path[i] == 2:
            print("tokenC->", end="")
        elif path[i] == 3:
            print("tokenD->", end="")
        elif path[i] == 4:
            print("tokenE->", end="")
    if path[-1] == 0:
        print(f"tokenA, tokenB balance={profit}")
    elif path[-1] == 1:
        print(f"tokenB, tokenB balance={profit}")
    elif path[-1] == 2:
        print(f"tokenC, tokenB balance={profit}")
    elif path[-1] == 3:
        print(f"tokenD, tokenB balance={profit}")
    elif path[-1] == 4:
        print(f"tokenE, tokenB balance={profit}")
# Set the target profit
target_profit = 20

# Find a profitable path
path, profit = find_profitable_path(pools, arbitrager_holdings, target_profit)

# print(path, profit)
print_result(path, profit)
