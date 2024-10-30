import os
from dotenv import load_dotenv

load_dotenv()

def get_env(variable_name):
  return os.getenv(variable_name)