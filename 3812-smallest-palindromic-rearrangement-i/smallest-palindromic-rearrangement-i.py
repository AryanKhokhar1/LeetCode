class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = [0]*26
        for letter in s:
            count[ord(letter)-97] += 1
        odd  = ""
        answer = ""
        for index,n in enumerate(count):
            if n:
                if n%2 != 0:
                    odd = chr(index+97)
                answer += chr(index+97)*(n//2)
        answer = answer + odd + answer[-1::-1]
        return answer
