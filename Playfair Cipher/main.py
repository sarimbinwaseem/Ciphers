"""
PlayFair Cipher
github.com/sarimbinwaseem/Ciphers
"""

import argparse
from string import ascii_uppercase
from pprint import pprint
from utils import PlayfairUtils


class Playfair(PlayfairUtils):
    """Playfair Cipher"""

    def __init__(self, keyword):
        super().__init__()
        self.keyword = self.clean_keyword(keyword.upper())
        self.message_pair: list[str] = []

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
        Encrypts message with the keyword matrix.
        Encrypt:
            A loop gets all the pairs.
            Checks are done for same row, same column and diff row and col.
        """

        assert isinstance(message, str)
        encrypted_msg: str = ""

        self.make_message_pair(message)
        print(f"Message Pair: {self.message_pair}")

        for pair in self.message_pair:

            # idx = index

            row_idx_one = self.get_letter_row(pair[0])
            row_idx_two = self.get_letter_row(pair[1])

            letter_idx_one = self.get_letter_index(row_idx_one, pair[0])
            letter_idx_two = self.get_letter_index(row_idx_two, pair[1])

            # Both alphabets are in same row
            if row_idx_one == row_idx_two:

                if letter_idx_one == 4:
                    new_letter_idx_one = 0
                else:
                    new_letter_idx_one = letter_idx_one + 1

                if letter_idx_two == 4:
                    new_letter_idx_two = 0
                else:
                    new_letter_idx_two = letter_idx_two + 1

                encrypted_msg += f"{self.matrix[row_idx_one][new_letter_idx_one]}{self.matrix[row_idx_one][new_letter_idx_two]}"

            # Check for one column
            # Both alphabets are in same column
            elif letter_idx_one == letter_idx_two:

                if row_idx_one == 4:
                    new_idx_one = 0
                else:
                    new_idx_one = row_idx_one + 1

                if row_idx_two == 4:
                    new_idx_two = 0
                else:
                    new_idx_two = row_idx_two + 1

                encrypted_msg += f"{self.matrix[new_idx_one][letter_idx_one]}{self.matrix[new_idx_two][letter_idx_two]}"

            # Alphabets in diff row and column
            elif row_idx_one != row_idx_two and letter_idx_one != letter_idx_two:
                new_letter_idx_one = letter_idx_two
                new_letter_idx_two = letter_idx_one

                encrypted_msg += f"{self.matrix[row_idx_one][new_letter_idx_one]}{self.matrix[row_idx_two][new_letter_idx_two]}"

        return encrypted_msg

    def decrypt(self, message: str) -> str:
        """
        Decrypts message with the keyword matrix.
        Decrypt:
            A loop gets all the pairs.
            Checks are done for same row, same column and diff row and col.
        """

        assert isinstance(message, str)
        decrypted_msg: str = ""

        self.make_message_pair(message)
        print(f"Message Pair: {self.message_pair}")

        for pair in self.message_pair:

            # idx = index

            row_idx_one = self.get_letter_row(pair[0])
            row_idx_two = self.get_letter_row(pair[1])

            letter_idx_one = self.get_letter_index(row_idx_one, pair[0])
            letter_idx_two = self.get_letter_index(row_idx_two, pair[1])

            # Both alphabets are in same row
            if row_idx_one == row_idx_two:

                if letter_idx_one == 0:
                    new_letter_idx_one = 4
                else:
                    new_letter_idx_one = letter_idx_one - 1

                if letter_idx_two == 0:
                    new_letter_idx_two = 4
                else:
                    new_letter_idx_two = letter_idx_two - 1

                decrypted_msg += f"{self.matrix[row_idx_one][new_letter_idx_one]}{self.matrix[row_idx_one][new_letter_idx_two]}"

            # Check for one column
            # Both alphabets are in same column
            elif letter_idx_one == letter_idx_two:

                if row_idx_one == 0:
                    new_idx_one = 4
                else:
                    new_idx_one = row_idx_one - 1

                if row_idx_two == 0:
                    new_idx_two = 4
                else:
                    new_idx_two = row_idx_two - 1

                decrypted_msg += f"{self.matrix[new_idx_one][letter_idx_one]}{self.matrix[new_idx_two][letter_idx_two]}"

            # Alphabets in diff row and column
            elif row_idx_one != row_idx_two and letter_idx_one != letter_idx_two:
                new_letter_idx_one = letter_idx_two
                new_letter_idx_two = letter_idx_one

                decrypted_msg += f"{self.matrix[row_idx_one][new_letter_idx_one]}{self.matrix[row_idx_two][new_letter_idx_two]}"

        return decrypted_msg


def main():
    """main entry point."""

    parser = argparse.ArgumentParser(
        description="Encrypts and decrypts using Playfair Cipher",
    )

    parser.add_argument("-k", "--key", type=str, help="Put key value here.", required = True)
    parser.add_argument(
        "-m", "--message", type=str, help="Put message here.", required=True
    )
    parser.add_argument(
        "-e", "--encrypt", help="Encrypts the message.", action="store_true"
    )
    parser.add_argument(
        "-d", "--decrypt", help="Decrypts the message.", action="store_true"
    )
    args = parser.parse_args()

    MESSAGE = args.message.replace(' ', '')
    KEY = args.key

    if any([args.encrypt, args.decrypt]):

        playfair = Playfair(KEY)
        playfair.create_matrix()

    else:
        print("[!] Please pass a flag for encrypt/decrypt/both.")
        parser.print_usage()
        sys.exit(1)

    if args.encrypt:
        res = playfair.encrypt(MESSAGE.upper())
        print(f"Encrypted: {res}")

    if args.decrypt:
        decres = playfair.decrypt(MESSAGE.upper())
        print(f"Decrypted: {decres}")


if __name__ == "__main__":
    main()
