class SequenceIterator:
	def __init__(self, sequence):
		self._sequence = sequence
		self._index = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._index < len(self._sequence):
			item = self._sequence[self._index]
			self._index += 1
			return item
		else:
			raise StopIteration

class PlayfairUtils(object):
	"""docstring for PlayfairUtils"""
	def __init__(self):
		super().__init__()
	
	def key_matrix(self) -> list[list]:
		...

	def clean_keyword(self, keyword: str) -> str:
		"""Remove repeating letters from the keyword
		datetype set doesn't work as it randomizes the letters.
		"""
		
		key_set = set()
		key_set = "".join(dict.fromkeys(keyword))

		return key_set


def main():
	pu = PlayfairUtils()
	e = pu.clean_keyword("newcombination")
	print(e)

if __name__ == '__main__':
	main()