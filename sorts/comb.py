# comb排序算法的python的实现

def comb_sort(a):
    shrink_factor = 0.8
    gap = len(a)
    swapped = True

    while gap>1 or swapped:
        gap = int(float(gap)*shrink_factor)
        swapped = False
        i = 0
        while i+gap < len(a):
            if a[i] > a[i+gap]:
                a[i], a[i+gap] = a[i+gap], a[i]
                swapped = True
            i += 1
    return a

if __name__ == '__main__':
    sort_a = comb_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sort_a)