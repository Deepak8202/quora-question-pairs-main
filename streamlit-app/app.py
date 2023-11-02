import streamlit as st
import helper
import pickle
model =""
try:
    with open('model.pkl', 'rb') as file:
        # STOP_WORDS = pickle.load(file)
        model = pickle.load(file)
    print("model loaded successfully.")
except FileNotFoundError:
    print("File 'stopwords.pkl' not found. Make sure the file exists.")
except Exception as e:
    print(f"An error occurred: {e}")


st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

# q1 = "What is the step by step guide to invest in share market in india?"
# q2 = "What is the step by step guide to invest in share market?"

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]
    print("result --")

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')


