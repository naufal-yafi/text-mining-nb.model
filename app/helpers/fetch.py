import os 
from dotenv import load_dotenv
import requests

load_dotenv()

BASE_API_URL = os.getenv('BASE_API_URL')
API_KEY = os.getenv('API_KEY')


def post(request_body, route):
  try:
    url = f"{BASE_API_URL}{route}"
    headers = {
      "Authorization": f"Bearer {API_KEY}",
      "Content-Type": "application/json"
    }
    
    res = requests.post(url, headers=headers, json=request_body)
    return res.status_code
  except Exception as err:
    print(err)