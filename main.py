import streamlit as st
from streamlit_option_menu import option_menu

option = ["Home", "Prediction", "Help"]
selected_menu = ""


def main():
    # streamlit columns
    col1, col2 = st.columns(2)

    col1.markdown("<div style='text-align: center'><img style='width:13rem;' src='https://img.freepik.com/free-vector/cute-cat-sitting-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-4148.jpg' alt=''></div>", unsafe_allow_html=True)

    col2.markdown('''
        # Cat Diagnostic
        sebuah aplikasi untuk mendiagnosa penyakit kucing berdasarkan gejala yang dialami.
    ''')

    selected_menu = option_menu(
        menu_title=False,
        options=option,
        default_index=0,
        orientation="horizontal",
        icons=[" ", " ", " "],
        menu_icon="cast",
        styles={
            "container": {"border-radius": "100px"},
            "nav-link": {"--hover-color": "#FFA1A9", "border-radius": "100px"}
        }
    )

    if selected_menu == "Home":
        st.markdown('''
            ## Home
            Selamat datang di aplikasi Cat Diagnostic
        ''')
        # input text
        st.text_input("Nama Kucing")
    # if selected menu is Prediction
    elif selected_menu == "Prediction":
        st.markdown('''
            ## Prediction
            ini adalah halaman prediction
        ''')
    # if selected menu is Help
    elif selected_menu == "Help":
        st.markdown('''
            ## Help
            ini adalah halaman help
        ''')


main()
