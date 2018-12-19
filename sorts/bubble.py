
# 冒泡排序算法的python实现
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == '__main__':
    a = [2,1,4,7,6,8,9,5,4,0,7,10,34,23,12,5,6]
    print(bubble_sort(a))