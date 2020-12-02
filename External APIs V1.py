# This python script uses VirusTotal APIv2 to check a MD5 Hash against a plethora of threat databases including BitDefender, Avast, McAfee, FireEye and many more.

# When the program is run the following steps take place:
# 1. It will ask for a Web Address or IP Address which can be entered in plain text format.
# 2. The script will then convert this String to a MD5 Hash and print it.
# 3. It then submits this MD5 Hash to the VirusTotal APIv2 in JSON format.
# 4. The API returns a list of databases that it has checked the MD5 Hash against in JSON (Formatted).

# This is only the first interation of this script so it is quite simple but it can be easily added to in future.

import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi

API_KEY = 'ff6aca2929257f82bae81b43899079578ae999d2dc1290e71ec94153cea5728d'

text = input(str("Type a Web Address or IP Address: ")).encode('utf-8')

MD5 = hashlib.md5(text).hexdigest()

print("MD5 Hash: " + MD5)

API = VirusTotalPublicApi(API_KEY)

response = API.get_file_report(MD5)

print(json.dumps(response, sort_keys=False, indent=2))
