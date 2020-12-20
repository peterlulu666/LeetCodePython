def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0
    for index in range(0, len(haystack) - len(needle) + 1):
        if haystack[index: index + len(needle)] == needle:
            return index
    return -1


def main():
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))


main()
