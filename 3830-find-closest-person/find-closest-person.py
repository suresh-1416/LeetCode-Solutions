class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-y) > abs(z-x): 
            return 1
        elif abs(z-y) == abs(z-x) :
            return 0
        else :
            return 2