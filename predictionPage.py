import streamlit as st
import pandas as pd
from streamlit_modal import Modal

class Prediction :
    def __init__(self) :
        self.option = ["Home", "Prediction", "Help"]
        
        self.df = pd.read_csv("./dataset/data.csv")
        self.symptoms = self.df.columns[:-1]
        self.diseases = self.df["penyakit"].unique()

    def main(self) :
        modal = Modal("Modal Hasil Prediksi", "modal_hasil_prediksi")
        
        st.markdown('''
            ### Prediction
            Sebelum melakukan prediksi, pastikan anda melengkapi semua data yang dibutuhkan berikut ini:
        ''')

        st.markdown(''' --- ''')
        
        # column 1
        col1, col2 = st.columns(2)
        # col 1 text field
        with col1 :
            st.text_input("Nama Kucing", "")

        # Gejala
        st.markdown(''' ''')
        st.markdown('''
            Pilih gejala yang dialami oleh kucing anda
        ''')

        user_input = []
        col1, col2 = st.columns(2)
        for i in range(len(self.symptoms)) :
            if i < len(self.symptoms) / 2 :
                with col1 :
                    user_input.append(st.checkbox(self.symptoms[i]))
            else :
                with col2 :
                    user_input.append(st.checkbox(self.symptoms[i]))

        st.write("")
        predict = st.button("Predict")

        if predict :
            modal.open()
        
        if modal.is_open() :
            with modal.container() :
                st.write("Modal is open")