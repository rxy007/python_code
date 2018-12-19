import math
# 跳转搜索算法的python实现
def jump_search(a, p):
    n = int(math.sqrt(len(a)))
    for i in range(n):
        j = i
        while j < len(a):
            if a[j] == p:
                return j
            else:
                j += n 
    return -1

if __name__ == '__main__':
    a = [2,1,4,7,6,8,9,5,4,0,7,10,34,23,12,5,6]
    print(jump_search(a, 123))