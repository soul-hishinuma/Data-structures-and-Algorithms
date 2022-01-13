from typing import List
import random

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers) #リストの長さ
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j] #入れ替える処理
    return numbers

if __name__ == "__main__":
    nums = [random.randint(0,1000) for _ in range(10)]
    print(bubble_sort(nums))