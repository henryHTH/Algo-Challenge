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