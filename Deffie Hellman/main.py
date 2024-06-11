"""Deffie Hellman
Code by: Sarim Bin Waseem
github.com/sarimbinwaseem
"""

import random
from multiprocessing import Pipe
from threading import Thread

from utils import DH_UTILS

# PUBLIC
PRIME_NUMBER = 13


class DeffieHellman:
    def __init__(self, prime_number: int, pipe, the_G: int):
        self.prime_number = prime_number
        self.pipe = pipe
        self.the_G = the_G

    def _get_random_int(self) -> int:
        return random.choice(range(10, 100))

    def _calc_secret(self, power: int, G: int) -> int:

        return pow(G, power) % self.prime_number

    def _calc_key(self, base: int, power: int) -> int:
        return pow(base, power) % self.prime_number

    def source(self):
        """At source of Deffie Hellman"""

        a_secret: int = self._get_random_int()

        x_secret: int = self._calc_secret(a_secret, self.the_G)
        self.pipe.send(x_secret)

        y = self.pipe.recv()
        key_A = self._calc_key(y, a_secret)

        # return key_A
        print(f"Key A: {key_A}")

    def destination(self):
        """At destination of Deffie Hellman"""

        b_secret: int = self._get_random_int()

        y_secret: int = self._calc_secret(b_secret, self.the_G)
        self.pipe.send(y_secret)

        x = self.pipe.recv()
        key_B = self._calc_key(x, b_secret)

        # return key_B
        print(f"Key B: {key_B}")


if __name__ == "__main__":
    source_end, destination_end = Pipe(duplex=True)
    utility = DH_UTILS(PRIME_NUMBER)
    utility._primitive_root()

    the_G: int = input("Check for repetition and enter G: ")
    the_G = int(the_G)

    source = DeffieHellman(PRIME_NUMBER, source_end, the_G)
    destination = DeffieHellman(PRIME_NUMBER, destination_end, the_G)

    source_thread = Thread(target=source.source)
    destination_thread = Thread(target=destination.destination)

    source_thread.start()
    destination_thread.start()
