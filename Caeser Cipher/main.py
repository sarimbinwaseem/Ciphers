#!/usr/bin/python

from map import Table

class CaeserCipher():
	"""docstring for CeaserCipher"""
	def __init__(self, key: int):
		super().__init__()
		self.key: int = key

	def encrypt(self, message: str, maps: dict) -> str:
		themap, revmap = maps

		indexes:list = []
		for m in message.upper():
			indexes.append(revmap[m])

		indexes = [idx + self.key for idx in indexes]

		encmsg = [themap[idx % len(themap)] for idx in indexes]

		return ''.join(encmsg)

	def decrypt(self) -> str:
		...

table = Table()
cc = CaeserCipher(3)
res = cc.encrypt("zorinOS", table.get_alpha_map())
print(res)
