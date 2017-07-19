from barbie.barbie import *
import barbie.susy_interface as susy

import subprocess
import os.path
from shutil import rmtree
import time

def barbiefy(dir, codes, disc, turma, lab):

	"""
	Code for testing the submit page while susy has no open class
	
	time.sleep(3)
	# Temporary while susy is offile
	results = list()
	for i in range(1, 11):
		results.append(BarbieTest(0, None, None, i, None, 'None', None))
	for i in range(21, 21):
		results.append(BarbieTest(i*3, 'Susy: Vamos dizer que isso fudeu', 'Barbie: Vamos dizer que isso fudeu', i, 'None', 'None', 'None'))
	return results
	"""
	# Try to compile the source code
	try:
		exec_file = compile_c(codes, temp=True, dir=dir)
		print('Código compilado com sucesso!')
	# If there was a compilation problem
	except subprocess.CalledProcessError:
		# Notificate the user about the problem
		print("Falha na compilação!")
		# Show the compilation output and end the program
		return 1

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
