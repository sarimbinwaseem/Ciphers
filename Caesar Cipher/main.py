#!/usr/bin/python

# from functools import cache
import sys
import argparse
from map import Table


class CaesarCipher:
    """docstring for CaesarCipher"""

    def __init__(self, key: int):
        super().__init__()
        self.key: int = key

    # @cache
    def encrypt(self, message: str, maps: tuple) -> str:
        """Encrypt a message by Caesar Cipher"""

        themap, revmap = maps

        indexes: list = []

        # Getting the indexes of alphabets.
        for m in message.upper():
            indexes.append(revmap[m])

        # Adding/Increasing key to the indexes of alphabets.
        indexes = [idx + self.key for idx in indexes]

        # Taking mod of the new indexes.
        encmsg = [themap[idx % len(themap)] for idx in indexes]

        # Returning as string.
        return "".join(encmsg)

    def decrypt(self, message: str, maps: tuple) -> str:
        """Decrypt a message encrypted by Caesar Cipher"""

        themap, revmap = maps

        indexes: list = []
        for m in message.upper():
            indexes.append(revmap[m])

        indexes = [idx - self.key for idx in indexes]

        decmsg = [themap[idx % len(themap)] for idx in indexes]

        return "".join(decmsg)


def main():
    parser = argparse.ArgumentParser(
        description="Encrypts and decrypts using Caesar Cipher",
    )

    parser.add_argument("-k", "--key", default=3, type=int, help="Put key value here.")
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

        table = Table()
        alpha_map = table.get_alpha_map()
        cc = CaesarCipher(key=KEY)

    else:
        print("[!] Please pass a flag for encrypt/decrypt/both.")
        parser.print_usage()
        sys.exit(1)

    if args.encrypt:
        res = cc.encrypt(MESSAGE, alpha_map)
        print(f"Encrypted: {res}")

    if args.decrypt:
        decres = cc.decrypt(MESSAGE, alpha_map)
        print(f"Decrypted: {decres}")


if __name__ == "__main__":
    main()
