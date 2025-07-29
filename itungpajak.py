import streamlit as st

def format_ribuan(nilai):
    return f"{nilai:,.0f}".replace(",", ".")

def calculate_dpp(nilai, kena_ppn):
    if kena_ppn:
        return (100 / 111) * nilai
    return nilai

def calculate_dppcoretax(nilai, kena_ppn):
    if kena_ppn:
        return (100 / 111) * (11 / 12) * nilai
    return nilai     

def calculate_ppn(dpp):
    return 0.12 * dppcoretax

def calculate_pph22(dpp):
    return 0.015 * dpp

def calculate_pph23(dpp):
    return 0.02 * dpp

st.title("Kalkulator Pajak dengan DPP")

# Langkah 1: Apakah kena PPN?
kena_ppn = st.radio(":blue[Apakah transaksi dikenakan PPN?]", ["Ya", "Tidak"]) == "Ya"

# Langkah 2: Pilih jenis PPh
jenis_pph = st.selectbox(":blue[Pilih Jenis PPh]", ["PPh 22", "PPh 23"])

# Langkah 3: Input nilai transaksi
nilai_str = st.text_input(":blue[Masukkan Nilai Transaksi (misal: 1.000.000)]")

if nilai_str:
    try:
        nilai = float(nilai_str.replace(".", "").replace(",", "."))
        dpp = calculate_dpp(nilai, kena_ppn)
        dppcoretax = calculate_dppcoretax(nilai, kena_ppn)

        st.write(f"**Nilai Transaksi:** Rp {format_ribuan(nilai)}")        
        st.info(f"**DPP (Dasar Pengenaan Pajak) PPN Coretax:** Rp {format_ribuan(dppcoretax)}")
        
        if kena_ppn:
            ppn = calculate_ppn(dppcoretax)
            st.info(f"**PPN (12%) = Rp {format_ribuan(ppn)}**")
            
        st.write("")    
        st.info(f"**DPP (Dasar Pengenaan Pajak) PPh:** Rp {format_ribuan(dpp)}")        
        if jenis_pph == "PPh 22":
            pph22 = calculate_pph22(dpp)
            st.info(f"**PPh 22 (1,5%) = Rp {format_ribuan(pph22)}**")
        elif jenis_pph == "PPh 23":
            pph23 = calculate_pph23(dpp)
            st.info(f"**PPh 23 (2%) = Rp {format_ribuan(pph23)}**")

    except ValueError:
        st.error("Masukkan angka yang valid.")
