import streamlit as st

st.write("""
# Aplikasi Cek BBM
Ini adalah aplikasi mengecek kebutuhan BBM Perjalanan Dinas
""")


original_list = ["Pilih Kabupaten/Kota",
                 "Kab. Bandung", 
                 "Kab. Bandung Barat",
                 "Kab. Bekasi",
                 "Kab. Bogor",
                 "Kab. Ciamis",
                 "Kab. Cianjur",
                 "Kab. Cirebon",
                 "Kab. Garut",
                 "Kab. Indramayu",
                 "Kab. Karawang",
                 "Kab. Kuningan",
                 "Kab. Majalengka",
                 "Kab. Pangandaran",
                 "Kab. Purwakarta",
                 "Kab. Subang",
                 "Kab. Sukabumi",
                 "Kab. Sumedang",
                 "Kab. Tasikmalaya",
                 "Kota Bandung",
                 "Kota Banjar",
                 "Kota Bekasi",
                 "Kota Bogor",
                 "Kota Cimahi",
                 "Kota Cirebon",
                 "Kota Depok",
                 "Kota Sukabumi",
                 "Kota Tasikmalaya",
                 "DKI Jakarta"]


asal = st.text_input("Masukan Tempat Asal", original_list)
tujuan = st.selectbox("Masukan Tempat Tujuan",original_list)

if asal == "Kota Bandung" and tujuan == "Kab. Bandung":
   st.write ("Jumlah Maksimalnya adalah", 18, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 19, "liter")
     
elif asal == "Kota Bandung" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 37, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 43, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 47, "liter")
     
elif asal == "Kota Bandung" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 44, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")
     
elif asal == "Kota Bandung" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 51, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")
     
elif asal == "Kota Bandung" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kota Bandung" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 70, "liter")

elif asal == "Kota Bandung" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 28, "liter")
     
elif asal == "Kota Bandung" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kota Bandung" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kota Bandung" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Bandung" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bandung" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")

elif asal == "Kota Bandung" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 18, "liter")     

elif asal == "Kota Bandung" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")
     
elif asal == "Kota Bandung" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Bandung" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Bandung" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Bandung" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")


elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 19, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 37, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 43, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 47, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 44, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 51, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 70, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 28, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 18, "liter")     

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")


elif asal == "Kab. Bekasi" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 19, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 37, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 43, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 47, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 44, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 51, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 70, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 28, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 18, "liter")     

elif asal == "Kab. Bekasi" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bekasi" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
