class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y:
            p1a, p1b, v1 = "a", "b", x
            p2a, p2b, v2 = "b", "a", y
        else:
            p1a, p1b, v1 = "b", "a", y
            p2a, p2b, v2 = "a", "b", x
        points = 0
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 2 and stack[-2] == p1a and stack[-1] == p1b:
                stack.pop()
                stack.pop()
                points += v1
        strack2 = []
        for c in stack:
            strack2.append(c)
            if len(strack2) >= 2 and strack2[-2] == p2a and strack2[-1] == p2b:
                strack2.pop()
                strack2.pop()
                points += v2
        return points
