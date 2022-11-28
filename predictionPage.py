import streamlit as st
from streamlit_modal import Modal
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


class Prediction:
    def __init__(self):
        self.option = ["Home", "Prediction", "Help"]

        self.df = pd.read_csv("./dataset/data.csv")
        self.symptoms = self.df.columns[:-1]
        self.diseases = self.df["penyakit"].unique()

    def main(self):
        modal = Modal("Modal Hasil Prediksi", "modal_hasil_prediksi")

        st.markdown('''
            ### Prediction
            Sebelum melakukan prediksi, pastikan anda melengkapi semua data yang dibutuhkan berikut ini:
        ''')

        st.markdown(''' --- ''')

        # column 1
        col1, col2 = st.columns(2)
        # col 1 text field
        with col1:
            st.text_input("Nama Kucing", "")

        # Gejala
        st.markdown(''' ''')
        st.markdown('''
            Pilih gejala yang dialami oleh kucing anda
        ''')

        user_input = []
        col1, col2 = st.columns(2)
        for i in range(len(self.symptoms)):
            if i < len(self.symptoms) / 2:
                with col1:
                    user_input.append(st.checkbox(self.symptoms[i]))
            else:
                with col2:
                    user_input.append(st.checkbox(self.symptoms[i]))

        st.write("")
        predict = st.button("Predict")

        if predict:
            modal.open()

        if modal.is_open():
            with modal.container():
                # Membaca dataset dari folder dataset dan melakukan data prepocessing
                df = pd.read_csv('dataset/data.csv')
                attributes = np.array(df[['anorexia', 'muntah', 'lemah', 'kurang_respon', 'dehidrasi', 'demam', 'diare', 'hipersevalis',
                                         'radang_telinga', 'batuk', 'hidung_meler', 'gatal', 'telinga_keropeng', 'pilek', 'bersin2', 'mata_berair']])
                lables = np.array(df['penyakit'])
                lb = LabelBinarizer()
                new_lables = lb.fit_transform(lables)
                # End data processing

                # Membagi dataset menjadi data train dan data test
                X_train, X_test, y_train, y_test = train_test_split(
                    attributes, new_lables, test_size=0.2)
                # End pembagian dataset

                # Membuat model KNN
                K = 3
                model = KNeighborsClassifier(n_neighbors=K)
                model.fit(X_train, y_train)
                # End model KNN

                # Menerima input dari user
                anorexia = 0
                muntah = 0
                lemah = 0
                kurang_respon = 0
                dehidrasi = 0
                demam = 1
                diare = 1
                hipersevalis = 1
                radang_telinga = 1
                batuk = 1
                hidung_meler = 1
                gatal = 1
                telinga_keropeng = 1
                pilek = 1
                bersin2 = 1
                mata_berair = 1
                # End menerima input dari user

                # Proses prediksi
                X_new = np.array([anorexia, muntah, lemah, kurang_respon, dehidrasi, demam, diare, hipersevalis, radang_telinga,
                                 batuk, hidung_meler, gatal, telinga_keropeng, pilek, bersin2, mata_berair]).reshape(1, -1)
                y_new = model.predict(X_new)
                prediksi = lb.inverse_transform(y_new)
                # End proses prediksi

                # Cek akurasi dan report classification
                y_pred = model.predict(X_test)
                acc = accuracy_score(y_test, y_pred)
                cls_report = classification_report(y_test, y_pred)
                # End akurasi dan report classification
                st.write("Modal is open")
                st.write("Hasil Prediksi : ", prediksi)
                st.write("Akurasi : ", acc)
                st.write("Classification Report : ", cls_report)
