# split words
# check if the last word is the empty string, if no, return the length
# of yes, check the second last word
# if you checked every word and every word is empty string, retirn 0
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
