class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i, v in enumerate(operations):
            if v not in ['+', 'C', "D"]:
                stack.append(int(v))
            elif v == '+':
                first = stack.pop()
                second = stack.pop()
                nxt = first + second
                stack.append(second)
                stack.append(first)
                stack.append(nxt)
            elif v == 'C':
                stack.pop()
            elif v == 'D':
                stack.append(2 * stack[-1])
        totalSum = 0
        for i in stack:
            totalSum = totalSum + i
        return totalSum