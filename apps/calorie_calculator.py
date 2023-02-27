import streamlit as st
from PIL import Image

def app():
    st.title("Calories Calculator")
    st.write("Hiii, disini lu bisa tau kira kira kebutuhan kalori luu berapa yapsskyyy")
    st.write("Jadi metode kita pakeee namanya TDEE dan BMI intinya berapa banyak energi yang lu keluarin \n LANJUTANNYA CARI SENDIRI JAN MALES")

    Method = st.sidebar.selectbox("Masukinn Jenis Perhitungan",('BMI','TDEE'))

    if Method=='BMI':
        st.image('BMI.jpeg')
        tinggi_coba = st.sidebar.number_input("Masukin Yuk Tinggi Badan (cm)",value=160)
        berat_coba = st.sidebar.number_input("Masukin berat badann (kg)",value=50)
        tinggi_coba_fix = tinggi_coba/100
        bmi = berat_coba/(tinggi_coba_fix**2)
        st.write('Dari Perhitungan Nilai BMI lu adalahhh')
        st.write(bmi)

    if Method=='TDEE':
        nama = st.sidebar.text_input("Masukin Nama Lu Sokap",value='Joni')
        sex = st.sidebar.selectbox("Masukinn Jenis Kelamin Lauu",('Laki Laki','Perempuan'))
        age = st.sidebar.number_input("Masukin Umur Lauuu")
        age_fix = int(age)
        tinggi= st.sidebar.number_input("Masukin Tinggi Badan (cm)",value=1)
        tinggi_fix = int(tinggi)
        berat = st.sidebar.number_input("Masukin Berat Badann ( Tenang Aja Rahasia Kok 🤣) (kg)",value=1)
        berat_fix = float(berat)
        activity = st.sidebar.selectbox("Kira Kira Aktifitas Perminggu Lu Gimana??",('Ga Olga','Olga 3-5 Kali','Olga 5-7 Kali'))

        if activity =='Ga Olga':
            activ = 1.2
        if activity=='Olga 3-5 Kali':
            activ = 1.55
        if activity=='Olga 5-7 Kali':
            activ = 1.725

        if sex == 'Perempuan':
            nilai = ((10 * berat_fix) + (6.25 * tinggi_fix) - (5 * age_fix -161)) * activ
        if sex == 'Laki Laki':
            nilai = ((10 * berat_fix) + (6.25 * tinggi_fix) - (5 * age_fix +5)) * activ
        
        
        st.write('HI {}'.format(nama))
        st.write('Ini ada informasi beberapa hal tentang diri lu yaaa')
        st.write('Jenis Kelamin Luu : {}'.format(sex))
        st.write('Umur Luu : {}'.format(age))
        st.write('Tinggi Luu : {}'.format(tinggi_fix))
        st.write('Berat Luu : {}'.format(berat_fix))
        st.write('Dari perhitungan TDEE Lu butuh sekitar {} Kalori Per Hari'.format(nilai))