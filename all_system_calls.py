import os
from collections import Counter
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import numpy as np
from scipy import sparse

import util

def find_all_system_calls(direc = 'train'):
	
	sys_call_dict = {}

	for datafile in os.listdir(direc):

		xml_tree = ET.parse(os.path.join(direc,datafile))
		in_all_section = False

		for el in xml_tree.iter():
			if el.tag == 'all_section' and not in_all_section:
				in_all_section = True
			elif el.tag == 'all_section' and in_all_section:
				in_all_section = False
			elif in_all_section:
				sys_call_dict.update({el.tag: 1})

	return sys_call_dict.keys()

def main():
	all_system_calls = find_all_system_calls()
	print len(all_system_calls)
	print all_system_calls
	print sorted(all_system_calls)

if __name__ == '__main__': main()

