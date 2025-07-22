import streamlit as st

def calculate_pph22(amount):
    return 0.015 * amount

def calculate_pph23(amount):
    return 0.02 * amount

def calculate_ppn(amount):
    return 0.11 * amount

st.title("Kalkulator Pajak Sederhana (PPh 22, PPh 23, PPN)")

nilai = st.number_input("Masukkan Nilai Transaksi (Rp)", min_value=0.0)

if nilai > 0:
    pph22 = calculate_pph22(nilai)
    pph23 = calculate_pph23(nilai)
    ppn = calculate_ppn(nilai)

    st.write(f"**PPh 22 (1,5%): Rp {pph22:,.0f}**")
    st.write(f"**PPh 23 (2%): Rp {pph23:,.0f}**")
    st.write(f"**PPN (11%): Rp {ppn:,.0f}**")
