class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele == "+" or ele == "-" or ele == "*" or ele == "/":
                if ele == "+":
                    stack.append(stack.pop() + stack.pop())
                elif ele == "-":
                    first = stack.pop()
                    last = stack.pop()
                    stack.append(last-first)
                elif ele == "*":
                    stack.append(stack.pop() * stack.pop())
                elif ele == "/":
                    first = stack.pop()
                    last = stack.pop()
                    stack.append(int(last/first))
            else:
                stack.append(int(ele))
            print(stack)
        return stack.pop()