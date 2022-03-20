# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import requests
import json
from datetime import datetime

req = requests.get("http://api.open-notify.org/iss-now.json")

json_obj = req.json()

print('json_obj: ' + '\n' + str(json_obj))

with open('/var/www/musimatic/data/iss_location.json', 'w') as f:
    json.dump(json_obj, f)

f.close()

# print('\n\n')
# print('Longitude of ISS Space Station: ' + str(json_obj['iss_position']['longitude']))
# print('Latitude of ISS Space Station: ' + str(json_obj['iss_position']['latitude']))
# unix_timestamp = int(json_obj['timestamp'])
# TODO: Convert this to EDT timezone:
# print('Timestamp (UNIX Time): ' + str(datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')))

