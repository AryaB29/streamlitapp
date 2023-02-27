import streamlit as st
import pandas as pd

def app():
    st.title("Hiii Welcome too caloriee tracker")
    st.write('disini luu bisa liat ada berapa banyak makanan yang udahh luu makann')
    data = pd.read_csv('data makanan.csv',on_bad_lines='skip',sep=';')
    makan_pagi = st.sidebar.multiselect("Makan Pagi",data['Food'])
    makan_siang = st.sidebar.multiselect("Makan Siang",data['Food'])
    makan_malem = st.sidebar.multiselect("Makan Malem",data['Food'])
    kalori_pagi = pd.DataFrame(data.query("Food=={}".format(makan_pagi))[["Food","Serving","Calories"]])
    kalori_siang = pd.DataFrame(data.query("Food=={}".format(makan_siang))[["Food","Serving","Calories"]])
    kalori_malem = pd.DataFrame(data.query("Food=={}".format(makan_malem))[["Food","Serving","Calories"]])
    dataf1 = pd.DataFrame(kalori_pagi)
    dataf2 = pd.DataFrame(kalori_siang)
    dataf3 = pd.DataFrame(kalori_malem)

    st.write("Asupan Pagi Hari")
    st.write(dataf1)
    st.write("Asupan Siang Hari")
    st.write(dataf2)
    st.write("Asupan Malam Hari")
    st.write(dataf3)


    st.write("Total Kalori Pagi Hari")
    cb = list(dataf1['Calories'])
    kt = [words for segments in cb for words in segments.split()]
    ct=[]
    for i in range(len(kt)):
        if i%2==0:
            kg = int(kt[i])
            ct.append(kg)     
    st.write(sum(ct))

    st.write("Total Kalori Siang Hari")
    tu = list(dataf2['Calories'])
    pt = [words for segments in tu for words in segments.split()]
    ac=[]
    for j in range(len(pt)):
        if j%2==0:
            ok = int(pt[j])
            ac.append(ok)     
    st.write(sum(ac))

    st.write("Total Kalori Malam Hari")
    psc= list(dataf3['Calories'])
    aop = [words for segments in psc for words in segments.split()]
    iop=[]
    for k in range(len(aop)):
        if k%2==0:
            sui = int(aop[k])
            iop.append(sui)     
    st.write(sum(iop))

    uip = sum(ct)
    uiw = sum(ac)
    uwo = sum(iop)
    nuio = uip+uiw+uwo

    st.write("Total Asupan Kalori Hari Ini ")
    st.write(nuio)