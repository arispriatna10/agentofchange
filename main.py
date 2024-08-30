import streamlit as st

st.write("""
# Aplikasi Cek Kelengkapan Dokumen SPJ
Ini adalah aplikasi untuk mengecek Dokumen Kelengkapan SPJ
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
original_lists = ["Pilih Mekanisme Pembayaran", "LS", "UP"]
                 

asal = st.selectbox("Masukan Jenis Belanja",original_list)
mekanisme = st.selectbox("Masukan Mekanisme Pembayaran",original_lists)

if asal == "Paket Meeting Fullday" and mekanisme == "LS":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Ringkasan Kontrak")
  st.write ("2. Surat Pesanan (SP)/Surat Perintah Kerja (SPK)")
  st.write ("3. Surat Perintah Mulai Kerja (SPMK)")
  st.write ("4. Berita Acara Pemeriksaan dan Serah Terima Pekerjaan (BAST)")
  st.write ("5. Permohonan Pembayaran")
  st.write ("6. Berita Acara Persetujuan Pembayaran (BAPP)")
  st.write ("7. E-Bupot PPh Pasal 23")
  st.write ("8. Rekening Koran")
  st.write ("9. Daftar Menu Makanan")
  st.write ("10. Daftar Hadir")
  st.write ("11. Undangan dan Rundown Acara")
  st.write ("12. Notulensi dan Dokumentasi Kegiatan")

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

elif asal == "Perjalanan Dinas Paket Meeting":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Surat Undangan")
  st.write ("2. Surat Perintah")
  st.write ("3. Rampung Rincian Perjalanan Dinas")
  st.write ("4. Daftar Nominatif")
  st.write ("5. Visum/Surat Perjalanan Dinas")
  st.write ("6. Tanda Bukti Transport")
  st.write ("7. Laporan dan Dokumentasi Perjalanan Dinas")

elif asal == "Perjalanan Dinas Luar Kota Dalam Provinsi":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Surat Undangan")
  st.write ("2. Surat Perintah")
  st.write ("3. Rampung Rincian Perjalanan Dinas")
  st.write ("4. Daftar Nominatif")
  st.write ("5. Visum/Surat Perjalanan Dinas")
  st.write ("6. Tanda Bukti Transport")
  st.write ("7. Tanda Bukti Penginapan")
  st.write ("8. Laporan dan Dokumentasi Perjalanan Dinas")

elif asal == "Perjalanan Dinas Luar Provinsi":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Surat Undangan")
  st.write ("2. Surat Perintah")
  st.write ("3. Rampung Rincian Perjalanan Dinas")
  st.write ("4. Daftar Nominatif")
  st.write ("5. Visum/Surat Perjalanan Dinas")
  st.write ("6. Tanda Bukti Transport")
  st.write ("7. Tanda Bukti Penginapan")
  st.write ("7. Laporan dan Dokumentasi Perjalanan Dinas")

elif asal == "Perjalanan Dinas Luar Negeri":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Kerangka Acuan Kerja (KAK)")
  st.write ("2. Persuratan")
  st.write ("3. SK Tim")
  st.write ("4. Usulan peserta ke Kemendagri")
  st.write ("5. Rekomendasi dari Kemendagri ke Setneg")
  st.write ("6. Surat Izin dari Setneg")
  st.write ("7. Surat Perintah ")
  st.write ("8. Rampung Rincian Perjalanan Dinas")
  st.write ("9. Daftar Nominatif")
  st.write ("10. Visum/Surat Perjalanan Dinas")
  st.write ("11. Tanda Bukti Transport")
  st.write ("12. Paspor Biru (fotocopy yang ada cap kedatangan/kepulangan")
  st.write ("13. Visa (fotocopy yang ada cap kedatangan/kepulangan")
  st.write ("14. E-Tiket dari maskapai")
  st.write ("15. Boarding Pass")
  st.write ("16. Laporan dan Dokumentasi Perjalanan Dinas")
  st.write ("17. Bukti Penyampaian Laporan ke Kemendagri")

elif asal == "Makanan dan Minuman Rapat":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Surat Undangan")
  st.write ("2. Proses Pengadaan Barang dan Jasa")
  st.write ("3. Bukti Pembelian")
  st.write ("4. Daftar Hadir")
  st.write ("5. Notulensi Rapat")
  st.write ("6. Foto Makanan dan Minuman Rapat")
  st.write ("7. Dokumentasi Kegiatan")
  st.write ("8. E-Bupot PPh Pasal 22/PPh Pasal 23")
  st.write ("9. Bukti Setor PPh Pasal 22/PPh Pasal 23")

elif asal == "Makanan dan Minuman Tamu":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Surat Undangan")
  st.write ("2. Proses Pengadaan Barang dan Jasa")
  st.write ("3. Bukti Pembelian")
  st.write ("4. Dokumentasi Kegiatan")
  st.write ("5. E-Bupot PPh Pasal 22/PPh Pasal 23")
  st.write ("6. Bukti Setor PPh Pasal 22/PPh Pasal 23")
  
elif asal == "Honorarium Narasumber":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Curriculum Vitae/Portfolio")
  st.write ("2. Surat Permohonan Narasumber")
  st.write ("3. Surat Tugas (jika PNS)")
  st.write ("4. Surat Kesediaan Menjadi Narasumber (jika Non PNS")
  st.write ("2. Daftar Hadir")
  st.write ("3. Daftar Nominatif")
  st.write ("4. Undangan dan Rundown Acara")
  st.write ("5. Notulensi/Paparan Materi")
  st.write ("6. Dokumentasi Kegiatan")
  st.write ("7. E-Bupot PPh Pasal 21")
  st.write ("8. Bukti Setor PPh Pasal 21")
  

elif asal == "Tenaga Ahli Non Sertifikat":
  st.write ("Dokumen Kelengkapan:")
  st.write ("1. Kerangka Acuan Kerja (KAK)")
  st.write ("2. Curriculum Vitae/Portfolio")
  st.write ("3. Surat Perjanjian Kerja")
  st.write ("4. Laporan Pekerjaan")
  st.write ("5. Daftar Hadir")
  st.write ("6. Daftar Nominatif")
  st.write ("7. NPWP")
  st.write ("5. E-Bupot PPh Pasal 21")
  st.write ("6. Bukti Setor PPh Pasal 21")




