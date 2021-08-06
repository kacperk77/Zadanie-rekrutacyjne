import os.path
import re

class Pairs:
    # constructor
    def __init__(self, array, n):

        self.array = array
        self.n = n

    # function which finds pairs for given array and its length
    def find_pairs(self):

        # opening new file which will contain results
        output = open('wynik.txt', 'w')

        # loop which saves pairs to the file
        for i in range(0, self.n - 1):
            for j in range(i + 1, self.n):
                if self.array[i] + self.array[j] == 12 and self.array[i] != -1 and self.array[j] != -1:
                    output.write("%s\n" % list([self.array[i], self.array[j]]))
                    self.array[i] = -1
                    self.array[j] = -1
        output.close()


def Main():
    # importing input data
    with open('dane_wejsciowe.txt') as f:
        alist = [line.rstrip() for line in f]
    f.close()

    array = list(map(int, alist))
    n = len(array)

    obj_Pairs = Pairs(array, n)
    obj_Pairs.find_pairs()


if __name__ == "__main__":
    Main()


import sys

