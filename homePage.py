import streamlit as st
    
class Home:
    def __init__(self):
        self.option = ["Home", "Prediction", "Help"]

    def main(self):

        col1, col2 = st.columns(2)

        with col1 :
            st.markdown("<div style='text-align: center'><img style='width:70% ;' src='https://img.freepik.com/free-vector/cute-cat-sitting-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-4148.jpg' alt=''></div>", unsafe_allow_html=True)

        with col2 :
            st.markdown('''#### *Cat Diagnostic*''', unsafe_allow_html=True)
            st.markdown('''
                <p style="font-size:1rem;"><i>Cat Diagnostic</i> adalah sebuah aplikasi web yang dapat digunakan untuk membantu para pemelihara kucing melakukan diagnosa kondisi kesehatan pada kucingnya. Aplikasi ini dapat memberikan diagnosa penyakit kucing berdasarkan gejala yang dialami. Aplikasi ini juga dapat memberikan informasi mengenai penyakit yang diderita oleh kucing.</p>
            ''', unsafe_allow_html=True)
        
        st.markdown('''
            <br/>
            <p style="font-size:1rem;">Cara kerja aplikasi ini adalah para pemelihara kucing dapat memiilih gejala yang dialami oleh kucing pada menu “Prediction”. Dan nantinya akan didapatkan hasil prediksi penyakit yang diderita oleh kucing dan bagaimana cara mengatasinya. Dengan begitu para pemelihara kucing dapat melakukan penanganan atau pengobatan yang tepat pada kucingnya.</p>
        ''', unsafe_allow_html=True)
