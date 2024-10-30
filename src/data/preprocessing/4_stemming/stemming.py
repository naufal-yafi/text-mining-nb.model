from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from package.path import base_dir, join
from package.env import get_env
from package.dataframe import check_available_column, create
from package.system import error, exit

input_path = f"{base_dir('preprocessing', 2)}/filtering-dataset.csv"
output_path = f"{base_dir('preprocessing', 3)}/stemming-dataset.csv"

csv_file = join(get_env('BASE_DIR'), input_path)

df = check_available_column('Aduan', create(csv_file))

try:
  stemmer = StemmerFactory().create_stemmer()
  
  df['Aduan'] = df['Aduan'].apply(lambda x: stemmer.stem(x))
  df.to_csv(output_path, index=False)
  exit(f"Success: stemming data, output on {output_path}\n")
except Exception as err:
  error(err)