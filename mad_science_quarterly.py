def answer(L, k):
    sorted_list = sorted(L,reverse = True)
    positiveIntCount = getPositiveIntCount(sorted_list)
    L_sum = {}
    L_sum[0] = 0
    for index, val in  enumerate(L):
        L_sum[index + 1] = L_sum[index] + val
    maxSum = -1
    while positiveIntCount > 0:
        nextPositiveInt = sorted_list[positiveIntCount - 1]
        positiveIntIndex = L.index(nextPositiveInt)
        for i in range(0,2):
            if positiveIntIndex + i + 1 > len(L):
                break
            calSum = L_sum[positiveIntIndex + i + 1] - L_sum[i]
            maxSum = max(maxSum,calSum)
        positiveIntCount -= 1
    return maxSum

def getPositiveIntCount(list):
    n = len(list)
    if n == 1:
        if list[0] > 0:
            return 1
        else:
            return 0
    mid = n >> 1
    if list[mid] > 0:
        return mid + getPositiveIntCount(list[mid:])
    else:
        return getPositiveIntCount(list[:mid])
