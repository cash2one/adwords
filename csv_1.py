import csv
import re

template = "Book Yoga Retreats in {0}, {1} from {2} euros"

placeholders = re.findall('{\d+}', template)
fileName = 'test' + ascii(len(placeholders)) + '.csv'

csv = csv.reader(open(fileName, newline = ""))

for row in csv:
	if len(row) != len(placeholders):
		raise('FUUUCK')
	sentence = template
	for p in range(0, len(placeholders)):
		placeholder = ('{' + ascii(p) + '}')
		sentence = sentence.replace(placeholder, row[p])
	print(sentence)




######################################################################################

#framework: universal component lists
yoga = ['yoga']

holiday_word1 = [
'retreat',  
'retreats', 
'vacation',
'vacations',
'resort',
'resorts',
'camp',
'camps',
'package',
'packages',
'center',
'centers',
'centre',
'centres',
'deal',
'deals',
'training',
'trainings'
]

holiday_word2 = [
'retreat',  
'retreats', 
'vacation',
'vacations',
'resort',
'resorts',
'camp',
'camps',
'package',
'packages',
'center',
'centers',
'centre',
'centres',
'deal',
'deals',
'training',
'trainings',
''
]

######################################################################################

