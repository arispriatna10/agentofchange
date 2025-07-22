import streamlit as st

st.set_page_config(
    page_title="Aplikasi Cek Kelengkapan SPJ", 
    page_icon="📑",
)

st.info("""
# Aplikasi Cek Kelengkapan Dokumen SPJ
Ini adalah aplikasi untuk mengecek Dokumen Kelengkapan SPJ
""")


original_list = ["Pilih Jenis Belanja",                
                "Pembayaran Honorarium dan Transport untuk Narasumber atau Pembahas, Moderator dan Pembawa Acara",
                "Biaya uang saku/transport kegiatan sosialisasi/penyuluhan kepada Masyarakat serta uang saku/transport kegiatan Pendidikan dan pelatihan",
                "Honorarium Tenaga Teknis Pelaksana Kegiatan dan Tenaga Ahli",
                "Upah Tenaga Harian Lepas dan Honorarium Non ASN Lainnya",
                "Honorarium Rohaniwan dan Penceramah",
                "Honorarium Pengawalan Kepala Daerah dan Wakil Kepala Daerah",
                "Belanja Barang dan Jasa",
                "Belanja Makanan dan Minuman Rapat/Peserta/Petugas/Panitia",
                "Belanja Telepon, Air, Listrik, Koran/Majalah/Surat Kabar dan Sejenisnya",
                "Perpanjangan STNK (Tahunan/Lima Tahunan)",
                "Belanja Jasa KIR",
                "Belanja Jasa Uji Laboratorium/Uji Sampling",
                "Belanja Pajak Bumi dan Bangunan (PBB)",
                "Instalasi PAM/Pemasangan Baru Listrik/Penambahan Daya Listrik/ Jaringan Internet/ TV Kabel",
                "Bahan Bakar Kendaraan Dinas dan Alat Berat",
                "Belanja pembayaran jasa jalan Tol",
                "Belanja Sewa Hotel (Paket Meeting)",
                "Belanja perawatan kendaraan bermotor",
                "Belanja Jasa Penerangan/Iklan/Reklame/Film/Pemotretan",                 
                ]
                 

asal = st.selectbox(''':blue[Masukan Jenis Belanja]''',original_list)




if asal == "Pembayaran Honorarium dan Transport untuk Narasumber atau Pembahas, Moderator dan Pembawa Acara":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Surat permohonan narasumber atau undangan/ disposisi")
  st.info ("- Laporan hasil kegiatan")
  st.info ("- Daftar Hadir")
  st.info ("- Kuitansi")
  st.info ("- Biodata Narasumber")
  st.info ("- Daftar Nominatif Honorarium")
  st.info ("- Bukti transfer kepada penerima")
  st.info ("- Billing pajak")
  st.info ("- Bukti penerimaan negara")

elif asal == "Biaya uang saku/transport kegiatan sosialisasi/penyuluhan kepada Masyarakat serta uang saku/transport kegiatan Pendidikan dan pelatihan":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Undangan dan/atau surat tugas")
  st.info ("- Daftar hadir/bukti kehadiran/laporan (untuk peserta sosialisasi/penyuluhan kepada Masyarakat)")
  st.info ("- Laporan hasil kegiatan (untuk peserta Pendidikan dan pelatihan)")
  st.info ("- Daftar uang transportasi")

elif asal == "Honorarium Tenaga Teknis Pelaksana Kegiatan dan Tenaga Ahli":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Daftar Nominatif Gaji")
  st.info ("- Daftar Hadir")
  st.info ("- Lampiran Keputusan Gubernur pada awal tahun/pada saat ada perubahan")
  st.info ("- Laporan Kegiatan Individu")
  st.info ("- Billing BPJS, Billing PPh")
  st.info ("- Sertifikat Keahlian (untuk tenaga ahli)")
  st.info ("- Bukti Penerimaan Negara")
                               
elif asal == "Upah Tenaga Harian Lepas dan Honorarium Non ASN Lainnya":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Daftar Nominatif Upah")
  st.info ("- Rekapitulasi Pembayaran Upah")
  st.info ("- Laporan Hasil Pekerjaan")
  st.info ("- Dokumen lain sesuai Peraturan Perundang-undangan")
  st.info ("- Billing PPh")
  st.info ("- Bukti Penerimaan Negara")
 
elif asal == "Honorarium Rohaniwan dan Penceramah":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Daftar Hadir")
  st.info ("- Daftar Honor/Kuitansi")
  st.info ("- Surat Permohonan sebagai Penceramah")
  st.info ("- Billing PPh")
  st.info ("- Bukti Penerimaan Negara")

 elif asal == "Honorarium Pengawalan Kepala Daerah dan Wakil Kepala Daerah":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Daftar Nominatif Honorarium")
  st.info ("- Surat Keputusan Penunjukan dari Kesatuan")
  st.info ("- Dokumen lain sesuai Peraturan Perundang-undangan")
  st.info ("- Billing PPh")
  st.info ("- Bukti Penerimaan Negara")

elif asal == "Belanja Barang dan Jasa":
  st.info ("Dokumen Kelengkapan:")
  st.info ("Belanja barang dan jasa s.d Rp10.000.000,- dilampirkan bukti pembelian/pembayaran (Bukti Pembelian dapat berupa faktur/bon/invoice, struk, dan nota kontan) / Surat Pesanan")
  st.info ("Belanja barang dan jasa Rp 10.000.000,- s.d Rp50.000.000,- dilengkapi kuitansi / Surat Pesanan")
  st.info ("Belanja barang dan jasa Rp 50.000.000,- s.d Rp200.000.000,- atau Belanja Jasa Konsultansi s.d Rp100.000.000,- dan Belanja Jasa Konstruksi s.d Rp200.000.000,- dilengkapi Surat Perintah Kerja (SPK) / Surat Pesanan")
  st.info ("Belanja barang dan jasa di atas Rp 200.000.000,- dan Belanja Jasa Konsultansi di atas Rp100.000.000,- dilengkapi dengan Surat Perjanjian / Surat Pesanan")
  st.info ("- E-Faktur untuk yang dikenakan PPN dan Penyedia PKP")
  st.info ("- Billing PPh")
  st.info ("- Bukti Penerimaan Negara")
  st.info ("- Berita Acara Hasil Pemeriksaan PPK dengan Penyedia")
  st.info ("- Berita Acara Serah Terima PPK dengan Penyedia")
  st.info (" ")
  st.info ("Dokumen kelengkapan pertanggungjawaban yang menjadi tanggung jawab PPTK sesuai tugasnya, diantaranya :")
  st.info ("- Surat Permohonan kebutuhan dari PPTK ke PA/KPA/PPK (dibuat sekaligus di awal tahun/kebutuhan")
  st.info ("- Surat Permintaan dari PPK ke Pejabat Pengadaan (dibuat sekaligus di awal tahun/kebutuhan")
  st.info ("- Salinan Bukti Pembelian/Pembayaran")
  st.info ("- Salinan e-Faktur untuk yang dikenakan PPN dan Penyedia merupakan PKP")
  st.info (" ")
  st.info ("Dalam hal belanja barang modal, maka perlu dibuat :")
  st.info ("- Berita Acara Hasil Pemeriksaan PPK dengan Penyedia")
  st.info ("- Berita Acara Serah Terima PPK dengan Penyedia")
  st.info ("- Berita Acara Penyelesaian Pekerjaan dari PPK ke PA/KPA")
  st.info ("- Surat Permintaan PA/KPA kepada PJPHP/PPHP untuk melakukan pemeriksaan Administrasi")
  st.info ("- Berita Acara Pemeriksaan Administrasi oleh PJPHP (tidak menjadi syarat pembayaran")
    
elif asal == "Belanja Makanan dan Minuman Rapat/Peserta/Petugas/Panitia":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")


elif asal == "Belanja Telepon, Air, Listrik, Koran/Majalah/Surat Kabar dan Sejenisnya":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
    
elif asal == "Perpanjangan STNK (Tahunan/Lima Tahunan)":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")


elif asal == "Belanja Jasa KIR":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
   
elif asal == "Belanja Jasa Uji Laboratorium/Uji Sampling":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")

elif asal == "Belanja Pajak Bumi dan Bangunan (PBB)":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")

elif asal == "Instalasi PAM/Pemasangan Baru Listrik/Penambahan Daya Listrik/ Jaringan Internet/ TV Kabel":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")

elif asal == "Bahan Bakar Kendaraan Dinas dan Alat Berat":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")

elif asal == "Belanja pembayaran jasa jalan Tol":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
                 
elif asal == "Belanja Sewa Hotel (Paket Meeting)":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")

elif asal == "Belanja perawatan kendaraan bermotor":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")


elif asal == "Belanja Jasa Penerangan/Iklan/Reklame/Film/Pemotretan":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
  st.info ("- ")
