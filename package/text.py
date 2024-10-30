import re

def clean_text(text):
  return re.sub(r'[,\.\d]', '', str(text))