from typing import List

def kali_dua(data: List[int]) -> List[int]:
    return [int(i) * 2 for i in data]

print(kali_dua([1, 2, 3, 4, 5])) # [2, 4, 6, 8, 10]
print(kali_dua(['1', '2', '3', '4', '5'])) # [1, 2, 3, 4, 5]

a = 10
print(a)
a = "Yudha Islami Sulistya"
print(a)