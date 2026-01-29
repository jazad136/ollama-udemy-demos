import ollama
import streamlit as st
import os

st.title("Image describer")

uploaded_files = st.file_uploader("Choose an image", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

print(uploaded_files)

if len(uploaded_files) != 0: 
    for uploaded_file in uploaded_files:
        print(uploaded_file.name)
        print(type(uploaded_file.name))
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        
        response = ollama.chat(model='llava:7b',
                       messages = [{'role': 'user',
                                    'content': 'Describe the image',
                                    'images' : [uploaded_file.name]}])
        st.markdown(response['message']['content'])
        print(response['message']['content'])     


# '''Output from run 1: (took about 2 minutes)
#  The image is a digital artwork or composite that features two panels, 
#  each with a unique design. In the left panel, there's an illustrated 
#  scene at night under a starry sky. A figure stands in the foreground, 
#  looking out towards a mountain range that extends into the distance. 
#  In the background, a large white llama, which appears to be a fictional
#  or mythical creature, stands majestically on top of a rock formation. 
#  The mountains are surrounded by planets and stars, creating an otherworldly atmosphere.

# In the right panel, the same figure from the left image is now standing 
# in front of the llama with the same distant mountain range behind them. 
# The llama's expression appears to be contemplative or curious as it 
# gazes at the figure. The background remains consistent with the cosmic 
# theme of the first panel, and the overall color scheme includes shades 
# of purple, blue, and white, enhancing the ethereal feel of the artwork. 
# '''

# Seems a lot different from the output on the cmdline_llava.py file.
# Two panels??

# Output from run 2: (took a while, 2 minutes 1 s accd to ollama) 
# The image you've shared is a vibrant, digital artwork that appears to be a blend of 
# science fiction and fantasy themes. It shows two separate images with an illustration style 
# that suggests a mix of classic pop culture references with surreal elements.

# In the left image, there is a person standing on what looks like a rocky outcropping 
# with mountains in the background. The sky is filled with colorful, nebulous clouds and 
# stars, which are typical of space or science fiction settings. There's also an alien-like 
# creature that resembles a llama or alpaca standing next to the person.

# The right image features the same scene but with a different perspective. The llama 
# is now in the foreground, and the person stands further back, providing a sense of depth. 
# Both figures are positioned under a sky filled with stars, planets, and spacecraft, 
# including what appears to be a large spaceship or structure that includes an antenna.

# The overall color palette is rich and saturated, with a wide range of blues, purples,
# and greens contributing to the cosmic atmosphere. The presence of the llama and human-like 
# figure together in this fantastical setting creates an interesting contrast between real-life animals and human-made elements.

# The artwork does not contain any text that can be discerned from the image provided. 
# It is a creative piece that seems to invite viewers into a whimsical and imaginative universe, 
# blending elements of reality with fantastical concepts.

# Output from run 3 on frozen_lake_dql.py
# The image is a composite of two separate photographs. 
# On the left, there's a smaller photograph showing a computer 
# screen displaying a scatter plot with two sets of data points: 
# one set on the x-axis and the other on the y-axis, both labeled 
# as "0.2". There are horizontal lines at the top and bottom of 
# each graph, likely indicating some sort of threshold or limit 
# for the values plotted. The right photograph appears to be a 
# larger image that contains the left graphic as an inset, 
# superimposed onto what looks like a different piece of paper 
# with some writing on it, which is not fully legible due to the 
# angle and resolution of the photo. This second photo seems to 
# have been taken in a physical setting with various lines and 
# markings on it, suggesting that it might be related to 
# scientific or technical documentation or analysis. 
# 
# The background of the second image is blurred, but it 
# appears to be an indoor space with lighting fixtures visible.