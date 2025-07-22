import streamlit as st
from fpdf import FPDF
from io import BytesIO
from datetime import date

st.set_page_config(page_title="Pembuat Surat PDF", layout="centered")
st.title("📄 Pembuat Surat Otomatis (PDF)")

# Input form
st.subheader("🔹 Data Surat")
nama = st.text_input("Nama Pegawai")
jabatan = st.text_input("Jabatan")
kegiatan = st.text_area("Nama Kegiatan")
tanggal = st.date_input("Tanggal Surat", value=date.today())
jenis_surat = st.selectbox("Jenis Surat", ["Surat Tugas", "SPTJM", "Kwitansi", "Berita Acara"])

# Tombol buat surat
if st.button("📝 Buat PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=jenis_surat.upper(), ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Nama    : {nama}", ln=True)
    pdf.cell(200, 10, txt=f"Jabatan : {jabatan}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Kegiatan: {kegiatan}")
    pdf.cell(200, 10, txt=f"Tanggal : {tanggal.strftime('%d %B %Y')}", ln=True)
    pdf.ln(20)
    pdf.cell(200, 10, txt="Ditandatangani secara resmi.", ln=True)

    buffer = BytesIO()
    pdf.output(buffer, 'F')
    buffer.seek(0)

    st.success("✅ Surat PDF berhasil dibuat!")
    st.download_button(
        label="⬇️ Unduh PDF",
        data=buffer,
        file_name=f"{jenis_surat.lower().replace(' ', '_')}.pdf",
        mime="application/pdf"
    )
