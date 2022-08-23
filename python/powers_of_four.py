class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # We can solve this without logarithms
        # by looking at the binary representations of powers of four:
        # In [13]: powers_of_four = [4**x for x in range(0, 20)]
        # In [14]: [bin(x) for x in powers_of_four]
        # Out[14]:
        # ['0b1',
        #  '0b100',
        #  '0b10000',
        #  '0b1000000',
        #  '0b100000000',
        #  '0b10000000000',
        #  '0b1000000000000',
        #  '0b100000000000000',
        #  '0b10000000000000000',
        #  '0b1000000000000000000',
        #  '0b100000000000000000000',
        #  '0b10000000000000000000000',
        #  '0b1000000000000000000000000',
        #  '0b100000000000000000000000000',
        #  '0b10000000000000000000000000000',
        #  '0b1000000000000000000000000000000',
        #  '0b100000000000000000000000000000000',
        #  '0b10000000000000000000000000000000000',
        #  '0b1000000000000000000000000000000000000',
        #  '0b100000000000000000000000000000000000000']
        # In [16]: [len(bin(x)[2:]) for x in powers_of_four]
        # Out[16]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
        # even-length binary string, 1 with an odd number of 0's following it
        # so we can check by seeing if n follows that rule
        binary_representation = bin(n)[2:]  # chop off the "0b"
        return len(binary_representation) % 2 == 1 and binary_representation[0] == "1" and all(x == "0" for x in binary_representation[1:])
