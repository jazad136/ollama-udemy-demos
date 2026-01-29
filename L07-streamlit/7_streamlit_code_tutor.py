import io
import ollama
import sys
import streamlit as st
st.title('Ollama!')
prompt = st.text_area(label = 'Write your prompt.')
button = st.button('Okay')

if button: 
    if prompt:
        while True: 
            response = ollama.generate(model='llama3.1', prompt=prompt + '\nNote: Output must have only python code, do not add any other explanation.')
            print(response['response'])
            old_stdout = sys.stdout
            sys.stdout = buffer = io.StringIO()

            code = response['response'].replace('python', '').replace("```", "")
            try: 
                exec(code)
            except Exception as e: 
                print(f"Error executing generated code: {e}")
            
            sys.stdout = old_stdout
            output = buffer.getvalue()

            if "Error executing generated code" in output:
                prompt = f"""
                The following code has this error: {output}
                Code: 
                {code}
                """
                st.markdown(f"Code has an error, fixing... \n{response['response']} \n {output}")
            else: 
                st.markdown(f"Code is working well. \n{response['response']} \n {output}")
                st.session_state['response'] = response['response']
                break

question = st.text_area(label = 'Write your question')
ask = st.button("ASK")
if ask: 
    st.markdown(st.session_state['response'])

    prompt=f"""
    Can you explain why we used this code
    "{question}"
    {st.session_state['response']}
    """
    answer = ollama.generate(model='llama3.3', prompt = prompt)
    st.markdown(answer['response'])


                        