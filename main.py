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
  st.text (" ")
  st.info ("Dokumen kelengkapan pertanggungjawaban yang menjadi tanggung jawab PPTK sesuai tugasnya, diantaranya :")
  st.info ("- Surat Permohonan kebutuhan dari PPTK ke PA/KPA/PPK (dibuat sekaligus di awal tahun/kebutuhan")
  st.info ("- Surat Permintaan dari PPK ke Pejabat Pengadaan (dibuat sekaligus di awal tahun/kebutuhan")
  st.info ("- Salinan Bukti Pembelian/Pembayaran")
  st.info ("- Salinan e-Faktur untuk yang dikenakan PPN dan Penyedia merupakan PKP")
  st.text (" ")
  st.info ("Dalam hal belanja barang modal, maka perlu dibuat :")
  st.info ("- Berita Acara Hasil Pemeriksaan PPK dengan Penyedia")
  st.info ("- Berita Acara Serah Terima PPK dengan Penyedia")
  st.info ("- Berita Acara Penyelesaian Pekerjaan dari PPK ke PA/KPA")
  st.info ("- Surat Permintaan PA/KPA kepada PJPHP/PPHP untuk melakukan pemeriksaan Administrasi")
  st.info ("- Berita Acara Pemeriksaan Administrasi oleh PJPHP (tidak menjadi syarat pembayaran")
    
elif asal == "Belanja Makanan dan Minuman Rapat/Peserta/Petugas/Panitia":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Bukti Pembayaran/Kuitansi/SPK/Surat Perjanjian")
  st.info ("- Notulensi dan Dokumentasi")
  st.info ("- Daftar Hadir")
  st.info ("- Undangan Rapat")
  st.info ("- Billing PPh")
  st.info ("- Bukti Penerimaan Negara")
  st.info ("- Nota Pengiriman Barang / Surat Jalan untuk nilai di bawah Rp50.000.000,- dan ditandatangani PPK sebagai serah PPK dengan Penyedia")
  st.text (" ")
  st.info ("Untuk Belanja Makanan dan Minuman Harian Pegawai/Tamu/ di atas Rp50.000.000,- maka perlu dibuat : ")
  st.info ("- Berita Acara Serah Terima PPK dengan Penyedia")  

elif asal == "Belanja Telepon, Air, Listrik, Koran/Majalah/Surat Kabar dan Sejenisnya":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Surat atau Tagihan / Invocie dari Penyedia Jasa")
  st.info ("- Berita Acara Serah Terima Tagihan")
    
elif asal == "Perpanjangan STNK (Tahunan/Lima Tahunan)":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Bukti Pembayaran Pajak")
  st.info ("- Salinan Surat Ketetapan Kewajiban Pembayaran (SKKP)")
  
elif asal == "Belanja Jasa KIR":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Dokumen bukti uji KIR")
  st.info ("- Bukti Pembayaran KIR")
   
elif asal == "Belanja Jasa Uji Laboratorium/Uji Sampling":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Hasil Uji Lab / Uji Sampling")
  st.info ("- Billing Pajak")
  st.info ("- Bukti Penerimaan Pajak Negara")
  st.text (" ")
  st.text ("PPN dan PPh 23 dipungut dan dipotong jika dilakukan oleh Badan Usaha (Perusahaan atau Laboratorium Swasta)")

elif asal == "Belanja Pajak Bumi dan Bangunan (PBB)":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Surat Pemberitahuan Pajak Terhutang PBB (SPPT PBB)")
  st.info ("- Bukti Pembayaran Pajak Bumi dan Bangunan")
  st.info ("- Bukti Penerimaan Pajak Bumi dan Bangunan")
     
elif asal == "Instalasi PAM/Pemasangan Baru Listrik/Penambahan Daya Listrik/ Jaringan Internet/ TV Kabel":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Surat Permintaan Kepala SKPD")
  st.info ("- Surat Kesepakatan")
  st.info ("- Tagihan/Invoice")
  st.info ("- Billing PPh")
  st.info ("- Bukti Penerimaan Negara")

elif asal == "Bahan Bakar Kendaraan Dinas dan Alat Berat":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Invoice dan/atau Rekap penggunaan Bahan Bakar dari penyedia")
  st.info ("- Berita Acara Hasil Pemeriksaan dan berita acara serah terima (bila diperlukan)")
  st.info ("- Billing PPh untuk PPh 23 atas jasa pengangkutan atau pengiriman")
  st.info ("- Bukti Penerimaan Negara")
 
elif asal == "Belanja pembayaran jasa jalan Tol":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Struk pembayaran Tol")
  st.info ("- Rekapitulasi pembayaran Tol")
 
elif asal == "Belanja Sewa Hotel (Paket Meeting)":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Pesanan dari Pejabat Pengadaan/Pokja Pemilihan kepada penyedia")
  st.info ("- Penawaran dari penyedia")
  st.info ("- Invoice/kuitansi/bukti pembayaran/SPK/Surat Perjanjian dari penyedia")
  st.info ("- Daftar hadir")
  st.info ("- Undangan rapat/kegiatan")
  st.info ("- Billing PPh Pasal 23")
  st.info ("- Bukti Pembayaran Negara")
  
elif asal == "Belanja perawatan kendaraan bermotor":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Surat Permohonan Pemeliharaan Kendaraan yang diajukan oleh Pengguna")
  st.info ("- Surat Jalan dari pengurus barang SKPD/UPTD dan di tanda tangani oleh penyedia")
  st.info ("- Invoice, kuitansi dan faktur")
  st.info ("- Billing PPh")
  st.info ("- Bukti Penerimaan Negara")
  st.info ("- Perjanjian kerjasama Pengguna Anggaran/ Kuasa Pengguna Anggaran / Pejabat Pembuat Komitmen dengan penyedia (dibuat oleh PPTK)")
 
elif asal == "Belanja Jasa Penerangan/Iklan/Reklame/Film/Pemotretan":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Surat Pesanan/Surat Perjanjian/Kontrak (MoU)")
  st.info ("- Surat Tagihan")
  st.info ("- e-Faktur PPN, Billing PPN dan PPh 23, dan bukti penerimaan negara")
  st.info ("- Bukti Terbit (untuk media cetak)")
  st.info ("- Bukti Tayang: Jadwal siaran/penayangan, rekaman film, VCD, DVD dan CD (untuk media elektronik)")
  st.info ("- Bukti Transfer")
  
