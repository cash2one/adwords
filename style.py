#BookYogaRetreats
#Style Only Keywords

######################################################################################

import sys

#user provides the style 

print "Please type in the style of yoga."
style = raw_input()
yoga = ['%s yoga'%style]

#set max cpc bid for keyword and ad group here
print "Please type in the max cpc for the landing page."
max_cpc = float(raw_input())

if type(max_cpc) != float:
    sys.exit("Please type in a price in form of 0.00")

######################################################################################

holiday_word1 = [
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
'deals']

holiday_word2 = [
'package',
'packages',
'resort',
'resorts',
'retreat',
'retreats',
'deal',
'deals',
'']

######################################################################################

import itertools

a1 = [yoga, holiday_word1, holiday_word2]
a2 = [holiday_word1, holiday_word2, yoga]
a3 = [holiday_word1, yoga, holiday_word2]

comb1 = list(set(itertools.product(*a1)))
comb2 = list(set(itertools.product(*a2)))
comb3 = list(set(itertools.product(*a3)))

comb = comb1 + comb2 + comb3

######################################################################################

#clean the list
for i in range(len(comb)): #remove all empty strings
    comb[i] = tuple(x for x in comb[i] if x != '')
    comb[i] = ' '.join(comb[i])
    comb[i] = tuple(comb[i].split())

all_comb = list(set(comb))

#remove adjacent duplicates
#e.g. retreat retreat
#e.g. retreat retreats
#e.g. retreats retreat
#e.g. yoga yoga

for i in range(len(all_comb)):
    a = all_comb[i]
    for x in range(len(a)-1):
        if (a[x] == a[x+1]) or (a[x]+'s' == a[x+1]) or (a[x] == a[x+1]+'s'):
            all_comb[i] = a[:x+1] + a[x+2:]

def remove_duplicates(values): #aux
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

all_comb = sorted(set(all_comb)) #remove duplicates and sort the list in an alphabetical order 

#remove keywords with plural/singular duplicates within them 
#e.g. yoga retreat budget retreat, yoga retreats budget retreat

for i in range(len(all_comb)): #yoga retreat budget retreat
    all_comb[i] = tuple(remove_duplicates(all_comb[i]))

for i in range(len(all_comb)): #yoga retreats budget retreat, yoga retreat budget retreats
    if (all_comb[i][-1]+'s' == all_comb[i][1]) or (all_comb[i][-1] == all_comb[i][1]+'s'): 
        all_comb[i] = []

all_comb = [x for x in all_comb if x != []] #remove empty lists in all_comb

for i in range(len(all_comb)): #remove all duplicate words 
    all_comb[i] = tuple(remove_duplicates(all_comb[i]))
    all_comb[i] = '[' + ' '.join(all_comb[i]) + ']'

#remove duplicates, sort in alphabetical order
all_comb = sorted(set(all_comb)) 

######################################################################################

#export keywords onto a csv file
import csv

file_name = "%s keywords.csv" %style

with open(file_name, 'wb') as f:
    writer = csv.writer(f)
    for i in range(len(all_comb)):
        writer.writerow([all_comb[i]])

print "[Notification] %s [style] keywords are generated successfully. Please check your current directory for the output in a CSV file." %len(all_comb)
