import os 
from dotenv import load_dotenv
import pandas as pd

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

load_dotenv()

output_path = './data/pre-processing/6_filtering/filtering-aduan-siswa.csv'
input_path = 'data/pre-processing/5_cleaning/cleaning-aduan-siswa.csv'

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, input_path)

try:
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')

if 'Aduan' in df.columns:
  try:
    stop_words = set(stopwords.words('indonesian'))
    df['Aduan'] = df['Aduan'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
    df.to_csv(output_path, index=False)
    
    print(f'Success: filtering data, output on {output_path}\n')
  except Exception as err:
    print(f'Err: {err}\n')
else:
  print("Err: Column 'Aduan' doesn't exist\n")