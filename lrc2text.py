import re
import sys
from os import path

version = 0.1

if len(sys.argv) == 2:
	fname = sys.argv[1]
	if path.isfile(fname):
		if fname.endswith('.lrc'):
			lfile = open(fname,'r', encoding='utf16') 
			lines = lfile.readlines()
			cleanlines = list(map(str.strip, lines))
			
			ofname = fname[:-3]+'-lrc2.txt'
			
			outf = open(ofname, 'w')
			print('LRC properties:\n')
			#~ print(cleanlines)
			for line in cleanlines:
				#~ print(line)
	
				me = re.fullmatch(r'\[\d\d:\d\d.\d\d\](?P<lrcline>.+)?', line)

				if not me:
					#~ print(line) 
					ta = re.fullmatch(r'\[(?P<pname>.+): (?P<value>.+)\]', line)
					if ta != None:
						pname = ta.group('pname')
						value = ta.group('value')
						print(f'{pname}: {value}')
				else:
					lrcline = me.group('lrcline')
					if lrcline == None:
						outf.write('\n')
					else:
						outf.write(lrcline+'\n')
		else:
			print('Wrong input file. You need to feed me with a *.lrc file')
	else:
		print('Invalid, non-existant file')
else:
	print('Wrong number of arguments')