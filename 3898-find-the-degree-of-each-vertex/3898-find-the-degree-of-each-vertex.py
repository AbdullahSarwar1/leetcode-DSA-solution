class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = []
        for x in matrix:
            n.append(sum(x))
        return n