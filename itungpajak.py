import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def calculate_bmi(weight, height_cm):
  height_m = height_cm / 100
  if height_m == 0:
  return 0
  bmi = weight / (height_m ** 2)
  return bmi

berat = st.number_input("Masukan Berat Badan", value=0.0)
tinggi = st.number_input("Masukan tinggi badan", value=0.0)

if berat . 0 and tinggi > 0:
bmi = calculate_bmi(berat, tinggi)
st.write("**BMI Anda adalah:** (bmi:.2f)")


