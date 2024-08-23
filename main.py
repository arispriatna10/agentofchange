import streamlit as st

st.write(""""
# Aplikasi Cek BBM
Ini adalah aplikasi mengecek kebutuhan BBM Perjalanan Dinas
""")

original_list = ["Pilih Jenis Belanja",
                 "Belanja Perjalanan Dinas",
                 "DKI Jakarta", 
                 "Kab Bandung Barat"]


asal = st.selectbox("Masukan Tempat Asal",original_list)


if asal == "Belanja Langsung":
   st.write ("Dokumen Kelengkapan:")
   st.write ("1. Surat Permintaan Pembayaran", 15)

elif asal == "Belanja Perjalanan Dinas":
   st.write ("Dokumen Kelengkapan:")
   st.write ("1. Rampung Rincian Belanja Perjalanan Dinas")
   st.write ("2. Daftar Nominatif")
   st.write ("3. Surat Perintah")
   st.write ("4. Visum Surat Perjalanan Dinas")
   st.write ("5. Laporan dan Dokumentasi Perjalanan Dinas")
   st.write ("6. Tanda Bukti BBM, Tol, Tiket Pesawat, dan lain-lain")



   
