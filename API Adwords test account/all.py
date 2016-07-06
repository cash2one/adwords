#1. open campaigns

#!/usr/bin/python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example adds campaigns.

To get campaigns, run get_campaigns.py.

The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.

"""








import datetime
import uuid
from googleads import adwords

camps = ['USA', 'UK', 'Malaysia', 'India'] #campaign names
groups = ['Retreats', 'Holidays', 'Yoga Weekends', 'Budget'] #ad group names
campaign_ids = [] #campaign id storage for later
campaign_names = [] #campaign name storage for later
ad_group_ids = [] #ad group id storage for later
ad_group_names = []#ad group name storage for later

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
            'microAmount': '100000000' #100 euros
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

#########################################################################

#2. get campaigns + open ad groups

#!/usr/bin/python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example gets all campaigns.

To add a campaign, run add_campaign.py.

The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.

"""

import logging
import time
from googleads import adwords

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)


PAGE_SIZE = 100


def main(client):
  # Initialize appropriate service.
  campaign_service = client.GetService('CampaignService', version='v201603')

  # Construct selector and get all campaigns.
  offset = 0
  selector = {
      'fields': ['Id', 'Name', 'Status'],
      'paging': {
          'startIndex': str(offset),
          'numberResults': str(PAGE_SIZE)
      }
  }

  more_pages = True
  while more_pages:
    page = campaign_service.get(selector)

    # Display results.
    if 'entries' in page:
      for campaign in page['entries']:
        print ('Campaign with id \'%s\', name \'%s\', and status \'%s\' was '
               'found.' % (campaign['id'], campaign['name'],
                           campaign['status']))
        campaign_ids.append(str(campaign['id']))
        campaign_names.append(str(campaign['name'])[9:])


    else:
      print ('No campaigns were found.')
    offset += PAGE_SIZE
    selector['paging']['startIndex'] = str(offset)
    more_pages = offset < int(page['totalNumEntries'])
    time.sleep(1)


if __name__ == '__main__':
  adwords_client = adwords.AdWordsClient.LoadFromStorage()
  main(adwords_client)


  # Initialize appropriate service.
  ad_group_service = client.GetService('AdGroupService', version='v201603')

  for i in range(len(camps)):
    destination = ' %s' %campaign_names[i]
    campaign_id = campaign_ids[i]

    for i in range(len(groups)):
      ad_group_name = groups[i] + destination

      operations = [{
          'operator': 'ADD',
          'operand': {
              'campaignId': campaign_id,
              #'name': 'Earth to Mars Cruises #%s' % uuid.uuid4(),
              'name': 'Longtail %s' %ad_group_name,
              #'label': 'type=dest' .  
              'status': 'ENABLED',
              'biddingStrategyConfiguration': {
                  'bids': [
                      {
                          'xsi_type': 'CpcBid',
                          'bid': {
                              'microAmount': '1000000'
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

      ad_groups = ad_group_service.mutate(operations)

      # Display results.
      for ad_group in ad_groups['value']:
        print ('Ad group with name \'%s\' and id \'%s\' was added.'
               % (ad_group['name'], ad_group['id']))



print (campaign_ids)

#########################################################################

#3. get ad groups

from googleads import adwords

PAGE_SIZE = 500

ad_group_service = client.GetService('AdGroupService', version='v201603')


for i in range(len(campaign_ids)):

  campaign_id = campaign_ids[i]

  offset = 0
  selector = {
    'fields': ['Id', 'Name', 'Status'],
    'predicates': [
        {
            'field': 'CampaignId',
            'operator': 'EQUALS',
            'values': [campaign_id]
        }
    ],
    'paging': {
        'startIndex': str(offset),
        'numberResults': str(PAGE_SIZE)
    }
}
more_pages = True
while more_pages:
  page = ad_group_service.get(selector)

  # Display results.
  if 'entries' in page:
    for ad_group in page['entries']:
      print ('Ad group with name \'%s\', id \'%s\' and status \'%s\' was '
             'found.' % (ad_group['name'], ad_group['id'],
                         ad_group['status']))
      ad_group_names.append(ad_group['name'])
      ad_group_ids.append(ad_group['id'])

  else:
    print ('No ad groups were found.')

  offset += PAGE_SIZE
  selector['paging']['startIndex'] = str(offset)
  more_pages = offset < int(page['totalNumEntries'])

#########################################################################

"""
ad_group_dict_id = {}
ad_group_dict_type= {}

styles = []


for i in range(len(ad_group_ids)):
  if ('Retreat' in ad_group_names[i]) or ('retreat' in ad_group_names[i]):
    type1 = 'dest'
  
  else:
    for x in range(len(styles)):
      
      if styles[x] in ad_group_names[i]:
        type1 = 'style'

      else: 
        type1 = 'cat'

  ad_group_dict_type['%s' %str(ad_group_names[i])] = '%s' %type1


print (ad_group_dict_type)

"""
# for i in range(len(ad_group_ids):
#   ad_group_dict_type['%s' %ad_group_names[i]] = '%s' %ad_group_ids





#4. get longtail keywords (destination only)

# dest_ad_group_names = []
# dest_ad_group_ids = []

# for i in range(len(ad_group_names)):
#   c
#     dest_ad_group_names.append(ad_group_names[i])
#     dest_ad_group_ids.append(ad_group_ids[i])

