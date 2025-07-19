import streamlit as st

st.set_page_config(
    page_title="Multipage App",    
)



st.markdown("""
    <style>
    /* Ubah background halaman */
    .stApp {
        background: linear-gradient(to bottom, #0F2027, #203A43, #2C5364);
        color: white;
    }

    /* Gaya box header */
    .big-font {
        font-size: 30px;
        font-weight: bold;
        background-color: #2C5364;
        padding: 20px;
        border-radius: 10px;
    }

    /* Label input */
    label {
        color: #00BFFF !important;
        font-weight: bold;
    }

    /* Hasil box */
    .result-box {
        background-color: #1B6CA8;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 18px;
        color: white;
    }

    /* Dropdown style */
    section[data-testid="stSelectbox"] > div {
        background-color: #2C5364;
        border-radius: 8px;
        padding: 5px;
    }

    /* Text di selectbox */
    section[data-testid="stSelectbox"] span {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)


st.sidebar.info("Pilih Halaman di atas")
