######################################################################################

#BookYogaRetreats
#Automatic Longtail Keyword & Ad Copy Generator for Destination Landing Pages Only in BookYogaRetreats

#This code is used where the landing page ONLY contains destination.
#This means no category and no style, even when combined with a destination.

#The script has two inputs:
#(a) landing page url
#(b) max cpc

#For a provided landing page with only destination, this code will automatically generate:
#(a) longtail keywords (exact match) with provided max cpc
#(b) ad copies 

#The script exports two seperate csv files in the current directory:
#(a) one file consists of the longtail keywords (exact match)
#(b) the other file consists of the ad copies
#Both files are readily prepared for bulk upload in Google Adwords.

######################################################################################

#Coverage
# Categories Style Destination
#   0          0       0        (null)
#   0          0       1        (covered in this code)
#   0          1       0        (covered in style.py)
#   0          1       1        (will be covered in style.py)
#   1          0       0        (covered in cat.py)
#   1          0       1        (covered in cat.py)
#   1          1       0        (covered in cat.py)
#   1          1       1        (covered in cat.py)

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

#ask user to provide landing page url
import urllib3
import urllib.request
from bs4 import BeautifulSoup

print ("Please type in the landing page url.")
url = input()
print ("")

######exception for non-url input goes here######## 

import sys

#set max cpc bid for keyword and ad group here
print ("Please type in the max cpc for the landing page.")
max_cpc = float(input())
print ("")

if type(max_cpc) != float:
    sys.exit("Please type in a price in form of 0.00")

######################################################################################

#extract the number of listings from landing page title
soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
page_title = str(soup.title.string)
count = page_title.split()[0]

if count.isdigit() == False:
    #print
    sys.exit("[Alert] Cannot proceed further: the landing page has less than 3 listings. Please choose a different landing page with at least 3 listings.")

######################################################################################

#find and extract all characters after the last occuring dash (destination)
#then strip punctuations (dash replaced with space)
else:
    find = '/'
    dest_index = max(pos for pos, char in enumerate(url) if char == find)+1
    destination = url[dest_index:].title().replace("-", " ").split()
    
    #if there is more than one destination (e.g. Asia and Oceania)
    if 'And' in destination:
        cut = destination.index('And')
        destination1 = ' '.join(destination[:cut])
        destination2 = ' '.join(destination[cut+1:])
        destination_back = ['in '+destination1, destination1, 'in '+destination2, destination2]
        destination_front = [destination1, destination2]
        
        print ("")
        print ("[Checking] destination_back:", destination_back)
        print ("[Checking] destination_front:", destination_front)
        
        headline1 = count+' '+' '.join(page_title.split()[1:3] + destination_front[0].split())
        headline2 = ' '.join(page_title.split()[1:3] + destination_front[1].split()) + ' 2016'
        headline3 = count+' '+' '.join(page_title.split()[1:3] + destination_front[0].split())
        headline4 = ' '.join(page_title.split()[1:3] + destination_front[1].split()) + ' 2016'
        
        headlines = [headline1, headline2, headline3, headline4]
    
    #if there is only one destination (e.g. Germany)    
    else: 
        destination1 = ' '.join(destination)
        destination_back = ['in '+destination1, destination1]
        destination_front = [destination1]

        print ("[Checking] destination_back:", destination_back)
        print ("[Checking] destination_front:", destination_front)

        headline1 = count+' '+ ' '.join(page_title.split()[1:3] + destination_front[0].split())
        headline2 = ' '.join(page_title.split()[1:3] + destination_front[0].split()) + ' 2016'
        
        headlines = [headline1, headline2]

print ("[Checking] headlines:"), headlines

for i in range(len(headlines)):
    if (len(headlines[i]) > 25) and ('2016' in headlines[i]):
        headlines[i] = headlines[i].replace(' 2016', '')
        
destination_f = destination_front[:]

if destination_front[0] == 'United Arab Emirates':
    destination_front.append('UAE')
    destination_back.append('in UAE')
    destination_back.append('UAE')
elif destination_front[0] == 'South Africa':
    destination_front.append('SA')
    destination_back.append('in SA')
    destination_back.append('SA')
elif destination_front[0] == 'New Zealand':
    destination_front.append('NZ')
    destination_back.append('in NZ')
    destination_back.append('NZ')
elif destination_front[0] == 'United Kingdom':
    destination_front.append('UK')
    destination_front.append('the UK')
    destination_back.append('in UK')
    destination_back.append('UK')
    destination_back.append('in the UK')
    destination_back.append('the UK')
elif destination_front[0] == 'Massachusetts':
    destination_front.append('MA')
    destination_back.append('in MA')
    destination_back.append('MA')
elif destination_front[0] == 'North Carolina':
    destination_front.append('NC')
    destination_back.append('in NC')
    destination_back.append('NC')
elif destination_front[0] == 'South Carolina':
    destination_front.append('SC')
    destination_back.append('in SC')
    destination_back.append('SC')
elif destination_front[0] == 'Western Australia':
    destination_front.append('WA')
    destination_back.append('in WA')
    destination_back.append('WA')
elif destination_front[0] == 'Pennsylvania':
    destination_front.append('PA')
    destination_back.append('in PA')
    destination_back.append('PA')
elif destination_front[0] == 'Usa':
    destination_front[0] = 'USA'
    destination_front.append('US')
    destination_front.append('the US')
    destination_front.append('United States')
    destination_back[0] = 'in USA'
    destination_back[1] = 'USA'
    destination_back.append('in US')
    destination_back.append('US')
    destination_back.append('in the US')
    destination_back.append('the US')
    destination_back.append('in United States')
    destination_back.append('United States')
elif destination_front[0] == 'California':
    destination_front.append('CA')
    destination_back.append('in CA')
    destination_back.append('CA')
elif destination_front[0] == 'Central Coast California':
    destination_front.append('Central Coast CA')
    destination_back.append('in Central Coast CA')
    destination_back.append('Central Coast CA')
elif destination_front[0] == 'Nevada California':
    destination_front[0] = 'Nevada, California'
    destination_back[0] = 'in Nevada, California'
    destination_back[1] = 'Nevada, California'
    destination_front.append('Nevada, CA')
    destination_back.append('in Nevada, CA')
    destination_back.append('Nevada, CA')
elif destination_front[0] == 'Northern California':
    destination_front.append('Northern CA')
    destination_back.append('in Northern CA')
    destination_back.append('Northern CA')
elif destination_front[0] == 'Queensland':
    destination_front.append('qld')
    destination_back.append('in qld')
    destination_back.append('qld')
elif destination_front[0] == 'New York':
    destination_front.append('NY')
    destination_back.append('in NY')
    destination_back.append('NY')
elif destination_front[-1] == 'Caribbean':
    destination_front.append('the Caribbean')
    destination_back.append('in the Caribbean')
    destination_back.append('the Caribbeans')
    destination_front.append('South America')
    destination_back.append('in South America')
    destination_back.append('South America')
    destination_front.append('Central America')
    destination_back.append('in Central America')
    destination_back.append('Central America')
elif destination_front[0] == 'New Jersey':
    destination_front.append('NJ')
    destination_back.append('in NJ')
    destination_back.append('NJ')
elif destination_front[0] == 'Koh Samui':
    destination_front.append('Samui')
    destination_back.append('in Samui')
    destination_back.append('Samui')

######################################################################################

#prepare keyword components
a1 = [yoga,holiday_word1,holiday_word2,destination_back]
a2 = [destination_front,yoga,holiday_word1,holiday_word2]

import itertools

#create all possible combinations where destination is in the back
comb = list(itertools.product(*a1)) 

#create all possible combinations where destination is in the front
comb2 = list(itertools.product(*a2)) 

#remove adjacent duplicates
#e.g. holidays holidays
#e.g. holiday holidays
#e.g. holidays holiday
i = 0
for i in range(len(comb)):
    if comb[i][1] == comb[i][2]:
        comb[i] = (comb[i][0], comb[i][1], comb[i][3])
    elif comb[i][1]+'s' == comb[i][2]:
        comb[i] = (comb[i][0], comb[i][1], comb[i][3])
    elif comb[i][1] == comb[i][2]+'s':
        comb[i] = (comb[i][0], comb[i][1], comb[i][3])
    i = i+1

i = 0
for i in range(len(comb2)):
    if comb2[i][2] == comb2[i][3]:
        comb2[i] = (comb2[i][0], comb2[i][1], comb2[i][2])
    elif comb2[i][2]+'s' == comb2[i][3]:
        comb2[i] = (comb2[i][0], comb2[i][1], comb2[i][2])
    elif comb2[i][2] == comb2[i][3]+'s':
        comb2[i] = (comb2[i][0], comb2[i][1], comb2[i][2])
    i = i+1

#remove duplicates
comb = list(set(comb)) 
comb2 = list(set(comb2))

#join the 2 lists
all_comb = comb + comb2

for i in range(len(all_comb)):
    all_comb[i] = tuple(x for x in all_comb[i] if x != '')

#join strings within the list
results = []

for i in range(len(all_comb)):
    results.append('['+(' '.join(all_comb[i]))+']')
    i+1

#sort the result in alphabetical order
results = sorted(set(results))

######################################################################################

#prepare csv file  for keywords

#if there is only one destination
if len(destination_back) == 1:
    str_destination = destination_back[0]

#if there are more than one destination    
else:
    str_destination = ' '.join(destination).replace('And', '&')

######################################################################################

#column titles for keywords
kw_column_titles = ["Keyword state", 
                    "Keyword", 
                    "Match type",
                    "Campaign",
                    "Ad group",
                    "Keyword max CPC",
                    "Ad group max CPC"]

######################################################################################                    

#prepare column values
keyword_state = ['enabled'] * len(results)
#keyword -> results
match_type = ['Exact'] * len(results)
campaign = ['Longtail %s'%str_destination] * len(results)
ad_group = ['Longtail %s %s'%('Retreats', str_destination)] * len(results)
keyword_max_cpc = [max_cpc] * len(results)
ad_group_max_cpc = [max_cpc] * len(results)

######################################################################################

#tweaks before zipping
for i in range(len(campaign)): #Usa -> USA, Uk -> UK, United Kingdom -> UK
    if 'Usa' in campaign[i]:
        campaign[i] = campaign[i].replace('Usa', 'USA')
    elif 'Uk' in campaign[i]:
        campaign[i] = campaign[i].replace('Uk', 'UK')
    elif 'United Kingdom' in campaign[i]:
        campaign[i] = campaign[i].replace('United Kingdom', 'UK')

for i in range(len(ad_group)): #Usa -> USA, Uk -> UK, United Kingdom -> UK
    if 'Usa' in ad_group[i]:
        ad_group[i] = ad_group[i].replace('Usa', 'USA')
    elif 'Uk' in ad_group[i]:
        ad_group[i] = ad_group[i].replace('Uk', 'UK')
    elif 'United Kingdom' in ad_group[i]:
        ad_group[i] = ad_group[i].replace('United Kingdom', 'UK')

######################################################################################

#zip each columns

rows = []
for i in range(len(results)):
    rows.append([keyword_state[i],
                 results[i],
                 match_type[i],
                 campaign[i],
                 ad_group[i],
                 keyword_max_cpc[i],
                 ad_group_max_cpc[i]])

######################################################################################

#export longtail keywords in a csv file
import csv

file_name = "%s keywords.csv" %destination_front
new_csv = open(file_name, 'w')
open_file_object = csv.writer(new_csv)



# for i in range(len(kw_column_titles)):
#     kw_column_titles[i] = bytes(kw_column_titles[i])

#write rows
open_file_object.writerow(kw_column_titles)

#write columns
for row in rows:
    open_file_object.writerow(row)

new_csv.close()

print ("")
print ("""[Notification] %i longtail keywords for %s are generated successfully. 
Please check your current directory for the stored result in a csv file. """ %(len(results), destination_front))

######################################################################################

#prepare csv file for ads

#set ad descriptions here       
desc11 = "Reviews & Best Price Guarantee!" 
desc12 = "Reserve Your Dream Retreat Today"

desc21 = "Reviews & Best Price Guarantee!"
desc22 = "%s Top Rated Package Deals Online"%count

#how many ads?
how_many_ads = int(len(destination_f) * 4)

######################################################################################

#prepare column titles for ads
ac_column_titles = ["Ad state",
                    "Ad",
                    "Description line 1",
                    "Description line 2",
                    "Display URL",
                    "Final URL",
                    "Device preference type",
                    "Campaign",
                    "Ad group",
                    "Ad type"]

######################################################################################

#prepare column values for ads
ad_state = ['enabled'] * how_many_ads
ad = headlines * 2
d1 = ([desc11] * 2 + [desc21] * 2) * len(destination_f)
d2 = ([desc12] + [desc22]) * 2 * len(destination_f)
display_url = ['www.bookyogaretreats.com/%s'%url[dest_index:].title()] * how_many_ads
final_url = [url] * how_many_ads
device = ['All'] * int(how_many_ads / 2) + ['Mobile'] * int(how_many_ads / 2) 
campaign = ['Longtail %s'%str_destination] * how_many_ads
ad_group = ['Longtail %s %s'%('Retreats', str_destination)] * how_many_ads
ad_type = ['Text ad'] * how_many_ads

######################################################################################

#tweaks before zipping
for i in range(len(campaign)): #Usa -> USA, Uk -> UK, United Kingdom -> UK
    if 'Usa' in campaign[i]:
        campaign[i] = campaign[i].replace('Usa', 'USA')
    elif 'Uk' in campaign[i]:
        campaign[i] = campaign[i].replace('Uk', 'UK')
    elif 'United Kingdom' in campaign[i]:
        campaign[i] = campaign[i].replace('United Kingdom', 'UK')

for i in range(len(ad_group)): #Usa -> USA, Uk -> UK, United Kingdom -> UK
    if 'Usa' in ad_group[i]:
        ad_group[i] = ad_group[i].replace('Usa', 'USA')
    elif 'Uk' in ad_group[i]:
        ad_group[i] = ad_group[i].replace('Uk', 'UK')
    elif 'United Kingdom' in ad_group[i]:
        ad_group[i] = ad_group[i].replace('United Kingdom', 'UK')

for i in range(len(ad)): #Usa -> USA, Uk -> UK, United Kingdom -> UK

    if 'Usa' in ad[i]:
        ad[i] = ad[i].replace('Usa', 'USA')
    elif 'Uk' in ad[i]:
        ad[i] = ad[i].replace('Uk', 'UK')
    elif 'United Kingdom' in ad[i]:
        ad[i] = ad[i].replace('United Kingdom', 'UK')

    if len(ad[i]) > 25: #yoga retreats the americas -> yoga retreats americas
        if 'The' in ad[i]:
            ad[i] = ad[i].replace("The Americas", 'Americas')

for i in range(len(display_url)): #www.../United-Kingom -> www.../UK
    if 'United-Kingdom' in display_url[i]:
        display_url[i] = 'www.bookyogaretreats.com/UK'
    elif 'Canary-Islands' in display_url[i]:
        display_url[i] = 'www.bookyogaretreats.com/Spain'

######################################################################################

#zip column
ac_rows_all =[]
for i in range(how_many_ads):
    ac_rows_all.append([ad_state[i],
                    ad[i],
                    d1[i],
                    d2[i],
                    display_url[i],
                    final_url[i],
                    device[i],
                    campaign[i],
                    ad_group[i],
                    ad_type[i]])

######################################################################################

#export ads into a csv file
file_name = "%s ads.csv" %destination_f
new_csv = open(file_name, 'w')
open_file_object = csv.writer(new_csv)

#rows
open_file_object.writerow(ac_column_titles)

#columns
open_file_object.writerows(ac_rows_all)
new_csv.close()

print ("")
print ("""[Notification] All %s ads for %s are generated successfully. 
Please check your current directory for the stored result in a csv file. """ %(len(ac_rows_all), destination_front))
print ("")
######################################################################################

for i in range(how_many_ads):
    if len(ad[i]) > 25:
        print ("[Warning] Headline %i longer than 25 chars" %(i+1))
        print (ad[i])
        print (len(ad[i]))
        print ("")
    if len(d1[i]) > 35:
        print ("[Warning] Description line 1 longer than 35 chars")
        print (d1[i])
        print (len(d1[i]))
        print ("")
    if len(d2[i]) > 35:
        print ("[Warning] Description line 2 longer than 35 chars")
        print (d2[i])
        print (len(d2[i]))
        print ("")
    if len(display_url[i]) > 35:
        print ("[Warning] Display URL longer than 35 chars")
        print (display_url[i])
        print (len(display_url[i]))
        print ("")

######################################################################################