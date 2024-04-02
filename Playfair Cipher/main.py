"""
PlayFair Cipher
github.com/sarimbinwaseem/Ciphers
"""


from string import ascii_uppercase
from pprint import pprint
from utils import PlayfairUtils

class Playfair(PlayfairUtils):
	"""Playfair Cipher"""
	def __init__(self, keyword):
		super().__init__()
		self.keyword = self.clean_keyword(keyword.upper())
		self.message_pair:list[str] = []
		self.encrypted_msg:str = ""

		
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
			# print(s)
			temp_msg += s
			count += 1
			# print(count)

		if len(temp_msg) == 1:
			temp_msg += 'x'

		new_message.append(temp_msg)

		self.message_pair = new_message

	def encrypt(self, message) -> str:

		self.make_message_pair(message)
		pair = self.message_pair[0]

		########## Check for one row ##########################

		idx_one = self.get_letter_row(pair[0])
		idx_two = self.get_letter_row(pair[1])


		# Both alphabets are in same row
		if idx_one == idx_two:
			letter_idx_one = self.get_letter_index(idx_one, pair[0])
			letter_idx_two = self.get_letter_index(idx_two,pair[1])

			if letter_idx_one == 4:
				new_letter_idx_one = 0
			else:
				new_letter_idx_one = letter_idx_one + 1

			if letter_idx_two == 4:
				new_letter_idx_two = 0
			else:
				new_letter_idx_two = letter_idx_two + 1

			self.encrypted_msg += f"{self.matrix[idx_one][new_letter_idx_one]}{self.matrix[idx_one][new_letter_idx_two]}"

			print(self.encrypted_msg)

		#######################################################

		########## Check for one column (not done) ##########################

		idx_one = self.get_letter_row(pair[0])
		idx_two = self.get_letter_row(pair[1])

		letter_idx_one = self.get_letter_index(idx_one, pair[0])
		letter_idx_two = self.get_letter_index(idx_two,pair[1])


		# Both alphabets are in same column
		if letter_idx_one == letter_idx_two:

			if idx_one == 4:
				new_idx_one = 0
			else:
				new_idx_one = idx_one + 1

			if idx_two == 4:
				new_idx_two = 0
			else:
				new_idx_two = idx_two + 1

			self.encrypted_msg += f"{self.matrix[new_idx_one][letter_idx_one]}{self.matrix[new_idx_two][letter_idx_two]}"

			print(self.encrypted_msg)

		#######################################################

		# new_letter = ""
		# new_index = 0
		# for index_row, row in enumerate(self.matrix):
		# 	if letter in row:
		# 		idx_letter = row.index(letter)
		# 		print(f"Letter in Row: {letter} at Index: {idx_letter}")
		# 		if idx_letter == 4:
		# 			new_idx_letter = 0
		# 		else:
		# 			new_idx_letter = idx_letter + 1

				
		# 		new_index_row = index_row

		# 		new_letter = self.matrix[new_index_row][new_idx_letter]


		# print(new_letter)




def main():

	pf = Playfair(keyword = "reeeq")
	pf.create_matrix()
	pprint(pf.matrix)
	# pf.make_message_pair(message = "BAQLAWA")
	# print(pf.message_pair)

	pf.encrypt("RAT")
	# e = pf.get_letter_row('G')
	# print(e)
if __name__ == '__main__':
	main()


