class CustomInt(int):
    def __call__(self, v):
        return CustomInt(self + v)

def add():
    return CustomInt(v)
