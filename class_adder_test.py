class Adder(object):
    #def __init__(self):
        #self.n = n

    def add1(self, n):
        x = n + 1
        return x

    def add2(self, n):
        x = n + 1
        return x

    def add3(self, n):
        x = add1(n)
        x = add2(x)

        return x
