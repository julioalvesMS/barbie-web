from barbie.barbie import *
import barbie.susy_interface as susy

import subprocess
import os.path
import sys
from shutil import rmtree
from threading import Timer

constant_DirectoryDuration = 36

# Pode ser removido depois dos testes
import time

def barbiefy(dir, codes, disc, turma, lab):

	# Try to compile the source code
	try:
		exec_file, gcc_f, sucess = compile_c(codes, temp=True, dir=dir)
		assert sucess, "Falha na compilação"
		# If there was a compilation problem
	except AssertionError as e:
		eprint("Falha na compilação!\n")
		# Show the compilation output and end the program
		with open(gcc_f, 'r') as gcc:
			eprint(gcc.read())
		return None

	#"""
	# Code for testing the submit page while susy has no open class

	time.sleep(3)
	# Temporary while susy is offile
	results = list()
	for i in range(1, 11):
		results.append(BarbieTest(0, None, None, i, None, 'None', None))
	for i in range(11, 21):
		results.append(BarbieTest(i*3, 'Susy: Vamos dizer que isso fudeu', 'Barbie: Vamos dizer que isso fudeu', i, 'None', 'None', 'None'))
	return results
	#"""

	tests_dir_name = os.path.join(dir, 'testes/')

	in_files = None
	res_files = None


	# Connect to susy system and discover the test page url
	url = susy.discover_susy_url(disc, turma, lab)
	# List all susy files of open tests
	in_files, res_files = susy.get_susy_files(url)

	# Download all the open tests
	susy.download_tests(url, in_files, res_files, tests_dir_name)

	results = list()
	# If we sucessufuly got all needed files,
	# we may run all tests and compare our output with the expected
	if in_files and res_files:
		results = run_and_compare(exec_file, in_files, res_files, tests_dir_name)

	return results

def cleanUp(folder):
	rmtree(folder, ignore_errors=True)

def timedCleanUp(folder):
	tmr = Timer(constant_DirectoryDuration, cleanUp, args=[folder])
	tmr.start()
