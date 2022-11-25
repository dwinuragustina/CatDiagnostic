import streamlit as st
from streamlit_option_menu import option_menu

from homePage import Home
from predictionPage import Prediction
from helpPage import Help

st.set_page_config(page_title="Cat Diagnostic", page_icon=":cat:", layout="centered")


option = ["Home", "Prediction", "Help"]
selected_menu = ""

def main():

    st.title(":cat: Cat Diagnostic")

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

    # if selected menu is Home
    if selected_menu == "Home":
        Home().main()
    # if selected menu is Prediction
    elif selected_menu == "Prediction":
        Prediction().main()
    # if selected menu is Help
    elif selected_menu == "Help":
        Help().main()


main()
