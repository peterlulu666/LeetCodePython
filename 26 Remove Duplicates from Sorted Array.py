#  i
# [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#  ptr
# if left num and right num is not the same
# increment the ptr and copy the right num to nums[ptr]
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ptr = 0
    for index in range(0, len(nums) - 1):
        if nums[index] != nums[index + 1]:
            ptr = ptr + 1
            nums[ptr] = nums[index + 1]
    return ptr + 1


def main():
    num_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(num_list))


main()
