class CountSquares:

    def __init__(self):
        self.ptCount = defaultdict(int) #
        self.point = []

    def add(self, point: List[int]) -> None:
        self.ptCount[tuple(point)] += 1 #
        self.point.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.point:
            if abs(py - y) != abs(px - x) or y == py or x == px:
                continue

            res += self.ptCount[(x, py)] * self.ptCount[(px, y)] #
        return res