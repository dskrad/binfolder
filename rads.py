#!/usr/bin/env python
# copyright DSK 2012
import requests
import json

query_params = {'login': 'dskrad',
                'apiKey': 'R_6f20edd903e0e3f5fb7f1e7c8a74c705',
                'query': 'radiology',
                'limit': 10}

endpoint = 'https://api-ssl.bitly.com/v3/search'
response = requests.get(endpoint, params= query_params)

data = json.loads(response.content)
for result in data['data']['results']:
  print result['title']
  print result['description']
  print result['url']
  print

