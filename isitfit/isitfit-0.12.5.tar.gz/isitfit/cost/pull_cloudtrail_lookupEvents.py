# boto3 implementation of
# https://gist.github.com/shadiakiki1986/f6e676d1ab5800fcf7899b6a392ab821
# Docs
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.get_paginator
#
# Requirements: pip3 install boto3 tqdm pandas
# Run: python3 t2.py
#
# Edit 2019-09-13: copied file pull_cloudtrail_lookupEvents.py from git-remote-aws into isitfit so as to avoid confusion in download statistics
#----------------------------------------

# imports
import datetime as dt
from dateutil.relativedelta import relativedelta
import boto3
from tqdm import tqdm
import json

import logging
logger = logging.getLogger('isitfit')

#------------------------------
# utility to serialize date
#def json_serial(obj):
#    """JSON serializer for objects not serializable by default json code"""
#
#    if isinstance(obj, (dt.datetime, dt.date)):
#        return obj.isoformat()
#    raise TypeError ("Type %s not serializable" % type(obj))


#----------------------------------------
# iterate

# use jmespath like awscli
# https://stackoverflow.com/a/57018780/4126114
# Example
#   >>> mydata
#   {'foo': {'bar': [{'name': 'one'}, {'name': 'two'}]}}
#   >>> jmespath.search('foo.bar[?name==`one`]', mydata)
#   [{'name': 'one'}]
# import jmespath

#----------------------------------------
class Ec2Typechanges:
  
    def __init__(self, eventName):
      self.eventName = eventName

    # get paginator
    def getIterator(self, client):
        """
        eventName - eg 'ModifyInstanceAttribute'
        """
        # arguments to lookup-events command
        # From docs: "Currently the list can contain only one item"
        LookupAttributes=[
        #    {'AttributeKey': 'EventSource', 'AttributeValue': 'ec2.amazonaws.com'},
            {'AttributeKey': 'EventName', 'AttributeValue': self.eventName},
        ]

        # go back x time
        # https://stackoverflow.com/a/38795526/4126114
        # StartTime=dt.datetime.now() - relativedelta(years=1)
        # StartTime=dt.datetime.now() - relativedelta(days=90)
        PaginationConfig={
          'MaxResults': 3000
        }

        # client = boto3.client('cloudtrail')
        cp = client.get_paginator(operation_name="lookup_events")
        iterator = cp.paginate(
          LookupAttributes=LookupAttributes, 
          #StartTime=StartTime, 
          PaginationConfig=PaginationConfig
        )
        return iterator


    def handleIterator(self, iterator):
      i=1
      r_all = []
      for i, response in tqdm(enumerate(iterator), desc="Cloudtrail page %i"%i):
        #with open('t2.json','w') as fh:
        #  json.dump(response, fh, default=json_serial)

        # print(response.keys())
        for event in response['Events']:
          result = self._handleEventAny(event)
          if result is None: continue
          r_all.append(result)

      return r_all


    def _handleEventAny(self, event):
        if self.eventName == 'RunInstances':
          return self._handleEventRun(event)
          
        if self.eventName == 'ModifyInstanceAttribute':
          return self._handleEventModify(event)
          
        raise ValueError("Unsupported event name %s"%self.eventName)
      
      
    def _handleEventRun(self, event):
          # logger.debug("Cloudtrail event: %s"%json.dumps(event, default=json_serial))

          if 'Resources' not in event:
            logger.debug("No 'Resources' key in event. Skipping")
            return None # ignore this situation
        
          instanceId = [x for x in event['Resources'] if x['ResourceType']=='AWS::EC2::Instance']
          if len(instanceId)==0:
            logger.debug("No AWS EC2 instances in event. Skipping")
            return None # ignore this situation

          # proceed
          instanceId = instanceId[0]

          if 'ResourceName' not in instanceId:
            logger.debug("No ResourceName key in event. Skipping")
            return None # ignore this situation
          
          # proceed
          instanceId = instanceId['ResourceName']

          if 'CloudTrailEvent' not in event:
            logger.debug("No CloudTrailEvent key in event. Skipping")
            return None # ignore this situation

          ce_dict = json.loads(event['CloudTrailEvent'])

          if 'requestParameters' not in ce_dict:
            logger.debug("No requestParameters key in event['CloudTrailEvent']. Skipping")
            return None # ignore this situation

          if 'instanceType' not in ce_dict['requestParameters']:
            logger.debug("No instanceType key in event['CloudTrailEvent']['requestParameters']. Skipping")
            return None # ignore this situation

          newType = ce_dict['requestParameters']['instanceType']

          if 'EventTime' not in event:
            logger.debug("No EventTime key in event. Skipping")
            return None # ignore this situation

          ts_obj = event['EventTime']
          # ts_obj = dt.datetime.utcfromtimestamp(ts_int)
          # ts_str = ts_obj.strftime('%Y-%m-%d %H:%M:%S')

          result = {
            'EventTime': ts_obj,  # ts_str,
            'instanceId': instanceId,
            'instanceType': newType,
          }

          return result
          
          
    def _handleEventModify(self, event):
          if 'CloudTrailEvent' not in event:
            logger.debug("No CloudTrailEvent key in event. Skipping")
            return None # ignore this situation

          ce_dict = json.loads(event['CloudTrailEvent'])

          if 'requestParameters' not in ce_dict:
            logger.debug("No requestParameters key in event['CloudTrailEvent']. Skipping")
            return None # ignore this situation

          rp_dict = ce_dict['requestParameters']
          newType = None

          #newType = jmespath.search('instanceType', rp_dict)
          #if newType is None:
          #  newType = jmespath.search('attributeName==`instanceType`', rp_dict)

          if 'instanceType' in rp_dict:
            # logging.error(json.dumps(rp_dict))
            newType = rp_dict['instanceType']['value']

          if 'attribute' in rp_dict:
            if rp_dict['attribute']=='instanceType':
              newType = rp_dict['value']

          if newType is None:
            return None

          ts_obj = event['EventTime']
          # ts_obj = dt.datetime.utcfromtimestamp(ts_int)
          # ts_str = ts_obj.strftime('%Y-%m-%d %H:%M:%S')

          if 'instanceId' not in rp_dict:
            logger.debug("No instanceId key in requestParameters. Skipping")
            return None # ignore this situation

          result = {
            'EventTime': ts_obj, # ts_str,
            'instanceId': rp_dict['instanceId'],
            'instanceType': newType,
          }

          return result


class GeneralManager:
    def __init__(self, client):
        self.client = client
        
    def ec2_typeChanges(self):
        import pandas as pd
        from termcolor import colored
        import botocore
        import sys

        def run_iterator(man2_i, iterator_i):
          try:
            r_i = man2_i.handleIterator(iterator_i)
          except botocore.exceptions.ClientError as e:
            logger.error(colored("\n"+str(e), 'red'))
            sys.exit(1)

          return r_i

        man2_run = Ec2Typechanges(eventName='RunInstances')
        iterator_run = man2_run.getIterator(self.client)
        r_run = run_iterator(man2_run, iterator_run)
        
        man2_mod = Ec2Typechanges(eventName='ModifyInstanceAttribute')
        iterator_mod = man2_mod.getIterator(self.client)
        r_mod = run_iterator(man2_mod, iterator_mod)
       
        # split on instance ID and gather
        r_all = r_run + r_mod
        # logging.error(r_all)
        df = pd.DataFrame(r_all)

        if df.shape[0]==0:
          # early return
          return df

        df = df.set_index(["instanceId", "EventTime"]).sort_index()
        
        return df


if __name__=='__main__':
    client = boto3.client('cloudtrail')
    man1 = GeneralManager(client)
    df = man1.ec2_typeChanges()
    print("")
    print(df)
