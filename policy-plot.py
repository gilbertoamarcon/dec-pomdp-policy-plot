#!/usr/bin/env python

import re
import os
import shutil
import sys


if len(sys.argv) < 2:
	print '\033[31m[ERROR]\033[0m Missing argument: Please provide the input file name.'
	sys.exit(2)
else:
	input_file = sys.argv[1]

working_dir = input_file+'_agents/'

# Removing / Creating directory
try:
	shutil.rmtree(working_dir)
except:
	pass

os.mkdir(working_dir)

reg = '(\w+)\s+(\w+)\s*\{([^}]*)\}'

# Reading XML
with open(input_file,'rb') as f:
	pol = f.read()

# Parsing 
parsed = re.findall(reg,pol)
for p in parsed:

	# File names and content
	agent_policy_dot_file_name = working_dir+p[1]+'.dot'
	agent_policy_svg_file_name = working_dir+p[1]+'.svg'
	agent_policy_dot_format = p[0]+' '+p[1]+'{'+p[2]+'}\n'

	# Graphviz dot description
	with open(agent_policy_dot_file_name,'w') as f:
		f.write(agent_policy_dot_format)

	# Graphviz SVG
	command = 'dot -Tsvg ' + agent_policy_dot_file_name + ' -o ' + agent_policy_svg_file_name
	os.system(command)




