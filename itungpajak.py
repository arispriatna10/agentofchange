import streamlit as st
from docxtpl import DocxTemplate
from io import BytesIO
from datetime import date

st.set_page_config(page_title="Pembuat Surat Otomatis", layout="centered")
st.title("📄 Pembuat Surat Otomatis")

# Input data dasar
st.subheader("🔹 Data Dasar Surat")
nama = st.text_input("Nama Pegawai")
jabatan = st.text_input("Jabatan")
kegiatan = st.text_area("Nama Kegiatan")
tanggal = st.date_input("Tanggal Surat", value=date.today())
jenis_surat = st.selectbox("Pilih Jenis Surat", ["Surat Tugas", "SPTJM", "Kwitansi", "Berita Acara"])

# Upload template DOCX
st.subheader("📎 Upload Template Surat (.docx)")
uploaded_template = st.file_uploader("Unggah file template .docx", type="docx")

# Tombol generate surat
if uploaded_template and st.button("📝 Buat Surat"):
    try:
        doc = DocxTemplate(uploaded_template)

        context = {
            "nama": nama,
            "jabatan": jabatan,
            "kegiatan": kegiatan,
            "tanggal": tanggal.strftime("%d %B %Y")
        }

        doc.render(context)

        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        st.success(f"{jenis_surat} berhasil dibuat!")
        st.download_button(
            label=f"⬇️ Unduh {jenis_surat}.docx",
            data=buffer,
            file_name=f"{jenis_surat.lower().replace(' ', '_')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    except Exception as e:
        st.error("Gagal membuat surat.")
        st.exception(e)
else:
    st.info("Silakan lengkapi data dan upload template sebelum membuat surat.")
