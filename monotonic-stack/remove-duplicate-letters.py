class Solution(object):
    def removeDuplicateLetters(self, s):
        freq = dict(Counter(s))
        stack = []
        in_stack = set()

        for ch in s:
            
            freq[ch] -= 1

            if ch in in_stack:
                continue

            while stack and stack[-1] > ch and freq[stack[-1]]> 0:
                in_stack.remove(stack.pop())
            stack.append(ch)
            in_stack.add(ch)
        return "".join(stack)