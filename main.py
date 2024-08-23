import streamlit as st

st.write(""""
# Aplikasi Cek BBM
Ini adalah aplikasi mengecek kebutuhan BBM Perjalanan Dinas
""")

original_list = ["Pilih Kabupaten/Kota","Kota Bandung","DKI Jakarta", "Kab Bandung Barat"]


asal = st.selectbox("Masukan Tempat Asal",original_list)
tujuan = st.selectbox("Masukan Tempat Tujuan",original_list)

if asal == "Kota Bandung" and tujuan == "DKI Jakarta":
   st.write ("Jumlah Maksimalnya adalah", 15)
   st.write ("Jumalh Minimalnya adalah", 15)

elif asal == "Kota Bandung" and tujuan == "Kab Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 20)


   
