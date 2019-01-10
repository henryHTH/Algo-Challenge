def cc(coins, target):
    if (len(coins), target) in memo:
        return memo[(len(coins), target)]
    if target == 0: return 1
    if target < 0: return 0
    if len(coins) == 0:
        return 0
    memo[(len(coins), target)] = cc(coins, target - coins[-1]) + cc(coins[:-1], target)
    return memo[(len(coins), target)]


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        coins = [int(x) for x in input().strip().split()]
        target = int(input())
        memo = {}
        print(cc(coins, target))
        
