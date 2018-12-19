# 鸡尾酒排序算法的python实现

def cocktail_shaker_sort(a):
    for i in range(len(a)-1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swapped = True
        
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            return a

if __name__ == '__main__':
    sort_a = cocktail_shaker_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sort_a)