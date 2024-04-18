"""Utilities for Hill Cipher"""

import numpy as np
import string

class Utils:
    """docstring for Utils"""
    def __init__(self):
        super().__init__()

        self.themap = dict(enumerate(string.ascii_uppercase))
        self.themap.update({26: ' '})

        self.revmap = {char: index for index, char in enumerate(string.ascii_uppercase)}
        self.revmap.update({' ': 26})
        
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

    def convert_key_to_matrix(self, key: str) -> np.array:
        """Converts key: str to numpy matrix for
        further multiplication process.
        """

        q = list(map(int, key.split()))
        e = [[q[0], q[1]], [q[2], q[3]]]

        np_key = np.array(e)
        
        return np_key


    def msg_to_matrix(self, msg: list[list[str]]) -> list[list[int]]:
        """Converts every pair of msg to numpy array of indices"""

        msg_matrix = [[self.revmap[l] for l in m] for m in msg]
        np_msg_matrix = list(map(np.array, msg_matrix))

        return np_msg_matrix

    def matrix_to_msg(self, matrix: list[list[int]]) -> str:
        """Converts every pair of matrix to str"""

        msg_matrix = [[self.themap[l] for l in m] for m in matrix]

        return "".join(["".join(a) for a in msg_matrix])

