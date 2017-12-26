#!/usr/local/bin/env python
import re
p = re.compile('^function\s(\w+_+\w+)')
with open('vmm_common.sh','r') as f:
	d = f.readlines()
with open('vmm_common.sh','w') as f:
	for line in d:
		if re.search('^function',line):
			upp = p.match(line).group()
			low = upp.lower()
			f.write(re.sub(upp,low, line))
		else:
			f.write(line)			#this is very important
