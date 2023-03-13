from typing import List


def foo(nums: List[int]) -> List[int]:
    # TODO: Add your code here
    new_list = []
    multiplication = 1
    for i in nums:
        multiplication *= i
    for i in nums:
        new_list.append(int(multiplication/i))



    return new_list

print(foo([1,2,3,4,5,6]))
