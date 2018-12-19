# 插入排序算法的python实现

def insert_sort(a):
    for index in range(1, len(a)):
        while index > 0 and a[index-1] > a[index]:
            a[index-1], a[index] = a[index], a[index-1]
            index -= 1
    return a

if __name__ == '__main__':
    a = [2,1,4,7,6,8,9,5,4,0,7,10,34,23,12,5,6]
    print(insert_sort(a))