import streamlit as st

class Help :
    def __init__(self) :
        self.option = ["Home", "Prediction", "Help"]
    
    def main(self) :
        st.markdown('''
            #### *Help*
            *Cat Diagnostic* adalah sebuah aplikasi web yang dapat digunakan untuk membantu para pemelihara kucing melakukan diagnosa kondisi kesehatan pada kucingnya. Aplikasi ini dapat memberikan diagnosa penyakit kucing berdasarkan gejala yang dialami. Aplikasi ini juga dapat memberikan informasi mengenai penyakit yang diderita oleh kucing.
            
            #### *How To Use Cat Diagnostic*
            Cara Penggunaan aplikasi Cat Diagnostic sangatlah mudah, cukup lakukan langkah berikut ini:
            1. Masuk pada menu `prediction`.
            2. Masukan data `Nama Kucing`.
            3. Pilih `gejala` yang dialami oleh kucing.
            4. Kllik button `Predict`.
            5. Menampilkan hasil prediksi penyakit kucing.
        ''')