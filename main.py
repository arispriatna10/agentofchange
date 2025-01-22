import streamlit as st

st.info("""
# Aplikasi Cek Kelengkapan Dokumen SPJ
Ini adalah aplikasi untuk mengecek Dokumen Kelengkapan SPJ
""")


original_list = ["Pilih Jenis Belanja",
                 "Honorarium Panitia/Pejabat Pengadaan/Penerima Barang dan Jasa PNS Provinsi", 
                 "Honorarium PNS Non Provinsi dan Non PNS (Peserta)",
                 "Upah Harian Lepas",
                 "Uang Hadiah"]
                 

asal = st.selectbox(''':blue[Masukan Jenis Belanja]''',original_list)


if asal == "Honorarium Panitia/Pejabat Pengadaan/Penerima Barang dan Jasa PNS Provinsi":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Daftar Penerimaan Pembayaran Honor Kuitansi")
  st.info ("- SK Pejabat/Panitia Pengadaan dan Pejabat/Panitia Penerima Barang dan Jasa")
  st.info ("- Rekapitulasi paket pekerjaan yang berisi Informasi tentang nilai dan jenis pekerjaan khusus untuk Pejabat/Panitia pengadaan Dan Pejabat/Panitia Penerima Barang/Jasa, Kecuali yang 1 (satu) paket pekerjaan melampirkan Fotokopi SPK dan Berita Acara Serah Terima Barang/Jasa khusus untuk pembayaran Honorarium Panitia/Pejabat Penerima Barang/Jasa")
  st.info ("- Bukti transfer/SPPT jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Honorarium PNS Non Provinsi dan Non PNS (Peserta)":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Daftar penerimaan pembayaran uangsaku dan atau transport")
  st.info ("- Daftar Hadir")
  st.info ("- Bukti transfer/SPPT jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang (untuk uang saku)")

elif asal == "Upah Harian Lepas":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Daftar Pembayaran Upah")
  st.info ("- Daftar Hadir")
  st.info ("- Bukti transfer/SPPT jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Bukti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Uang Hadiah":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Keputusan Gubernur/Keputusan Kepala SKPD tentang Standar besaran Uang/Hadiah dan penetapan pemenang dan atau Keputusan Dewan Hakim/Juri Penilai perlombaan kegiatan")
  st.info ("- Daftar pembayaran dan atau tanda terima uang hadiah/penghargaan")
  st.info ("- Bukti Transfer ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Buktti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")

elif asal == "Uang Hadiah":
  st.info ("Dokumen Kelengkapan:")
  st.info ("- Bukti Pembelian/ Pembayaran")
  st.info ("- Daftar pembayaran dan atau tanda terima uang hadiah/penghargaan")
  st.info ("- Bukti Transfer ke pihak penyedia barang/ jasa jika pembayarannya melalui transfer")
  st.info ("- e-Billing dan Buktti Penerimaan Pajak Negara sesuai ketentuan peraturan perundang-undang")











