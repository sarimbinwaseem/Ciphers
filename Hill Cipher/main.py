#!/usr/bin/python

"""
Code implementation by Sarim Bin Waseem
github.com/sarimbinwaseem
linkedin.com/in/sarimbinwaseem

Hill Cipher
"""

import sys
import argparse
import numpy
from Utils.utils import Utils


class HillCipher(Utils):
    """docstring for HillCipher"""
    def __init__(self):
        super().__init__()
        self.MOD = 26

    def encrypt(self, key: str, msg: str):

        if ' ' in msg:
            self.MOD = 27

        print(f"[+] Moding from: {self.MOD}")

        final_msg: str = ""
        tmp_msg_one = []
        tmp_msg_two = []
        KEY: numpy.array = self.convert_key_to_matrix(key)

        msg_pairs: list[str] = self.make_message_pair(msg)

        MSG_MATRIX = self.msg_to_matrix(msg_pairs)

        # Multiplying the key and text
        for pair in MSG_MATRIX:
            tmp_msg_one.append(numpy.dot(KEY, pair))

        for pair in tmp_msg_one:
            pair[0] = pair[0] % self.MOD
            pair[1] = pair[1] % self.MOD

        return self.matrix_to_msg(tmp_msg_one)

def main():
    """main entry point."""

    parser = argparse.ArgumentParser(
        description="Encrypts and decrypts using Hill Cipher",
    )

    parser.add_argument(
        "-k",
        "--key",
        type=str,
        help="Put key value here. like: a b c d -> 7 8 11 11",
        required=True,
    )
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

    MESSAGE = args.message
    KEY = args.key

    if any([args.encrypt, args.decrypt]):

        hill = HillCipher()

    else:
        print("[!] Please pass a flag for encrypt/decrypt/both.")
        parser.print_usage()
        sys.exit(1)

    if args.encrypt:
        res = hill.encrypt(KEY, MESSAGE.upper())
        print(f"Encrypted: {res}")

    if args.decrypt:

        print("[!] Not implemented yet.")
        # decres = hill.decrypt(MESSAGE.upper())
        # print(f"Decrypted: {decres}")


if __name__ == "__main__":
    main()
