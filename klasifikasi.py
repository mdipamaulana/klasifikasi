import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('karyawan.sav', 'rb'))

st.title('Prediksi Karyawan Meninggalkan Perusahaan')

Education = st.number_input('Pendidikan Karyawan (0= S1, 1= S2, 2= PHD)')
JoiningYear = st.number_input('Tahun Bergabung Dengan Perusahaan')
PaymentTier = st.number_input('Tingkat Gaji (0= Tinggi, 1= Menengah, 2= Rendah)')
Age = st.number_input('Usia')
Gender = st.number_input('Jenis Kelamin (0= L, 1= P)')
EverBenched = st.number_input('Tidak Mengerjakan Projek Dalam Sebulan (0= Tidak, 1= Ya)')
ExperienceInCurrentDomain = st.number_input('Lama Kerja Di Perusahaan Ini')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Education, JoiningYear, PaymentTier, Age, Gender, EverBenched, ExperienceInCurrentDomain]])
    
    if (prediksi [0] == 0):
        prediksi = 'Karyawan Tidak Meninggalkan Perusahaan Dalam 2 Tahun Ke Depan'
    else:
        prediksi = 'Karyawan Akan Meninggalkan Perusahaan Dalam 2 Tahun Ke Depan'
st.success(prediksi)