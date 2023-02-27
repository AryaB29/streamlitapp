from turtle import home
import streamlit as st
from multipage import MultiPage
from PIL import Image
from apps import calorie_calculator,calorie_tracker,home,sport_calculator

st.set_page_config(
     page_title="Aplikasi Untuk Shabrina",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Report a bug': 'https://github.com/AryaB29', 
         'Get help': 'https://github.com/AryaB29',
         'About': "Merupakan Sebuah Aplikasi Untuk Mendeteksi Karakterisasi Sensor SWD" 
     }
 )

app= MultiPage()
st.title("Aplikasi Untuk Shabrina")
app.add_page('Halaman Utama',home.app)
app.add_page('Kalkulator BMI & TDEE',calorie_calculator.app)
app.add_page('Kalkulator Nutrisi',calorie_tracker.app)
app.add_page('Kalkulator Olahraga',sport_calculator.app)
app.run()