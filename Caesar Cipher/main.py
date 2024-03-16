#!/usr/bin/python

# from functools import cache
from map import Table


class CaesarCipher:
	"""docstring for CeaserCipher"""

	def __init__(self, key: int):
		super().__init__()
		self.key: int = key

	# @cache
	def encrypt(self, message: str, maps: tuple) -> str:
		themap, revmap = maps
		print(themap, revmap)
		indexes: list = []
		for m in message.upper():
			indexes.append(revmap[m])

		indexes = [idx + self.key for idx in indexes]

		encmsg = [themap[idx % len(themap)] for idx in indexes]

		return "".join(encmsg)

	def decrypt(self) -> str: ...


MESSAGE = "The dark romans are attacking zombies We have a window of two minutes"

table = Table()
cc = CaesarCipher(key = 3)
res = cc.encrypt(MESSAGE, table.get_alpha_map())
print(res)
