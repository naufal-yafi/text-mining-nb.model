import os 
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

output_path = './dist/aduan-siswa.csv'
input_path = 'data/pre-processing/8_labeling/aduan-siswa.csv'

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, input_path)

try:
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')
  
try:
  df.to_csv(output_path, index=False)
    
  print(f'Success: preprocessing data, output on{output_path}\n')
except Exception as err:
  print(f'Err: {err}\n')