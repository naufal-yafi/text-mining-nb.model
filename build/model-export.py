import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

load_dotenv()

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, 'dist/new-dataset.csv')
df = pd.read_csv(csv_file)

output_path_model = './dist/text-mining.pkl'
output_path_vectorizer = './dist/vectorizer.pkl'

if 'Aduan' in df.columns:
  if 'Label' in df.columns:
    X_text = df['Aduan']
    y = df['Label']
    
    try:
      vectorizer = TfidfVectorizer()
      X = vectorizer.fit_transform(X_text)
      
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

      model = MultinomialNB()
      model.fit(X_train, y_train)
    except Exception as err:
      print(f'Err: {err}\n')
  else:
    print("Err: Column 'Label' doesn't exist\n")
else:
  print("Err: Column 'Aduan' doesn't exist\n")

try:
  joblib.dump(model, output_path_model)
  joblib.dump(vectorizer, output_path_vectorizer)
  
  print(f'Success: export model on {output_path_model}')
  print(f'Success: export vectorizer on {output_path_vectorizer}\n')
except Exception as err:
  print(f'Err: {err}\n')