import streamlit as st
from fpdf import FPDF
from io import BytesIO

st.set_page_config(page_title="Checklist SPJ Otomatis", layout="centered")
st.title("✅ Checklist SPJ Otomatis")

st.markdown("""
Masukkan kelengkapan dokumen SPJ berikut ini dengan mencentang jika sudah tersedia:
""")

# Daftar dokumen SPJ
items = [
    "Surat Permintaan Pembayaran (SPP)",
    "Surat Perintah Membayar (SPM)",
    "Bukti Transfer atau Bukti Pembayaran",
    "Tanda Tangan Lengkap",
    "Faktur Pajak PPN (jika ada)",
    "Bukti Potong PPh (jika ada)",
    "SPTJM / Pernyataan Tanggung Jawab",
    "Kuitansi",
    "Berita Acara (jika diperlukan)",
    "Dokumentasi Kegiatan (Foto/Undangan/Daftar Hadir)"
]

# Input nama kegiatan dan tanggal
nama_kegiatan = st.text_input("Nama Kegiatan")
tanggal = st.date_input("Tanggal Pemeriksaan")
pemeriksa = st.text_input("Nama Pemeriksa")

# Checklist input
checked = {}
col1, col2 = st.columns(2)
for i, item in enumerate(items):
    with (col1 if i % 2 == 0 else col2):
        checked[item] = st.checkbox(item)

# Tombol simpan & export
if st.button("📄 Simpan dan Unduh PDF"):
    lengkap = all(checked.values())
    status = "LENGKAP" if lengkap else "TIDAK LENGKAP"

    pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Judul utama
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "CHECKLIST DOKUMEN SPJ", ln=True, align="C")
pdf.set_font("Arial", "", 12)
pdf.cell(0, 8, f"Tanggal Pemeriksaan: {tanggal.strftime('%d-%m-%Y')}", ln=True)
pdf.cell(0, 8, f"Pemeriksa: {pemeriksa}", ln=True)
pdf.cell(0, 8, f"Nama Kegiatan: {nama_kegiatan}", ln=True)
pdf.ln(5)

# Garis batas
pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.5)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(5)

# Header tabel
pdf.set_font("Arial", "B", 12)
pdf.cell(10, 8, "No", 1, 0, "C")
pdf.cell(140, 8, "Nama Dokumen", 1, 0, "C")
pdf.cell(40, 8, "Status", 1, 1, "C")

# Isi checklist
pdf.set_font("Arial", "", 11)
for i, item in enumerate(items, start=1):
    tanda = "Sudah" if checked[item] else "Belum"
    pdf.cell(10, 8, str(i), 1, 0, "C")
    pdf.cell(140, 8, item, 1, 0)
    pdf.cell(40, 8, tanda, 1, 1, "C")

pdf.ln(5)

# Status akhir
status = "LENGKAP" if all(checked.values()) else "TIDAK LENGKAP"
pdf.set_font("Arial", "B", 12)
pdf.set_fill_color(230, 230, 0)  # warna kuning muda
pdf.cell(0, 10, f"STATUS KELENGKAPAN: {status}", ln=True, fill=True, align="C")


# Simpan ke BytesIO
from io import BytesIO  
    
pdf_buffer = BytesIO()
pdf_output = pdf.output(dest='S').encode('latin1')  # hasilkan string PDF, lalu encode
pdf_buffer.write(pdf_output)
pdf_buffer.seek(0)


st.success(f"Checklist berhasil dibuat. Status: {status}")
st.download_button(
    label="⬇️ Unduh Checklist PDF",
    data=pdf_output,
    file_name="checklist_spj.pdf",
    mime="application/pdf"
    )
