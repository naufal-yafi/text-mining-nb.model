from package.path import join
from package.env import get_env
from package.dataframe import create, check_available_column
from package.system import error, exit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

csv_file = join(get_env('BASE_DIR'), 'dist/accurate-dataset.csv')
df = check_available_column('Aduan', check_available_column('Label', create(csv_file)))

output_path_model = './dist/text-mining.pkl'
output_path_vectorizer = './dist/vectorizer.pkl'

try:
  X_text = df['Aduan']
  y = df['Label']
  
  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(X_text)
      
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
  model = MultinomialNB()
  model.fit(X_train, y_train)
  
  joblib.dump(model, output_path_model)
  joblib.dump(vectorizer, output_path_vectorizer)
except Exception as err:
  error(err)