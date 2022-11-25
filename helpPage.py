import streamlit as st

class Help :
    def __init__(self) :
        self.option = ["Home", "Prediction", "Help"]
    
    def main(self) :
        st.markdown('''
            ### Help
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse laborum doloremque nulla aliquam ab sapiente quaerat facilis tenetur! Veritatis ea quia sunt laborum quisquam consectetur, odit temporibus qui quasi voluptatem?
        ''')

        st.success("This is an info message")