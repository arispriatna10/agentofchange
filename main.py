import streamlit as st

st.info("""
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
                 "Tenaga Ahli Non Sertifikat",
                 "Makanan dan Minuman Rapat (Platform GRATIS ONGKIR)",
                 "Makanan dan Minuman Tamu (Platform GRATIS ONGKIR)"]
original_lists = ["Pilih Mekanisme Pembayaran", "LS", "UP"]
                 

asal = st.selectbox(''':blue[Masukan Jenis Belanja]''',original_list)
mekanisme = st.selectbox(''':blue[Masukan Mekanisme Pembayaran]''',original_lists)

if asal == "Paket Meeting Fullday" and mekanisme == "LS":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Ringkasan Kontrak")
  st.info ("2. Surat Pesanan (SP)/Surat Perintah Kerja (SPK)")
  st.info ("3. Surat Perintah Mulai Kerja (SPMK)")
  st.info ("4. Berita Acara Pemeriksaan dan Serah Terima Pekerjaan (BAST)")
  st.info ("5. Permohonan Pembayaran")
  st.info ("6. Berita Acara Persetujuan Pembayaran (BAPP)")
  st.info ("7. E-Bupot PPh Pasal 23")
  st.info ("8. Id Billing PPh Pasal 23")
  st.info ("9. Rekening Koran")
  st.info ("10. Daftar Menu Makanan")
  st.info ("11. Daftar Hadir")
  st.info ("12. Undangan dan Rundown Acara")
  st.info ("13. Notulensi dan Dokumentasi Kegiatan")

elif asal == "Paket Meeting Fullboard" and mekanisme == "LS":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Ringkasan Kontrak")
  st.info ("2. Surat Pesanan (SP)/Surat Perintah Kerja (SPK)")
  st.info ("3. Surat Perintah Mulai Kerja (SPMK)")
  st.info ("4. Berita Acara Pemeriksaan dan Serah Terima Pekerjaan (BAST)")
  st.info ("5. Permohonan Pembayaran")
  st.info ("6. Berita Acara Persetujuan Pembayaran (BAPP)")
  st.info ("7. E-Bupot PPh Pasal 23")
  st.info ("8. Id Billing PPh Pasal 23")
  st.info ("9. Rekening Koran")
  st.info ("10. Daftar Kamar")
  st.info ("11. Daftar Menu Makanan")
  st.info ("12. Daftar Hadir")
  st.info ("13. Undangan dan Rundown Acara")
  st.info ("14. Notulensi dan Dokumentasi Kegiatan")

elif asal == "Makanan dan Minuman Rapat" and mekanisme == "LS":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Ringkasan Kontrak")
  st.info ("2. Surat Pesanan (SP)/Surat Perintah Kerja (SPK)")
  st.info ("3. Surat Perintah Mulai Kerja (SPMK)")
  st.info ("4. Berita Acara Pemeriksaan dan Serah Terima Pekerjaan (BAST)")
  st.info ("5. Permohonan Pembayaran")
  st.info ("6. Berita Acara Persetujuan Pembayaran (BAPP)")
  st.info ("7. E-Bupot PPh Pasal 22/PPh Pasal 23")
  st.info ("8. Id Billing PPh Pasal 22/PPh Pasal 23")
  st.info ("9. Daftar Hadir")
  st.info ("10. Foto Makanan dan Minuman Rapat")
  st.info ("11. Undangan dan Rundown Acara")
  st.info ("12. Notulensi dan Dokumentasi Kegiatan")
    
elif asal == "Honorarium Narasumber" and mekanisme == "LS":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Curriculum Vitae/Portfolio")
  st.info ("2. Surat Permohonan Narasumber")
  st.info ("3. Surat Tugas (jika PNS)")
  st.info ("4. Surat Kesediaan Menjadi Narasumber (jika Non PNS")
  st.info ("2. Daftar Hadir")
  st.info ("3. Daftar Nominatif")
  st.info ("4. Undangan dan Rundown Acara")
  st.info ("5. Notulensi/Paparan Materi")
  st.info ("6. Dokumentasi Kegiatan")
  st.info ("7. E-Bupot PPh Pasal 21")
  st.info ("8. Id Billing PPh Pasal 21")
  st.info ("9. Rekening Koran")

elif asal == "Tenaga Ahli Non Sertifikat" and mekanisme == "LS":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Kerangka Acuan Kerja (KAK)")
  st.info ("2. Curriculum Vitae/Portfolio")
  st.info ("3. Surat Perjanjian Kerja")
  st.info ("4. Laporan Output")
  st.info ("5. Daftar Hadir")
  st.info ("6. Daftar Nominatif")
  st.info ("7. E-Bupot PPh Pasal 21")
  st.info ("8. Bukti Setor PPh Pasal 21")
  st.info ("9. Rekening Koran")
  
elif asal == "Paket Meeting Fullday" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Surat Perintah Pembayaran Transfer (SPPT)/SI")
  st.info ("2. Ringkasan Kontrak")
  st.info ("3. Surat Pesanan (SP)/Surat Perintah Kerja (SPK)")
  st.info ("4. Surat Perintah Mulai Kerja (SPMK)")
  st.info ("5. Berita Acara Pemeriksaan dan Serah Terima Pekerjaan (BAST)")
  st.info ("6. E-Bupot PPh Pasal 23")
  st.info ("7. Bukti Setor PPh Pasal 23")
  st.info ("8. Daftar Menu Makanan")
  st.info ("9. Daftar Hadir")
  st.info ("10. Undangan dan Rundown Acara")
  st.info ("11. Notulensi dan Dokumentasi Kegiatan")

elif asal == "Paket Meeting Fullboard" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Surat Perintah Pembayaran Transfer (SPPT)/SI")
  st.info ("2. Ringkasan Kontrak")
  st.info ("3. Surat Pesanan (SP)/Surat Perintah Kerja (SPK)")
  st.info ("4. Surat Perintah Mulai Kerja (SPMK)")
  st.info ("5. Berita Acara Pemeriksaan dan Serah Terima Pekerjaan (BAST)")
  st.info ("6. E-Bupot PPh Pasal 23")
  st.info ("7. Bukti Setor PPh Pasal 23")
  st.info ("8. Daftar Kamar")
  st.info ("9. Daftar Menu Makanan")
  st.info ("10. Daftar Hadir")
  st.info ("11. Undangan dan Rundown Acara")
  st.info ("12. Notulensi dan Dokumentasi Kegiatan")

elif asal == "Perjalanan Dinas Paket Meeting" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Surat Undangan")
  st.info ("2. Surat Perintah")
  st.info ("3. Rampung Rincian Perjalanan Dinas")
  st.info ("4. Daftar Nominatif")
  st.info ("5. Visum/Surat Perjalanan Dinas")
  st.info ("6. Tanda Bukti Transport")
  st.info ("7. Laporan dan Dokumentasi Perjalanan Dinas")

elif asal == "Perjalanan Dinas Luar Kota Dalam Provinsi" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Surat Undangan")
  st.info ("2. Surat Perintah")
  st.info ("3. Rampung Rincian Perjalanan Dinas")
  st.info ("4. Daftar Nominatif")
  st.info ("5. Visum/Surat Perjalanan Dinas")
  st.info ("6. Tanda Bukti Transport")
  st.info ("7. Tanda Bukti Penginapan")
  st.info ("8. Laporan dan Dokumentasi Perjalanan Dinas")

elif asal == "Perjalanan Dinas Luar Provinsi" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Surat Undangan")
  st.info ("2. Surat Perintah")
  st.info ("3. Rampung Rincian Perjalanan Dinas")
  st.info ("4. Daftar Nominatif")
  st.info ("5. Visum/Surat Perjalanan Dinas")
  st.info ("6. Tanda Bukti Transport")
  st.info ("7. Tanda Bukti Penginapan")
  st.info ("7. Laporan dan Dokumentasi Perjalanan Dinas")

elif asal == "Perjalanan Dinas Luar Negeri" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Kerangka Acuan Kerja (KAK)")
  st.info ("2. Persuratan")
  st.info ("3. SK Tim")
  st.info ("4. Usulan peserta ke Kemendagri")
  st.info ("5. Rekomendasi dari Kemendagri ke Setneg")
  st.info ("6. Surat Izin dari Setneg")
  st.info ("7. Surat Perintah ")
  st.info ("8. Rampung Rincian Perjalanan Dinas")
  st.info ("9. Daftar Nominatif")
  st.info ("10. Visum/Surat Perjalanan Dinas")
  st.info ("11. Tanda Bukti Transport")
  st.info ("12. Paspor Biru (fotocopy yang ada cap kedatangan/kepulangan")
  st.info ("13. Visa (fotocopy yang ada cap kedatangan/kepulangan")
  st.info ("14. E-Tiket dari maskapai")
  st.info ("15. Boarding Pass")
  st.info ("16. Laporan dan Dokumentasi Perjalanan Dinas")
  st.info ("17. Bukti Penyampaian Laporan ke Kemendagri")

elif asal == "Makanan dan Minuman Rapat" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Surat Undangan")
  st.info ("2. Proses Pengadaan Barang dan Jasa")
  st.info ("3. Bukti Pembelian")
  st.info ("4. Daftar Hadir")
  st.info ("5. Notulensi Rapat")
  st.info ("6. Foto Makanan dan Minuman Rapat")
  st.info ("7. Dokumentasi Kegiatan")
  st.info ("8. E-Bupot PPh Pasal 22/PPh Pasal 23")
  st.info ("9. Bukti Setor PPh Pasal 22/PPh Pasal 23")

elif asal == "Makanan dan Minuman Tamu" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Surat Undangan")
  st.info ("2. Proses Pengadaan Barang dan Jasa")
  st.info ("3. Bukti Pembelian")
  st.info ("4. Dokumentasi Kegiatan")
  st.info ("5. E-Bupot PPh Pasal 22/PPh Pasal 23")
  st.info ("6. Bukti Setor PPh Pasal 22/PPh Pasal 23")
  
elif asal == "Honorarium Narasumber" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Curriculum Vitae/Portfolio")
  st.info ("2. Surat Permohonan Narasumber")
  st.info ("3. Surat Tugas (jika PNS)")
  st.info ("4. Surat Kesediaan Menjadi Narasumber (jika Non PNS")
  st.info ("6. Daftar Nominatif")
  st.info ("7. Undangan dan Rundown Acara")
  st.info ("8. Notulensi/Paparan Materi")
  st.info ("9. Dokumentasi Kegiatan")
  st.info ("10. E-Bupot PPh Pasal 21")
  st.info ("11. Bukti Setor PPh Pasal 21")
  

elif asal == "Tenaga Ahli Non Sertifikat" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Kerangka Acuan Kerja (KAK)")
  st.info ("2. Curriculum Vitae/Portfolio")
  st.info ("3. Surat Perjanjian Kerja")
  st.info ("4. Laporan Pekerjaan")
  st.info ("5. Daftar Hadir")
  st.info ("6. Daftar Nominatif")
  st.info ("7. NPWP")
  st.info ("5. E-Bupot PPh Pasal 21")
  st.info ("6. Bukti Setor PPh Pasal 21")

elif asal == "Makanan dan Minuman Rapat (Platform GRATIS ONGKIR)" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Surat Undangan")
  st.info ("2. Invoice")
  st.info ("3. Surat Pesanan")
  st.info ("4. Berita Acara Penerimaan")
  st.info ("5. Daftar Hadir")
  st.info ("6. Notulensi Rapat")
  st.info ("7. Foto Makanan dan Minuman Rapat")
  st.info ("8. Dokumentasi Kegiatan")
  st.info ("9. E-Bupot PPh Pasal 22/PPh Pasal 23")
  st.info ("10. Bukti Setor PPh Pasal 22/PPh Pasal 23")

elif asal == "Makanan dan Minuman Tamu (Platform GRATIS ONGKIR)" and mekanisme == "UP":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Invoice")
  st.info ("2. Surat Pesanan")
  st.info ("3. Berita Acara Penerimaan")
  st.info ("4. Dokumentasi Kegiatan")
  st.info ("5. E-Bupot PPh Pasal 22/PPh Pasal 23")
  st.info ("6. Bukti Setor PPh Pasal 22/PPh Pasal 23")




