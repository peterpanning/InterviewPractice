def isPalindrome(word):
    if not word[0] == word[-1]:
        return False
    elif len(word) < 2:
        return True
    else:
        return isPalindrome(word[1:-1])