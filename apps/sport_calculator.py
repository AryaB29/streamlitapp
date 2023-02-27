import streamlit as st
import pandas as pd

def app():
    st.title("Sport Calculator")
    st.write("Hiiiii, disini luu bisa liat berapa banyakk kalori yang dibakar per 1 jam olgaaa")

    data2 = pd.read_csv('exercise_dataset.csv')
    data2 = data2.rename(columns={'Activity, Exercise or Sport (1 hour)': 'Jenis_Olahraga'})
    jenis_olga = st.sidebar.multiselect("Tipe Olahraga",data2['Jenis_Olahraga'],default='Unicycling')
    badan = st.sidebar.number_input("Masukan Berat Badann")
    waktu = st.sidebar.number_input("Masukan Lama Olahraga (Dalam Jam)")
    info_or = pd.DataFrame(data2.query("Jenis_Olahraga=={}".format(jenis_olga))[["Jenis_Olahraga","Calories per kg"]])
    st.write(info_or)
    st.write("Berat Badan yang dimasukan")
    st.write(badan)
    st.write("Lama Waktu Olahraga")
    st.write(waktu)



    st.write("Total Kalori yang dibakar")
    kzq = list(info_or['Calories per kg'])
    tpq = int(kzq[0])
    kalori = badan * waktu * tpq
    st.write(kalori)