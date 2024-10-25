import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

input_path = 'data/raw/dataset.csv'
output_path = './data/preprocessing/1-case-folding/dataset-case-folding.csv'

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, input_path)

try:
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')
  
if 'Aduan' in df.columns:
  try:
    df['Aduan'] = df['Aduan'].str.lower()
    df.to_csv(output_path, index=False)
    
    print(f'Success: case folding, output on {output_path}\n')
  except Exception as err:
    print(f'Err: {err}\n')
else:
  print("Err: Column 'Aduan' doesn't exist\n")