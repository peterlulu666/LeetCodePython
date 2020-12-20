#  i
# [0, 1, 2, 2, 3, 0, 4, 2]
#  ptr
# if array element and the target is not the same
# copy array element to nums[ptr] and increment the ptr
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    ptr = 0
    for index in range(0, len(nums)):
        if nums[index] != val:
            nums[ptr] = nums[index]
            ptr = ptr + 1
    return ptr


def main():
    num_list = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(removeElement(num_list, val))


main()
