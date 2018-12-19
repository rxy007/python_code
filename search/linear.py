def linear_search(a, k):
    for i, v in enumerate(a):
        if v == k:
            return i
    return -1

if __name__ == '__main__':
    a = [2,1,4,7,6,8,9,5,4,0,7,10,34,23,12,5,6]
    print(linear_search(a, 12))