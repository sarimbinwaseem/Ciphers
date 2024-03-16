#!/usr/bin/python
import string


class Table:
	"""docstring for Table"""

	def __init__(self):
		pass
		# super().__init__()

	def get_alpha_map(self) -> tuple:

		# {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F' ... }
		# {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5 ... }

		return (
			dict(enumerate(string.ascii_uppercase)),
			{char: index for index, char in enumerate(string.ascii_uppercase)},
		)

	def get_alpha_num_map(self) -> dict: ...
