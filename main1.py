import streamlit as st

st.info("""
# Aplikasi Cek Gaji Pokok
""")
st.write("Ini adalah aplikasi untuk mengecek Gaji Pokok Berdasarkan Masa Kerja dan Golongan")

golongan_gendut = ["Pilih Golongan",
                 "Golongan Ia",
                 "Golongan Ib"]
masa_kerja = ["Pilih Masa Kerja", 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
                 

golongan_gendutt = st.selectbox(''':blue[Masukan Golongan]''', golongan_gendut)
masa_kerjaa = st.selectbox(''':blue[Masukan Masa Kerja (Dalam Tahun)]''',masa_kerja)

if golongan_gendutt == "Golongan Ia" and 0 <= masa_kerjaa <= 1:
  st.info ("Gaji Pokoknya adalah 1.685.700")

elif golongan_gendutt == "Golongan Ia" and 2 <= masa_kerjaa <= 3:
  st.write ("Gaji Pokoknya adalah 1.738.800")

elif golongan_gendutt == "Golongan Ia" and 4 <= masa_kerjaa <= 5:
  st.write ("Gaji Pokoknya adalah 1.793.500")
  
elif golongan_gendutt == "Golongan Ia" and 6 <= masa_kerjaa <= 7:
  st.write ("Gaji Pokoknya adalah 1.850.000")

elif golongan_gendutt == "Golongan Ia" and 8 <= masa_kerjaa <= 9:
  st.write ("Gaji Pokoknya adalah 1.908.300")

elif golongan_gendutt == "Golongan Ia" and 10 <= masa_kerjaa <= 11:
  st.write ("Gaji Pokoknya adalah 1.968.400")
  
elif golongan_gendutt == "Golongan Ia" and 12 <= masa_kerjaa <= 13:
  st.write ("Gaji Pokoknya adalah 2.030.400")

elif golongan_gendutt == "Golongan Ia" and 14 <= masa_kerjaa <= 15:
  st.write ("Gaji Pokoknya adalah 2.094.300")

elif golongan_gendutt == "Golongan Ia" and 16 <= masa_kerjaa <= 17:
  st.write ("Gaji Pokoknya adalah 2.160.300")
  
elif golongan_gendutt == "Golongan Ia" and 18 <= masa_kerjaa <= 19:
  st.write ("Gaji Pokoknya adalah 2.228.300")

elif golongan_gendutt == "Golongan Ia" and 20 <= masa_kerjaa <= 21:
  st.write ("Gaji Pokoknya adalah 2.298.500")

elif golongan_gendutt == "Golongan Ia" and 22 <= masa_kerjaa <= 23:
  st.write ("Gaji Pokoknya adalah 2.370.900")
  
elif golongan_gendutt == "Golongan Ia" and 24 <= masa_kerjaa <= 25:
  st.write ("Gaji Pokoknya adalah 2.445.500")

elif golongan_gendutt == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.write ("Gaji Pokoknya adalah 2.522.600")





