#BookYogaRetreats
#Generic Keywords

######################################################################################

import sys

#set max cpc bid for keyword and ad group here
print "Please type in the max cpc for the landing page."
max_cpc = float(raw_input())

if type(max_cpc) != float:
    sys.exit("Please type in a price in form of 0.00")

######################################################################################

yoga = ['yoga']

holiday_words = [
'holiday',
'holidays',
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

'holiday retreat',
'holiday retreats',
'holidays retreat',
'holidays retreats',

'holiday resort',
'holiday resorts',
'holidays resort',
'holidays resorts',

'holiday package',
'holiday packages',
'holidays package',
'holidays packages',

'holiday deal',
'holiday deals',
'holidays deal',
'holidays deals',

'retreat holiday',
'retreat holidays',
'retreats holiday',
'retreats holidays',

'retreat vacation',
'retreat vacations',
'retreats vacation',
'retreats vacations',

'retreat resort',
'retreat resorts',
'retreats resort',
'retreats resorts',

'retreat camp',
'retreat camps',
'retreats camp',
'retreats camps',

'retreat package',
'retreat packages',
'retreats package',
'retreats packages',

'retreat center',
'retreat centers',
'retreats center',
'retreats centers',

'retreat centre',
'retreat centres',
'retreats centre',
'retreats centres',

'retreat deal',
'retreat deals',
'retreats deal',
'retreats deals',

'retreat training',
'retreat trainings',
'retreats training',
'retreats trainings',

'camp holiday',
'camp holidays',
'camps holiday',
'camps holidays',

'camp retreat',
'camp retreats',
'camps retreat',
'camps retreats',

'camp vacation',
'camp vacations',
'camps vacation',
'camps vacations',

'camp resort',
'camp resorts',
'camps resort',
'camps resorts',

'camp package',
'camp packages',
'camps package',
'camps packages',

'camp deal',
'camp deals',
'camps deal',
'camps deals',

'camp training',
'camp trainings',
'camps training',
'camps trainings',

'center retreat',
'center retreats',
'centers retreat',
'centers retreats',

'centre retreat',
'centre retreats',
'centres retreat',
'centres retreats',

'center training',
'center trainings',
'centers training',
'centers trainings',

'centre training',
'centre trainings',
'centres training',
'centres trainings',

'vacation retreat',
'vacation retreats',
'vacations retreat',
'vacations retreats',

'vacation camp',
'vacation camps',
'vacations camp',
'vacations camps',

'vacation package',
'vacation packages',
'vacations package',
'vacations packages',

'vacation deal',
'vacation deals',
'vacations deal',
'vacations deals',

'resort holiday',
'resort holidays',
'resorts holiday',
'resorts holidays',

'resort retreat',
'resort retreats',
'resorts retreat',
'resorts retreats',

'resort vacation',
'resort vacations',
'resorts vacation',
'resorts vacations',

'resort camp',
'resort camps',
'resorts camp',
'resorts camps',

'resort package',
'resort packages',
'resorts package',
'resorts packages',

'resort deal',
'resort deals',
'resorts deal',
'resorts deals',

'package holiday',
'package holidays',
'packages holiday',
'packages holidays',

'package retreat',
'package retreats',
'packages retreat',
'packages retreats',

'package vacation',
'package vacations',
'packages vacation',
'packages vacations',

'package resort',
'package resorts',
'packages resort',
'packages resorts',

'package camp',
'package camps',
'packages camp',
'packages camps',

'package deal',
'package deals',
'packages deal',
'packages deals',

'package training',
'package trainings',
'packages training',
'packages trainings',

'training holiday',
'training holidays',
'trainings holiday',
'trainings holidays',

'training retreat',
'training retreats',
'trainings retreat',
'trainings retreats',

'training vacation',
'training vacations',
'trainings vacation',
'trainings vacations',

'training camp',
'training camps',
'trainings camp',
'trainings camps',

'training package',
'training packages',
'trainings package',
'trainings packages',

'training center',
'training centers',
'trainings center',
'trainings centers',

'training centre',
'training centres',
'trainings centre',
'trainings centres'
]

months = [
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'Novebmer',
'December',
'']

year = ['2016', '']


a1 = [yoga, holiday_word1, holiday_word2, holiday_word3, months, year] #ex) yoga retreat holiday package
