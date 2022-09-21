from typing import List


def what_this_func_is_doing(nums: List[int], target: int) -> List[int]:
    """
    Two sum solution
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
    hashmap = {}
    for i, el in enumerate(nums):
        # key - parameter, value - index
        hashmap[el] = i
    for i, el in enumerate(nums):
        complement = target - el
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


if __name__ == '__main__':
    print(what_this_func_is_doing(nums=[1, 2, 3], target=3))
    print(what_this_func_is_doing(nums=[1, 2, 3, 4, 5, 6], target=10))
    print(what_this_func_is_doing(nums=[1, 3, 5], target=2))

