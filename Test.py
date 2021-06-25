# import requests
#
# response = requests.get("https://api.covid19india.org/data.json").json()
#
# for i in response['statewise']:
#     if i['state'] == 'Total':
#         print(i['active'])
#
a = '24/06/2021 20:46:10'

from datetime import datetime
from dateutil.parser import parse

date_time_obj = datetime.strptime(a, '%d/%m/%Y %H:%M:%S')

print(datetime.strftime(date_time_obj, '%b %d %Y'))