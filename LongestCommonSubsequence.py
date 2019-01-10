'''
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .


Output:
For each test case print the length of longest  common subsequence of the two strings .


Constraints:
1<=T<=200
1<=size(str1),size(str2)<=100


Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2

Explanation
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

LCS of "ABC" and "AC" is "AC" of length 2
'''

def longcommon(arr1, arr2):
    ind1 = len(arr1)
    ind2 = len(arr2)

    if (ind1, ind2) in common:
        return common[(ind1, ind2)]
    if ind1 == 0 or ind2 == 0:
        return 0
    if arr1[-1] == arr2[-1]:
        common[(ind1, ind2)] = longcommon(arr1[:-1], arr2[:-1]) + 1
    else:
        common[(ind1, ind2)] = max(longcommon(arr1[:-1], arr2), longcommon(arr1, arr2[:-1]))
    return common[(ind1, ind2)]


if __name__ == '__main__':
    for i in range(int(input())):
        n = [int(x) for x in input().strip().split()]
        arr1 = input()
        arr2 = input()
        common = {}
        longcommon(arr1, arr2)
        print(common[(n[0], n[1])])
