import rand

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    mergeIndex = 0

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[mergeIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[mergeIndex] = rightArr[rightIndex]
            rightIndex += 1
        mergeIndex += 1

    while leftIndex < len(leftArr):
        mergeArr[mergeIndex] = leftArr[leftIndex]
        leftIndex += 1
        mergeIndex += 1

    while rightIndex < len(rightArr):
        mergeArr[mergeIndex] = rightArr[rightIndex]
        rightIndex += 1
        mergeIndex += 1

    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)
