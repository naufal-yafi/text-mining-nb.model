import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

output_path = './data/pre-processing/1_translated/translated-aduan-siswa.csv'
input_path = 'data/pre-processing/1_translated/translated-university-student-complaints.csv'

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, input_path)

try:
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')
  
if 'Translate' in df.columns:
  try:
    translateColumn = df['Translate']
    translateColumn.to_csv(output_path, index=False)
    
    print(f'Success: csv has translated on {output_path}\n')
  except Exception as err:
    print(f'Err: {err}\n')
else:
  print("Err: Column 'Translate' doesn't exist\n")