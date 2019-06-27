class MovingTotal:
    def __init__(self):
        self.elems = []
        self.totals = set()

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        self.elems += numbers
        if len(self.elems) >= 3:
            self.totals.add(sum(self.elems[-3:]))
        # print(self.elems)

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        print(self.totals)
        return total in self.totals

movingtotal = MovingTotal()
movingtotal.append([1, 2, 3])
print(movingtotal.contains(6))
print(movingtotal.contains(9))
movingtotal.append([0])
#print(movingtotal.contains(9))
print(movingtotal.contains(5))
