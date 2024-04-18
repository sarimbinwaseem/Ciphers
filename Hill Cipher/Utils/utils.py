"""Utilities for Hill Cipher"""

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
        