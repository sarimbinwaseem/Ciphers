"""
PlayFair Cipher
github.com/sarimbinwaseem/Ciphers
"""


from string import ascii_uppercase
from utils import PlayfairUtils

class Playfair(PlayfairUtils):
	"""Playfair Cipher"""
	def __init__(self, keyword):
		super().__init__()
		self.keyword = self.clean_keyword(keyword.upper())

		
	def create_matrix(self) -> None:
		"""
		create matrix with keyword and alphabets
		"""
		self.insert_into_matrix(self.keyword)

		keyword_set = set([a for a in self.keyword])

		# make a set of alphabets
		ascii_set = set([a for a in ascii_uppercase])

		# remove same letters from alphabets
		remaining_set = ascii_set - keyword_set
		remaining = list(remaining_set)

		# sort the alphabets
		remaining.sort()

		self.insert_into_matrix(remaining)

	def make_message_pair(self, message: str) -> list[str]:
		
		new_message = []
		temp_msg = ""
		count = 0
		for s in message:
			if count == 2:
				new_message.append(temp_msg)
				temp_msg = ""
				count = 0
			print(s)
			temp_msg += s
			count += 1
			print(count)

		if len(temp_msg) == 1:
			temp_msg += 'x'

		new_message.append(temp_msg)

		return new_message

	def encrypt(self, message) -> str:
		pass




def main():

	pf = Playfair("reeeq")
	# pf.create_matrix()
	# print(pf.matrix)
	d = pf.make_message_pair("carpete")
	print(d)
if __name__ == '__main__':
	main()


