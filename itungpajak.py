import streamlit as st

def format_ribuan(nilai):
    return f"{nilai:,.0f}".replace(",", ".")

st.title("Kalkulator Pajak dengan Format Ribuan")

nilai_str = st.text_input("Masukkan Nilai Transaksi (misal: 1.000.000)")

if nilai_str:
    try:
        nilai = float(nilai_str.replace(".", "").replace(",", "."))
        
        st.write(f"**Nilai Transaksi (terbaca): Rp {format_ribuan(nilai)}**")
        
        pph22 = 0.015 * nilai
        pph23 = 0.02 * nilai
        ppn = 0.11 * nilai

        st.write(f"PPh 22 (1,5%) = Rp {format_ribuan(pph22)}")
        st.write(f"PPh 23 (2%)   = Rp {format_ribuan(pph23)}")
        st.write(f"PPN (11%)     = Rp {format_ribuan(ppn)}")
        
    except ValueError:
        st.error("Masukkan angka yang valid.")
