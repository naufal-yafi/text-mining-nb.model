import os
from dotenv import load_dotenv
import pandas as pd
from stopwords import load_stopwords, remove_stopwords

load_dotenv()

# csv file
input_path = 'data/preprocessing/2-cleaning/dataset-cleaning.csv'
output_path = './data/preprocessing/3-filtering/dataset-filtering.csv'
# stopword file
stopword_path = 'data/preprocessing/3-filtering/stopword-list.txt'

BASE_DIR = os.getenv('BASE_DIR')
stopword_file = os.path.join(BASE_DIR, stopword_path)
csv_file = os.path.join(BASE_DIR, input_path)

try:
  stopwords = load_stopwords(stopword_file)
  df = pd.read_csv(csv_file)
except Exception as err:
  print(f'Err: {err}\n')
  
if 'Aduan' in df.columns:
  try:
    df['Aduan'] = df['Aduan'].apply(lambda text: remove_stopwords(text, stopwords))
    df.to_csv(output_path, index=False)
    
    print(f'Success: filtering, output on {output_path}\n')
  except Exception as err:
    print(f'Err: {err}\n')
else: 
  print("Err: Column 'Aduan' doesn't exist\n")