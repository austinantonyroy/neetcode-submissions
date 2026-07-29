class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=re.sub('[^a-zA-Z0-9]',"",s)
        j=i.lower()
        k=j[::-1]
        if j==k:
            return True
        else:
            return False
        