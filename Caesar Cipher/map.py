#!/usr/bin/python
import string

class Table():
	"""docstring for Table"""
	def __init__(self):
		super().__init__()

	def get_alpha_map(self) -> tuple:

		return ({index: n for index, n in enumerate(string.ascii_uppercase)},
			{char: index for index, char in enumerate(string.ascii_uppercase)}
			)

	def get_alpha_num_map(self) -> dict:
		...
		