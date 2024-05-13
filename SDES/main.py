"""SDES Cipher"""

from tables import Tables

class SDES(Tables):
    """
    10 bit key
    10 bit Plaintext  
    """

    def __init__(self):
        super.__init__(self)
        self.sub_key_1 = None
        self.sub_key_2 = None

    def sub_key_generation(self, key: str | int):
        """
        P10 -> Shift 1 bit ->
        P8 -> Shift 2 bit -> P8
        """

