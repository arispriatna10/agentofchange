import streamlit as st

st.set_page_config(
    page_title="Multipage App",    
)



st.title("SELAMAT DATANG DI MULTI APP TOOLS")
st.text("Disini anda bisa mengecek tools bbm dan tools kelengkapan spj")
st.markdown("[CEK BBM](https://multipagetools.streamlit.app/CEK_BBM)")
st.markdown("""
    <style>
    .warna-kustom {
        background-color: #F9E79F;
        color: #1D8348;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    <div class="warna-kustom">Ini teks dengan warna latar khusus dan teks hijau</div>
""", unsafe_allow_html=True)



st.sidebar.info("Pilih Halaman di atas")
