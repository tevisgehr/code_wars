class NextHighestAnagram():
    def __init__(self, n):
        self.n = n

    def permutations(self, iterable, r=None):
        # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
        # permutations(range(3)) --> 012 021 102 120 201 210
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = range(n)
        cycles = range(n, n-r, -1)
        yield tuple(pool[i] for i in indices[:r])
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return

    def do_stuff(self, n):
        #n = 12354
        z=[]
        x = list(str(n))
        print "n= ", n
        y = list(self.permutations(x))
        print "Number of permutations: ", len(y)


        for i in y:
            z.append(int(''.join(map(str,i))))

        z = sorted(z)

        result = n

        for b in z:
            if b > n:
                result = b
                break

        return result




def next_bigger(n):
    nha = NextHighestAnagram(n)
    nha.do_stuff(n)
