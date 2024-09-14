import streamlit as st
import os
from dotenv import load_dotenv
import joblib

load_dotenv()

BASE_DIR = os.getenv('BASE_DIR')
model_file = os.path.join(BASE_DIR, 'dist/text-mining.pkl')
vectorizer_file = os.path.join(BASE_DIR, 'dist/vectorizer.pkl')
icon_file = os.path.join(BASE_DIR, 'app/icon.png')

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
    if not input_text.strip():
        popup_placeholder.error("Tolong untuk mengisi form saran terlebih dahulu sebelum mengirimnya.")
    elif len(input_text) < 12:
        popup_placeholder.error("Saran harus terdiri dari minimal 12 huruf.")
    else:
        popup_placeholder.success("Terimakasih telah memberikan saran, kami akan memprosesnya segera.")
        st.write("Hasil:")
        predict = model.predict(vectorizer.transform([input_text]))
        st.write(predict)
