#!/usr/bin/python

# from functools import cache
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
	MESSAGE = "The dark romans are attacking zombies We have a window of two minutes"

	table = Table()
	alpha_map = table.get_alpha_map()
	cc = CaesarCipher(key=8)

	# Encrypting
	res = cc.encrypt(MESSAGE, alpha_map)
	print(f"Encrypted: {res}")

	# Decrypting
	decres = cc.decrypt(res, alpha_map)
	print(f"Decrypted: {decres}")


if __name__ == "__main__":
	main()
