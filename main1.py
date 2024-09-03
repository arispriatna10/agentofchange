import streamlit as st

st.write("""
# Aplikasi Cek Gaji Pokok
Ini adalah aplikasi untuk mengecek Gaji Pokok Berdasarkan Masa Kerja dan Golongan
""")


golongan_gendut = ["Pilih Golongan",
                 "Golongan IIa",
                 "Golongan IIb"]
masa_kerja = ["Pilih Masa Kerja", 
              "1 Tahun", 
              "2 Tahun"]
                 

golongan_gendutt = st.selectbox("Masukan Golongan",golongan_gendut)
masa_kerjaa = st.selectbox("Masukan Masa Kerja",masa_kerja)

if golongan_gendutt == "Golongan IIa" and masa kerjaa == "1 Tahun":
  st.write ("Gaji Pokoknya adalah 2.300.000")
 




