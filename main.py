import streamlit as st

st.set_page_config(
    page_title="Aplikasi Cek Kelengkapan SPJ", 
    page_icon="📑",
)



st.info("""
# Aplikasi Cek Kelengkapan Dokumen SPJ
Ini adalah aplikasi untuk mengecek Dokumen Kelengkapan SPJ yang mengacu pada Handbook Penatausahaan Keuangan yang dapat diakses pada link berikut "https://drive.google.com/file/d/1Mztwn26NKliPXlurodgqX044EuJLPugd/view?usp=sharing"
""")

original_list = ["Pilih Jenis Belanja",
                 "Honorarium Panitia/Pejabat Pengadaan/Penerima Barang dan Jasa PNS Provinsi", 
                 "Honorarium PNS Non Provinsi dan Non PNS (Peserta)",
                 "Upah Harian Lepas",
                 "Uang Hadiah",
                "Belanja Bahan Pakai Habis",
                "Belanja Bahan/Material",
                "Belanja langganan Telepon/Listrik/Air/Internet/TV Kabel",
                "Belanja Lengganan Surat Kabar/ Majalah/ Buletin",
                "Belanja Jasa Paket Pengiriman/ Kebersihan/ Keamanan/ Pengelolaan Aset",
                "Belanja Pajak Bumi dan Bangunan (PBB)",
                "Belanja Surat Tanda Nomor Kendaraan",
                "Belanja Jasa KIR",
                "Belanja Jasa Uji Laboratorium/ Uji Sampling",
                "Belanja Jasa Profesi (tenaga pengajar, penceramah/ narasumber / notulen/ Instruktur/ Wakil Instruktur/ Pembina Instruktur/ Moderator/ Pengamat Kelas)",
                "Belanja Jasa Pengumuman Lelang melalui Media Surat Kabar",
                "Belanja Jasa Akomodasi",
                "Belanja Premi Asuransi",
                "Belanja Jasa Penerangan/ Iklan/ Reklame/ Film/ Pemotretan (Media Cetak)",
                "Belanja Jasa Penerangan/ Iklan/ Reklame/ Film/ Pemotretan (Media Elektronik)",
                "Belanja Perawatan Kendaraan Bermotor (belanja servis, penggantian suku cadang, pelumas)",
                "Belanja Perawatan Perlengkapan Kantor",
                "Belanja Pemeliharaan Taman",
                "Belanja Cetak dan Penggandaan",
                "Belanja Sewa Rumah/ Gedung/ Gudang/ Parkir/ Tempat",
                "Belanja Paket Meeting",
                "Belanja Sewa Sarana Mobilitas",
                "Belanja Sewa Alat Berat",
                "Belanja Sewa Perlengkapan dan Peralatan Kantor",
                "Belanja Sewa Perlengkapan dan Peralatan Kantor",
                "Perjalanan Dinas Dalam Kota/ Kabupaten",
                "Belanja Perjalanan Dinas Paket Meeting",
                "Perjalanan Dinas Dalam Daerah (Kabupaten/ Kota)",
                "Belanja Perjalanan Dinas Luar Provinsi",
                "Belanja Perjalanan Dinas Luar Negeri",
                "Belanja Perjalanan Dinas Bagi Non PNS Dinas Dalam dan Luar Daerah",
                "Belanja PNS yang mengikuti Diklat Jabatan Struktural/ Fungsional yang dilaksanakan oleh Instansi Daerah lain, Instansi Provinsi, Instansi Pusat maupun Organisasi Diklat lainnya",
                "PNS yang mengikuti Diklat/ Bimtek apabila lebih dari 3 (tiga) hari yang harus ada biaya kontribusi",
                "Biaya sewa stand pameran tingkat provinsi dan tingkat nasional",
                "Belanja Paket Meeting",
                "Perjalanan Dinas Paket Meeting",
                "Belanja Makan minum rapat",
                "Belanja Makan minum tamu",
                "Belanja Konstruksi",
                "Belanja Tenaga Ahli Non Sertifikat",
                "Belanja Modal Pengadaan Tanah",
                "Belanja Modal Pengadaan Perlengkapan Kantor/Peralatan dan Mesin/Alat-alat Bengkel/Peralatan Dapur/Penghias Ruangan/Alat-alat Studio/Buku/ Perpustakaan/Belanja Model sejenis lainnya"
                ]
                 

asal = st.selectbox(''':blue[Masukan Jenis Belanja]''',original_list)


if asal == "Honorarium Panitia/Pejabat Pengadaan/Penerima Barang dan Jasa PNS Provinsi":
  st.info ("Dokumen yang perlu dilengkapi untuk Honorarium Panitia/Pejabat Pengadaan/Penerima Barang dan Jasa PNS Provinsi: ")  
  st.info ("- Daftar Penerimaan Pembayaran Honor Kuitansi")
  st.info ("- SK Pejabat/Panitia Pengadaan dan Pejabat/Panitia Penerima Barang dan Jasa")
  st.info ("- Rekapitulasi paket pekerjaan yang berisi Informasi tentang nilai dan jenis pekerjaan khusus untuk Pejabat/Panitia pengadaan Dan Pejabat/Panitia Penerima Barang/Jasa, Kecuali yang 1 (satu) paket pekerjaan melampirkan Fotokopi SPK dan Berita Acara Serah Terima Barang/Jasa khusus untuk pembayaran Honorarium Panitia/Pejabat Penerima Barang/Jasa")
  st.info ("- Bukti transfer/SPPT jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Honorarium PNS Non Provinsi dan Non PNS (Peserta)":
  st.info ("Dokumen yang perlu dilengkapi untuk Honorarium PNS Non Provinsi dan Non PNS (Peserta):")   
  st.info ("- Daftar penerimaan pembayaran uangsaku dan atau transport")
  st.info ("- Daftar Hadir")
  st.info ("- Bukti transfer/SPPT jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang (untuk uang saku)")

elif asal == "Upah Harian Lepas":
  st.info ("Dokumen yang perlu dilengkapi untuk Upah Harian Lepas:")  
  st.info ("- Daftar Pembayaran Upah")
  st.info ("- Daftar Hadir")
  st.info ("- Bukti transfer/SPPT jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Uang Hadiah":
  st.info ("Dokumen yang perlu dilengkapi untuk Uang Hadiah:") 
  st.info ("- Keputusan Gubernur/Keputusan Kepala SKPD tentang Standar besaran Uang/Hadiah dan penetapan pemenang dan atau Keputusan Dewan Hakim/Juri Penilai perlombaan kegiatan")
  st.info ("- Daftar pembayaran dan atau tanda terima uang hadiah/penghargaan")
  st.info ("- Bukti Transfer ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Buktti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Bahan Pakai Habis":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Bahan Pakai Habis:")
  st.info ("- Bukti Pembelian/ Pembayaran")
  st.info ("- Faktur Barang")
  st.info ("- Surat Pesanan/ Surat Perjanjian Kerjasma/Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU)")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Bukti Transfer/ SPPT ke pihak penvedia barang/jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimann Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Bahan/Material":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Bahan/Material:") 
  st.info ("- Bukti Pembelian/ Pembayaran")
  st.info ("- Faktur Barang")
  st.info ("- Surat Pesanan/ Surat Pejanjian Kejasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/Kontrak (MoU]")
  st.info ("- Surat tagihan jika belanja melalui surat pesanan/ kontrak (MoU)")
  st.info ("- Bukti Transfer ke pihak penyedia barang/jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimann Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja langganan Telepon/Listrik/Air/Internet/TV Kabel":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja langganan Telepon/Listrik/Air/Internet/TV Kabel:")
  st.info ("- Bukti Pembelian/ Pembayaran")
  st.info ("- Surat tagihan dari penyedia jasa")
  st.info ("- Bukti Transfer/SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Lengganan Surat Kabar/ Majalah/ Buletin":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Lengganan Surat Kabar/ Majalah/ Buletin:") 
  st.info ("- Bukti Pembelian/ Pembayaran")
  st.info ("- Surat tagihan dari penyedia jasa")
  st.info ("- Bukti Transfer/SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")
  
elif asal == "Belanja Jasa Paket Pengiriman/ Kebersihan/ Keamanan/ Pengelolaan Aset":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Jasa Paket Pengiriman/ Kebersihan/ Keamanan/ Pengelolaan Aset:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Surat Pejanjian Kerjasama/ Kontrak (MoU) jika melalui Kerjasama/ Kontrak (MoU)")
  st.info ("- Surat Tagihan jika pembayaran melalui Kerjasama/ Kontrak (MoU)")
  st.info ("- Surat tagihan dari penyedia jasa")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimann Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Pajak Bumi dan Bangunan (PBB)":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Pajak Buml dan Bangunan (PBB):")
  st.info ("- Surat Pemberitahuan Pajak Terutang PBB (SPPT PBB)")
  st.info ("- Bukti Pembayaran Pajak Bumi dan Bangunan")
  st.info ("- Bukti Transfer/ SPPT jika pembayarannya melalui transfer")
  st.info ("- Bukti Penerimaan Pajak Bumi dan Bangunan")

elif asal == "Belanja Surat Tanda Nomor Kendaraan":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Surat Tanda Nomor Kendaraan:")
  st.info ("- Fotokopi Surat Ketetapan Pajak Daerah")
  st.info ("- Fotokopi Bukti Pembayaran Pajak")
  st.info ("- Bukti Transfer/ SPPT jika pembayarannya melalui transfer")
 
elif asal == "Belanja Jasa KIR":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Jasa KIR:")
  st.info ("- Dokumen bukti uji KIR")
  st.info ("- Bukti Pembayaran KIR")
  st.info ("- Bukti Transfer/ SPPT jika pembayarannya melalui transfer")

elif asal == "Belanja Jasa Uji Laboratorium/ Uji Sampling":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Jasa Uji Laboratorium/ Uji Sampling:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Jasa Profesi (tenaga pengajar, penceramah/ narasumber / notulen/ Instruktur/ Wakil Instruktur/ Pembina Instruktur/ Moderator/ Pengamat Kelas)":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Jasa Profesi (tenaga pengajar, penceramah/ narasumber / notulen/ Instruktur/ Wakll Instruktur/ Pembina Instruktur/ Moderator/ Pengamat Kelas):")
  st.info ("- Curriculum vitae (CV)/Biodata")
  st.info ("- Surat Pcrmohonan Permintaan Narasumber")
  st.info ("- Daftar Hadir")
  st.info ("- Jadwal acara")
  st.info ("- Kuitansi / Daftar penerimaan pembayaran")
  st.info ("- Bukti Transfer/SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimann Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Jasa Pengumuman Lelang melalui Media Surat Kabar":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Jasa Pengumuman Lelang melalui Media Surat Kabar:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Surat Pesanan")
  st.info ("- Surat Tagihan")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia jasa jika pembayarannva melalui transfer")
  st.info ("- Surat Kabar Hasil Pengumuman Lelang {dilampirkan)")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimann Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Jasa Akomodasi":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Jasa Akomodasi:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Daftar hadir")
  st.info ("- Surat undangan dari penyelenggara")
  st.info ("- Surat pesanan")
  st.info ("- Surat tagihan")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia jasa jika pembayarannya melalui transfer")

elif asal == "Belanja Premi Asuransi":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Premi Asuransi:")
  st.info ("- Bukti pembayaran")
  st.info ("- Fotocopy polis asuransi")
  st.info ("- Bukti Transfer/ SPPT ke pihak penvedia barang/ jasa jika pembayarannya melalui transfer")

elif asal == "Belanja Jasa Penerangan/ Iklan/ Reklame/ Film/ Pemotretan (Media Cetak)":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Jasa Penerangan/ Iklan/ Reklame/ Film/ Pemotretan (Media Cetak):")
  st.info ("- Bukti Pembayaran")
  st.info ("- Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU]")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")
  st.info ("- Bukti Terbit")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")

elif asal == "Belanja Jasa Penerangan/ Iklan/ Reklame/ Film/ Pemotretan (Media Elektronik)":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Jasa Penerangan/ Iklan/ Reklame/ Film/ Pemotretan (Media Elektronik):")
  st.info ("- Bukti Pembayaran")
  st.info ("- Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU]")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")
  st.info ("- Bukti Tayang : Jadwal Siaran/ Penayangan Rekaman Film, VCD, DVD, CD")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")

elif asal == "Belanja Perawatan Kendaraan Bermotor (belanja servis, penggantian suku cadang, pelumas)":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Perawatan Kendaraan Bermotor (belanja servis, penggantian suku cadang, pelumas):")
  st.info ("- Nota Dinas Usulan dari pengguna kendaraan operasional")
  st.info ("- Bukti Pembelian/ Pembayaran")
  st.info ("- Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU]")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Perawatan Perlengkapan Kantor":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Perawatan Perlengkapan Kantor:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Faktur (invoice)")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing. e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Pemeliharaan Taman":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Pemeliharaan Taman:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Faktur (invoice]")
  st.info ("- Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU)")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Cetak dan Penggandaan":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Cetak dan Penggandaan:")
  st.info ("- Bukti Pembelian/ Pembayaran")
  st.info ("- Faktur Barang")
  st.info ("- Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU)")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Sewa Rumah/ Gedung/ Gudang/ Parkir/ Tempat":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Sewa Rumah/ Gedung/ Gudang/ Parkir/ Tempat:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Surat Perjanjian/ Kontrak (MoU) Sewa jika sewa menyewa dilakukan melalui perjanjian/ kontrak")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Bukti Transfer/ SPPT jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Paket Meeting":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Paket Meeting:")
  st.info ("- Surat Pesanan (SP)")
  st.info ("- Berita Acara Pemeriksaan dan Serah Terima Pekerjaan")
  st.info ("- Berita Acara Persetujuan Pembayaran")
  st.info ("- Invoice/Kuitansi")
  st.info ("- Daftar Kamar")
  st.info ("- Daftar menu makanan")
  st.info ("- Dokumentasi")

elif asal == "Belanja Sewa Sarana Mobilitas":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Sewa Sarana Mobilitas:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Fotokopi STNK")
  st.info ("- Surat Pesanan/ Surat Pejanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU)")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Bukti Transfer/ SPPT jika pembayarannva melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Sewa Alat Berat":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Sewa Alat Berat:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Surat Pesanan/Surat Perjanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU}")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Bukti Transfer/ SPPT jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Sewa Perlengkapan dan Peralatan Kantor":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Sewa Perlengkapan dan Peralatan Kantor:")
  st.info ("- Bukti Pembayaran")
  st.info ("- Faktur (Invoice)")
  st.info ("- Surat Pesanan/ Surat Pejanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU)")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Sewa Perlengkapan dan Peralatan Kantor":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Sewa Perlengkapan dan Peralatan Kantor:")
  st.info ("- Bukti Pembayaran/Pembayaran dan Faktur")
  st.info ("- Undangan Rapat/ Nota Dinas Permohonan/ Surat perintahLembur")
  st.info ("- Surat Pesanan/ Surat Pejanjian Kerjasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontrak (MoU)")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU)")
  st.info ("- Daftar Hadir")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-Faktur PPN dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Perjalanan Dinas Dalam Kota/ Kabupaten":
  st.info ("Dokumen yang perlu dilengkapi untuk Perjalanan Dinas Dalam Kota/ Kabupaten:")
  st.info ("- Surat Undangan/ Surat Perintah dengan jadwal yang terlampir (minimal 8 jam)")
  st.info ("- Rincian Biaya Perjalanan Dinas (SPD Rampung)")
  st.info ("- Daftar Penerimaan Uang Harian dan atau Uang Saku")
  st.info ("- Tanda Bukti Akomodasi meliputi Kuitansi/ Nota/ Faktur/ Bill/ yang memuat nama Pelaksana perjalanan dinas dari Hotel yang telah distempel oleh penyedia atau dari situs penyedia jasa akomodasi (jika lebih dari 4 hari)")
  st.info ("- Tanda Bukti Transportasi meliputi: Struk BBM dan Struk Tol")
  st.info ("- Bukti Transfer/ SPPT dan atau kuitansi pembayaran sesuai dengan jumlah pada SPD Rampung")
  st.info ("- Surat Perjalanan Dinas (SPD)/ Visum ditandatangani dan dicap/ stempel oleh pejabat yang berwenang/ pihak terkait (tempat tujuan/ tempat pelaksanaan kegiatan)")
  st.info ("- Laporan perjalanan dinas dibuat, dilaporkan kepada pemberi perintah dan diarsipkan")

elif asal == "Belanja Perjalanan Dinas Paket Meeting":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Perjalanan Dinas Paket Meeting:")
  st.info ("- Surat Undangan")
  st.info ("- Surat Perintah")
  st.info ("- Visum")
  st.info ("- Rampung")
  st.info ("- Daftar Nominatif")
  st.info ("- BBM + Tol")
  st.info ("- Laporan Perjalanan Dinas")
  st.info ("- Dokumentasi")

elif asal == "Perjalanan Dinas Dalam Daerah (Kabupaten/ Kota)":
  st.info ("Dokumen yang perlu dilengkapi untuk Perjalanan Dinas Dalam Daerah (Kabupaten/ Kota):")
  st.info ("- Surat Undangan/ Surat Perintah")
  st.info ("- Rincian Biaya Pejalanan Dinas (SPD Rampung)")
  st.info ("- Daftar Penerimaan Uang Harian dan atau Uang Saku")
  st.info ("- Tanda Bukti Akomodasi meliputi: Kuitansi / Nota/ Faktur/ Bill yang memuat nama Pelaksana perjalanan dinas dari Hotel yang telah distempel oleh penyedia atau dari situs penyedia jasa akomodasi (jika lebih dari 1 hari)")
  st.info ("- Tanda Bukti Transportasi meliputi: 1.Perjalanan Dinas Dalam Daerah (Kabupaten/ Kota) Tiket Bus/ Bukti Pembelian Tiket Kereta Api dan atau Tiket Kereta Api beserta Boarding Pass, 2.Jika menggunakan kendaraan dinas/ operasional, laınpirkan: Struk atau Nota BBM dan Bukti Tol, 3. Jika menggunakan Sewa Kendaraan, lampirkan: 1.Kuitansi/ Nota/ Faktur Sewa Kendaraan, 2.Fotocopy STNK Kendaraan: Sewa kendaraan hanya diperuntukkan bagi Pejabat Negara yang melakukan pejalanan dinas dalam negeri di tempat tujuan dan Pelaksanaan Kegiatan yang membutuhkan mobilitas tînggi, berskala besar, dan tidak tersedia kendaraan dinas serta dilakukan secara selektif dan efisien; Satuan biaya sewa kendaraan sııdah termasuk bahan bakar dan pengemudi)")
  st.info ("- Bukti Transfer/ SPPT dan atau kuitansi pembayaran sesuai dengan jumlah pada SPD Rampung")
  st.info ("- Surat Pejalanan Dinas (SPD)/ Visum ditandatangani dan dicap/ stempel oleh pejabat yang berwenang/ pihak terkait (tempat tujuan/ tempat pelaksanaan Kegiatan)")
  st.info ("- Laporan pejalanan dinas dibuat, dilaporkan kepada pemberi perintah dan diarsipkan")
  st.info ("- Surat Undangan")
  st.info ("- Surat Perintah")
  st.info ("- Visum")
  st.info ("- Rampung")
  st.info ("- Daftar Nominatif")
  st.info ("- Uang Refresentatif")
  st.info ("- BBM + Tol")
  st.info ("- Invoice Hotel")
  st.info ("- Laporan Perjalanan Dinas")
  st.info ("- Dokumentasi")

elif asal == "Belanja Perjalanan Dinas Luar Provinsi":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Perjalanan Dinas Luar Provinsi:")
  st.info ("- Surat Undangan/ Surat Perintah")
  st.info ("- Rincian Biaya Pejalanan Dinas (SPD Rampung)")
  st.info ("- Daftar Penerimaan Uang Harian dan atau Uang Saku dan Uang Taksi")
  st.info ("- Tanda Bukti Akomodasi meliputi: Kuitansi / Nota/ Faktur/ Bill yang memuat nama Pelaksana perjalanan dinas dari Hotel yang telah distempel oleh penyedia atau dari situs penyedia jasa akomodasi (jika lebih dari 1 hari)")
  st.info ("- Tanda Bukti Transportasi Tiket Bus/ Tiket Pesawat beserta Boarding Pass/ Tiket Kereta Api beserta Boarding pass/ Kuitansi Sewa Kendaraan (Sewa kendaraan hanya diperbolehkan jika kegiatan dilaksanakan di luar Ibu Kota Provinsi dan dilengkapi dengan Surat Keterangan yang rnenjelaskan lokasi tujuan pejalanan dinas)")
  st.info ("- Bukti Transfer/ SPPT dan atau kuitansi pembayaran sesuai dengan jumlah pada SPD Rampung")
  st.info ("- Surat Pejalanan Dinas (SPD)/ Visum ditandatangani dan dicap/ stempel oleh pejabat yang berwenang/ pihak terkait (tempat tujuan/ tempat pelaksanaan Kegiatan)")
  st.info ("- Laporan pejalanan dinas dibuat, dilaporkan kepada pemberi perintah dan diarsipkan")
  st.info ("- Surat Undangan")
  st.info ("- Surat Perintah")
  st.info ("- Visum")
  st.info ("- Rampung")
  st.info ("- Daftar Nominatif")
  st.info ("- Uang Refresentatif")
  st.info ("- Bukti transport")
  st.info ("- E-tiket dari maskapai")
  st.info ("- Boardingpass")
  st.info ("- Invoice Hotel")
  st.info ("- Laporan Perjalanan Dinas")
  st.info ("- Dokumentasi")

elif asal == "Belanja Perjalanan Dinas Luar Negeri":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Perjalanan Dinas Luar Negeri:")
  st.info ("- Surat Perintah/Surat Undangan Pejalanan Dinas ke Luar Negeri dapat dilaksanakan setelah mendapat ijin dari Gubernur")
  st.info ("- Passport Biru (Dinas)")
  st.info ("- Rincian Biaya Pejalanan Dinas (SPD Rampung)")
  st.info ("- Daftar Penerimaan Uang Harian")
  st.info ("- Bukti Pembayaran pengurusan Passport/Visa/Exit Permitted yang dibubuhi tandatangan keberangkatan dan kepulangan (Imigrasi)")
  st.info ("- Tanda Bukti Transportasi : Tiket Bus /Tiket Pesawat beserta Boording pass/ Tiket Kereta Api beserta boarding pass/ Kuitansi Sewa Kendaraan")
  st.info ("- Tanda Bukti akomodasi meliputi Kuitansi/ Nota/ Faktur/Bill yang memuat nama Pelaksana perjalanan dinas dari Hotel yang telah distempel oleh penyedia atau dari situs penyedia jasa akomodasi (jika lebih dari 1 hari)")
  st.info ("- Bukti Transfer/ SPPT dan atau kuitansi pembayaran sesuai dengan jumlah pada SPD Rampung")
  st.info ("- Surat Pejalanan Dinas (SPD)/ Visum ditandatangani dan dicap/ stempel oleh pejabat yang berwenang/ pihak terkait (tempat tujuan/ tempat pelaksanaan Kegiatan)")
  st.info ("- Laporan pejalanan dinas dibuat, dilaporkan kepada pemberi perintah dan diarsipkan")
  st.info ("- Kerangka Acuan Kerja (KAK)")
  st.info ("- Persuratan")
  st.info ("- SK Tim")
  st.info ("- Usulan peserta ke Kemendagri")
  st.info ("- Rekomendasi dari Kemendagri ke Setneg")
  st.info ("- Surat Ijin dari Setneg")
  st.info ("- Surat Perintah")
  st.info ("- Visum")
  st.info ("- Rampung")
  st.info ("- Daftar Nominatif")
  st.info ("- Uang Refresentatif")
  st.info ("- Bukti transport")
  st.info ("- Paspor Biru (foto copy yang ada cap kedatangan/ kepulangan)")
  st.info ("- Visa (foto copy yang ada cap kedatangan/kepulangan)")
  st.info ("- E_tiket dari maskapai")
  st.info ("- Boardingpass")
  st.info ("- Invoice Hotel")
  st.info ("- Laporan Perjalanan Dinas")
  st.info ("- Bukti penyampaian laporan ke Kemendagri")
  st.info ("- Dokumentasi")

elif asal == "Belanja Perjalanan Dinas Bagi Non PNS Dinas Dalam dan Luar Daerah":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Perjalanan Dinas Bagi Non PNS Dinas Dalam dan Luar Daerah:")
  st.info ("- Surat undangan/ Surat Perintah")
  st.info ("- Rincian Biaya Pejalanan Dinas (SPD Rampung)")
  st.info ("- Daftar Penerimaan Uang Harian dan atau Uang Saku dan Uang Taksi")
  st.info ("- Tanda Bukti Akomodasi meliputi: Kuitansi/ Nota/ Faktur/ Bill yang memuat nama Pelaksana perjalanan dinas dari Hotel yang telah distempel oleh penyedia atau dari situs penyedia jasa akomodasi (jika lebih dari 1 hari)")
  st.info ("- Tanda Bukti Transportasi Tiket Bus/ Tiket Pesawat beserta Boarding Pass/ Tiket Kereta Api beserta Boarding pass/ Kuitansi Sewa Kendaraan (Sewa kendaraan hanya diperbolehkan jika kegiatan dilaksanakan di luar Ibu Kota Provinsi dan dilengkapi dengan Surat Keterangan yang rnenjelaskan lokasi tujuan pejalanan dinas)")
  st.info ("- Bukti Transfer/ SPPT dan atau kuitansi pembayaran sesuai dengan jumlah pada SPD Rampung")
  st.info ("- Surat Perjalanan Dinas (SPD)/ Visum ditandatangani dan dicap/ stempel oleh pejabat yang berwenang/ pihak terkait (tempat tujuan/ tempat pelaksanaan kegiatan)")
  st.info ("- Laporan pejalanan dinas dibuat, dilaporkan kepada pemberi perintah dan diarsipkan")

elif asal == "Belanja PNS yang mengikuti Diklat Jabatan Struktural/ Fungsional yang dilaksanakan oleh Instansi Daerah lain, Instansi Provinsi, Instansi Pusat maupun Organisasi Diklat lainnya":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja PNS yang mengikuti Diklat Jabatan Struktural/ Fungsional yang dilaksanakan oleh Instansi Daerah lain, Instansi Provinsi, Instansi Pusat maupun Organisasi Diklat lainnya:")
  st.info ("- Radiogram/ Surat Pemberitahuan untuk mengikuti Diklat")
  st.info ("- Surat Perintah")
  st.info ("- Surat Perjalanan Dinas (SPD)/ Visum ditandatangani oleh pejabat yang berwenang")
  st.info ("- Rincian Biaya Perjalanan Dinas dilengkapi dengan Daftar Penerimaan Uang harian dan Uang Taksi, Akomodasi, dan sewa kendaraan/ Tiket")
  st.info ("- Jadwal Diklat")
  st.info ("- Bukti Transfer/ SPPT dan atau kuitansi pembayaran sesuai dengan jumlah pada SPD Rampung")
  st.info ("- Fotocopy Sertifikat telah mengikuti Diklat")

elif asal == "PNS yang mengikuti Diklat/ Bimtek apabila lebih dari 3 (tiga) hari yang harus ada biaya kontribusi":
  st.info ("Dokumen yang perlu dilengkapi untuk PNS yang mengikuti Diklat/ Bimtek apabila lebih dari 3 (tiga) hari yang harus ada biaya kontribusi:")
  st.info ("- Surat Undangan/ Radiogram dari Bagian Kepegawaian atau penyelenggara")
  st.info ("- Surat Perintah")
  st.info ("- Kuitansi uang harian dan uang saku")
  st.info ("- Fotokopi sertifikat")

elif asal == "Biaya sewa stand pameran tingkat provinsi dan tingkat nasional":
  st.info ("Dokumen yang perlu dilengkapi untuk Biaya sewa stand pameran tingkat provinsi dan tingkat nasional:")
  st.info ("- Surat Undangan dari penyelenggara")
  st.info ("- Surat Perintah")
  st.info ("- Bukti Pembayaran")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- Bukti Dokumentasi")

elif asal == "Belanja Paket Meeting":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Paket Meeting:")
  st.info ("- Surat Pesanan (SP)")
  st.info ("- Berita Acara Pemeriksaan dan Serah Terima Pekerjaan")
  st.info ("- Permohonan Pembayaran")
  st.info ("- Berita Acara Persetujuan Pembayaran")
  st.info ("- Invoice/Kuitansi")
  st.info ("- Daftar Kamar")
  st.info ("- Daftar menu makanan")
  st.info ("- Dokumentasi")

elif asal == "Perjalanan Dinas Paket Meeting":
  st.info ("Dokumen yang perlu dilengkapi untuk Perjalanan Dinas Paket Meeting:")
  st.info ("- Surat Undangan")
  st.info ("- Surat Perintah")
  st.info ("- Visum")
  st.info ("- Rampung")
  st.info ("- Daftar Nominatif")
  st.info ("- BBM + Tol")
  st.info ("- Laporan Perjalanan Dinas")
  st.info ("- Dokumentasi")

elif asal == "Belanja Makan minum rapat":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Makan minum rapat:")
  st.info ("- Surat Undangan")
  st.info ("- Bukti Pembelian")
  st.info ("- Daftar Hadir")
  st.info ("- Notulensi Rapat")
  st.info ("- ID Billing PPh 22/PPh 23")
  st.info ("- e-bupot")
  st.info ("- Dokumentasi")

elif asal == "Belanja Makan minum tamu":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Makan minum tamu:")
  st.info ("- Surat Undangan")
  st.info ("- Proses Pengadaan Barang dan Jasa")
  st.info ("- Bukti Pembelian")
  st.info ("- ID Billing PPh 22/PPh 23")
  st.info ("- e-bupot")
  st.info ("- Dokumentasi")

elif asal == "Belanja Konstruksi":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Konstruksi:")
  st.info ("- Surat Perintah Kerja/Surat Perjanjian")
  st.info ("- Surat Perintah Mulai Kerja (SPMK)")
  st.info ("- Berita Acara Serah Terima Pekerjaan")
  st.info ("- Permohonan Pembayaran")
  st.info ("- Berita Acara Persetujuan Pembayaran")
  st.info ("- Kuitansi")
  st.info ("- Faktur Pajak")
  st.info ("- ID Billing PPN dan PPh Ps.4 ayat 2")
  st.info ("- Dokumentasi")

elif asal == "Belanja Tenaga Ahli Non Sertifikat":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Tenaga Ahli Non Sertifikat:")
  st.info ("- Kerangka Acuan Kerja (KAK)")
  st.info ("- Curriculum Vitae/Portopolio")
  st.info ("- Surat Perjanjian Kerja")
  st.info ("- Laporan Pekerjaan")
  st.info ("- Daftar Hadir")
  st.info ("- Daftar Nominatif (Tanda Terima)")
  st.info ("- ID Billing PPh 21")
  st.info ("- e_bupot")

elif asal == "Belanja Modal Pengadaan Tanah":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Modal Pengadaan Tanah:")
  st.info ("- Keputusan Gubernur tentang Penetapan Lokasi Pengadaan Tanah")
  st.info ("- Keputusan Kepala BPN tentang Susunan Keanggotaan Pelaksana Pengadaan Tanah")
  st.info ("- Laporan Appraisal")
  st.info ("- Berita cara Kesepakatan Harga")
  st.info ("- Validasi pemberian Ganti Kerugian dari BPN")
  st.info ("- Daftar penerimaan pembayaran dan atau bukti penerimaan konsinyasi dalam hal penyelesaian pengadaan lahan melalui pengadilan")
  st.info ("- Bukti Transfer/ SPPT ke pihak pemilik")
  st.info ("- e-Billing, e-Faktur PPN dan bukti penerimaan pajak negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Belanja Modal Pengadaan Perlengkapan Kantor/Peralatan dan Mesin/Alat-alat Bengkel/Peralatan Dapur/Penghias Ruangan/Alat-alat Studio/Buku/ Perpustakaan/Belanja Model sejenis lainnya":
  st.info ("Dokumen yang perlu dilengkapi untuk Belanja Modal Pengadaan Perlengkapan Kantor/Peralatan dan Mesin/Alat-alat Bengkel/Peralatan Dapur/Penghias Ruangan/Alat-alat Studio/Buku/ Perpustakaan/Belanja Model sejenis lainnya):")
  st.info ("- Bukti Pembelian/Pembayaran")
  st.info ("- Faktur Barang")
  st.info ("- Surat Pesanan/ Surat Perjanjian Ker]jasama/ Kontrak (MoU) jika belanja melalui Pesanan/ Kerjasama/ Kontra (MoU)")
  st.info ("- Surat Tagihan jika belanja melalui Surat Pesanan/ Surat Perjanjian Kerjasama/ Kontrak (MoU}")
  st.info ("- Bukti Transfer/ SPPT ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing, e-faktur PPN dan bukti penerimaan pajak negara sesuai ketentuan peraturan perundang-undang") 
  st.info ("- Bukti Transfer")
  
