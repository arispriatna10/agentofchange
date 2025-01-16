import streamlit as st

st.info("""
# Aplikasi Cek Kelengkapan Dokumen SPJ
Ini adalah aplikasi untuk mengecek Dokumen Kelengkapan SPJ
""")


original_list = ["Pilih Jenis Belanja",
                 "Honorarium Panitia/Pejabat Pengadaan/Penerima Barang dan Jasa PNS Provinsi", 
                 "Honorarium PNS Non Provinsi dan Non PNS (Peserta)",
                 "Upah Harian Lepas",
                 "Uang Hadiah",
                 "Perjalanan Dinas Luar Provinsi",
                 "Perjalanan Dinas Luar Negeri",
                 "Makanan dan Minuman Rapat",
                 "Makanan dan Minuman Tamu",
                 "Honorarium Narasumber",
                 "Tenaga Ahli Non Sertifikat",
                 "Makanan dan Minuman Rapat (Platform GRATIS ONGKIR)",
                 "Makanan dan Minuman Tamu (Platform GRATIS ONGKIR)"]
                 

asal = st.selectbox(''':blue[Masukan Jenis Belanja]''',original_list)


if asal == "Honorarium Panitia/Pejabat Pengadaan/Penerima Barang dan Jasa PNS Provinsi":
  st.info ("Dokumen Kelengkapan:")
  st.info ("1. Daftar Penerimaan Pembayaran Honor Kuitansi")
  st.info ("2. SK Pejabat/Panitia Pengadaan dan Pejabat/Panitia Penerima Barang dan Jasa")
  st.info ("3. Rekapitulasi paket pekerjaan yang berisi Informasi tentang nilai dan jenis pekerjaan khusus untuk Pejabat/Panitia pengadaan Dan Pejabat/ Panitia Penerima Barang/Jasa, Kecuali yang 1 (satu) paket pekerjaan melampirkan Fotokopi SPK dan Berita Acara Serah Terima Barang/Jasa khusus untuk pembayaran Honorarium Panitia/Pejabat Penerima Barang/Jasa")
  st.info ("4. Bukti transfer/SPPT jika pembayarannya melalui transfer")
  st.info ("5. e-Billing dari Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")






