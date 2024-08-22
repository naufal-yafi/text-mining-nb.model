import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

load_dotenv()

BASE_DIR = os.getenv('BASE_DIR')
csv_file = os.path.join(BASE_DIR, 'src/suggestions.csv')
df = pd.read_csv(csv_file)

X_text = df['Saran']
y = df['Label']

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_text)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

model = MultinomialNB()
model.fit(X_train, y_train)

joblib.dump(model, './dist/text-mining.pkl')
joblib.dump(vectorizer, './dist/vectorizer.pkl')