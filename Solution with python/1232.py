class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]
        for i in range(2, len(coordinates)):
            dyp = coordinates[i][1] - coordinates[0][1]
            dxp = coordinates[i][0] - coordinates[0][0]
            if dy * dxp != dx * dyp:
                return False
        return True