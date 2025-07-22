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
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "CHECKLIST SPJ", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Nama Kegiatan : {nama_kegiatan}", ln=True)
    pdf.cell(200, 10, f"Tanggal       : {tanggal.strftime('%d-%m-%Y')}", ln=True)
    pdf.cell(200, 10, f"Pemeriksa     : {pemeriksa}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Hasil Checklist:", ln=True)
    pdf.set_font("Arial", size=11)
    for item in items:
        tanda = "[x]" if checked[item] else "[ ]"
        pdf.cell(200, 8, f"{tanda} {item}", ln=True)


    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, f"STATUS KELENGKAPAN: {status}", ln=True)

    # Simpan ke BytesIO
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    st.success(f"Checklist berhasil dibuat. Status: {status}")
    st.download_button(
        label="⬇️ Unduh Checklist PDF",
        data=pdf_output,
        file_name="checklist_spj.pdf",
        mime="application/pdf"
    )
