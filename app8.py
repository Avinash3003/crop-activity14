import streamlit as st
import pickle

st.title('Crop Prediction System')
model=pickle.load(open('model.pkl','rb'))

col1,col2,col3=st.columns(3)
n=col1.number_input('Enter Nitrogen: ')
p=col2.number_input('Enter Phosporous: ')
k=col3.number_input('Enter potassium: ')
t=col1.number_input('Enter Temperature: ')
h=col2.number_input('Enter Humidity: ')
ph=col3.number_input('Enter PH: ')
r=col1.number_input('Enter Rainfall: ')

if st.button('Predict'):
    data=[[n,p,k,t,h,ph,r]]
    result=model.predict(data)[0]
    st.success(result)

