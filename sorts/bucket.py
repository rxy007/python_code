from insert import insert_sort
import math
# 桶排序算法的python实现
BUCKET_SIZE = 5

def bucket_sort(a, bucket_size = BUCKET_SIZE):
    min_value = min(a)
    max_value = max(a)
    bucket_count = math.floor((max_value - min_value)/bucket_size) + 1
    buckets = []
    for i in range(bucket_count):
        buckets.append([])
    for i in a:
        buckets[math.floor((i - min_value)/bucket_size)].append(i)
    sort_a = []
    for bucket in buckets:
        insert_sort(bucket)
        for b in bucket:
            sort_a.append(b)
    return sort_a

if __name__ == '__main__':
    sort_a = bucket_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sort_a)