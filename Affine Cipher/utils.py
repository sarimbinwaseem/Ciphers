"""Utilities for Affine Cipher"""

class AffineMaths():
	"""This class contains mathematics for Affine Cipher.

	gcd: calculates GCD of number and len(table).
	mul_inverse: calculates multiplicative inverse of a number.
	"""
	def __init__(self, arg):
		super().__init__()
		self.arg = arg
