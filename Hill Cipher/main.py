#!/usr/bin/python

"""
Code implementation by Sarim Bin Waseem
github.com/sarimbinwaseem
linkedin.com/in/sarimbinwaseem

Hill Cipher
"""
import argparse
from Utils.utils import Utils

class HillCipher(Utils):
	"""docstring for HillCipher"""
	# def __init__():
	# 	super().__init__()
	# 	self.arg = arg

	# def make_f(self, msg):
	# 	self.make_message_pair(msg)

def main():

	hc = HillCipher()
	w = hc.make_message_pair("SARIM")
	print(w)

if __name__ == "__main__":
	main()
