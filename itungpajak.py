import streamlit as st
from fpdf import FPDF
from io import BytesIO
from datetime import date

st.set_page_config(page_title="Pembuat Surat PDF", layout="centered")
st.title("📄 Pembuat Surat Otomatis (PDF versi tanpa logo dan ttd)")

# Form input
st.subheader("📝 Data Surat")
nama = st.text_input("Nama Pegawai")
jabatan = st.text_input("Jabatan")
kegiatan = st.text_area("Nama Kegiatan")
tanggal = st.date_input("Tanggal Surat", value=date.today())
jenis_surat = st.selectbox("Jenis Surat", ["Surat Tugas", "SPTJM", "Kwitansi", "Berita Acara"])
instansi = st.text_input("Nama Instansi (Sebagai Logo Header)", value="PEMERINTAH KABUPATEN XYZ")

# Tombol buat
if st.button("✅ Buat PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # "Logo" dari teks
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=instansi, ln=True, align='L')

    # Judul surat
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt=jenis_surat.upper(), ln=True, align='C')
    pdf.ln(10)

    # Isi surat
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Nama    : {nama}", ln=True)
    pdf.cell(200, 10, txt=f"Jabatan : {jabatan}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Kegiatan: {kegiatan}")
    pdf.cell(200, 10, txt=f"Tanggal : {tanggal.strftime('%d %B %Y')}", ln=True)
    pdf.ln(30)

    # Tanda tangan
    pdf.cell(200, 10, txt="Hormat kami,", ln=True)
    pdf.ln(20)
    pdf.cell(200, 10, txt="(Tanda Tangan Digital)", ln=True)
    pdf.cell(200, 10, txt=nama, ln=True)

    # Output
    pdf_data = pdf.output(dest='S').encode('latin-1')
    buffer = BytesIO(pdf_data)

    st.success("✅ Surat PDF berhasil dibuat!")
    st.download_button(
        label="⬇️ Unduh PDF",
        data=buffer,
        file_name=f"{jenis_surat.lower().replace(' ', '_')}.pdf",
        mime="application/pdf"
    )
