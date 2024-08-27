import streamlit as st

st.write("""
# Aplikasi Cek BBM
Ini adalah aplikasi mengecek kebutuhan BBM Perjalanan Dinas
""")


original_list = ["Pilih Jenis Belanja",
                 "Paket Meeting Fullday", 
                 "Paket Meeting Fullboard",
                 "Perjalanan Dinas Paket Meeting",
                 "Perjalanan Dinas Luar Kota Dalam Provinsi",
                 "Perjalanan Dinas Luar Provinsi",
                 "Perjalanan Dinas Luar Negeri",
                 "Makanan dan Minuman Rapat",
                 "Makanan dan Minuman Tamu",
                 "Honorarium Narasumber",
                 "Tenaga Ahli Non Sertifikat",]
                 

asal = st.selectbox("Masukan Jenis Belanja",original_list)

if asal == "Paket Meeting Fullday":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Berita Acara Pemeriksaan")

elif asal == "Paket Meeting Fullboard":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Ringkasan Kontrak")
  st.write ("2. Surat Pesanan (SP)/Surat Perintah Kerja (SPK)")
  st.write ("3. Surat Perintah Mulai Kerja (SPMK)")
  st.write ("4. Berita Acara Pemeriksaan dan Serah Terima Pekerjaan (BAST)")
  st.write ("5. Permohonan Pembayaran")
  st.write ("6. Berita Acara Persetujuan Pembayaran (BAPP)")
  st.write ("7. E-Bupot PPh Pasal 23")
  st.write ("8. Rekening Koran")
  st.write ("9. Daftar Kamar")
  st.write ("10. Daftar Menu Makanan")
  st.write ("11. Daftar Hadir")
  st.write ("12. Undangan dan Rundown Acara")
  st.write ("13. Notulensi dan Dokumentasi Kegiatan")


