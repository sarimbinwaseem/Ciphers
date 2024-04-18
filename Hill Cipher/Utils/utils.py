"""Utilities for Hill Cipher"""

import numpy as np


class Utils:
    """docstring for Utils"""
    # def __init__(self):
    #   super().__init__()
        
    def make_message_pair(self, message: str) -> list[str]:
        """
        Break message into pairs.
        if the last letter is single, it will pair with X
        """

        new_message = []
        temp_msg = ""
        count = 0
        for s in message:
            if count == 2:
                new_message.append(temp_msg)
                temp_msg = ""
                count = 0
            # print(s)
            temp_msg += s
            count += 1
            # print(count)

        if len(temp_msg) == 1:
            temp_msg += "X"

        new_message.append(temp_msg)

        return new_message

    def convert_key_to_matrix(self, key: str):
        """Converts key: str to numpy matrix for
        further multiplication process.
        """

        q = list(map(int, key.split()))
        e = [[q[0], q[1]], [q[2], q[3]]]

        np_key = np.array(e)
        
        return np_key


    def get_alpha_map(self) -> tuple:

        # {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F' ... }

        themap = dict(enumerate(string.ascii_uppercase))
        themap.update({26: ' '})

        return themap
