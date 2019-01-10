'''
Given a number N, the task is to find the largest prime factor of that number.

Input:
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case contains an integer N.

Output:
For each test case, in a new line, print the largest prime factor of N.

Constraints:
1 <= T <= 100
2 <= N <= 1010

Example:
Input:
2
6
15
Output:
3
5
'''

def lpf(num):
    while num % 2 == 0:
        num = num / 2
    if num == 1: return num
    n = num
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while num % i == 0:
            num = num / i
        if num == 1:
            return i
    return num


if __name__ == '__main__':
    import math

    for i in range(int(input())):
        num = int(input())
        print(int((lpf(num))))