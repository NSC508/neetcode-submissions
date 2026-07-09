class Solution:
    def minOperations(self, logs: List[str]) -> int:
        distanceFromMain = 0
        for i in logs:
            if i.startswith('..'):
                distanceFromMain = max(distanceFromMain - 1, 0)
            elif i.startswith('.'):
                distanceFromMain = distanceFromMain
            else:
                distanceFromMain = distanceFromMain + 1
        return distanceFromMain