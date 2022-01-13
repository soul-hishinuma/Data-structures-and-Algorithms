from typing import List
import random

def bucket_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    bucket_size = max_num // len_numbers

    buckets = [[] for _ in range(bucket_size)]
    for num in numbers:
        i = num // bucket_size
        if i != bucket_size:
            buckets[i].append(num)
        else:
            buckets[bucket_size-1].append(num)
    for i in range(bucket_size):
        insertion_sort(buckets[i]) #それぞれのバケットをインサーションソート

    result = []
    for i in range(bucket_size):
        result += buckets[i]

    return result


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp

    return numbers

if __name__ == "__main__":
    nums = [random.randint(0,1000) for i in range(10)]
    print(bucket_sort(nums))