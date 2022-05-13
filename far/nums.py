class calculations:
    def __init__(self, per1, per2):
        self.per1 = 0
        self.per2 = 0

    def plus(a, b):
        return b

    def minus(a, b) -> 'ВЫЧТЕТ ИЗ А Б':
        return a - b

    def delit(a, b):
        if a <= b:
            return b / a
        if b > a:
            return a / b


if __name__ == '__main__':
    a = calculations
    print(a.plus(2, 4))
    print(a.minus(21, 22))
    print(a.delit(4, 8))
