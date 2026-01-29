import ollama
import streamlit as st
import os


response = ollama.chat(model='llava:7b',
                       messages = [{'role': 'user',
                                    'content': 'Describe the image',
                                    'images' : ['image.png']}])
print(response['message']['content'])

# '''Output from run 1: (took about 3 minutes)
#  The image is a vibrant and imaginative representation of a surreal landscape. 
#  At the center, there's an astronaut standing on a rocky surface, with a backdrop 
#  of a vast galaxy, complete with multiple celestial bodies like planets and stars, 
#  all bathed in cosmic light. The astronaut is gazing into the distance, 
#  where a majestic llama, also known as a vicuña, stands tall. This llama is 
#  uniquely adorned with what appears to be a humanoid figure on its back, 
#  contributing to a whimsical and surreal scene.

# The sky above is filled with a constellation of stars and planets, creating 
# an expansive view that gives the impression of being in outer space or looking 
# into the cosmos. The landscape is dotted with towering mountains that 
# add depth and texture to the image.

# There's a sense of serenity and wonder in the scene, as if the astronaut 
# and the llama are on an interstellar adventure. The artwork style is 
# reminiscent of pop art, with its bold colors and contrasting elements
# that evoke a sense of otherworldliness and fantasy. 
# '''