import streamlit as st

st.success("""
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


asal = st.selectbox("Masukan Tempat Asal",original_list)
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

elif asal == "Kab. Bandung" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 15, "liter")
     
elif asal == "Kab. Bandung" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Bandung" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")
     
elif asal == "Kab. Bandung" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bandung" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")
     
elif asal == "Kab. Bandung" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kab. Bandung" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 18, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bandung" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 15, "liter")     

elif asal == "Kab. Bandung" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")
     
elif asal == "Kab. Bandung" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Bandung" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bandung" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")


elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 15, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 37, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 22, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 47, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 32, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 21, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 19, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")     

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bandung Barat" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bandung Barat" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")


elif asal == "Kab. Bekasi" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 65, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 37, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")     

elif asal == "Kab. Bekasi" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Bekasi" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bekasi" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Bekasi" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")



elif asal == "Kab. Bogor" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 37, "liter")
     
elif asal == "Kab. Bogor" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bogor" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Bogor" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")
     
elif asal == "Kab. Bogor" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 70, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Bogor" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kab. Bogor" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 43, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Bogor" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")     

elif asal == "Kab. Bogor" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")
     
elif asal == "Kab. Bogor" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Bogor" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kab. Bogor" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")


elif asal == "Kab. Ciamis" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")
     
elif asal == "Kab. Ciamis" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kab. Ciamis" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kab. Ciamis" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")
     
elif asal == "Kab. Ciamis" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Ciamis" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Ciamis" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 15, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 47, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Ciamis" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")     

elif asal == "Kab. Ciamis" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Ciamis" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Ciamis" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Ciamis" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 60, "liter")



elif asal == "Kab. Cianjur" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 22, "liter")
     
elif asal == "Kab. Cianjur" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Cianjur" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Cianjur" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Cianjur" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Cianjur" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Cianjur" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 44, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Cianjur" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")     

elif asal == "Kab. Cianjur" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Cianjur" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 16, "liter")

elif asal == "Kab. Cianjur" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cianjur" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")


elif asal == "Kab. Cirebon" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Cirebon" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Cirebon" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Cirebon" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Cirebon" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Cirebon" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Cirebon" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 44, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Cirebon" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")     

elif asal == "Kab. Cirebon" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Cirebon" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 53, "liter")

elif asal == "Kab. Cirebon" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Cirebon" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")


elif asal == "Kab. Garut" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 47, "liter")
     
elif asal == "Kab. Garut" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kab. Garut" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kab. Garut" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Garut" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Garut" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")

elif asal == "Kab. Garut" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Garut" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Garut" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")

elif asal == "Kab. Garut" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Garut" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 15, "liter")

elif asal == "Kab. Garut" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Garut" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kab. Garut" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Garut" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Garut" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")

elif asal == "Kab. Garut" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Garut" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")


elif asal == "Kab. Indramayu" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 42, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 32, "liter")
     
elif asal == "Kab. Indramayu" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Indramayu" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Indramayu" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kab. Indramayu" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Indramayu" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Indramayu" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 51, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Indramayu" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")     

elif asal == "Kab. Indramayu" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 15, "liter")
     
elif asal == "Kab. Indramayu" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 67, "liter")

elif asal == "Kab. Indramayu" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Indramayu" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")


elif asal == "Kab. Karawang" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 21, "liter")
     
elif asal == "Kab. Karawang" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Karawang" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Karawang" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Karawang" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")
     
elif asal == "Kab. Karawang" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 41, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Karawang" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Karawang" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")     

elif asal == "Kab. Karawang" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Karawang" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 39, "liter")

elif asal == "Kab. Karawang" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Karawang" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kab. Kuningan" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Kuningan" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")
     
elif asal == "Kab. Kuningan" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Kuningan" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kab. Kuningan" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Kuningan" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 59, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")
     
elif asal == "Kab. Kuningan" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Kuningan" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")     

elif asal == "Kab. Kuningan" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Kuningan" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Kuningan" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Kuningan" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")


elif asal == "Kab. Majalengka" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Majalengka" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Majalengka" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 38, "liter")
     
elif asal == "Kab. Majalengka" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")
     
elif asal == "Kab. Majalengka" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Majalengka" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 47, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 41, "liter")
     
elif asal == "Kab. Majalengka" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 41, "liter")
     
elif asal == "Kab. Majalengka" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")     

elif asal == "Kab. Majalengka" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Majalengka" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Majalengka" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Majalengka" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")


elif asal == "Kab. Pangandaran" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Pangandaran" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 65, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 70, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")
     
elif asal == "Kab. Pangandaran" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Pangandaran" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Pangandaran" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Pangandaran" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 85, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Pangandaran" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 15, "liter")
     
elif asal == "Kab. Pangandaran" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 65, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 65, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")     

elif asal == "Kab. Pangandaran" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Pangandaran" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 65, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Pangandaran" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 65, "liter")


elif asal == "Kab. Purwakarta" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kab. Purwakarta" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Purwakarta" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Purwakarta" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Purwakarta" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kab. Purwakarta" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Purwakarta" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kab. Purwakarta" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kab. Purwakarta" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kab. Purwakarta" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Purwakarta" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kab. Subang" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")
     
elif asal == "Kab. Subang" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Subang" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Subang" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Subang" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 55, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")
     
elif asal == "Kab. Subang" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Subang" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Subang" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Subang" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Subang" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kab. Subang" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Subang" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Subang" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kab. Subang" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kab. Subang" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Subang" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kab. Subang" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Subang" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kab. Sukabumi" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kab. Sukabumi" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Sukabumi" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Sukabumi" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Sukabumi" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kab. Sukabumi" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Sukabumi" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kab. Sukabumi" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kab. Sukabumi" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kab. Sukabumi" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Sukabumi" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kab. Sumedang" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kab. Sumedang" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Sumedang" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Sumedang" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Sumedang" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kab. Sumedang" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Sumedang" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kab. Sumedang" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kab. Sumedang" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kab. Sumedang" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kab. Sumedang" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Sumedang" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kab. Tasikmalaya" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kab. Tasikmalaya" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kota Banjar" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Banjar" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kota Banjar" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kota Banjar" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kota Banjar" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Banjar" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kota Banjar" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Banjar" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Banjar" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kota Banjar" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Banjar" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Banjar" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kota Banjar" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kota Banjar" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Banjar" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kota Banjar" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Banjar" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kota Bekasi" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kota Bekasi" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Bekasi" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kota Bekasi" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kota Bekasi" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kota Bekasi" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kota Bekasi" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kota Bekasi" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kota Bekasi" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kota Bekasi" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kota Bekasi" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Bekasi" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")



elif asal == "Kota Bogor" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kota Bogor" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Bogor" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kota Bogor" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kota Bogor" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kota Bogor" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bogor" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kota Bogor" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Bogor" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Bogor" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kota Bogor" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Bogor" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Bogor" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kota Bogor" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kota Bogor" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Bogor" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kota Bogor" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Bogor" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")



elif asal == "Kota Cimahi" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kota Cimahi" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Cimahi" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kota Cimahi" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kota Cimahi" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kota Cimahi" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kota Cimahi" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kota Cimahi" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kota Cimahi" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kota Cimahi" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kota Cimahi" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Cimahi" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")



elif asal == "Kota Cirebon" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kota Cirebon" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Cirebon" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kota Cirebon" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kota Cirebon" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kota Cirebon" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kota Cirebon" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kota Cirebon" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kota Cirebon" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kota Cirebon" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kota Cirebon" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Cirebon" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kota Depok" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kota Depok" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Depok" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kota Depok" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kota Depok" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kota Depok" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Depok" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kota Depok" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Depok" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Depok" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kota Depok" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Depok" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Depok" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kota Depok" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kota Depok" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Depok" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kota Depok" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Depok" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kota Sukabumi" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kota Sukabumi" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Sukabumi" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kota Sukabumi" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kota Sukabumi" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kota Sukabumi" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kota Sukabumi" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kota Sukabumi" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kota Sukabumi" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kota Sukabumi" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kota Sukabumi" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Sukabumi" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")


elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "Kota Tasikmalaya" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "Kota Tasikmalaya" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "Kota Tasikmalaya" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "Kota Tasikmalaya" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "Kota Tasikmalaya" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Bandung":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Bandung Barat":
     st.write ("Jumlah Maksimalnya adalah", 10, "liter")
     
elif asal == "DKI Jakarta" and tujuan == "Kab. Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Bogor":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Ciamis":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")
     
elif asal == "DKI Jakarta" and tujuan == "Kab. Cianjur":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Garut":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
     
elif asal == "DKI Jakarta" and tujuan == "Kab. Indramayu":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Karawang":
     st.write ("Jumlah Maksimalnya adalah", 20, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Kuningan":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")
     
elif asal == "DKI Jakarta" and tujuan == "Kab. Majalengka":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Pangandaran":
     st.write ("Jumlah Maksimalnya adalah", 50, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Purwakarta":
     st.write ("Jumlah Maksimalnya adalah", 0, "liter")
     
elif asal == "DKI Jakarta" and tujuan == "Kab. Subang":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kab. Sumedang":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")
     
elif asal == "DKI Jakarta" and tujuan == "Kab. Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kota Bandung":
     st.write ("Jumlah Maksimalnya adalah", 25, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kota Banjar":
     st.write ("Jumlah Maksimalnya adalah", 56, "liter")
     
elif asal == "DKI Jakarta" and tujuan == "Kota Bekasi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kota Bogor":
     st.write ("Jumlah Maksimalnya adalah", 45, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kota Cimahi":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")     

elif asal == "DKI Jakarta" and tujuan == "Kota Cirebon":
     st.write ("Jumlah Maksimalnya adalah", 61, "liter")
     
elif asal == "DKI Jakarta" and tujuan == "Kota Depok":
     st.write ("Jumlah Maksimalnya adalah", 30, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kota Sukabumi":
     st.write ("Jumlah Maksimalnya adalah", 46, "liter")

elif asal == "DKI Jakarta" and tujuan == "Kota Tasikmalaya":
     st.write ("Jumlah Maksimalnya adalah", 40, "liter")

elif asal == "DKI Jakarta" and tujuan == "DKI Jakarta":
     st.write ("Jumlah Maksimalnya adalah", 35, "liter")
