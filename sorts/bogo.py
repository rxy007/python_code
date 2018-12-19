import random
# bogo排序算法的python实现
# 此算法是搞笑的哈哈哈
def bogo_sort(a):
    def is_sorted(a):
        if len(a)<2:
            return True
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                return False
        return True
    while not is_sorted(a):
        random.shuffle(a)
    return a

if __name__ == '__main__':
    sort_a = bogo_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sort_a)