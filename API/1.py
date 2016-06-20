######################################################################################

max_budget = '100000000' #100 euros
max_cpc = '1000000' #1 euro
match_type = 'EXACT' #BROAD, PHRASE, OR EXACT

results = ['banana', 'yoga', 'appled']

######################################################################################

import urllib2
from BeautifulSoup import BeautifulSoup

url = 'https://www.bookyogaretreats.com/all/d/asia-and-oceania/australia'

#extract the number of listings from landing page title
soup = BeautifulSoup(urllib2.urlopen(url))
page_title = str(soup.title.string)
count = page_title.split()[0]

if count.isdigit() == False:
    sys.exit("[Alert] Cannot proceed further: the landing page has less than 3 listings. Please choose a different landing page with at least 3 listings.")

######################################################################################

if ('/d/' in url) and ('/c/' not in url) and ('/s/' not in url): #destination only

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


import datetime
import uuid
from googleads import adwords

camps = ['USA', 'UK', 'Malaysia', 'India']
campaign_ids = []

ad_group_names = ['Retreats', 'Holidays', 'Yoga Weekends', 'Budget']
ad_group_ids = []


#create campaigns

if __name__ == '__main__':
  
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  client = adwords_client

  campaign_service = client.GetService('CampaignService', version='v201603')
  budget_service = client.GetService('BudgetService', version='v201603')

  for i in range(len(camps)):
    
    # Create a budget, which can be shared by multiple campaigns.
    budget = {
        'name': 'Budget #%s' % uuid.uuid4(),
        #'name': '100 %s' % float(i/100),
        'amount': {
            'microAmount': max_budget
        },
        'deliveryMethod': 'STANDARD'
    }

    budget_operations = [{
        'operator': 'ADD',
        'operand': budget
    }]

    # Add the budget.
    budget_id = budget_service.mutate(budget_operations)['value'][0][
        'budgetId']

    # Construct operations and add campaigns.
    operations = [{
        'operator': 'ADD',
        'operand': {
            #'name': 'Interplanetary Cruise #%s' % uuid.uuid4(),
            'name': 'Longtail %s' % camps[i],
            'status': 'ENABLED',
            'advertisingChannelType': 'SEARCH',
            'biddingStrategyConfiguration': {
                'biddingStrategyType': 'MANUAL_CPC',
            },
            'endDate': (datetime.datetime.now() +
                        datetime.timedelta(365)).strftime('20371230'),
            # Note that only the budgetId is required
            'budget': {
                'budgetId': budget_id
            },
            'networkSetting': {
                'targetGoogleSearch': 'true',
                'targetSearchNetwork': 'true',
                'targetContentNetwork': 'false',
                'targetPartnerSearchNetwork': 'false'
            },
            # Optional fields
            'startDate': (datetime.datetime.now() +
                          datetime.timedelta(1)).strftime('%Y%m%d'),
            'adServingOptimizationStatus': 'ROTATE',
            'frequencyCap': {
                'impressions': '5',
                'timeUnit': 'DAY',
                'level': 'ADGROUP'
            },
            'settings': [
                {
                    'xsi_type': 'GeoTargetTypeSetting',
                    'positiveGeoTargetType': 'DONT_CARE',
                    'negativeGeoTargetType': 'DONT_CARE'
                }
            ]
        }
    }]

    campaigns = campaign_service.mutate(operations)

    # Display results.
    for campaign in campaigns['value']:
      print ('Campaign with name \'%s\' and id \'%s\' was added.'
             % (campaign['name'], campaign['id']))
      #campaign_ids.append(str(campaign['id'])[0:-1])
      campaign_ids.append(str(campaign['id']))

print "campaign ids: %s" %campaign_ids

################################################################################

#create ad groups
import uuid
from googleads import AdWordsClient

if __name__ == '__main__':
    # Initialize client object.
    adwords_client = adwords.AdWordsClient.LoadFromStorage()

    client = adwords_client

    # Initialize appropriate services.
    ad_group_service = client.GetService('AdGroupService', version='v201603')


    for i in range(len(campaign_ids)): #iterate through each and all campaigns
        campaign_id = campaign_ids[i]
        destination = camps[i]
        #print destination
        

        for i in range(len(ad_group_names)): #iterate through each and all ad groups

            #ag_names.append(ad_group_names[i] + destination)
            #print ag_names[i]

            # Construct operations and add ad groups.
            operations = [{ 
                'operator': 'ADD',
                'operand': {
                    'campaignId': campaign_id,
                    #'name': 'Earth to Mars Cruises #%s' % uuid.uuid4(),
                    'name': 'Longtail %s %s' %(ad_group_names[i], destination),
                    'status': 'ENABLED',
                    'biddingStrategyConfiguration': {
                        'bids': [
                            {
                                'xsi_type': 'CpcBid',
                                'bid': {
                                    'microAmount': max_cpc
                                },
                            }
                        ]
                    },
                    'settings': [
                        {
                            # Targeting restriction settings. Depending on the
                            # criterionTypeGroup value, most TargetingSettingDetail only
                            # affect Display campaigns. However, the
                            # USER_INTEREST_AND_LIST value works for RLSA campaigns -
                            # Search campaigns targeting using a remarketing list.
                            'xsi_type': 'TargetingSetting',
                            'details': [
                                # Restricting to serve ads that match your ad group
                                # placements. This is equivalent to choosing
                                # "Target and bid" in the UI.
                                {
                                    'xsi_type': 'TargetingSettingDetail',
                                    'criterionTypeGroup': 'PLACEMENT',
                                    'targetAll': 'false',
                                },
                                # Using your ad group verticals only for bidding. This is
                                # equivalent to choosing "Bid only" in the UI.
                                {
                                    'xsi_type': 'TargetingSettingDetail',
                                    'criterionTypeGroup': 'VERTICAL',
                                    'targetAll': 'true',
                                },
                            ]
                        }
                    ]
                }
            }]

            """
            , {
                'operator': 'ADD',
                'operand': {
                    'campaignId': campaign_id,
                    'name': 'Earth to Venus Cruises #%s' % uuid.uuid4(),
                    'status': 'ENABLED',
                    'biddingStrategyConfiguration': {
                        'bids': [
                            {
                                'xsi_type': 'CpcBid',
                                'bid': {
                                    'microAmount': '1000000'
                                }
                            }
                        ]
                    }
                }
            }

            """

            ad_groups = ad_group_service.mutate(operations)

            # Display results.
            for ad_group in ad_groups['value']:
              print ('Ad group with name \'%s\' and id \'%s\' was added.'
                     % (ad_group['name'], ad_group['id']))
              ad_group_ids.append(str(ad_group['id']))

print ad_group_ids



if __name__ == '__main__':

    adwords_client = adwords.AdWordsClient.LoadFromStorage()

    client = adwords_client

    ad_group_criterion_service = client.GetService(
      'AdGroupCriterionService', version='v201603')

    for i in range(len(ad_group_ids)):
        AD_GROUP_ID = ad_group_ids[i]

        for i in range(len(results)):
            keyword1 = {
                'xsi_type': 'BiddableAdGroupCriterion',
                'adGroupId': AD_GROUP_ID,
                'criterion': {
                'xsi_type': 'Keyword',
                'matchType': match_type,
                'text': results[i]
                },

                # These fields are optional.
                'userStatus': 'ENABLED',
                # 'finalUrls': {
                # 'urls': ['http://example.com/mars']
                }