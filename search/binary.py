def binary_search(a, k):
    left = 0
    right = len(a) - 1
    while left<right:
        middle = (right + left) // 2
        if a[middle] == k:
            return middle
        elif a[middle] < k:
            left = middle + 1
        else:
            right = middle - 1
    return -1

if __name__ == '__main__':
    a = [0, 1, 2, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 10, 12, 23, 34]
    print(binary_search(a, 122))