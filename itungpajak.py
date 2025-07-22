import streamlit as st

st.title("Kalkulator Pajak dengan Format Ribuan")

# Input teks dengan titik
nilai_str = st.text_input("Masukkan Nilai Transaksi (misal: 1.000.000)")

if nilai_str:
    try:
        nilai = float(nilai_str.replace('.', '').replace(',', '.'))  # Bisa handle titik dan koma
        pph22 = 0.015 * nilai
        pph23 = 0.02 * nilai
        ppn = 0.11 * nilai

        st.write(f"**PPh 22 (1,5%) = Rp {pph22:,.0f}**")
        st.write(f"**PPh 23 (2%)   = Rp {pph23:,.0f}**")
        st.write(f"**PPN (11%)     = Rp {ppn:,.0f}**")
    except ValueError:
        st.error("Masukkan angka yang valid.")
