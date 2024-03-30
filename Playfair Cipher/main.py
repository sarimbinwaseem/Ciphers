from string import ascii_uppercase
from utils import PlayfairUtils

class Playfair(PlayfairUtils):
	"""docstring for Playfair"""
	def __init__(self, keyword):
		super().__init__()
		self.keyword = self.clean_keyword(keyword.upper())

		
	def create_matrix(self):
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




def main():

	pf = Playfair("mant")
	pf.create_matrix()
	print(pf.matrix)
if __name__ == '__main__':
	main()