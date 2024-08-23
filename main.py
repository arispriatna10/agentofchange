import streamlit as st

st.write(""""
# Aplikasi Cek BBM
Ini adalah aplikasi mengecek kebutuhan BBM Perjalanan Dinas
""")

original_list = ["Pilih Kabupaten/Kota","Belanja Langsung","DKI Jakarta", "Kab Bandung Barat"]


asal = st.selectbox("Masukan Tempat Asal",original_list)


if asal == "Belanja Langsung":
   st.write ("Dokumen Kelengkapan:")
   st.write ("1. Surat Permintaan Pembayaran", 15)

elif asal == "Kota Bandung" and tujuan == "Kab Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 20)


   
