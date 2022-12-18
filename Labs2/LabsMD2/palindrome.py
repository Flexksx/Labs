def palindrome(s):
    if s == s[::-1]:
        return True
    return False


def makerawpalindrome(s):
    for i in range(len(s) + 1):
        a = s[:i]
        b = a[::-1]
        ans = b + s
        if palindrome(ans):
            return ans






x = "aabcbaaa"
print(makerawpalindrome(x))
