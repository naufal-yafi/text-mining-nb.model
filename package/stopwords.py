def load(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    stopwords = file.read().splitlines()
  return stopwords

def removing_text(text, stopwords):
  words = text.split()
  filtered = [word for word in words if word.lower() not in stopwords]
  return ' '.join(filtered)