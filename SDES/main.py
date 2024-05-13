"""SDES Cipher"""

from pprint import pprint
from copy import deepcopy
from tables import Tables


class SDES(Tables):
    """
    10 bit key
    10 bit Plaintext
    """

    def __init__(self):
        super().__init__()
        self.sub_key_1 = None
        self.sub_key_2 = None

    def split_key(self, data) -> tuple[list]:

        to_slices: int = len(data) // 2
        first_half: list = data[:to_slices]
        second_half: list = data[to_slices:]

        return (first_half, second_half)

    def _shift_1_bit(self, first_half, second_half) -> tuple[list]:

        first_half.append(first_half.pop(0))
        second_half.append(second_half.pop(0))

        return (first_half, second_half)

    def _shift_2_bit(self, first_half, second_half) -> tuple[list]:

        for _ in range(2):
            first_half.append(first_half.pop(0))
            second_half.append(second_half.pop(0))

        return (first_half, second_half)

    def get_subkey(self, e):

        permuted_8 = []
        permuted_8 = [e[p] for p in self.P8]

        return permuted_8

    def sub_key_generation(self, key: str | int):
        """
        P10 -> Shift 1 bit ->
        P8 -> Shift 2 bit -> P8
        """

        if len(key) != 10:
            raise ValueError("Key lenght is not 10.")

        e = {}
        for index, k in enumerate(key):
            e[index + 1] = k

        pprint(e)

        permuted_10 = []
        permuted_10 = [e[p] for p in self.P10]
        pprint(permuted_10)

        first_half, second_half = self.split_key(permuted_10)
        first_half, second_half = self._shift_1_bit(first_half, second_half)

        print(first_half)
        print(second_half)

        for_p8 = deepcopy(first_half)
        for_p8.extend(second_half)

        print(f"For P8: {for_p8}")

        self.sub_key_1 = self.get_subkey(e)

        first_half, second_half = self._shift_2_bit(first_half, second_half)
        for_p8 = deepcopy(first_half)
        for_p8.extend(second_half)
        e = {}
        for index, k in enumerate(for_p8):
            e[index + 1] = k
        
        self.sub_key_2 = self.get_subkey(e)

        print(f"Sub Key 1: {self.sub_key_1}")
        print(f"Sub Key 2: {self.sub_key_2}")


sdes = SDES()
sdes.sub_key_generation("1010111010")
