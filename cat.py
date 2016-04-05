######################################################################################

#ask user to provide landing page url.
import urllib2
from BeautifulSoup import BeautifulSoup

print "Please type in the landing page url."
url = raw_input()
print ""

#######################################################################################
import sys

#set max cpc bid for keyword and ad group here
print "Please type in the max cpc for the landing page."
max_cpc = float(raw_input())

if type(max_cpc) != float:
    sys.exit("Please type in a price in form of 0.00")

#######################################################################################

#extract the number of listings from landing page title
soup = BeautifulSoup(urllib2.urlopen(url))
page_title = str(soup.title.string)
count = page_title.split()[0]

if count.isdigit() == False:
    #print ""
    sys.exit("[Alert] Cannot proceed further: the landing page has less than 3 listings. Please choose a different landing page with at least 3 listings.")

#######################################################################################

#prepare keyword components
yoga = ['yoga']

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

remove_list = [
'yoga',
'retreat',  
'retreats', 
'vacation',
'vacations',
'package',
'packages',
'resort',
'resorts',
'camp',
'camps',
'center',
'centers',
'centre',
'centres',
'and'
]

requires_and = [
'beach',
'horse riding',
'painting',
'cooking',
'cycling',
'dancing',
'detox',
'health',
'hiking',
'meditation',
'pilates',
'running',
'sailing',
'silent',
'ski',
'spa',
'spiritual',
'surf',
'surfing',
'walking',
'wellness',
'writing'
]

cat = ''
style = ''
destination = ''
destination1 = ''
destination2 = ''
destination_front = ''
destination_back = ''

cat_mrkr = '/c/'
style_mrkr = '/s/'
cont_mrkr = '/d/'

######################################################################################

#extract categories, styles and destination from the URL
import itertools

cat_idx_front = url.find(cat_mrkr)+3 #find the starting index of categories (after /c/)

if (cont_mrkr not in url) and (style_mrkr not in url): #only categories
    cat_idx_back = len(url) #find the ending index of categories

    cat = url[cat_idx_front:cat_idx_back].replace("-", " ") #replace dash with space

    #remove word(s) in category that is already mentioned in prep list
    #e.g. couples yoga retreat -> couples
    #e.g. budget retreats -> budget
    #except for 200/300/500 hour yoga teacher training
    cat = ' '.join(i for i in cat.split() if i not in remove_list)
    cat = [cat] #listify the category

    destination_f = '' #no destination

######################################################################################

elif (cont_mrkr not in url) and (style_mrkr in url): #categories and style
    cat_idx_back = url.find(style_mrkr) #find the ending index of categories (before /s/)

    style_idx_front = url.find(style_mrkr)+3 #find the starting index of style (after /s/)
    style_idx_back = len(url) #find the ending index of style
    
    style = url[style_idx_front:style_idx_back].replace('-', " ") 
    style = [style] #listify style
    
    cat = url[cat_idx_front:cat_idx_back].replace("-", " ") #replace dash with space

    #remove word(s) in category that is already mentioned in prep list
    #e.g. yoga teacher training -> teacher training
    #e.g. budget retreats -> budget
    cat = ' '.join(i for i in cat.split() if i not in remove_list)
    cat = [cat] #listify categories

    destination_f = '' #no destination

######################################################################################

elif (cont_mrkr in url) and (style_mrkr not in url): #categories and destination
    cat_idx_back = url.find(cont_mrkr) #find the ending index of categories (before /d/)

    find = '/'
    cont_idx = max(pos for pos, char in enumerate(url) if char == find)+1 #index of the last slash. last slash is always followed by destination
    destination = url[cont_idx:].title().replace("-", " ").split() #replace dash with space, listify destination

    cat = url[cat_idx_front:cat_idx_back].replace("-", " ") #replace dash with space

    #remove word(s) in category that is already mentioned in prep list
    #e.g. yoga teacher training -> teacher training
    #e.g. budget retreats -> budget
    cat = ' '.join(i for i in cat.split() if i not in remove_list)
    cat = [cat] #listify categories
    
    #if there is more than one destination (e.g. Asia and Oceania)
    if 'And' in destination:
        cut = destination.index('And')
        destination1 = ' '.join(destination[:cut])
        destination2 = ' '.join(destination[cut+1:])
        destination_back = ['in '+destination1, destination1, 'in '+destination2, destination2]
        destination_front = [destination1, destination2] 
        
        destination_f = destination_front[:] #destinations before adding variants
        
    #if there is only one destination (e.g. Germany)    
    else: 
        destination1 = ' '.join(destination)
        destination_back = ['in '+destination1, destination1]
        destination_front = [destination1]
        
        destination_f = destination_front[:] #destination before adding variants

        #adding destination name variants
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

elif (cont_mrkr in url) and (style_mrkr in url): #categories, style and destination
    cat_idx_back = url.find(style_mrkr) #find the ending index of category

    style_idx_front = url.find(style_mrkr)+3 #find the starting index of style
    style_idx_back = url.find(cont_mrkr) #find the ending index of style
    style = url[style_idx_front:style_idx_back] #style
    style = url[style_idx_front:style_idx_back].replace('-', " ") #replace dash with space
    style = [style] #listify style 

    find = '/'
    cont_idx = max(pos for pos, char in enumerate(url) if char == find)+1 #index of the last slash. last slash is always followed by destination
    destination = url[cont_idx:].title().replace("-", " ").split() #replace dash with space, listify destination
    
    destination_f = destination_front[:] #destination without variants
    
    cat = url[cat_idx_front:cat_idx_back].replace("-", " ") #replace dash with space

    #remove word(s) in category that is already mentioned in prep list
    #e.g. yoga teacher training -> teacher training
    #e.g. budget retreats -> budget
    cat = ' '.join(i for i in cat.split() if i not in remove_list)
    cat = [cat] #listify category
    
    #if there is more than one destination (e.g. Asia and Oceania)
    if 'And' in destination:
        cut = destination.index('And')
        destination1 = ' '.join(destination[:cut])
        destination2 = ' '.join(destination[cut+1:])
        destination_back = ['in '+destination1, destination1, 'in '+destination2, destination2]
        destination_front = [destination1, destination2]
        
        destination_f = destination_front[:]

    #if there is only one destination (e.g. Germany)    
    else: 
        destination1 = ' '.join(destination)
        destination_back = ['in '+destination1, destination1]
        destination_front = [destination1]
        
        destination_f = destination_front[:] #destination without variants

        #adding destination name variants
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

#exceptions/variants per category
#200/300/500 hour yoga teacher training exception
if 'hour' in cat[0]:
    cat[0] = cat[0].split()
    cat[0].insert(2, 'yoga')
    cat[0] = ' '.join(cat[0])
    yoga = [''] 

#yoga holidays exception
if 'holidays' in cat[0]:
    cat[0] = 'yoga holiday'
    cat.append('yoga holidays')
    yoga = ['']
    holiday_word1 = ['retreat',
                     'retreats',
                     'vacation',
                     'vacations',
                     'package',
                     'packages',
                     'resort',
                     'resorts',
                     'camp',
                     'camps'] 
    
#ashrams variant
if 'ashrams' in cat[0]:
    cat.append('ashram')

#beginner variant
if 'beginner' in cat[0]:
    cat.append('for beginner')
    cat.append('for a beginner')
    
    cat.append('beginners')
    cat.append('for beginners')

#couples variant
if 'couples' in cat[0]:
    cat.append('for couples')

    cat.append('couple')
    cat.append('for couple')
    cat.append('for a couple')
    
#family variant
if 'family' in cat[0]:
    cat.append('for family')
    cat.append('for a family')

    cat.append('families')
    cat.append('for families')
    
#women variant
if 'women' in cat[0]:
    cat.append('womens')
    cat.append('for women')
        
    cat.append('woman')
    cat.append('womans')
    cat.append('for woman')
    cat.append('for a woman')

#surfing variant
if 'surf' in cat[0]:
    cat.append('surfing')

#singles variant
if 'singles' in cat[0]:
    cat.append('for singles')

    cat.append('single')
    cat.append('for single')
    cat.append('for a single')

#short (weekend & short breaks) exception/variant
if cat[0] == 'short':
    cat[0] = 'yoga weekend'
    cat.append('weekend yoga')
    cat.append('yoga weekends')
    cat.append('weekends yoga')
    cat.append('yoga break')
    cat.append('yoga breaks')
    cat.append('short yoga break')
    cat.append('short yoga breaks')
    cat.append('yoga short break')
    cat.append('yoga short breaks')
    cat.append('short yoga retreat')
    cat.append('short yoga retreats')
    yoga = ['']
    holiday_word2 = ['']

#budget variant
if 'budget' in cat[0]:
    cat.append('on a budget')
    cat.append('affordable')
    cat.append('cheap')
    cat.append('inexpensive')

######################################################################################

#check variables
print """
[Checking] category:""", cat
print "[Checking] style:", style
print "[Checking] destination_back:", destination_back
print "[Checking] destination_front:", destination_front
print "[Checking] destination_f:", destination_f

######################################################################################

#make combination lists and generate keywords
if (cont_mrkr not in url) and (style_mrkr not in url): #only categories

    a1 = [cat, yoga, holiday_word1, holiday_word2] #ex) budget yoga retreat package
    a2 = [yoga, cat, holiday_word1, holiday_word2] #ex) yoga for beginners retreat deal
    a3 = [cat, holiday_word1, yoga, holiday_word2] #ex) budget holiday yoga retreat
    a4 = [yoga, holiday_word1, cat, holiday_word2] #ex) yoga retreat budget package
    a5 = [cat, holiday_word1, holiday_word2, yoga] #ex) luxury holiday resort yoga
    a6 = [yoga, holiday_word1, holiday_word2, cat] #ex) yoga holiday resort budget
    a7 = [cat, yoga] #ex) detox yoga
    a8 = [yoga, cat] #ex) yoga and meditation

    comb1 = list(set(itertools.product(*a1)))
    comb2 = list(set(itertools.product(*a2)))
    comb3 = list(set(itertools.product(*a3)))
    comb4 = list(set(itertools.product(*a4)))
    comb5 = list(set(itertools.product(*a5)))
    comb6 = list(set(itertools.product(*a6)))
    comb7 = list(set(itertools.product(*a7)))
    comb8 = list(set(itertools.product(*a8)))

    all_comb = comb1 + comb2 + comb3 + comb4 + comb5 + comb6 + comb7 +comb8

######################################################################################

elif (cont_mrkr not in url) and (style_mrkr in url): #categories and style
    
    a1 = [style, cat, holiday_word1, holiday_word2] #ashtanga yoga luxury retreat package
    a2 = [cat, style, holiday_word1, holiday_word2] #luxury ashtanga yoga holiday deal
    a3 = [style, holiday_word1, cat, holiday_word2] #kundalini yoga retreat luxury package
    a4 = [cat, holiday_word1, style, holiday_word2] #budget retreat ashtanga yoga package
    a5 = [style, holiday_word1, holiday_word2, cat] #kundalini yoga retreat package on a budget
    a6 = [cat, holiday_word1, holiday_word2, style] #budget retreat center ashtanga yoga
    a7 = [style, cat] #hatha yoga luxury
    a8 = [cat, style] #luxury hatha yoga

    comb1 = list(set(itertools.product(*a1)))
    comb2 = list(set(itertools.product(*a2)))
    comb3 = list(set(itertools.product(*a3)))
    comb4 = list(set(itertools.product(*a4)))
    comb5 = list(set(itertools.product(*a5)))
    comb6 = list(set(itertools.product(*a6)))
    comb7 = list(set(itertools.product(*a7)))
    comb8 = list(set(itertools.product(*a8)))
    
    all_comb = comb1 + comb2 + comb3 + comb4 + comb5 + comb6 + comb7 +comb8

######################################################################################

elif (cont_mrkr in url) and (style_mrkr not in url): #categories and destination
    
    a1 = [cat, yoga, holiday_word1, holiday_word2, destination_back] #ex) luxury yoga retreat package in New Zealand
    a2 = [destination_front, cat, yoga, holiday_word1, holiday_word2]#ex) New Zealand budget yoga holiday deal
    
    a3 = [yoga, cat, holiday_word1, holiday_word2, destination_back] #ex) yoga budget retreat center in Cambodia
    a4 = [destination_front, yoga, cat, holiday_word1, holiday_word2]#ex) Cambodia yoga budget retreat center
    
    a5 = [yoga, holiday_word1, holiday_word2, cat, destination_back] #ex) yoga holiday package budget Bali
    a6 = [destination_front, yoga, holiday_word1, holiday_word2, cat]#ex) Bali yoga holiday package budget
    
    a7 = [cat, holiday_word1, holiday_word2, yoga, destination_back] #ex) luxury holiday retreat yoga in South Africa
    a8 = [destination_front, cat, holiday_word1, holiday_word2, yoga]#ex) South Africa budget vacation deal yoga
    
    a9 = [yoga, holiday_word1, cat, holiday_word2, destination_back] #ex) yoga retreat budget package California
    a10 = [destination_front, yoga, holiday_word1, cat, holiday_word2]#ex) California yoga retreat luxury resort
    
    a11 = [cat, holiday_word1, yoga, holiday_word2, destination_back] #ex) budget retreat yoga pakcage Netherlands
    a12 = [destination_front, cat, holiday_word1, yoga, holiday_word2]#ex) Netherlands luxury holiday yoga retreat
    
    a13 = [yoga, holiday_word1, holiday_word2, destination_back, cat] #ex) yoga retreat deal Bali budget
    a14 = [destination_front, yoga, holiday_word1, holiday_word2, cat]#ex) Bali yoga vacation package luxury
    
    a15 = [cat, holiday_word1, holiday_word2, destination_back, yoga] #ex) surfing holiday deal NSW yoga
    a16 = [destination_front, cat, holiday_word1, holiday_word2, yoga]#ex) NSW surfing vacatiion package yoga
    
    a17 = [yoga, cat, destination_back] #yoga and surfing Tasmania
    a18 = [destination_front, yoga, cat]#Tasmania yoga and surfing
    
    a19 = [cat, yoga, destination_back] #meditation and yoga Hong Kong
    a20 = [destination_front, cat, yoga]#Hong Kong meditation and yoga
    
    comb1 = list(set(itertools.product(*a1)))
    comb2 = list(set(itertools.product(*a2))) 
    comb3 = list(set(itertools.product(*a3)))
    comb4 = list(set(itertools.product(*a4)))
    comb5 = list(set(itertools.product(*a5)))
    comb6 = list(set(itertools.product(*a6)))
    comb7 = list(set(itertools.product(*a7)))
    comb8 = list(set(itertools.product(*a8)))
    comb9 = list(set(itertools.product(*a9))) 
    comb10 = list(set(itertools.product(*a10))) 
    comb11 = list(set(itertools.product(*a11)))
    comb12 = list(set(itertools.product(*a12)))
    comb13 = list(set(itertools.product(*a13)))
    comb14 = list(set(itertools.product(*a14)))
    comb15 = list(set(itertools.product(*a15)))
    comb16 = list(set(itertools.product(*a16)))
    comb17 = list(set(itertools.product(*a17)))
    comb18 = list(set(itertools.product(*a18)))
    comb19 = list(set(itertools.product(*a19)))
    comb20 = list(set(itertools.product(*a20)))

    #join 
    all_comb = comb1 + comb2 + comb3 + comb4 + comb5 + comb6 + comb7 + comb8 + comb9 + comb10 + comb11 + comb12 + comb13 + comb14 + comb15 + comb16 + comb17 + comb18 + comb19 + comb20 

######################################################################################

elif (cont_mrkr in url) and (style_mrkr in url): #categories, style and destination
    
    a1 = [style, cat, holiday_word1, holiday_word2, destination_back]
    a2 = [destination_front, style, cat, holiday_word1, holiday_word2]
    
    a3 = [cat, style, holiday_word1, holiday_word2, destination_back]
    a4 = [destination_front, cat, style, holiday_word1, holiday_word2]
    
    a5 = [style, holiday_word1, holiday_word2, destination_back, cat]
    a6 = [destination_front, style, holiday_word1, holiday_word2, cat]
    
    a9 = [style, cat, destination_back]
    a10 = [destination_front, style, cat]
    
    a11 = [cat, style, destination_back]
    a12 = [destination_front, cat, style]

    comb1 = list(set(itertools.product(*a1)))
    comb2 = list(set(itertools.product(*a2))) 
    comb3 = list(set(itertools.product(*a3)))
    comb4 = list(set(itertools.product(*a4)))
    comb5 = list(set(itertools.product(*a5)))
    comb6 = list(set(itertools.product(*a6)))
    
    comb9 = list(set(itertools.product(*a9)))
    comb10 = list(set(itertools.product(*a10)))
    comb11 = list(set(itertools.product(*a11)))
    comb12 = list(set(itertools.product(*a12)))
    
    #join
    all_comb = comb1 + comb2 + comb3 + comb4 +comb5 + comb6 + comb9 + comb10 + comb11 + comb12

######################################################################################

#remove keywords like "UK (for women's) yoga retreat"
for i in range(len(all_comb)):
    if (all_comb[i][0] in destination_front) and ('for' in all_comb[i][1]):
        all_comb[i] = []

all_comb = [x for x in all_comb if x != []] #remove empty lists in all_comb

######################################################################################
for i in range(len(all_comb)): #remove empty strings wihtin each list in all_comb
    all_comb[i] = tuple(x for x in all_comb[i] if x != '')

#delete some keywords
for i in range(len(all_comb)): #delete keywords with 'on a budget' in the very front of the keyword
    if 'on a budget' in all_comb[i][0]:
        all_comb[i] = []
    elif "for" in all_comb[i][0]:
        all_comb[i] = []
        
all_comb = [x for x in all_comb if x != []] #remove empty lists in all_comb
all_comb = sorted(set(all_comb))#remove duplicates

######################################################################################

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

all_comb = sorted(set(all_comb)) #remove duplicates and sort the list in an alphabetical order 

######################################################################################

#count how many keywords have been created
how_many_kw = len(all_comb)

#add 'and' between cat and yoga for certain categories
copy = list(all_comb)

if cat[0] in requires_and: 
    for i in range(how_many_kw):
        copy[i] = list(copy[i])
        for x in range(len(copy[i])-1):
            if (copy[i][x] in requires_and) and (copy[i][x+1] == 'yoga'):
                copy[i].insert(x+1, 'and')
            elif (copy[i][x] == 'yoga') and (copy[i][x+1] in requires_and): 
                copy[i].insert(x+1, 'and')
        copy[i] = tuple(copy[i])
        
    #align the list in an alphabetical order  
    all_comb = sorted(all_comb + copy)

######################################################################################

#remove duplicates, sort in alphabetical order
all_comb = sorted(set(all_comb)) 

######################################################################################

#prepare for csv file

#string style
if style == '': #if there is no style
    str_style = ''

if style != '': #if there is a style
    str_style = style[0].split()[0].title()

#string destination
if destination_f == '': #if there is no destination
    str_destination = ''

if len(destination_f) == 1: #when there is only 1 destination
    str_destination = destination_f[0]
    
if len(destination_f) > 1: #when there is more than 1 destination (e.g. The Americas and Carribean)
    str_destination = ' '.join(destination).replace('And', '&') #(e.g. The Americas and Carribean -> The Americas & Carribeans)

#######################################################################################
    
#prepare column titles for the csv file
kw_column_titles = ["Keyword state", 
                    "Keyword", 
                    "Match type",
                    "Campaign",
                    "Ad group",
                    "Keyword max CPC",
                    "Ad group max CPC"]

#######################################################################################

#for column 'campaign'
if str_destination == '': #without destination 
    if style == '': #cat only
        camp = 'Longtail [Categories]'

    elif style != '': #cat and style
        camp = 'Longtail [Categories] [Style]'

else: #cat and destination. cat, style and destination
    camp = 'Longtail %s' %str_destination
    
#######################################################################################

#prepare each column  
keyword_state = ['enabled'] * len(all_comb) #universal
match_type = ['Exact'] * len(all_comb) #universal
keyword_max_cpc = [max_cpc] * len(all_comb) #set on top of the file; same for all keywords
ad_group_max_cpc = [max_cpc] * len(all_comb) #set on top of the file; same for all keywords
campaign = [camp] * len(all_comb) #custom per landing page; same for all keywords


#ad_group ---> custom per landing page; same for all keywords if number of keywords < 5000 
#         ---> custom per landing page; different for keywords if number of keywords > 5000  AND len(cat) > 1
#         --->                          if len(all_comb) > 5000 AND len(cat) = 1, numerical system

#prepare column ad_group

str_cat = cat[0].title()
adg = "Longtail %s %s %s" %(str_cat, str_style, str_destination)

#eliminate double spaces
adg = adg.split()
adg = ' '.join(adg)

ad_group = [adg] * len(all_comb)

######################################################################################

#all_comb -> keywords
keywords = []

#join, split then join again (eliminates double spaces)
for i in range(len(all_comb)):
    keywords.append(' '.join(all_comb[i]))
    keywords[i] = keywords[i].split()
    keywords[i] = ' '.join(keywords[i])
    
#add '[' and ']' in the result (keywords)
for i in range(len(keywords)):
    keywords[i] = '[' + keywords[i] + ']'   

keywords = sorted(set(keywords))

######################################################################################

#minor tweaks before zipping
for i in range(len(campaign)):
    if 'Usa' in campaign[i]:
        campaign[i] = campaign[i].replace('Usa', 'USA')
    elif 'Uk' in campaign[i]:
        campaign[i] = campaign[i].replace('Uk', 'UK')

for i in range(len(ad_group)):
    if 'Usa' in ad_group[i]:
        ad_group[i] = ad_group[i].replace('Usa', 'USA')
    if 'Uk' in ad_group[i]:
        ad_group[i] = ad_group[i].replace('Uk', 'UK')

#zip each columns
rows = []
for i in range(len(keywords)):
    rows.append([keyword_state[i],
                 keywords[i],
                 match_type[i],
                 campaign[i],
                 ad_group[i],
                 keyword_max_cpc[i],
                 ad_group_max_cpc[i]])
        
######################################################################################

#export longtail keywords in a csv file
import csv

file_name = "%s %s %s keywords.csv" %(cat[:5], style, destination_front)
new_csv = open(file_name, 'wb')
open_file_object = csv.writer(new_csv)

#write rows
open_file_object.writerow(kw_column_titles)

#write columns
for row in rows:
    open_file_object.writerow(row)

new_csv.close()

print """
[Notification] %i longtail keywords for %s %s %s are generated successfully. 
Please check your current directory for the stored result in a csv file. 
""" %(len(keywords), cat, style, destination_front)
######################################################################################
#prepare csv file content for ads
how_many_ads = len(set(ad_group)) * 4

######################################################################################

#prepare column titles
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
#headliens + description 1 + description 2

headlines = []
desc1 = []
desc2 = []

a = str_cat

#healines and description line 1 & 2
if str_destination == '': #without destination

    if style == '': #cat only

        headline1 = "%s Yoga Retreats" %a
        headline2 = "Yoga %s Retreats" %a
        headlines.append(headline1)
        headlines.append(headline2)

        desc11 = 'Reviews & Best Price Guarantee!'
        desc21 = 'Reviews & Best Price Guarantee!'
        desc1.append(desc11)
        desc1.append(desc21)

        desc12 = 'Book Your Dream Retreat Today'
        desc22 = 'Compare and Book Top Rated Litings'
        desc2.append(desc12)
        desc2.append(desc22)


    elif style != '': #cat and style

        headline1 = "%s Yoga Retreats" %str_style
        headline2 = "%s Yoga Packages" %str_style
        headlines.append(headline1)
        headlines.append(headline2)

        desc11 = "Book Online %s Retreats." %a
        desc21 = "View %s %s Retreats Now." %(count, a)
        desc1.append(desc11)
        desc1.append(desc21)

        desc12 = 'Reviews & Best Price Guarantee!'
        desc22 = 'Reviews & Best Price Guarantee!'
        desc2.append(desc12)
        desc2.append(desc22)

else: #with destination 

    if style == '': #cat and destination

        if len(destination_f) == 1: #when there is only 1 destination

            headline1 = "Yoga Retreats %s" %str_destination
            headline2 = "%s Yoga Retreats" %str_destination
            headlines.append(headline1)
            headlines.append(headline2)

        elif len(destination_f) > 1: #when there are two destinations
            headline1 = "Yoga Retreats %s" %destination_front[0]
            headline2 = "Yoga Retreats %s" %destination_front[1]
            headlines.append(headline1)
            headlines.append(headline2)

        desc11 = "%s Retreats Book Online." %a
        desc21 = "View %s %s Yoga Retreats." %(count, a)
        desc1.append(desc11)
        desc1.append(desc21)

        desc21 = "Reviews & Best Price Guarantee!"
        desc22 = 'Compare and Book Top Rated Listings'
        desc2.append(desc21)
        desc2.append(desc22)

    elif style != '':#cat, style and destination

        if len(destination_f) == 1: #when there is only 1 destination
            headline1 = "Yoga Retreats %s" %str_destination
            headline2 = "%s Yoga Retreats" %str_destination
            headlines.append(headline1)
            headlines.append(headline2)

        elif len(destination_f) > 1: #when there are two destinations
            headline1 = "Yoga Retreats %s" %destination_front[0]
            headline2 = "Yoga Retreats %s" %destination_front[1]
            headlines.append(headline1)
            headlines.append(headline2)

        desc11 = "%s %s Yoga Deals." %(a, str_style)
        desc12 = "%s Yoga %s Retreat." %(str_style, a)
        desc1.append(desc11)
        desc1.append(desc12)

        desc21 = "Reviews & Best Price Guarantee!"
        desc22 = "Compare and Book Top Rated Listings"
        desc2.append(desc21)
        desc2.append(desc22)

if 'Yoga' in str_cat:
    str_cat = str_cat.split()[1]
    
#prepare each column
ad_state = ['enabled'] * how_many_ads #universal
ad = headlines * (how_many_ads / 2) #universal
d1 = desc1 * (how_many_ads / 2)
d2 = desc2 * (how_many_ads / 2)
display_url = ['www.bookyogaretreats.com/%s'%str_cat.replace(' ', '')] * how_many_ads
final_url = [url] * how_many_ads
device = ['All'] * (how_many_ads / 2) + ['Mobile'] * (how_many_ads / 2)
campaign = [camp] * how_many_ads
ad_group2 = [adg] * how_many_ads
ad_type = ['Text ad'] * how_many_ads #universal

######################################################################################
#minor tweaks before zipping
for i in range(len(campaign)):
    if 'Usa' in campaign[i]:
        campaign[i] = campaign[i].replace('Usa', 'USA')
    elif 'Uk' in campaign[i]:
        campaign[i] = campaign[i].replace('Uk', 'UK')

for i in range(len(ad_group2)):
    if 'Usa' in ad_group2[i]:
        ad_group2[i] = ad_group2[i].replace('Usa', 'USA')
    if 'Uk' in ad_group2[i]:
        ad_group2[i] = ad_group2[i].replace('Uk', 'UK')

######################################################################################

#zip column
i=0
ac_rows1 =[]
for i in range(how_many_ads):
    ac_rows1.append([ad_state[i],
                    ad[i],
                    d1[i],
                    d2[i],
                    display_url[i],
                    final_url[i],
                    device[i],
                    campaign[i],
                    ad_group2[i],
                    ad_type[i]])

ac_rows_all = ac_rows1 

######################################################################################

#export ads into a csv file
file_name = "%s %s %s ads.csv" %(cat[:5], style, destination_front)
new_csv = open(file_name, 'wb')
open_file_object = csv.writer(new_csv)

#rows
open_file_object.writerow(ac_column_titles)

#columns
open_file_object.writerows(ac_rows_all)
new_csv.close()

print """[Notification] All %s ads for %s %s %s are generated successfully. 
Please check your current directory for the stored result in a csv file. 
""" %(len(ac_rows_all), cat, style, destination_front)

######################################################################################

for i in range(how_many_ads):
    if len(ad[i]) > 25:
        print "[Warning] Headline %i longer than 25 chars" %(i+1)
        print ad[i]
        print len(ad[i])
        print ""
    if len(d1) > 35:
        print "[Warning] Description line 1 longer than 35 chars"
        print d1[i]
        print len(d1[i])
        print ""
    if len(d2[i]) > 35:
        print "[Warning] Description line 2 longer than 35 chars"
        print d2[i]
        print len(d2[i])
        print ""
    if len(display_url[i]) > 35:
        print "[Warning] Display URL longer than 35 chars"
        print display_url[i]
        print len(display_url[i])
        print ""

######################################################################################