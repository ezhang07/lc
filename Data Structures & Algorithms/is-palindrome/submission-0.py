class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for character in s:
            if character.isalnum():
                newString+=character
        return newString.lower() == newString[::-1].lower()
