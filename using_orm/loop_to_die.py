import json
import sqlalchemy as sa
import requests
from pprint import pprint

proxies = None
token_str = ""  # Encrypted API token. This will need to be set manually or by a method of a subclass
max_retries = 10
requests_timeout = None
if True:
    _session = requests.Session()
else:
    _session = requests.api  # individual calls, slower

token_str = "ad_QwuFLmvAqx5-dDzwx2RsDphAoDmFCS7XNWBXiwVt4Xnumz2c-FwRMQFYaaaZC"

headers = {'Authorization': 'Bearer {}'.format(token_str), 'Content-Type': 'application/json'}

failed_id = []
start_id = 7423700
times = 0
while True:
    try:
        url = f"https://api.genius.com/songs/{start_id}"
        r = _session.request("GET", url,
                             headers=headers,
                             proxies=proxies,
                             params=None,
                             timeout=requests_timeout)
        print(start_id)
        print(r.status_code)
        if r.status_code == 404 or 200:
            times += 1
            continue
        elif r.status_code == 429:
            print(f"times looped before multiple requests msg: {times}")
            exit
        else:
            exit
    except Exception as e:
        failed_id.append(id)
        print(f"Exception: {e}")

    start_id += 1
# pprint(r.json())
# response = json.loads(r.text)
# pprint(response['response'])
