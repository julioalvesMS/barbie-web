from barbie.barbie import *
import barbie.susy_interface as susy

import subprocess
import os.path

def barbiefy(dir, codes, disc, turma, lab):

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

	# If the program is not set to run locally and no url was given,
	# prompt user for the class info and discover the url

	url = susy.discover_susy_url(disc, turma, lab)

	# List all susy files of open tests
	in_files, res_files = susy.get_susy_files(url)
	# Download all the open tests
	susy.download_tests(url, in_files, res_files, tests_dir_name)

	# If we sucessufuly got all needed files,
	# we may run all tests and compare our output with the expected
	if in_files and res_files:
		run_and_compare(exec_file, in_files, res_files, tests_dir_name)
