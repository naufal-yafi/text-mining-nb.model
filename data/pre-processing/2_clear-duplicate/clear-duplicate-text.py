import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

output_path = './data/pre-processing/2_clear-duplicate/no-duplicate-aduan-siswa.csv'
input_path = 'data/pre-processing/1_translated/translated-aduan-siswa.csv'

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, input_path)

try:
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')
  
if 'Translate' in df.columns:
  try:
    drop_duplicate = df.drop_duplicates(subset='Translate')
    drop_duplicate = drop_duplicate.rename(columns={'Translate': 'Aduan'})
    drop_duplicate.to_csv(output_path, index=False)
    
    print(f'Success: csv has clear duplicate text, output on {output_path}\n')
  except Exception as err:
    print(f'Err: {err}\n')
else:
  print("Err: Column 'Translate' doesn't exist\n")