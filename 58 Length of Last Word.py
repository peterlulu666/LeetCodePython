def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.split(" ")
    if len(s) == 0:
        return 0
    for index in range(len(s) - 1, -1, -1):
        if s[index] != '':
            return len(s[index])
    return 0


def main():
    s = " a"
    print(lengthOfLastWord(s))


main()
