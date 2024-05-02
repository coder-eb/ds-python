class Solution:
    dir = {
        "N": [0, 1],
        "S": [0, -1],
        "E": [1, 0],
        "W": [-1, 0],
    }

    def isPathCrossing(self, path: str) -> bool:
        visit = set()
        x, y = 0, 0
        for c in path:
            visit.add((x,y))

            dx, dy = self.dir[c]
            x, y = x + dx, y + dy

            if (x,y) in visit:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPathCrossing("NESW"))