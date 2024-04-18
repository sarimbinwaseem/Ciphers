#!/usr/bin/python

"""
Code implementation by Sarim Bin Waseem
github.com/sarimbinwaseem
linkedin.com/in/sarimbinwaseem

Hill Cipher
"""

import sys
import argparse
from Utils.utils import Utils


class HillCipher(Utils):
    """docstring for HillCipher"""

    # def __init__():
    # 	super().__init__()
    # 	self.arg = arg

    def encrypt(self, key: str, msg: str):
        key = self.convert_key_to_matrix(key)
        print(self.make_message_pair(msg))
        

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

    MESSAGE = args.message.replace(" ", "")
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
