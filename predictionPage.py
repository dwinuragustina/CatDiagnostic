import json
import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score


class Prediction:
    def __init__(self):
        self.option = ["Home", "Prediction", "Help"]

        self.df = pd.read_csv("./dataset/data_lama.csv")
        self.symptoms = self.df.columns[:-1]
        self.diseases = self.df["penyakit"].unique()

    def main(self):

        st.markdown('''
            #### *Prediction*
            Sebelum melakukan prediksi, pastikan anda melengkapi semua data yang dibutuhkan berikut ini:
            <br/>
        ''', unsafe_allow_html=True)
        # column 1
        col1, col2 = st.columns(2)
        # col 1 text field
        with col1:
            nama_kucing = st.text_input("Nama Kucing", "")

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
            # check nama kucing
            if nama_kucing == "":
                st.error("Nama kucing Harus diisi!", icon="🚨")
            # check gejala tidak kosong
            elif not any(user_input):
                st.error("Gejala Harus dipilih!", icon="🚨")
            # check gejala < 3
            elif sum(user_input) < 3:
                st.info("Gejala Harus lebih dari 3!", icon="ℹ️")
            # open model
            else:
                # separator
                st.markdown('''
                    <hr />
                ''', unsafe_allow_html=True)

                st.markdown('''
                    #### *Hasil Prediksi*
                ''', unsafe_allow_html=True)

                # prepare data
                attributes = self.df.drop("penyakit", axis=1)
                labels = self.df["penyakit"]

                # convert dataset
                lb = LabelBinarizer()
                labels = lb.fit_transform(labels)
                attributes = attributes.replace({"Yes": 1, "No": 0})

                # split data
                X_train, X_test, y_train, y_test = train_test_split(
                    attributes,
                    labels,
                    test_size=0.2,
                    random_state=42
                )

                # create model
                model = KNeighborsClassifier(n_neighbors=3)

                # fit model
                model.fit(X_train, y_train)

                # get accuracy
                y_pred = model.predict(X_test)
                accuracy = accuracy_score(y_test, y_pred)

                # user_input to dataframe
                user_input_df = pd.DataFrame(user_input)

                # predict
                prediksi = lb.inverse_transform(model.predict(user_input_df.T))

                # show result
                st.markdown(f'''
                    Haloo, Kucing anda yang bernama <br/>
                    <p style="font-size: 20px; font-weight: bold; margin-top:-1em; font-style: italic;">{nama_kucing.capitalize()}</p>
                    Menderita penyakit <br />
                    <p style="font-size: 26px; font-weight: bold; font-style: italic;">{prediksi[0].capitalize()}</p>
                ''', unsafe_allow_html=True)

                penyakit = json.load(open("./dataset/penyakit.json", "r"))
                penyakit = penyakit[prediksi[0]]

                st.markdown('''
                    <br /> 
                    
                    ##### Tentang Penyakit
                ''', unsafe_allow_html=True)

                # loop penyakit keys
                for key in penyakit.keys():
                    # expandable
                    with st.expander(key):
                        st.write(penyakit[key])
