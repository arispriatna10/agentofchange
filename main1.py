import streamlit as st

st.write("""
# Aplikasi Cek Gaji Pokok
Ini adalah aplikasi untuk mengecek Gaji Pokok Berdasarkan Masa Kerja dan Golongan
""")


golongan_gendut = ["Pilih Golongan",
                 "Golongan Ia",
                 "Golongan Ib"]
masa_kerja = ["Pilih Masa Kerja", 
              0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
                 

golongan_gendutt = st.selectbox("Masukan Golongan",golongan_gendut)
masa_kerjaa = st.selectbox("Masukan Masa Kerja (Dalam Tahun)",masa_kerja)

if golongan_gendutt == "Golongan Ia" and 0 <= masa_kerjaa <= 1:
  st.write ("Gaji Pokoknya adalah 1.685.700")

if golongan_gendutt == "Golongan Ia" and 2 <= masa_kerjaa <= 3:
  st.write ("Gaji Pokoknya adalah 1.738.800")




