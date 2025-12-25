# -*- coding: utf-8 -*-

import ollama
import streamlit as st
import os
# pip install streamlit==1.24.0

def save_uploaded_file(uploaded_file): 
    #Get the current working directory 
    save_path = os.getcwd()
    file_path = os.path.join(save_path, uploaded_file.name)
    
    # Save the file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return st.success(f"Saved file: {uploaded_file.name} to {save_path}")

st.title("Image Describer!")

uploaded_files = st.file_uploader("Choose an image", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

print(uploaded_files)
if len(uploaded_files) !=0:
    for uploaded_file in uploaded_files:
        save_uploaded_file(uploaded_file)
        print(uploaded_file.name)
        print(type(uploaded_file.name))

        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

        response = ollama.chat(model='llava:7b',
                               messages=[{'role': 'user',
                                          'content': 'Describe the following images separately',
                                          'images': [uploaded_file.name]}])

        st.markdown(response['message']['content'])
        print(response['message']['content'])