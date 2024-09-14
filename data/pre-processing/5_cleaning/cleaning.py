import os
from dotenv import load_dotenv
import pandas as pd
import re 

load_dotenv()

output_path = './data/pre-processing/5_cleaning/cleaning-aduan-siswa.csv'
input_path = 'data/pre-processing/4_case-folding/case-folding-aduan-siswa.csv'

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, input_path)

try:
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')
  
if 'Aduan' in df.columns:
  try:
    def clean_text(text):
      return re.sub(r'[,\.\d]', '', str(text))
    
    df['Aduan'] = df['Aduan'].apply(clean_text)
    df.to_csv(output_path, index=False)
    
    print(f'Success: case folding, output on {output_path}\n')
  except Exception as err:
    print(f'Err: {err}\n')
else:
  print("Err: Column 'Aduan' doesn't exist\n")