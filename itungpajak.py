import streamlit as st
from docxtpl import DocxTemplate, InlineImage, DocxTemplate
from io import BytesIO
from datetime import date
from docx import Document

# Fungsi bantu buat template docx dari string
def create_template(content: str):
    doc = Document()
    for line in content.split("\n"):
        doc.add_paragraph(line)
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

st.set_page_config(page_title="Template Surat Otomatis", layout="centered")
st.title("📄 Generator Template Surat")

# Definisi isi dasar dokumen dengan placeholder
templates = {
    "Surat Tugas": """SURAT TUGAS

Yang bertanda tangan di bawah ini:

Nama    : {{ nama }}
Jabatan : {{ jabatan }}

Menugaskan untuk kegiatan:
{{ kegiatan }}

Tanggal: {{ tanggal }}

(ditandatangani)""",
    "SPTJM": """SURAT PERNYATAAN TANGGUNG JAWAB MUTLAK (SPTJM)

Saya yang bertanda tangan di bawah ini:

Nama    : {{ nama }}
Jabatan : {{ jabatan }}

Menyatakan bahwa kegiatan:
{{ kegiatan }}

Tanggal: {{ tanggal }}

Segala sesuatu sesuai dengan ketentuan yang berlaku.""",
    "Kwitansi": """KWITANSI

Telah diterima dari: {{ nama }}
Jabatan: {{ jabatan }}

Sejumlah uang untuk keperluan:
{{ kegiatan }}

Tanggal: {{ tanggal }}

Terbilang: ______________________

Tanda tangan penerima: __________""",
    "Berita Acara": """BERITA ACARA

Pada hari ini, {{ tanggal }}, bertempat di tempat kegiatan.

Nama    : {{ nama }}
Jabatan : {{ jabatan }}

Telah melakukan kegiatan:
{{ kegiatan }}

Demikian berita acara ini dibuat dengan sebenar‑benarnya."""
}

st.write("Pilih template yang ingin dibuat:")

for surat_name, content in templates.items():
    if st.button(f"📥 Unduh template {surat_name}"):
        buffer = create_template(content)
        st.download_button(
            label=f"⬇️ {surat_name}.docx",
            data=buffer,
            file_name=f"{surat_name.lower().replace(' ', '_')}_template.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
