# Palindrome

def isPalindrome(word: str) -> bool:
    # Base case 1 : If it's a single letter or empty string, it's a palindrome
    if len(word) <= 1:
        return True
    # Base case 2 : If the last and first letters are different, it's not a palindrome
    if word[0] != word[-1]:
        return False
    # Recursive calls with the substring excluding the first and last letters every time
    return isPalindrome(word[1:-1])


# Tests
print(isPalindrome("pop")) # True
print(isPalindrome("rotator")) # True
print(isPalindrome("a")) # True
print(isPalindrome("")) # True
print(isPalindrome("hello")) # False
print(isPalindrome("hello world")) # False