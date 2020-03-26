#!/usr/bin/env python
import logging
import argparse


logging.basicConfig()
LOGGER = logging.getLogger()
LOGGER.setLevel('DEBUG')

def main():
	""" The main code for this project
	"""
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("--atestinput", help=' test input parameter to allow for seeing what happens if it is not set', choices=['set'], required=True)
	args = parser.parse_args()
	LOGGER.info('We are going to return a test value')
	print(','.join("DummyHost3", args.atestinput)

if __name__ == '__main__':
    	main()
