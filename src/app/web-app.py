import streamlit as st
import joblib
from package.fetch import post
from package.path import join
from package.env import get_env

model_file = join(get_env('BASE_DIR'), 'dist/text-mining.pkl')
vectorizer_file = join(get_env('BASE_DIR'), 'dist/vectorizer.pkl')
icon_file = join(get_env('BASE_DIR'), 'app/icon.png')

model = joblib.load(model_file)
vectorizer = joblib.load(vectorizer_file)

st.set_page_config(
  page_title="MTS 45 Wiradesa: Berikan saranmu",
  page_icon=icon_file,
  initial_sidebar_state="expanded"
)

st.title("Berikan saranmu disini!")
st.subheader('MTS 45 Wiradesa')

popup_placeholder = st.empty()

input_text = st.text_area(
  label="Saran", 
  label_visibility="hidden", 
  placeholder="Tuliskan saranmu disini..."
)

if st.button(
  label="Kirim", 
  type="primary",
  use_container_width=True
):
  MIN_LENGTH = 12
  
  if not input_text.strip():
    popup_placeholder.error("Tolong untuk mengisi form saran terlebih dahulu sebelum mengirimnya.")
  elif len(input_text) < MIN_LENGTH:
    popup_placeholder.error(f"Saran harus terdiri dari minimal {MIN_LENGTH} huruf.")
  else:
    predict = model.predict(vectorizer.transform([input_text]))
    getLabel = predict[0]
    
    if not get_env('BASE_API_URL'):
      st.write(getLabel)
    else:
      res = post(
        request_body={
          "message": input_text,
          "label": getLabel,
        },
        route='/messages'
      )
      
      if res == 201:
        popup_placeholder.success("Terima kasih telah memberikan saran, kami akan memprosesnya segera.")
      else:
        popup_placeholder.error("Gagal mengunggah saran, server ada masalah. Mohon tunggu dan mencoba beberapa saat lagi.")