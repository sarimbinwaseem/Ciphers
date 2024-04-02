"""
PlayFair Cipher
github.com/sarimbinwaseem/Ciphers
"""

# import argparse
from string import ascii_uppercase
from pprint import pprint
from utils import PlayfairUtils


class Playfair(PlayfairUtils):
    """Playfair Cipher"""

    def __init__(self, keyword):
        super().__init__()
        self.keyword = self.clean_keyword(keyword.upper())
        self.message_pair: list[str] = []
        self.encrypted_msg: str = ""

    def create_matrix(self) -> None:
        """
        create matrix with keyword and alphabets
        """
        self.insert_into_matrix(self.keyword)

        keyword_set = set(self.keyword)

        # make a set of alphabets
        ascii_set = set(ascii_uppercase)

        # remove same letters from alphabets
        remaining_set = ascii_set - keyword_set
        remaining = list(remaining_set)

        # sort the alphabets
        remaining.sort()

        self.insert_into_matrix(remaining)

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

        self.message_pair = new_message

    def encrypt(self, message: str) -> str:
        """
        Encrypts message with the keyword matrix
        Currently not implemented to the end.
        """

        assert isinstance(message, str)

        self.make_message_pair(message)
        print(f"Message Pair: {self.message_pair}")

        for pair in self.message_pair:
        ########## Check for one row ##########################

            idx_one = self.get_letter_row(pair[0])
            idx_two = self.get_letter_row(pair[1])

            # Both alphabets are in same row
            if idx_one == idx_two:
                letter_idx_one = self.get_letter_index(idx_one, pair[0])
                letter_idx_two = self.get_letter_index(idx_two, pair[1])

                if letter_idx_one == 4:
                    new_letter_idx_one = 0
                else:
                    new_letter_idx_one = letter_idx_one + 1

                if letter_idx_two == 4:
                    new_letter_idx_two = 0
                else:
                    new_letter_idx_two = letter_idx_two + 1

                self.encrypted_msg += f"{self.matrix[idx_one][new_letter_idx_one]}{self.matrix[idx_one][new_letter_idx_two]}"

                print(self.encrypted_msg)

        #######################################################

        ########## Check for one column #######################

            row_idx_one = self.get_letter_row(pair[0])
            row_idx_two = self.get_letter_row(pair[1])

            letter_idx_one = self.get_letter_index(row_idx_one, pair[0])
            letter_idx_two = self.get_letter_index(row_idx_two, pair[1])

            # Both alphabets are in same column
            if letter_idx_one == letter_idx_two:

                if row_idx_one == 4:
                    new_idx_one = 0
                else:
                    new_idx_one = row_idx_one + 1

                if row_idx_two == 4:
                    new_idx_two = 0
                else:
                    new_idx_two = row_idx_two + 1

                self.encrypted_msg += f"{self.matrix[new_idx_one][letter_idx_one]}{self.matrix[new_idx_two][letter_idx_two]}"

                print(self.encrypted_msg)

        #######################################################

        ##### Diff row and columns ############################

            if row_idx_one != row_idx_two and letter_idx_one != letter_idx_two:
                new_letter_idx_one = letter_idx_two
                new_letter_idx_two = letter_idx_one


                self.encrypted_msg += f"{self.matrix[row_idx_one][new_letter_idx_one]}{self.matrix[row_idx_two][new_letter_idx_two]}"

                print(self.encrypted_msg)
        #######################################################


def main():

    pf = Playfair(keyword="AACHEN")

    pf.create_matrix()
    pprint(pf.matrix)

    pf.encrypt("CHARLEMAGNE")


if __name__ == "__main__":
    main()
