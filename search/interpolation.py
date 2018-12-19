def __assert_sorted(a):
    if a != sorted(a):
        raise ValueError('list is not sorted')
    return True


def interpolation_search(a, k):
    left = 0
    right = len(a) - 1
    while left <= right:
        point = left + (k - a[left])*(right - left) // (a[right] - a[left])

        if point < 0 or point > right:
            return -1
        current = a[point]
        if current == k:
            return point
        elif current < k:
            left = point + 1
        else:
            right = point - 1

if __name__ == "__main__":
    print(interpolation_search([1, 2, 3, 4, 5], 3))
