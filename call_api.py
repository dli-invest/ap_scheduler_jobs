import requests
from config import COMPANIES
import os

base_url = os.environ.get("DLI_LINKEDIN_API")
for company in COMPANIES:
    url = f"{base_url}/company/{company}"
    x = requests.get(url)
    print(x)
