class SquareIterator:
    def __init__(self, max_n: int):
        self.max_n = max_n

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x > self.max_n:
            raise StopIteration

        sq = self.x ** 2
        self.x += 1
        return sq

square = SquareIterator(10)
sq_iter = square.__iter__()

for sq in sq_iter:
    print(sq)