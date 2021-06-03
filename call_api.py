import requests
from config import COMPANIES
import os
import time

base_url = os.environ.get("DLI_LINKEDIN_API")
for company in COMPANIES:
    url = f"{base_url}/company/{company}"
    x = requests.get(url)
    time.sleep(120)
    print(x)
