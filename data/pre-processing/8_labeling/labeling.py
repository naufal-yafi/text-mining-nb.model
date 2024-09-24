import os 
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

output_path = './dist/aduan-siswa.csv'
input_aduan_path = 'data/pre-processing/7_stemming/stemming-aduan-siswa.csv'
input_label_path = 'data/pre-processing/8_labeling/label.csv'

BASE_DIR = os.getenv('BASE_DIR')
csv_aduan_file = os.path.join(BASE_DIR, input_aduan_path)
csv_label_file = os.path.join(BASE_DIR, input_label_path)

df_aduan = pd.read_csv(csv_aduan_file)
df_label = pd.read_csv(csv_label_file)

try:
  combine = pd.concat([df_aduan, df_label], axis=1)
except Exception as err:
  print(f'Err: {err}\n')
  
try:
  combine.to_csv(output_path, index=False)
    
  print(f'Success: preprocessing data, output on {output_path}\n')
except Exception as err:
  print(f'Err: {err}\n')