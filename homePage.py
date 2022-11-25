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
                <p style="font-size:1rem;"><i>Cat Diagnostic</i> adalah aplikasi web yang dapat membantu Anda untuk mendiagnosis kondisi kesehatan kucing Anda. Aplikasi ini dapat mendiagnosis penyakit kucing berdasarkan gejala yang dialami, Aplikasi ini juga dapat memberikan informasi mengenai penyakit kucing yang diderita oleh kucing.</p>
            ''', unsafe_allow_html=True)