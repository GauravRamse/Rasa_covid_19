import requests

response = requests.get("https://api.covid19india.org/data.json").json()

for i in response['statewise']:
    if i['state'] == 'Total':
        print(i['active'])




        000000000000000000000